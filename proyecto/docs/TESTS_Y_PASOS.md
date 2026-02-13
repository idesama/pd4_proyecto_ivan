# Tests y pasos de verificación

## Estado actual
- La carpeta `proyecto/tests/` existe pero está vacía (no hay tests automatizados todavía).

## Pruebas manuales rápidas (smoke tests)
1. Iniciar la app:
   - `cd proyecto`
   - `python main.py`
2. Login con credenciales iniciales: `admin` / `1234`.
3. Crear un usuario nuevo (opción 1 del menú) — sólo admin.
4. Cerrar sesión y entrar con el usuario creado.
5. Intentar fichar (entrada/salida) y listar fichajes.

## Ejecución de tests automatizados (recomendación)
- Añadir `pytest` a `requirements.txt` y escribir tests en `proyecto/tests/`.
- Ejecutar:
  ```bash
  cd proyecto
  pytest -q
  ```

## Casos de test recomendados
- Login correcto / incorrecto / límites de intentos (3).
- Crear usuario duplicado (debe fallar).
- Fichaje: crear y listar fichajes por usuario.
- Repositorios en memoria: añadir/recuperar usuarios y fichajes.

## Ejemplo básico de test (sugerido)
- Archivo: `proyecto/tests/test_user_repository.py`
- Comprobar que `UserRepository.add_user` almacena el usuario y `get_user_by_username` lo recupera.

---
Si quieres, puedo añadir una suite inicial de `pytest` con ejemplos para los handlers y repositorios.
