# Arquitectura por capas ✅

El proyecto sigue una arquitectura por capas simple y separada:

1. Presentation (interfaz de consola)
   - Ruta: `proyecto/presentation/`
   - Responsable de interacciones con el usuario (`menu.py`).
   - Inyecta handlers desde `main.py`.

2. Application (casos de uso / handlers)
   - Ruta: `proyecto/application/`
   - Contiene `*Handler` y objetos `commands` que representan las operaciones del sistema (login, crear usuario, crear fichaje, obtener fichajes).
   - Orquesta llamadas a repositorios y entidades.

3. Domain (modelo de negocio)
   - Ruta: `proyecto/domain/`
   - Entidades: `User`, `Clock`, interfaces de repositorio (`IUserRepository`, `IClockRepository`) y servicios de dominio.
   - Regla principal: sólo el rol `ADMIN` puede crear usuarios.

4. Infrastructure (implementaciones técnicas)
   - Ruta: `proyecto/infrastructure/`
   - Implementaciones de repositorios (`UserRepository`, `ClockRepository`) y DB en memoria (`db.py`).

5. Tests
   - Ruta: `proyecto/tests/` (actualmente vacío — recomendado añadir tests con `pytest`).

---

Flujo de interacción básico:
- `main.py` instancia repositorios y handlers → `presentation.menu` muestra opciones → el handler ejecuta la lógica de negocio usando entidades y repositorios.

Beneficios:
- Separación clara de responsabilidades.
- Fácilmente testeable a nivel de handlers y repositorios.
- Posible sustitución de `infrastructure` por repositorios con persistencia real sin tocar la capa `application`.
