# Troubleshooting (problemas comunes y soluciones) ⚠️

### Credenciales incorrectas / límites de intentos
- **Síntoma:** "Credenciales incorrectas" y bloqueo tras 3 intentos.
- **Causa:** Usuario o contraseña erróneos.
- **Solución:** Usar `admin`/`1234` o crear otro usuario desde una sesión ADMIN.

### Error al crear/listar fichajes
- **Síntoma:** `KeyError` o lista vacía al agregar fichaje.
- **Causa probable:** Desajuste entre la firma de `create_clocks` (la interfaz pide `user_id` pero algunos usos pasaban un `Clock`).
- **Solución:** Ajustar la interfaz a `create_clocks(user_id: str)` y modificar `ClockRepository` y cualquier llamada.

### Contraseñas sin cifrar
- **Síntoma:** Las contraseñas se ven en claro en memoria.
- **Riesgo:** No apto para producción.
- **Solución:** Integrar hashing con `bcrypt` o similar en `UserService`/`UserRepository`.

### Pérdida de datos al reiniciar
- **Síntoma:** Los usuarios o fichajes desaparecen tras cerrar la app.
- **Causa:** El almacenamiento está en memoria y no se persiste.
- **Solución:** Añadir persistencia (archivo, SQLite, etc.) o migrar a un motor real.

### Menú responde "Operacion no valida"
- **Síntoma:** Opción no esperada en la selección.
- **Causa:** Entrada fuera de rango o el rol no tiene permiso para esa función.
- **Solución:** Verificar el número elegido y las opciones mostradas; la validación actual ignora roles.

> Puedo ayudarte a corregir los puntos anteriores y añadir tests que comprueben el comportamiento actualizado.
