# Reglas de negocio

- Rol ADMIN obligatorio para crear nuevos usuarios.
- El `username` debe ser único: `AddUserHandler` evita duplicados llamando a `get_user_by_username`.
- El sistema permite hasta **3 intentos** de login (ver `presentation/menu.py`).
- Si al fichar un usuario no tiene aún una lista de fichajes, se crea la estructura antes de añadir el primer registro (comportamiento esperado: `create_clocks`).
- Si el rol introducido al crear usuario no es `1` (ADMIN), se asigna `USER` por defecto.
- `Clock.date` se almacena en UTC (`datetime.now(timezone.utc)`).

---
Valores enumerados:
- `TYPE_CLOCK.IN` = entrada
- `TYPE_CLOCK.OUT` = salida

Archivos relevantes: `application/*_handler.py`, `domain/constants/*`, `infrastructure/*_repository.py`.
