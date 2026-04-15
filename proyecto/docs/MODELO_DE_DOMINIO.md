# Modelo de dominio

## Entidades

### User
- `id: str` — UUID generado por `uuid4()`.
- `username: str` — nombre único usado para login.
- `password: str` — contraseña sin cifrar (se recomienda hashing en el futuro).
- `rol: int` — valor de `USER_ROL` (`1`=ADMIN, `2`=USER).
- `active: bool` — flag de activación (actualmente siempre `True`).
- `clocks: dict` — estructura usada en el repositorio de pruebas, no esencial para el dominio en sí.

El método `get_dto()` en `base_entity.py` devuelve un diccionario con los campos para presentación.

### Clock
- `id: str` — UUID del fichaje.
- `id_user: str` — referencia al usuario.
- `date: datetime` — fecha-hora UTC del fichaje.
- `type: int` — valor de `TYPE_CLOCK` (`1`=IN, `2`=OUT).

### RequestBase
- `id: str` — UUID de la solicitud.
- `user_id: str` — referencia al usuario que hace la solicitud.

### ClockInRequest
- Hereda de `RequestBase`.
- `clock: Clock` — el fichaje solicitado.

### ClockCorrectionRequest
- Hereda de `RequestBase`.
- `clock: Clock` — el fichaje original.
- `clock_update: Clock` — el fichaje corregido solicitado.

## Servicios

- `UserService` (en `domain/user_service.py`) valida datos al crear usuarios y asigna roles.
- `ClockService` crea objetos `Clock` y gestiona la inicialización de listas en la DB de prueba.

## Interfaces

- `IUserRepository` define `add_user` y `get_user_by_username`.
- `IClockRepository` define `add_clock`, `get_clocks_by_user` y `create_clocks`.

> Estas interfaces permiten sustituir fácilmente la implementación en `infrastructure`.
