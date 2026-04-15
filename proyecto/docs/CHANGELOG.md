# CHANGELOG

Todas las versiones notables del proyecto.

## [0.3.0] - 2026-04-15
### Cambiado
- Actualizada documentación para reflejar el código actual del proyecto.
- Añadidas nuevas entidades de dominio: `RequestBase`, `ClockInRequest`, `ClockCorrectionRequest`.
- Añadido nuevo comando `GetUserClocksRequest` con filtro.
- Corregido caso de uso de fichaje: actualmente solo entrada, no salida.
- Actualizado modelo de dominio y reglas de negocio.

## [0.2.0] - 2026-03-11
### Cambiado
- Documentación completa regenerada para reflejar el funcionamiento actual.
- Se aclararon casos de uso, reglas de negocio y arquitectura.
- Se añadieron notas de troubleshooting y pasos de ejecución.

## [0.1.0] - 2026-02-13
### Añadido
- Estructura por capas (presentation, application, domain, infrastructure).
- Registro de usuarios y fichajes (entrada/salida).
- Repositorio en memoria Singleton (`infrastructure/db.py`) con usuario `admin` por defecto.
- Handlers y comandos para autenticación, creación de usuario y fichajes.

---
