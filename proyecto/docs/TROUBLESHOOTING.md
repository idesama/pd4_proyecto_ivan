# Troubleshooting (problemas comunes y soluciones) ⚠️

## Credenciales incorrectas / límites de intentos
- Síntoma: Mensaje "Credenciales incorrectas" y bloqueo tras 3 intentos.
- Causa: Usuario/contraseña erróneos.
- Solución: Usar el usuario por defecto `admin` / `1234` o crear un nuevo usuario desde una sesión ADMIN.

## Error al crear/listar fichajes (KeyError / AttributeError)
- Síntoma: Excepción al intentar crear o listar fichajes.
- Causa probable: Inconsistencia entre la firma de `create_clocks` en `IClockRepository`/`ClockRepository` y el uso en `AddClockHandler` (se pasa `user_id` cuando la implementación espera un `Clock`).
- Solución recomendada:
  1. Cambiar la firma de `create_clocks` a `create_clocks(user_id: str) -> bool` en `IClockRepository` y `ClockRepository`.
  2. Implementar `self.conection_db.clocks[user_id] = []` para inicializar la lista.
  3. Alternativamente, en `AddClockHandler` pasar un objeto `Clock` compatible (menos recomendable).

## Contraseñas en texto plano
- Síntoma: Las contraseñas se almacenan sin hashing.
- Riesgo: Seguridad baja; no apto para producción.
- Corrección: Añadir hashing (por ejemplo `bcrypt`) en el handler o en `UserRepository`.

## DB en memoria se pierde al reiniciar
- Síntoma: Datos no aparecen después de reiniciar la app.
- Causa: `DB` es un singleton en memoria sin persistencia.
- Solución: Implementar persistencia (fichero, SQLite, o migrar a una base de datos real).

## Mensajes de "Operacion no valida" en el menú
- Síntoma: Al seleccionar opciones el menú responde "Operacion no valida".
- Causa: Opción no permitida para el rol del usuario o input no esperado.
- Solución: Revisar las opciones visibles para `user['rol']` y usar los números correctos; mejorar validación en `presentation/menu.py` si se desea UX más robusta.

---
Si quieres, corrijo el problema de `create_clocks` y añado tests que validen el flujo de fichajes. ¿Quieres que lo haga ahora? 🔧
