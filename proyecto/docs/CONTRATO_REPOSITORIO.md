# Contrato de repositorio (interfaces)

Las interfaces en `domain/repository/` definen cómo deben comportarse los repositorios.

## IUserRepository
- `add_user(user: User) -> bool`
  - Inserta un usuario en el almacenamiento.
  - Retorna `True` si se añadió con éxito.
- `get_user_by_username(username: str) -> User | None`
  - Busca un usuario por su nombre de usuario.
  - Devuelve `None` si no existe.

## IClockRepository
- `add_clock(clock: Clock) -> bool`
  - Añade un registro de fichaje para el usuario.
- `get_clocks_by_user(user_id: str) -> list[Clock] | None`
  - Devuelve la lista de fichajes asociados a `user_id`.
- `create_clocks(user_id: str) -> bool` *(sujeta a corrección)*
  - Inicializa la entrada `user_id` con una lista vacía en la tabla de fichajes.

>Nota: la implementación actual en `ClockRepository` y su uso en `AddClockHandler` no coinciden exactamente
(siempre se pasa el `user_id`). Se recomienda ajustar la interfaz para evitar errores. Ver `TROUBLESHOOTING.md`.
