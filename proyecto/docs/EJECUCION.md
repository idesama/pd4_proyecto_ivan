# Ejecución

Paso a paso para iniciar y probar la aplicación.

1. Abrir una terminal.
2. Navegar al directorio principal:

   ```bash
   cd proyecto
   ```

3. Ejecutar el módulo principal:

   ```bash
   python main.py
   ```

4. En la primera pantalla, ingresar credenciales. Por defecto existe el usuario `admin` con contraseña `1234`.

5. Navegar por el menú según el rol:

   - ADMIN puede crear usuarios, buscar usuarios, fichar y ver fichajes.
   - Usuario estándar solo puede fichar y ver sus propios fichajes.

6. Para ejecutar los tests incluidos:

   ```bash
   python3 -m unittest discover -v
   ```

Requisitos: Python 3.8 o superior. No se han definido dependencias externas en `requirements.txt`.
