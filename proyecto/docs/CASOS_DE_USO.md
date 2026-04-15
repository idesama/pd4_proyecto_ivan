# Casos de uso principales

## 1) Login
- **Actor:** cualquier usuario registrado.
- **Precondición:** el usuario existe en el repositorio.
- **Flujo principal:**
  1. El usuario introduce `username` y `password` en la consola.
  2. `LoginHandler` consulta `UserRepository` y compara la contraseña.
  3. Si las credenciales son correctas se recupera el objeto `User` y se despliega el menú adecuado según su rol.
  4. Si fallan, el sistema permite hasta 3 intentos antes de bloquear.
- **Postcondición:** sesión iniciada o bloqueo tras 3 fallos.

## 2) Crear usuario (ADMIN exclusivo)
- **Actor:** usuario con rol ADMIN.
- **Precondición:** sesión iniciada como ADMIN.
- **Flujo principal:**
  1. El administrador elige la opción "Añadir nuevo usuario".
  2. Introduce el nombre, la contraseña y el rol (`1` para ADMIN, cualquier otro valor se interpreta como USER).
  3. Se construye un `CreateUserCommand` y `AddUserHandler` lo procesa: valida que no exista otro usuario con el mismo nombre y delega a `UserService` para crear la entidad.
  4. El repositorio guarda el nuevo `User` en memoria.
- **Postcondición:** el nuevo usuario queda disponible para el login.

## 3) Fichar entrada
- **Actor:** cualquier usuario autenticado.
- **Precondición:** sesión activa.
- **Flujo principal:**
  1. El usuario selecciona la opción de fichar en el menú.
  2. Se genera automáticamente un `Clock` con la fecha UTC y tipo de fichaje (`TYPE_CLOCK.IN`).
  3. `AddClockHandler` se asegura de que exista una lista de fichajes en la DB (invoca `create_clocks` si no) y añade el registro.
- **Postcondición:** registro de fichaje guardado.

## 4) Consultar fichajes de un usuario
- **Actor:** cualquier usuario autenticado (ADMIN puede ver su propio historial, la aplicación no soporta ver otro usuario actualmente).
- **Flujo principal:**
  1. El usuario elige la opción "mostrar fichajes".
  2. `GetUserClockHandler` obtiene la lista desde el repositorio y se presentan los DTOs.
- **Postcondición:** el historial de fichajes se imprime en pantalla.

---
*Implementación disponible en* `proyecto/presentation/menu.py` y las clases `*Handler` en `proyecto/application/`.
