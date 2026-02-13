# Modelo de dominio

## Entidades principales

### User
- Atributos:
  - `id: str` — UUID único.
  - `username: str` — identificador único.
  - `password: str` — contraseña en texto (actualmente sin hashing).
  - `rol: int` — valor tomado de `USER_ROL` (1=ADMIN, 2=USER).
  - `active: bool` — indica si el usuario está activo.
  - `clocks: dict` — mapeo user_id -> lista de `Clock`.
- Archivo: `domain/entities/user.py`
- Método utilitario: `get_dto()` desde `IBaseEntity` para representación serializable.

### Clock
- Atributos:
  - `id_user: str` — identificador del usuario.
  - `date: datetime` — timestamp UTC del fichaje.
  - `type: TYPE_CLOCK` — entrada/salida.
- Archivo: `domain/entities/clock.py`

## Servicios de dominio
- `UserService` con lógica básica de creación (en `domain/user_service.py`), aunque gran parte de la lógica está en handlers.

## Interfaces de repositorio
- `IUserRepository` y `IClockRepository` definen el contrato que deben implementar los repositorios.

---
Notas:
- Actualmente la contraseña se almacena en texto; para producción debe aplicarse hashing.
- `get_dto()` proviene de `domain/entities/base_entity.py` (usa `dataclasses.asdict`).
