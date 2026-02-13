# Casos de uso principales

## 1) Login
- Actor: Usuario
- Precondición: Usuario existe en la DB (por ejemplo `admin`).
- Flujo principal:
  1. Usuario introduce `username` y `password` en la consola.
  2. `LoginHandler` valida credenciales usando `UserRepository`.
  3. Si las credenciales son correctas, se muestra el menú correspondiente al rol.
- Postcondición: Sesión iniciada (acceso al menú).

## 2) Crear usuario (solo ADMIN)
- Actor: Administrador
- Precondición: El usuario es ADMIN.
- Flujo principal:
  1. Seleccionar opción "Añadir nuevo usuario".
  2. Introducir `nombre`, `contraseña` y `rol` (1=admin, 2=usuario).
  3. `AddUserHandler` valida unicidad y delega a `UserRepository.add_user`.
- Postcondición: Nuevo usuario creado en la DB en memoria.

## 3) Fichar (entrada/salida)
- Actor: Usuario autenticado
- Flujo principal:
  1. Usuario elige la opción de fichar (entrada/salida) en el menú.
  2. `AddClockHandler` crea una entidad `Clock` con `date` UTC y la guarda en `ClockRepository`.
- Postcondición: Nuevo registro de fichaje asociado al usuario.

## 4) Listar fichajes de un usuario
- Actor: Usuario autenticado (o admin buscando otro usuario)
- Flujo principal:
  1. Opción para listar fichajes → `GetUserClockHandler` solicita `get_clocks_by_user`.
  2. Se muestra la lista de `Clock` (fechas y tipo).

---
Referencia de implementación: `proyecto/presentation/menu.py`, `proyecto/application/*_handler.py`, `proyecto/infrastructure/*_repository.py`.
