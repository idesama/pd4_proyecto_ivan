# Contrato de repositorio (interfaces)

## IUserRepository
Definición (archivo): `domain/repository/IUserRepository.py`

- add_user(user) -> bool
  - Añade un `User` al almacenamiento.
  - Devuelve `True` si se añadió correctamente.

- get_user_by_username(username) -> User | None
  - Recupera un `User` por su `username`.
  - Devuelve `None` si no existe.

## IClockRepository
Definición (archivo): `domain/repository/IClockRepository.py`

- add_clock(clock: Clock) -> bool
  - Añade un `Clock` a la lista de fichajes del usuario.

- get_clocks_by_user(user_id) -> list[Clock] | None
  - Obtiene la lista de fichajes asociada a `user_id`.

- create_clocks(clock: Clock) -> bool
  - Inicializa la lista de fichajes para un usuario.

> Observación: la firma de `create_clocks` en la interfaz actualmente espera un `Clock` pero en el `AddClockHandler` se pasa `user_id` (string). Esto puede causar inconsistencias; ver `docs/TROUBLESHOOTING.md` para la recomendación de corrección.
