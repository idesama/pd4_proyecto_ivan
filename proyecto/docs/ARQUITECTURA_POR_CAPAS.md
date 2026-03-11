# Arquitectura por capas ✅

El proyecto mantiene una arquitectura de varias capas con responsabilidades bien separadas:

1. **Presentation** (interfaz de consola)
   - Ubicación: `proyecto/presentation/`
   - Solo maneja entrada/salida de texto. `menu.py` contiene el bucle interactivo que solicita credenciales y opciones.
   - Los handlers se crean e inyectan desde `main.py`.

2. **Application** (casos de uso)
   - Ubicación: `proyecto/application/`
   - Define clases `*Handler` y comandos (`CreateUserCommand`, `LoginCommand`, etc.).
   - Cada handler orquesta la lógica entre servicios de dominio y repositorios.

3. **Domain** (modelo de negocio)
   - Ubicación: `proyecto/domain/`
   - Contiene entidades (`User`, `Clock`), enums (`TYPE_CLOCK`, `USER_ROL`), servicios (`UserService`, `ClockService`) y las interfaces de repositorio (`IUserRepository`, `IClockRepository`).
   - Aquí residen las reglas de negocio, como la creación de usuarios o la generación de fichajes.

4. **Infrastructure** (implementaciones técnicas)
   - Ubicación: `proyecto/infrastructure/`
   - Implementa los repositorios en memoria (`UserRepository`, `ClockRepository`) y el almacenamiento singleton (`db.py` y `db_tests.py`).
   - Es posible reemplazar estos archivos por otros que utilicen bases de datos reales sin afectar las capas superiores.

5. **Tests**
   - Ubicación: `proyecto/tests/`
   - Actualmente contiene tests unitarios con `unittest` que cubren los servicios y handlers básicos.

**Flujo de interacción**:
- `main.py` instancia repositorios y servicios → crea handlers → llama a `presentation.menu.init_menu`.
- El menú crea comandos y llama a los handlers correspondientes.

Esta separación facilita la prueba y el mantenimiento; cada capa solo conoce la anterior y las interfaces.
