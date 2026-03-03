# REVISIONES

## REVISIÓN FASE 01 - 2026-03-03 — Nota: 7,5/10

### LO QUE ESTÁ BIEN

La estructura del proyecto está bien pensada y organizada. Tienes las cuatro capas correctas (`domain`, `application`, `infrastructure`, `presentation`) y las responsabilidades de cada capa son, en general, correctas.

Además, aplicas varios **patrones de diseño avanzados** que van más allá de lo solicitado para el proyecto,

- **Patrón Singleton** en `infrastructure/db.py`: implementado correctamente con `__new__` y la comprobación `hasattr(self, 'is_initialized')`. Garantiza que todos los repositorios comparten la misma instancia de datos en memoria.
- **Patrón Command** en `application/commands/`: los comandos encapsulan los datos de entrada de cada caso de uso.
- **Patrón Repository** con interfaces abstractas (`ABC`): defines contratos en `domain/repository/` e implementas en `infrastructure/`. Aunque no lo hemos visto es una buena práctica.
- **Inyección de dependencias** manual en `main.py`: cada handler recibe su repositorio por parámetro. 


### Seguimiento de revisiones anteriores (2026-02-03 y 2026-02-25)

- [ ] **La presentación no debe importar del dominio** — `menu.py` sigue importando `TYPE_CLOCK` desde `domain` (`presentation/menu.py:12`). Sin cambios.
- [ ] **La presentación debe limitarse a mostrar/pedir datos** — el menú sigue aplicando la lógica de permisos por rol (`presentation/menu.py:40, 57, 71`). Sin cambios.
- [ ] **Las reglas de negocio no pertenecen a la capa de aplicación** — la validación de contraseña sigue en `login_handler.py:13` y la política de asignación de rol sigue en `create_user_handler.py:21`. Sin cambios.
- [ ] **Herencia entre entidades propias del dominio** — `IBaseEntity` y `RequestBase` existen como base técnica pero sin jerarquía de negocio real (`Empleado`/`Administrador`, `FichajeEntrada`/`FichajeSalida`). Sin cambios.
- [ ] **Una única fuente de verdad para la relación User-Clock** — `User.clocks` y `DB.clocks` siguen coexistiendo. Sin cambios.
- [ ] **Integración real de las nuevas entidades en el flujo** — `ClockInRequest`, `ClockCorrectionRequest`, `RequestBase`, `UserService`, `ClockService` y `GetUserClocksRequest` siguen sin conectarse al flujo principal. Sin cambios.
- [ ] **Consistencia del contrato interfaz/implementación** — `AddClockHandler` sigue pasando `user_id: str` a `create_clocks`, que espera un objeto `Clock`. Sin cambios. (Ver Bugs en sección siguiente.)
- [ ] **Comportamiento funcional correcto** — los dos bugs de 2026-02-25 siguen presentes: rol siempre asignado como `USER` y `AttributeError` al fichar sin lista previa. Sin cambios. (Ver Bugs en sección siguiente.)
- [ ] **Contraseñas en texto plano** — sin hash. Sin cambios.

### LO QUE HAY QUE CORREGIR

#### Bugs funcionales (bloqueantes)

Hay dos bugs que hacen que la aplicación no funcione correctamente:

**Bug 1 — Error al crear usuarios: el rol siempre se asigna como `USER`**

En `application/create_user_handler.py`, la comparación del rol compara un `int` con un `str`:

```python
rol = USER_ROL.ADMIN.value if command.rol == '1' else USER_ROL.USER.value
```

`command.rol` llega como `int` (p. ej. `1`), pero se compara con el string `'1'`. La condición nunca es `True`, así que cualquier usuario que se crea acaba teniendo rol `USER` aunque hayas introducido `1`.

**Cómo arreglarlo:** cambia la comparación a `command.rol == 1` (sin comillas).

**Bug 2 — Error al fichar si el usuario no tiene fichajes previos: `AttributeError`**

En `application/create_clock_handler.py:25`, cuando el usuario no tiene lista de fichajes, llamas a:

```python
result = self._repo.create_clocks(command.id)  # command.id es un str (user_id)
```

Pero en `infrastructure/clock_repository.py`, `create_clocks` espera un objeto `Clock` y accede a `.id_user`:

```python
def create_clocks(self, clock: Clock):
    self.conection_db.clocks[str(clock.id_user)] = []  # AttributeError: 'str' has no attribute 'id_user'
```

La interfaz `IClockRepository.create_clocks` también declara el parámetro como `Clock`, pero en realidad se usa para inicializar la lista con un `user_id`.

**Cómo arreglarlo:** cambia el contrato y la implementación para que el parámetro sea `user_id: str`. Tanto la interfaz en `domain/repository/IClockRepository.py` como la implementación en `infrastructure/clock_repository.py` deben usar `user_id`:

```python
# En la interfaz:
@abstractmethod
def create_user_clocks(self, user_id):
    pass

# En la implementación:
def create_user_clocks(self, user_id):
    self.conection_db.clocks[user_id] = []
```

Y actualiza la llamada en `create_clock_handler.py`.

#### Separación de capas

Estos problemas ya se señalaron en la revisión de 2026-02-25 y siguen sin corregirse:

- **`presentation/menu.py:12`** importa `TYPE_CLOCK` desde `domain`. La presentación no debe importar del dominio directamente; debería recibir los datos ya procesados desde la capa de aplicación.
- **`presentation/menu.py:40, 57, 71`** aplica lógica de permisos por rol directamente en el menú. Esta lógica pertenece al dominio o a la aplicación.
- **`application/login_handler.py:13`** valida la contraseña en la capa de aplicación. La regla "la contraseña debe coincidir" es una regla de negocio del dominio.

#### Código sin usar

Hay clases definidas pero que no se usan: `RequestBase`, `ClockInRequest`, `ClockCorrectionRequest`, `UserService`, `ClockService`, `GetUserClocksRequest`. Si no las vas a conectar al flujo principal, mejor eliminarlas para no generar confusión o añade un comentario `# TODO:` explicando qué falta.


## REVISIÓN FASE 02 - 2026-03-03 — Nota: 7/10

### LO QUE ESTÁ BIEN

La carpeta `docs/` está completa: tienes los 12 documentos requeridos, incluyendo `ARQUITECTURA_POR_CAPAS.md`, `CASOS_DE_USO.md`, `REGLAS_DE_NEGOCIO.md`, `MODELO_DE_DOMINIO.md`, `CONTRATO_REPOSITORIO.md`, `DATOS_INICIALES.md`, `EJECUCION.md`, `TESTS_Y_PASOS.md` y `TROUBLESHOOTING.md`. Buen trabajo.


### Seguimiento de revisión anterior (2026-02-25)

- [ ] **README.md de la raíz** — sigue incompleto: comandos no reproducibles, "Geolocaliza el fichaje" sigue declarado pero no implementado. Sin cambios.
- [ ] **CHANGELOG** — sigue en versión `0.1.0`. Sin añadir la entrada `0.2.0` de documentación. Sin cambios.
- [ ] **Nomenclatura** — ningún nombre de la lista de la revisión anterior ha sido actualizado. Sin cambios.


### LO QUE HAY QUE CORREGIR

#### Docstrings incompletos

Los docstrings solo están presentes en `UserService` y `ClockService`. Faltan en:

- Todos los handlers (`LoginHandler`, `AddUserHandler`, `GetUserHandler`, `AddClockHandler`, `GetUserClockHandler`) — sus métodos `run()` deben tener docstring.
- Los repositorios (`UserRepository`, `ClockRepository`) — todos sus métodos deben tener docstring.
- Las entidades (`User`, `Clock`, `IBaseEntity`) — las clases deben tener docstring de clase.
- Los comandos — las clases deben tener docstring.

#### CHANGELOG no actualizado

`docs/CHANGELOG.md` solo tiene la versión `0.1.0`. Para la Fase 02 debes añadir una entrada `0.2.0` que liste los cambios de documentación que has añadido.

#### README.md de la raíz incompleto

El `README.md` de la raíz del repositorio tiene varios problemas:

- Las instrucciones de ejecución dicen "ejecutar archivo main como entry point" — esto no es reproducible. Debe ser un comando exacto como `python proyecto/main.py`.
- Declara una funcionalidad que no existe: "Geolocaliza el fichaje" (`README.md:16`), pero `docs/DESCRIPCION_Y_ALCANCE.md` la excluye explícitamente del alcance.

#### Nomenclatura: pendiente de corregirse

Ya se listaron en la revisión anterior (2026-02-25). Siguen pendientes todos los puntos de esa lista. Repasa los nombres en:

- Los comandos: `id` → `user_id`, `clock` → `clock_type`
- Las entidades: `USER_ROL` → `UserRole`, `TYPE_CLOCK` → `TypeClock`, `Clock.id_user` → `user_id`, `Clock.type` → `clock_type`, `User.rol` → `role`, `User.active` → `is_active`
- Infraestructura: `conection_db` → `connection_db` (error ortográfico), `DB` → `InMemoryDB`, `initialized` → `is_initialized`
- Presentación: `init_menu` → `run_menu`, `acceso` → `is_authenticated`, `salir` → `should_exit`, `opcion` → `menu_option`



## REVISIÓN FASE 03 - 2026-03-03 — Nota: 0/10

La carpeta `tests/` solo tiene un `__init__.py` vacío. No hay ningún test implementado. Para completar la Fase 03 necesitas:

1. Crear tests con `unittest` para al menos una clase del dominio (por ejemplo, testear que `AddClockHandler` crea un fichaje correctamente).
2. Crear un `requirements.txt` con `coverage` como dependencia.
3. Verificar que `docs/TESTS_Y_PASOS.md` describe cómo ejecutar los tests y obtener el informe de cobertura con comandos reales.


## REVISIÓN FASE 03 - 2026-02-25

- Sin implementar

## REVISIÓN FASE 02 - 2026-02-25

### RESULTADO DE LA REVISIÓN DE DOCUMENTACIÓN

- [x] **Propósito y alcance**  
- [x] **Instalación y requisitos**  
- [x] **Uso / quickstart**  
- [x] **Arquitectura y diseño**  
- [x] **Contrato / API interna**  
- [x] **Configuración**  
- [x] **Testing y calidad**  
- [x] **Operaciones / troubleshooting**  
- [x] **Documentación inline (docstrings/comentarios útiles)**  
- [ ] **Incumplimientos específicos de `README.md` (raíz)**  
  Estado: **No cumple** (como documento de entrada principal).  
  Evidencia base: `README.md:1-31`.
  - Instalación/requisitos incompletos: sin incluir
  - Comandos no reproducibles en formato estándar: incluye texto libre (`"ejecutar archivo main..."`) en lugar de pasos ejecutables verificables.
  - Uso/quickstart insuficiente: no muestra flujo de uso mínimo con entradas/salidas esperadas.
  - Alcance incompleto: no especifica límites ni exclusiones de forma explícita.
  - Arquitectura superficial: menciona "diseño por capas" sin enlazar estructura ni responsabilidades por capa.
  - Configuración ausente: no documenta variables/parámetros de configuración ni valores por defecto.
  - Testing ausente: no incluye cómo ejecutar pruebas ni criterios de calidad.
  - Coherencia documental: declara "Geolocaliza el fichaje" (`README.md:16`) mientras el alcance oficial la excluye (`proyecto/docs/DESCRIPCION_Y_ALCANCE.md:15`).
- [ ] **CHANGELOG**
  Estado: **Parcial**.  
  Evidencia: sin añadir 0.2.0 de documentación
- [ ] **Nomenclatura y legibilidad**  
  Estado: **Parcial**.  
  Evidencia (lista completa de nombres no conformes detectados):
  - `CreateClockCommand.id` (`proyecto/application/commands/create_clock_command.py:5`) -> no describe intención (es `id` genérico). Propuesta: `user_id`.
  - `CreateClockCommand.clock` (`proyecto/application/commands/create_clock_command.py:6`) -> no describe qué representa; no usa forma del dominio. Propuesta: `clock_type`.
  - `CreateUserCommand.user_name` (`proyecto/application/commands/create_user_command.py:2-3`) -> inconsistente con el resto (`username`). Propuesta: `username`.
  - `GetUserClocksRequest.filter` (`proyecto/application/commands/get_user_clocks_request.py:6`) -> nombre ambiguo y pisa término reservado habitual de filtrado genérico. Propuesta: `filters`.
  - `AddClockHandler` (`proyecto/application/create_clock_handler.py:8`) -> inconsistente con el caso de uso `CreateClockCommand` (acción create vs add). Propuesta: `CreateClockHandler`.
  - `AddUserHandler` (`proyecto/application/create_user_handler.py:8`) -> inconsistente con `CreateUserCommand`. Propuesta: `CreateUserHandler`.
  - `GetUserClockHandler` (`proyecto/application/get_user_clocks_handler.py:4`) -> singular/plural inconsistente con `get_user_clocks_handler.py` y `get_clocks_by_user`. Propuesta: `GetUserClocksHandler`.
  - `GetUserHandler.run(user_name)` (`proyecto/application/get_user_handler.py:11`) -> inconsistencia con `username` en el resto del código. Propuesta: `run(username: str)`.
  - `TYPE_CLOCK` (`proyecto/domain/constants/type_clock.py:2`) -> clase en mayúsculas; no sigue convención de clase y legibilidad. Propuesta: `TypeClock`.
  - `USER_ROL` (`proyecto/domain/constants/user_rol.py:2`) -> clase en mayúsculas e inconsistencia léxica (`rol`/`role`). Propuesta: `UserRole`.
  - `User.rol` (`proyecto/domain/entities/user.py:10`) -> mezcla idioma/convención con `username/password`; menor claridad. Propuesta: `role`.
  - `User.active` (`proyecto/domain/entities/user.py:11`) -> booleano no expresado como pregunta. Propuesta: `is_active`.
  - `Clock.id_user` (`proyecto/domain/entities/clock.py:9`) -> orden invertido frente a convención usada en el proyecto (`user_id`). Propuesta: `user_id`.
  - `Clock.type` (`proyecto/domain/entities/clock.py:11`) -> nombre poco expresivo y colisión semántica con built-in `type`. Propuesta: `clock_type`.
  - `IClockRepository.create_clocks(clock)` (`proyecto/domain/repository/IClockRepository.py:15`) -> plural no acorde a la operación y parámetro con nombre incorrecto respecto al uso real. Propuesta: `create_user_clocks(user_id: str)` (o `ensure_user_clocks(user_id: str)`).
  - `DB` (`proyecto/infrastructure/db.py:5`) -> nombre demasiado genérico, no describe implementación. Propuesta: `InMemoryDB`.
  - `initialized` (`proyecto/infrastructure/db.py:15,19`) -> booleano no expresado como pregunta. Propuesta: `is_initialized`.
  - `conection_db` (`proyecto/infrastructure/user_repository.py:7`, `proyecto/infrastructure/clock_repository.py:7`) -> errata ortográfica y baja legibilidad. Propuesta: `connection_db`.
  - `init_menu` (`proyecto/presentation/menu.py:16`) -> nombre técnico poco orientado a intención de caso de uso. Propuesta: `run_menu`.
  - `acceso` (`proyecto/presentation/menu.py:24,31,33,111`) -> booleano no expresado como pregunta. Propuesta: `is_authenticated`.
  - `salir` (`proyecto/presentation/menu.py:35,38,97`) -> booleano no expresado como pregunta. Propuesta: `should_exit`.
  - `opcion` (`proyecto/presentation/menu.py:52,57,71,81,91,96`) -> sin contexto semántico (opción de menú). Propuesta: `menu_option`.
  - `dtos` (`proyecto/presentation/menu.py:94`) -> abreviatura poco clara. Propuesta: `clock_dtos`.


## REVISIÓN FASE 01 - 2026-02-25

### RESULTADO DE LA VERIFICACIÓN DE LA REVISIÓN ANTERIOR

- [ ] **La capa de presentación no debería depender del dominio**  
  Estado: **No cumple**.  
  Evidencia: `presentation/menu.py:12` importa `TYPE_CLOCK` desde `domain`.

- [ ] **La presentación debería limitarse a pedir/mostrar datos, no aplicar reglas**  
  Estado: **No cumple**.  
  Evidencia: `presentation/menu.py:40`, `presentation/menu.py:57`, `presentation/menu.py:71` decide permisos/flujo por rol.

- [ ] **Reglas de negocio colocadas en aplicación (en vez de dominio)**  
  Estado: **No cumple**.  
  Evidencia: autenticación en `application/login_handler.py:13`; política de rol en `application/create_user_handler.py:21`.

- [ ] **Aplicación de herencia entre entidades**  
  Estado: **Parcial**.  
  Evidencia: existe base técnica (`IBaseEntity`, `RequestBase`), pero no hay jerarquía de negocio aplicada para roles o tipos de fichaje en uso real.

- [ ] **Una única fuente de verdad para relación User-Clock**  
  Estado: **No cumple**.  
  Evidencia: coexistencia de `User.clocks` (`domain/entities/user.py:12`) y `DB.clocks` (`infrastructure/db.py:18`).

### VERIFICACIÓN DE NUEVAS ENTIDADES Y FUNCIONALIDADES

- [ ] **Integración real de nuevas entidades en casos de uso**  
  Estado: **No cumple**. Supongo que todavía estás desarrollando esta parte 
  Evidencia: `ClockInRequest`, `ClockCorrectionRequest`, `RequestBase`, `UserService`, `ClockService`, `GetUserClocksRequest` no están conectados al flujo principal (solo definición).

- [ ] **Consistencia contrato interfaz/implementación para nuevas operaciones**  
  Estado: **No cumple**.  
  Evidencia: `AddClockHandler` pasa `user_id: str` a `create_clocks` (`application/create_clock_handler.py:25`) y `ClockRepository.create_clocks` espera objeto con `id_user` (`infrastructure/clock_repository.py:14-15`).

- [ ] **Comportamiento funcional correcto en nuevos escenarios**  
  Estado: **No cumple**.  
  Evidencia de ejecución:
  - crear usuario con `rol=1` termina en `stored_role 2` (error de tipos `int` al leer vs `str` al comprobar).
  - fichar para usuario sin lista inicial provoca `AttributeError 'str' object has no attribute 'id_user'`.

## REVISIÓN FASE 01 - 2026-02-03 (histórico)

### RECOMENDACIONES / COMENTARIOS

- En esta fase del proyecto la validación realmente aporta poco, era más interesante añadir más entidades y sus funcionalidades que son lo que podremos reutilizar en las siguientes fases del proyecto.
- Aplicar hash a las contraseñas, aunque supongo que lo tienes previsto.
- Yo intentaría que en estas fases iniciales el proyecto esté diseñado usando los principios que vemos en clase y si a lo largo de las fases ves que podrías aplicar otros patrones refactorizar entonces. Si el código empieza a diverger demasiado desde el principio adaptarlo a lo que se va a ir viendo/pidiendo puede ser más complejo.

### ASPECTOS A CAMBIAR / AÑADIR

- **La capa de presentación no debería depender del dominio**: `menu.py` (línea  9 y 10) importan User y USER_ROL, y el menú toma decisiones de flujo con eso (línea  34, línea  47 y línea  61).
- **La presentación debería limitarse a pedir/mostrar datos, no a aplicar reglas**: el “control de permisos” (qué opciones ve/puede ejecutar un usuario según rol) está en la presentación, en vez de estar en  el dominio.
- **Reglas de negocio colocadas en aplicación (en vez de dominio)**: autenticación como regla (“password coincide”) está en `login_handler.py` (línea s 12-15), y la política de asignación de rol desde entrada de usuario está en `add_user_handler.py` (línea  21) (son decisiones de dominio/negocio, aplicación debería dedicarse solo a orquestar).
- De momento **no se aplica herencia** entre entidades propias del proyecto. Igual de Usuario podrían derivar `Empleado` y `Administrador`. O más adelante cuando implementes los fichajes tener un `FichajeBase` del que hereden `FichajeEntrada`, `FichajeSalida`.
- No se aplica **encapsulación** en atributos del usuario ni hay getters ni setters.
- Aunque no has implementado los fichajes, `User` tiene como atributo `self.clocks = {}` y `Clock` tiene `id_user`; eso duplica la relación debería haber una sola “fuente de verdad”
