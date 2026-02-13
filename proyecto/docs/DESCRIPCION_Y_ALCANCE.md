# Descripción y alcance

## Descripción
Aplicación de consola para la gestión de fichajes (entradas/salidas) de empleados. Permite crear usuarios con rol (admin/usuario), autenticar usuarios, registrar fichajes y listar los fichajes de un usuario.

## Alcance funcional
- Autenticación (login) por usuario y contraseña.
- Crear usuarios (sólo admin).
- Registrar fichajes (entrada/salida).
- Listar fichajes de un usuario.

## Exclusiones / límites
- No hay persistencia en BD relacional; la aplicación utiliza un repositorio en memoria (`infrastructure/db.py`).
- No hay interfaz web ni API REST (solo consola).
- Geolocalización y otras características avanzadas están fuera del alcance actual.
