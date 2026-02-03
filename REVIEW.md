# REVISIÓN FASE 01

## RECOMENDACIONES / COMENTARIOS

- En esta fase del proyecto la validación realmente aporta poco, era más interesante añadir más entidades y sus funcionalidades que son lo que podremos reutilizar en las siguientes fases del proyecto.
- Aplicar hash a las contraseñas, aunque supongo que lo tienes previsto.
- Yo intentaría que en estas fases iniciales el proyecto esté diseñado usando los principios que vemos en clase y si a lo largo de las fases ves que podrías aplicar otros patrones refactorizar entonces. Si el código empieza a diverger demasiado desde el principio adaptarlo a lo que se va a ir viendo/pidiendo puede ser más complejo. 

## ASPECTOS A CAMBIAR / AÑADIR

- **La capa de presentación no debería depender del dominio**: `menu.py` (línea  9 y 10) importan User y USER_ROL, y el menú toma decisiones de flujo con eso (línea  34, línea  47 y línea  61).
- **La presentación debería limitarse a pedir/mostrar datos, no a aplicar reglas**: el “control de permisos” (qué opciones ve/puede ejecutar un usuario según rol) está en la presentación, en vez de estar en  el dominio.
- **Reglas de negocio colocadas en aplicación (en vez de dominio)**: autenticación como regla (“password coincide”) está en `login_handler.py` (línea s 12-15), y la política de asignación de rol desde entrada de usuario está en `add_user_handler.py` (línea  21) (son decisiones de dominio/negocio, aplicación debería dedicarse solo a orquestar).
- De momento **no se aplica herencia** entre entidades propias del proyecto. Igual de Usuario podrían derivar `Empleado` y `Administrador`. O más adelante cuando implementes los fichajes tener un `FichajeBase` del que hereden `FichajeEntrada`, `FichajeSalida`.
- No se aplica **encapsulación** en atributos del usuario ni hay getters ni setters.
- Aunque no has implementado los fichajes, `User` tiene como atributo `self.clocks = {}` y `Clock` tiene `id_user`; eso duplica la relación debería haber una sola “fuente de verdad” 
