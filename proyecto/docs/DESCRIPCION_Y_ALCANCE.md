# Descripción y alcance

Programa de consola para la gestión de fichajes de usuarios. Incluye:

- Autenticación (login) con nombre de usuario y contraseña.
- Gestión de usuarios con roles (ADMIN / USER). Solo ADMIN puede crear y buscar usuarios.
- Registro de fichajes (entrada o salida) con marca de tiempo UTC.
- Listado de fichajes de un usuario.
- Límite de 3 intentos de login.

## Alcance funcional

- Interfaz únicamente por consola.
- Repositorios en memoria (no persistente entre ejecuciones).
- Contraseñas almacenadas en texto plano.
- No existe API ni interfaz gráfica.

## Exclusiones

Elementos fuera del alcance actual:

- Persistencia en bases de datos reales.
- Cifrado de contraseñas.
- Control de horarios (promedio, cálculo de jornada, etc.).
- Funcionalidades de geolocalización o biometría.
