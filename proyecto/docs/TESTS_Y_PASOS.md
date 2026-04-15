# Tests y pasos de verificación

## Estado actual
- La carpeta `proyecto/tests/` contiene ya una suite basada en `unittest` (`tests_user.py` y `tests_clocks.py`) que cubren:
  - Creación de usuario con `AddUserHandler`.
  - Comprobación de duplicados.
  - Búsqueda de usuario con `GetUserHandler`.
  - Comportamiento del servicio al crear sin rol.
  - Tests para servicios de clock y repositorios.
- Para la base de datos en pruebas se utiliza `infrastructure/db_tests.py`.

## Ejecución de pruebas
Desde la raíz del proyecto:

```bash
cd proyecto
python3 -m unittest discover -v
```

También se puede instalar `pytest` y ejecutar los mismos ficheros:

```bash
pip install pytest
pytest tests/
```

## Pasos manuales rápidos
1. `cd proyecto && python main.py`
2. Iniciar sesión con `admin`/`1234`.
3. Crear un usuario y comprobar que no se permita duplicados.
4. Fichar y listar fichajes para el usuario actual.
5. Probar el límite de 3 intentos de login.

## Recomendaciones para nuevos tests
- Convertir los tests existentes a `pytest` y añadir más casos:
  - Validación de login (correcto/incorrecto/límites).
  - Fichajes y flujo de `create_clocks`.
  - Interacción entre servicios, handlers y repositorios.

> Si necesitas, puedo ayudarte a añadir una suite inicial de `pytest`.
