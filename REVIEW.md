# Revisión del proyecto — Iván (Sistema de Fichajes)

**Fuente de verdad:** `proyecto/`
**Fases detectadas:** 01 (diseño por capas), 02 (documentación), 03 (testing)

## REVISIÓN FASE 01 - 2026-04-10 — Nota: 8,5/10

### Resuelto desde la revisión anterior (2026-03-03, rama review-2)

Comparándolo con la revisión anterior, **NO se detectan cambios significativos resueltos**. Los siguientes bugs funcionales y problemas de separación de capas siguen sin resolverse:

**Bugs funcionales sin resolver:**
- [ ] **Bug 1: Rol siempre asignado como USER** — comparaba `int` con `str` '1' en `create_user_handler.py`
- [ ] **Bug 2: AttributeError al fichar sin histórico** — `command.id` es `str` pero `create_clocks` espera `Clock`

**Separación de capas sin resolver:**
- [ ] Presentación sigue importando `TYPE_CLOCK` desde dominio (`menu.py:12`)
- [ ] Lógica de permisos por rol sigue en menú (`menu.py:40, 57, 71`)
- [ ] Validación de contraseña sigue en capa de aplicación (`login_handler.py:13`)

**Código sin usar sin resolver:**
- [ ] Clases nunca instanciadas: `RequestBase`, `ClockInRequest`, `ClockCorrectionRequest`, `UserService`, `ClockService`, `GetUserClocksRequest`

**Aspectos positivos mantenidos:**
- [x] Estructura con capas presentes: `domain/`, `application/`, `infrastructure/`, `presentation/`
- [x] Patrones avanzados (Singleton, Command, Repository) bien implementados
- [x] Menú funcional con opciones principales activas

### Cumple

- El proyecto está organizado en capas: `domain/`, `application/`, `infrastructure/`, `presentation/`.
- Los apartados principales del menú funcionan: crear usuario, loguearse, registrar fichajes, ver historiales.
- La estructura de archivos sigue las pautas de módulos, paquetes y subpaquetes Python.
- Se han aplicado principios de POO: clases como `User`, `Clock`, `LoginHandler`, métodos con responsabilidades claras, uso del patrón Command y Repository.
- Los nombres de ficheros, clases y variables son significativos y siguen PEP8: `User`, `Clock`, `LoginHandler` (PascalCase); `create_user()`, `get_clock_history()` (snake_case).

### Errores y aspectos a mejorar

- **[IMPORTANTE] Separación de capas incompleta.** La presentación importa `TYPE_CLOCK` directamente desde el dominio (`presentation/menu.py:12`), lo que viola la separación de capas. La lógica de permisos por rol también está en el menú (`menu.py:40, 57, 71`), cuando debería estar en la capa de aplicación o dominio.
  - *Cómo resolverlo:* Mueve `TYPE_CLOCK` a la capa de aplicación o crea constantes en presentación sin importarlas del dominio. Traslada la lógica de permisos a un servicio de la capa de aplicación.

- **[BUG] Validación de contraseña en capa de aplicación.** La validación está en `application/login_handler.py:13`, pero debería estar en la capa de dominio para garantizar que nunca se cree un usuario con contraseña inválida.
  - *Cómo resolverlo:* Mueve la validación de contraseña a la clase `User` en el dominio y haz que el handler la llame.

- **[IMPORTANTE] Clases sin usar.** Hay clases definidas pero nunca instanciadas: `RequestBase`, `ClockInRequest`, `ClockCorrectionRequest`, `UserService`, `ClockService`, `GetUserClocksRequest`.
  - *Cómo resolverlo:* Elimina estas clases si no se usan, o si las añadiste para futuras extensiones, documenta por qué están aquí. No dejes código sin usar en un proyecto.


## REVISIÓN FASE 02 - 2026-04-10 — Nota: 8/10

### Resuelto desde la revisión anterior (2026-03-03, rama review-2)

El siguientes aspecto sigue sin resolverse:

**Documentación vs código:**
- [ ] README.md raíz incompleto.

**Aspectos positivos mantenidos:**
- [x] Carpeta `docs/` con 11 documentos presentes.
- [x] Docstrings presentes en módulos, clases y métodos.

### Cumple

- Documentación completa en carpeta `docs/` con 11 ficheros: README.md, DESCRIPCION_Y_ALCANCE.md, EJECUCION.md, ARQUITECTURA_POR_CAPAS.md, CASOS_DE_USO.md, REGLAS_DE_NEGOCIO.md, MODELO_DE_DOMINIO.md, CONTRATO_REPOSITORIO.md, DATOS_INICIALES.md, TESTS_Y_PASOS.md, TROUBLESHOOTING.md.
- README.md en raíz con instrucciones de instalación y ejecución.
- CHANGELOG.md presente con versiones v0.1.0 y v0.2.0.
- Nombres significativos: clases con PascalCase (`User`, `Clock`, `LoginHandler`), métodos y variables con snake_case (`create_user()`, `get_clock_history()`).
- Arquitectura documentada con descripción de capas y responsabilidades.
- Reglas de negocio descritas en documentación (`REGLAS_DE_NEGOCIO.md`).

### Errores y aspectos a mejorar

- **[IMPORTANTE] README.md incompleto.**:
  - [ ] Línea 16: Incluye "Geolocaliza el fichaje" pero esta funcionalidad **NO está implementada** (DESCRIPCION_Y_ALCANCE.md explícitamente la excluye).
  - [ ] Sección **Quickstart**: comando simple para ejecutar (solo pone "ejecutar archivo main", sin `python main.py` explícitamente).
  - [ ] Sección **Requisitos**: qué versión de Python, si hay dependencias externas.
  - [ ] Sección **Uso**: qué hace el programa (login, crear usuarios, registrar fichajes, ver historiales).
  - [ ] Sección **Estructura del proyecto**: árbol de carpetas + descripción de qué hace cada capa (domain/, application/, infrastructure/, presentation/).
  - [ ] Sección **Documentación**: enlace a la carpeta `docs/`.
  - [ ] Sección **Tests**: cómo ejecutar tests unitarios.
  - [ ] Credenciales de prueba: usuario `admin`, contraseña `1234`.
  
  *Cómo resolverlo:* (1) Usa como modelo el README.md de la expendedora y estructura el tuyo con esas 7 secciones. (2) **Elimina "Geolocaliza el fichaje"** del README.md — el README solo debe listar características implementadas. (3) Si quieres documentar características planificadas (como geolocalización), añade en **docs/DESCRIPCION_Y_ALCANCE.md** bajo una sección "Futuro".

- **[SUGERENCIA] Comentarios sobre cambios futuros en código.** Algunos métodos (ej. `ClockService.have_clocks()`) tienen comentarios sobre planes futuros ("se borrará cuando implementemos la bbdd"). Los comentarios en código deben explicar **por qué** la lógica es así (decisiones de dominio, restricciones), no planes futuros.
  - *Cómo resolverlo:* (1) Elimina comentarios de planes futuros del código. (2) Documenta esos planes en **DESCRIPCION_Y_ALCANCE.md**.

## REVISIÓN FASE 03 - 2026-04-10 — Nota: 7/10

### Según checklist oficial (@modelo/cepy_pd4/proyecto/README.md, Fase 03)

- [x] Reorganizar las pruebas en subcarpeta `tests/`
- [x] Tests para al menos dos clases del dominio: `User`, `Clock` (parcial)
- [x] `requirements.txt` incluye `coverage`
- [ ] Documentar ejecución de tests y coverage en `docs/TESTS_Y_PASOS.md` (presente pero incompleto)
- [ ] Actualizar `docs/EJECUCION.md` con pasos completos (parcial)
- [ ] Revisar y corregir documentos desactualizados en `docs/` (inconsistencias documentadas antes)
- [ ] Registrar cambios en `CHANGELOG.md` (versión `0.3.0` falta)
- [ ] Actualizar `README.md` para reflejar estructura y comandos (incompleto, según revisión Fase 02)

### Cumple

- Tests organizados en carpeta `tests/` con estructura clara.
- `tests/tests_user.py` contiene tests para `User` (crear, obtener).
- `requirements.txt` incluye `coverage` como dependencia.
- Documentación de tests presente en `docs/TESTS_Y_PASOS.md`.

### Errores y aspectos a mejorar

- **[IMPORTANTE] Cobertura de tests incompleta.** Se requieren tests para **al menos dos clases del dominio**. Actualmente hay tests para `User`, falta para otra clase del dominio.

- **[IMPORTANTE] Documentación de tests y coverage incompleta en `docs/TESTS_Y_PASOS.md`.** La checklist requiere documentar cómo ejecutar los tests y la cobertura, incluyendo el porcentaje de cobertura alcanzado. Actualmente el documento está presente pero sin detalles de ejecución ni reporte de cobertura.
  - *Cómo resolverlo:* Ejecuta `coverage run -m unittest discover` y `coverage report`, y documenta en `docs/TESTS_Y_PASOS.md` los comandos exactos y el porcentaje de cobertura obtenido.

- **[IMPORTANTE] `docs/EJECUCION.md` incompleto.** La checklist de la actividad requiere actualizar este documento con pasos completos desde clonar el repositorio hasta ejecutar los tests. Actualmente está parcialmente completo.
  - *Cómo resolverlo:* Añade instrucciones detalladas: creación del entorno virtual, activación, instalación de dependencias (`pip install -r requirements.txt`), ejecución del programa principal, y ejecución de tests con cobertura.

- **[IMPORTANTE] CHANGELOG.md sin versión 0.3.0.** La checklist requiere registrar cambios de fase 03 en `CHANGELOG.md` con versión `0.3.0`.
  - *Cómo resolverlo:* Añade una entrada con versión `0.3.0` en `CHANGELOG.md` listando los cambios de esta fase (tests, cobertura, estructura de carpeta `tests/`, etc.).

- **[IMPORTANTE] README.md no actualizado para fase 03.** Según la checklist, debe reflejar la estructura actual y comandos de ejecución de tests. Actualmente tiene problemas de documentación descritos en la revisión de fase 02 (geolocalización no implementada, falta de secciones estándar).
  - *Cómo resolverlo:* Completa todas las correcciones indicadas en la revisión de fase 02 (eliminar "Geolocaliza el fichaje", añadir secciones Quickstart, Requisitos, Uso, Estructura del proyecto, Documentación, Tests). Luego, dentro de la sección "Tests", documenta cómo ejecutar tests y cobertura.



