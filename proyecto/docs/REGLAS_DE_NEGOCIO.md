# Reglas de negocio

- Solo un usuario con rol `ADMIN` puede crear otros usuarios o buscarlos.
- Cada `username` debe ser único; intentar crear con un nombre existente produce un `ValueError` y el handler devuelve `False`.
- Los intentos de login se limitan a tres por ejecución; al agotarlos la aplicación finaliza.
- Cuando se registra un fichaje, si el usuario no tiene todavía una lista en la tabla `clocks`, el repositorio inicializa una lista vacía mediante `create_clocks`.
- Si el rol pasado al crear un usuario no es igual a `'1'`, el sistema asigna automáticamente el valor `2` (`USER`).
- Los timestamps de fichaje siempre se crean en UTC mediante `datetime.now(timezone.utc)`.
- Actualmente, solo se permite fichar entrada (`TYPE_CLOCK.IN`); no hay opción para salida.

**Enumeraciones usadas**
- `USER_ROL.ADMIN.value` = 1  (administrador)
- `USER_ROL.USER.value` = 2   (usuario normal)
- `TYPE_CLOCK.IN.value` = 1   (entrada)
- `TYPE_CLOCK.OUT.value` = 2  (salida)

> Nota: el servicio de dominio hace gran parte de la validación, pero los handlers manejan los resultados y errores.
