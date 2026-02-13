# Ejecución

## Requisitos
- Python 3.10+ recomendado.

## Pasos para ejecutar (desde la raíz del repositorio)
1. Abrir terminal y moverse al directorio `proyecto`:
   ```bash
   cd proyecto
   ```
2. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

## Usuario inicial (DB en memoria)
- Usuario: `admin`
- Contraseña: `1234`

> Nota: la base de datos es un singleton en memoria (`infrastructure/db.py`). Los datos no se persisten entre ejecuciones.

## Entorno de desarrollo (recomendado)
- Crear un virtualenv y activar:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt  # si hay dependencias
  ```

## Siguientes pasos sugeridos
- Añadir `pytest` y tests automatizados en `proyecto/tests/`.
- Implementar persistencia real si se necesita conservación entre ejecuciones.
