# Datos iniciales

El sistema utiliza un almacenamiento en memoria definido en `infrastructure/db.py` o en `db_tests.py` para los tests.
Al iniciar, se crea un usuario administrador de referencia y la estructura de fichajes vacía.

- Usuario `admin` con contraseña `1234` y rol ADMIN (valor numérico `1`).
- El diccionario `users` contiene al menos la entrada `{'admin': <User objeto>}`.
- El diccionario `clocks` se inicializa con la clave del admin apuntando a una lista vacía (`{'<admin-id>': []}`).

> Todos los datos se pierden al terminar la ejecución porque no hay persistencia externa.
