# Guía de rutas Flask — ivan (sistema de fichajes)

---

## El dominio en una línea

Sistema de fichajes donde un `User` (rol `ADMIN`|`USER`) registra entradas y salidas
(`Clock`) mediante solicitudes que pueden ser de dos tipos: `ClockInRequest` (fichaje nuevo)
o `ClockCorrectionRequest` (corrección de un fichaje anterior). Ambas clases heredan de
`RequestBase`, lo que permite tratarlas de forma uniforme en el código aunque por dentro
sean distintas.

---

## Inventario completo del menú

| Opción | Descripción | Handler invocado | Solo ADMIN |
|--------|-------------|-----------------|-----------|
| Login (previo) | Autenticación con username + password; máx. 3 intentos | `LoginHandler.run(LoginCommand)` | No |
| 1 | Añadir nuevo usuario | `AddUserHandler.run(CreateUserCommand)` | Sí |
| 2 | Buscar usuario por username | `GetUserHandler.run(username)` | Sí |
| 3 | Fichar entrada (`TYPE_CLOCK.IN`) | `AddClockHandler.run(CreateClockCommand)` | No |
| 4 | Mostrar fichajes propios | `GetUserClockHandler.run(user_id)` | No |
| 0 | Cerrar sesión | — (flag `salir = True`) | No |

> El menú muestra las opciones 1 y 2 **solo si** `user['rol'] == 1` (ADMIN).
> La opción de fichar está codificada como `TYPE_CLOCK.IN`; `TYPE_CLOCK.OUT` existe
> en el enum pero no hay opción de menú para ella todavía.

---

## Rutas sugeridas (toda la API)

Los parámetros de creación/modificación se pasan como segmentos de URL.

### Autenticación

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/auth/login/<username>/<password>` | `LoginHandler.run(LoginCommand)` | Inicia sesión; `400` si credenciales incorrectas. Nota: en ut4e1 la contraseña viaja en texto plano en la URL — antipatrón aceptable solo porque no hay autenticación real. |

### Usuarios

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/users/nuevo/<username>/<password>/<int:rol>` | `AddUserHandler.run(CreateUserCommand)` | Crea un usuario; `201` / `409` si ya existe |
| `/users/<username>` | `GetUserHandler.run(username)` | Devuelve el DTO del usuario; `404` si no existe |

### Fichajes

| Ruta Flask | Método del servicio | Descripción |
|------------|---------------------|-------------|
| `/clocks/nuevo/<user_id>/<int:tipo>` | `AddClockHandler.run(CreateClockCommand)` | Registra un fichaje; `tipo` 1=IN, 0=OUT; `201` / `400` |
| `/users/<user_id>/clocks` | `GetUserClockHandler.run(user_id)` | Lista los fichajes del usuario; `200` / `404` |
| `/clocks/<clock_id>` | *(handler pendiente: `GetClockHandler`)* | Detalle de un fichaje; `200` / `404` |

---

### Ejemplo: cómo quedaría `app.py` con dos rutas ya hechas

El siguiente fragmento muestra la estructura mínima de `app.py` con dos rutas implementadas
para que puedas tomar el patrón y aplicarlo al resto:

```python
from flask import Flask
from infrastructure.user_repository import UserRepository
from infrastructure.clock_repository import ClockRepository
from application.get_user_handler import GetUserHandler
from application.get_user_clocks_handler import GetUserClockHandler

app = Flask(__name__)

user_repository = UserRepository()
clock_repository = ClockRepository()
get_user_handler = GetUserHandler(user_repository)
get_user_clock_handler = GetUserClockHandler(clock_repository)


@app.route("/")
def bienvenida():
    return (
        "Bienvenido al sistema de fichajes\n"
        "  /users/<username>        → datos de un usuario\n"
        "  /users/<user_id>/clocks  → fichajes de un usuario\n"
    )


@app.route("/users/<username>")
def obtener_usuario(username):
    try:
        usuario = get_user_handler.run(username)
    except ValueError as e:
        return str(e), 404
    return str(usuario)


if __name__ == "__main__":
    app.run(debug=True)
```

**Lo que hace cada parte:**

- Los repositorios y los handlers se crean **una sola vez** fuera de las vistas, al arrancar la
  aplicación. Así todas las rutas comparten el mismo estado en memoria.
- Cada función de vista llama al handler correspondiente y devuelve texto plano.
- Cuando el handler lanza `ValueError` (usuario no encontrado, etc.) se captura y se devuelve
  una tupla `(mensaje, código)`: `return str(e), 404` o `return str(e), 400`.
- Recuerda convertir `datetime` y `Enum` a texto antes de devolverlos en la respuesta
  (ver sección "Advertencias" → Fechas y enumerados).

---

## Métodos a añadir o completar

Los handlers existentes cubren las operaciones del menú actual, pero la API REST
requiere funcionalidad adicional que todavía no existe:

> Los dos primeros son necesarios para ut4e1. El resto son opcionales o para actividades posteriores.

| Qué falta | Dónde añadirlo | Motivo |
|-----------|---------------|--------|
| Handler `GetClockHandler` (obtener un clock por `clock_id`) | `application/get_clock_handler.py` | La ruta `/clocks/<clock_id>` no tiene handler |
| Método `get_clock_by_id(clock_id)` en `IClockRepository` y `ClockRepository` | `domain/repository/IClockRepository.py` + `infrastructure/clock_repository.py` | Necesario para el handler anterior |
| Handler `DeleteUserHandler` o `DeactivateUserHandler` | `application/` | Para gestión completa de usuarios (ADMIN) |
| Handler `GetAllUsersHandler` | `application/` | Para listar usuarios (ADMIN); `IUserRepository` no expone `get_all_users` |
| Método `get_all_users()` en `IUserRepository` y `UserRepository` | `domain/repository/IUserRepository.py` + `infrastructure/user_repository.py` | Necesario para el handler anterior |
| Soporte a `TYPE_CLOCK.OUT` en el menú / API | `presentation/menu.py` o ruta Flask | La opción de fichar salida no está implementada en el menú |
| Conversión de `datetime` y `Enum` a texto | Capa de presentación Flask | `dataclasses.asdict` no convierte `datetime` ni `Enum`; habrá que convertirlos a `str`/`int` manualmente antes de devolverlos en el texto de respuesta |

---

## Advertencias

### Persistencia en memoria (`DB` — objeto único compartido)

Los datos viven en `DB._instance`. Cada reinicio del servidor Flask limpia el
estado; no hay base de datos persistente. Hay un admin precargado:
`admin / 1234` con UUID fijo `6d976e5f-85ab-4bce-8c0f-aa9270eaa308`.

```python
# infrastructure/db.py — inicialización
self.users  = {admin.username: admin}       # clave: username (str)
self.clocks = {'6d976e5f-...': []}          # clave: user_id (str UUID)
```

### Desnormalización de `clocks` en `User`

`User.clocks` es un `dict` declarado en el dataclass, pero **no se usa como
índice real**. Los fichajes se almacenan en `DB.clocks` indexados por
`str(user_id)`. El campo `clocks` en el objeto `User` queda siempre como `{}`.

En Flask: al llamar a `.get_dto()` (que usa `dataclasses.asdict`), el campo `clocks`
aparecerá vacío. Habrá que decidir si se omite o se rellena desde `DB.clocks` antes
de construir el texto de respuesta.

### Herencia de `Request` (`ClockInRequest` / `ClockCorrectionRequest`)

Ambas heredan de `RequestBase`:

```
RequestBase          (@dataclass — id: uuid4, user_id: uuid4)
├── ClockInRequest       (NO tiene @dataclass — atributo clock: Clock sin decorar)
└── ClockCorrectionRequest  (@dataclass — clock: Clock, clock_update: Clock)
```

Asimetría importante: `ClockInRequest` **no lleva `@dataclass`**, por lo que
no tiene `__init__` generado automáticamente. Al construir estas entidades en una
ruta Flask habrá que instanciarlas manualmente y asignar los atributos a mano,
o añadir el decorador.

### `CreateClockCommand.clock` es un `int`, no un objeto `Clock`

El command transporta `TYPE_CLOCK.IN.value` (entero `1` o `0`).
Es `ClockService.create_clock` quien construye el objeto `Clock` final con
`uuid4` y timestamp UTC. En la ruta Flask, el tipo de fichaje llega como segmento
de URL: `/clocks/nuevo/<user_id>/<int:tipo>` donde `tipo` es `1` (IN) o `0` (OUT).

### Instanciación duplicada de repositorios en `main.py`

`LoginHandler` y `GetUserHandler` reciben instancias `UserRepository()` **nuevas**
en lugar de la instancia compartida. Como `DB` es un objeto único compartido por
toda la aplicación esto no produce inconsistencia ahora, pero en Flask convendrá
inyectar una sola instancia de cada repositorio al crear la aplicación para
mantener la coherencia y facilitar futuros tests.

### Estado de autenticación (login / logout)

El menú de consola gestiona la sesión con un simple bucle y un flag. En `ut4e1`
no hay autenticación real en las rutas: se acepta el `username` directamente en
la URL. La protección de rutas se trabajará en actividades posteriores.

### Fechas y enumerados como texto

`dataclasses.asdict` copia los valores tal cual — los `datetime` y los miembros de `Enum`
no se convierten automáticamente a texto. Al construir la respuesta en el route, hay que
convertirlos explícitamente:

```python
dto = clock.get_dto()
fecha_texto = dto["date"].isoformat()     # datetime → "2026-04-28T09:00:00"
tipo_texto  = str(dto["type"].value)      # Enum → "1" o "0"
return f"Fichaje: {fecha_texto} tipo={tipo_texto}"
```

Alternativa más limpia: sobreescribir `get_dto()` en `Clock` para devolver ya los tipos
primitivos (str/int), de modo que el route no tenga que convertir nada.

---

## Códigos de estado HTTP sugeridos

| Situación | Código |
|-----------|--------|
| Lectura correcta | `200 OK` |
| Creación correcta | `201 Created` |
| Recurso no encontrado | `404 Not Found` |
| Conflicto (usuario ya existe) | `409 Conflict` |
| Body incorrecto / validación fallida | `400 Bad Request` |
