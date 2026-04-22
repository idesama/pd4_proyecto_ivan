# Revisión del proyecto — Iván (Sistema de Fichajes)

**Fuente de verdad:** `proyecto/`
**Fases detectadas:** 01 (diseño por capas), 02 (documentación), 03 (testing)
**Fecha de revisión:** 2026-04-22

## REVISIÓN FASE 01 - 2026-04-22 — Nota: 8,5/10

### Resuelto desde la revisión anterior (2026-04-15, rama review-3)

No se han detectado cambios en los puntos pendientes de la fase 01. Los commits posteriores a la revisión anterior se han concentrado en la fase 03 (test de Clock) y en preparación para la fase 04 (documento `DISEÑO_SQLITE`, `db_sqlite.py`), sin tocar los bugs ni los problemas de separación de capas señalados.

**Sin resolver** (se mantienen todos los puntos de la revisión anterior):
- [ ] Bug de rol siempre asignado como USER por comparación `int` vs `str`
- [ ] Presentación importa `TYPE_CLOCK` desde el dominio
- [ ] Lógica de permisos por rol en la presentación
- [ ] Validación de contraseña en la capa de aplicación
- [ ] Clases nunca instanciadas: `RequestBase`, `ClockInRequest`, `ClockCorrectionRequest`, `GetUserClocksRequest`

### Cumple

- El proyecto está organizado en capas: `domain/`, `application/`, `infrastructure/`, `presentation/`.
- Los apartados principales del menú funcionan: crear usuario, loguearse, registrar fichajes, ver historiales.
- La estructura de archivos sigue las pautas de módulos, paquetes y subpaquetes Python.
- Se han aplicado principios de POO: clases como `User`, `Clock`, `LoginHandler`, patrones Command y Repository bien implementados.
- Los nombres de ficheros, clases y variables son significativos y siguen PEP8.

### Errores y aspectos a mejorar

- **[BUG] `domain/user_service.py:24` — Comparación `rol == '1'` incompatible con el input del menú.** En `presentation/menu.py:63` el menú convierte la opción del rol con `int(input(''))`, así que al handler llega un `int`. En cambio `UserService.create_user` compara `rol == '1'` (string). La expresión `1 == '1'` es siempre `False`, así que **cualquier usuario nuevo se crea siempre como USER**, independientemente de lo que elija el administrador. El flag de administrador solo quedó bien en el usuario `admin` inicial porque se carga a mano en la base de datos.
  - *Cómo resolverlo:* Homogeneiza el tipo. Lo más claro es que la presentación transforme la opción del menú al valor del enum `USER_ROL` antes de construir el `CreateUserCommand`, y que `UserService.create_user` reciba directamente un `USER_ROL`. Eso además te ayuda a eliminar el `int` "mágico" del menú.

- **[DISEÑO] `presentation/menu.py:12` — La presentación importa constantes del dominio.** Sigue el `from domain.constants.type_clock import TYPE_CLOCK`. La presentación debería recibir del servicio o de la capa de aplicación los valores válidos (o construir los comandos con texto "entrada"/"salida" que el servicio traduzca), pero no importar directamente del dominio.
  - *Cómo resolverlo:* Define una pequeña constante o función en la capa de aplicación que exponga las opciones al menú, o haz que el servicio construya el `Clock` con la semántica que necesite. Así la presentación no depende del módulo de constantes del dominio.

- **[DISEÑO] `presentation/menu.py:40, 57, 71` — Lógica de permisos por rol en el menú.** El menú decide qué opciones mostrar y qué operaciones permitir en función de `user['rol'] == 1`. Esa lógica debería estar en la capa de aplicación (un servicio de autorización) o en el propio `User` como método (`es_administrador()`), no en la presentación. La presentación solo debe preguntar "¿puede este usuario hacer X?" y recibir `True`/`False`, no conocer los valores internos de los roles.
  - *Cómo resolverlo:* Añade un método `es_administrador()` a `User` (o un servicio `AuthorizationService`) y sustituye las comparaciones directas con `1` en el menú por llamadas a ese método.

- **[DISEÑO] `application/login_handler.py:13` — Validación de contraseña en capa de aplicación.** La comparación `user.password == command.password` debería estar en el dominio (`User.verificar_password(password)`), no en el handler. El dominio garantiza que nunca se valide mal una contraseña, venga de donde venga.
  - *Cómo resolverlo:* Añade `User.verificar_password(password)` en el dominio y llámalo desde el handler. De paso puedes encapsular ahí también cualquier regla de negocio futura (p. ej., bloquear tras N intentos fallidos, que aunque ahora está en el menú conviene traerla al dominio).

- **[IMPORTANTE] Clases nunca instanciadas.** Siguen existiendo sin uso: `RequestBase`, `ClockInRequest`, `ClockCorrectionRequest` (en `domain/entities/`) y `GetUserClocksRequest` (en `application/commands/`). `grep` no encuentra ninguna instanciación fuera del propio fichero donde se definen.
  - *Cómo resolverlo:* Elimina las clases que no usas. Si las conservas porque planeas usarlas en la fase 04, márcalo explícitamente en un comentario `# Pendiente de integrar en fase 04` y documenta el porqué. No dejes código "por si acaso".


## REVISIÓN FASE 02 - 2026-04-22 — Nota: 8/10

### Resuelto desde la revisión anterior (2026-04-15, rama review-3)

No se ha tocado el `README.md` ni los comentarios de planes futuros en el código desde la revisión anterior. Ambos puntos siguen pendientes.

### Cumple

- Documentación completa en carpeta `docs/` con 11 ficheros.
- `CHANGELOG.md` presente con versiones `0.1.0`, `0.2.0` y `0.3.0` (esta última añadida tras la revisión anterior).
- Docstrings presentes en módulos, clases y métodos.
- Nombres significativos siguiendo PEP8.
- Arquitectura documentada con descripción de capas y responsabilidades.
- Reglas de negocio descritas en `docs/REGLAS_DE_NEGOCIO.md`.

### Errores y aspectos a mejorar

- **[IMPORTANTE] `README.md` — Incompleto y describe funcionalidad no implementada.** El README de la raíz sigue diciendo "Geolocaliza el fichaje" (línea 16) pese a que `docs/DESCRIPCION_Y_ALCANCE.md` excluye explícitamente esa funcionalidad. Además siguen faltando las secciones estándar: Quickstart concreto (con `python main.py`), Requisitos (versión de Python), Uso, Estructura del proyecto, Documentación (enlace a `docs/`), Tests y credenciales de prueba (`admin` / `1234`).
  - *Cómo resolverlo:* (1) Elimina "Geolocaliza el fichaje" del README — el README solo debe listar lo implementado. (2) Usa como modelo el `README.md` de la expendedora en `modelo/cepy_pd4/proyecto/03-testing/expendedora/README.md` y estructura el tuyo con las mismas secciones. (3) Si quieres documentar planes futuros, añade un apartado "Futuro" en `docs/DESCRIPCION_Y_ALCANCE.md`.

- **[SUGERENCIA] Comentarios sobre cambios futuros en código.** Sigue habiendo comentarios del tipo "se borrará cuando implementemos la bbdd" en métodos como `ClockService.have_clocks()`. Los comentarios deben explicar el **por qué** de la lógica actual, no planes futuros.
  - *Cómo resolverlo:* Elimina esos comentarios del código y lleva los planes a `docs/DESCRIPCION_Y_ALCANCE.md` bajo una sección "Futuro" o similar.


## REVISIÓN FASE 03 - 2026-04-22 — Nota: 8/10

### Resuelto desde la revisión anterior (2026-04-15, rama review-3)

- **Tests para una segunda clase del dominio añadidos.** Nuevo fichero `tests/tests_clocks.py` con 4 tests que cubren `ClockService` y `AddClockHandler`. Ahora la suite cubre dos clases del dominio (`User` y `Clock`), como exige el checklist oficial. Total: 8 tests, todos pasan (`python3 -m unittest discover -s tests`).
- **`CHANGELOG.md` — Versión `[0.3.0] - 2026-04-15` añadida.** Con sección `Cambiado` recogiendo novedades de la fase.

### Cumplimiento del checklist oficial (Fase 03)

Según `@modelo/cepy_pd4/proyecto/README.md`:

- [x] Reorganizar las pruebas en subcarpeta `tests/`
- [x] Tests para al menos dos clases del dominio: `User`, `Clock`
- [x] `requirements.txt` incluye `coverage`
- [ ] Documentar ejecución de tests y coverage en `docs/TESTS_Y_PASOS.md` (parcial: tests documentados, coverage sin documentar)
- [ ] Actualizar `docs/EJECUCION.md` con pasos completos (falta venv, `pip install`, coverage)
- [ ] Revisar y corregir documentos desactualizados en `docs/`
- [x] Registrar cambios en `CHANGELOG.md` (versión `0.3.0`)
- [ ] Actualizar `README.md` para reflejar estructura y comandos

### Cumple

- Tests organizados en carpeta `tests/` con estructura clara.
- Tests cubren dos clases del dominio: `User` (`tests_user.py`) y `Clock` (`tests_clocks.py`).
- `tests_clocks.py` cubre tres escenarios relevantes de `ClockService` y un caso del handler de alta.
- 8 tests pasan con `python3 -m unittest discover -s tests`.
- `requirements.txt` incluye `coverage`.
- `CHANGELOG.md` con entrada para `0.3.0`.

### Errores y aspectos a mejorar

- **[IMPORTANTE] `docs/TESTS_Y_PASOS.md` — Sigue sin documentar la ejecución de `coverage`.** El documento explica cómo correr los tests con `unittest`, pero no incluye los comandos de cobertura (`coverage run -m unittest discover`, `coverage report`, `coverage html`) ni el porcentaje alcanzado. El checklist pide ambas cosas.
  - *Cómo resolverlo:* Ejecuta `coverage run -m unittest discover -s tests` y `coverage report`, copia el porcentaje obtenido y añade una sección "Cobertura" al documento con los tres comandos y el reporte resumido. También retira la sugerencia de usar `pytest`, porque en el curso se trabaja con `unittest`.

- **[IMPORTANTE] `docs/EJECUCION.md` — Sigue incompleto para la fase 03.** No describe la preparación del entorno virtual (`python -m venv .venv` y activación en distintos sistemas), no menciona `pip install -r requirements.txt`, y la sección de tests no incluye cobertura.
  - *Cómo resolverlo:* Añade una sección inicial "Preparación del entorno" con venv, activación (Linux/macOS y Windows) y `pip install -r requirements.txt`. Amplía la sección de tests para incluir los comandos de `coverage`.

- **[IMPORTANTE] `README.md` sin actualizar para la fase 03.** Los problemas señalados en la fase 02 (funcionalidad no implementada, falta de secciones estándar) también afectan a la fase 03: el README debería incluir cómo ejecutar los tests y la cobertura, y reflejar que hay carpeta `tests/`.
  - *Cómo resolverlo:* Cuando arregles el README siguiendo las indicaciones de la fase 02, añade un apartado "Tests" con los comandos de `unittest` y `coverage`, y asegúrate de que el árbol de estructura (si lo incluyes) refleje la existencia de `tests/`.

- **[SUGERENCIA] `docs/CHANGELOG.md` — El contenido de la entrada `[0.3.0]` no refleja los cambios reales de la fase.** La sección `Cambiado` describe actualizaciones de documentación, "nuevas entidades de dominio" (que en realidad son clases sin usar) y una corrección de casos de uso, pero **no menciona** el cambio más relevante de la fase: la creación de la carpeta `tests/`, los tests de `User` y `Clock`, ni la inclusión de `coverage` en `requirements.txt`.
  - *Cómo resolverlo:* Reescribe la entrada `[0.3.0]` para centrarla en la fase 03: añade una sección `Añadido` con "Suite de tests unitarios en `tests/` para `User` y `Clock`" y "`coverage` como dependencia en `requirements.txt`". Los cambios de documentación que sí sean reales déjalos en `Cambiado`.


## Resumen

En las dos semanas desde la revisión anterior has dedicado el esfuerzo principalmente a:

1. **Cumplir el mínimo del checklist oficial de fase 03**: has añadido los tests de `Clock` y la entrada `0.3.0` del CHANGELOG. Esto sube la fase 03 a 8/10.
2. **Preparar la fase 04**: `DISEÑO_SQLITE.md`, `db_sqlite.py`, regeneración del diagrama relacional.

Lo que queda por abordar antes de la fase 04:

- **Fase 01**: ninguno de los 5 puntos pendientes (bug de rol, separación de capas, clases sin usar) se ha tocado. El bug de rol es especialmente importante porque, si no se arregla antes de migrar a SQLite, los usuarios creados desde el menú quedarán con un rol incorrecto en la base de datos persistente.
- **Fase 02**: el `README.md` sigue describiendo una funcionalidad que no existe. Corrígelo antes de que nadie más clone el repositorio y piense que geolocalizas fichajes.
- **Fase 03**: documenta la cobertura (`docs/TESTS_Y_PASOS.md` y `docs/EJECUCION.md`) — es el último paso para cerrar el checklist oficial al 100%.

Priorízalo antes de seguir con SQLite: los bugs de la fase 01 se propagarán a la base de datos y cuestan lo mismo arreglarlos ahora que luego.
