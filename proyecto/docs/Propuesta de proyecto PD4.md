## Propuesta de Proyecto: Sistema de Gestión de Fichajes con Geolocalización, Solicitudes y Gestión de Turnos para Empresas

**1. Descripción General:**

El presente proyecto se enfoca en la creación de un sistema de gestión de fichajes para empresas. El sistema aborda el problema de la gestión manual y a menudo ineficiente de los registros de entrada y salida de los empleados. Este sistema, que gestiona el dominio de la gestión de recursos humanos y control de asistencia, permitirá a las empresas registrar, consultar y analizar la información de los fichajes de sus empleados de manera centralizada y eficiente. Además, permitirá la gestión de solicitudes de fichajes olvidados y la verificación de la ubicación de los empleados al fichar 

**2. Objetivos:**

* **Objetivo General:** Desarrollar un sistema de gestión de fichajes que permita a las empresas registrar, consultar y analizar la información de asistencia de sus empleados de manera eficiente y precisa, incluyendo la gestión de solicitudes de fichajes olvidados, la geolocalización.

* **Objetivos Específicos:**
  * Permitir el registro de fichajes de entrada y salida de los empleados.
  * Facilitar la consulta de fichajes por empleado, fecha o rango de fechas.
  * Permitir a los empleados hacer solicitudes de corrección de (entrada o salida).
  * Permitir a los administradores aprobar o rechazar las solicitudes de fichaje.
  * Registrar la geolocalización del usuario al realizar un fichaje.
  * Permitir a la empresa definir las coordenadas geográficas de sus centros de trabajo.
  * Permitir la gestión de usuarios con diferentes roles (administrador (empresa) y empleado).


**3. Características Principales:**

* **Entidades del Sistema:**
  * **Empleado:** Representa a un empleado de la empresa, con atributos como ID, nombre, apellido, departamento, cargo y tipo de contrato.
  * **Fichaje:** Representa un registro de entrada o salida de un empleado, con atributos como ID, fecha y hora, tipo de fichaje (entrada, salida, solicitud), empleado asociado y coordenadas geográficas.
  * **Departamento:** Representa un departamento dentro de la empresa, con atributos como ID, nombre y descripción.
  * **Usuario:** Representa un usuario del sistema (empleado o administrador) con atributos como ID, nombre de usuario, contraseña y rol (administrador o empleado).
  * **CentroDeTrabajo:** Representa un centro de trabajo de la empresa, con atributos como ID, nombre, descripción y coordenadas geográficas.
  * **Solicitud:** Representa una solicitud de fichaje olvidado, con atributos como ID, fecha, hora, tipo de fichaje (entrada o salida), empleado asociado, motivo y estado (pendiente, aprobada, rechazada).

* **Estados Relevantes:**
  * **Empleado:** Activo, Inactivo.
  * **Fichaje:** Pendiente (solicitud), Registrado, Rechazado.
  * **Solicitud:** Pendiente, Aprobada, Rechazada.

* **Acciones que se Podrán Realizar:**
  * **Administrador:**
      * Registrar nuevos empleados.
      * Modificar la información de los empleados.
      * Aprobar o rechazar solicitudes de fichajes olvidados.
      * Definir las coordenadas geográficas de los centros de trabajo
      * Gestionar usuarios y roles.
  * **Empleado:**
      * Registrar su propio fichaje (entrada y salida).
      * Solicitar un fichaje olvidado (entrada o salida).
      * Consultar su historial de fichajes.

**4. Alcance del Proyecto:**

* **Funcionalidades Incluidas:**
  * Registro y gestión de empleados.
  * Registro de fichajes (entrada y salida) con geolocalización.
  * Solicitud de fichajes olvidados (entrada o salida).
  * Aprobación o rechazo de solicitudes de fichajes olvidados por parte de los administradores.
  * Definición de las coordenadas geográficas de los centros de trabajo.
  * Consulta de fichajes por empleado, fecha o rango de fechas.
  * Gestión de usuarios con roles de administrador y empleado.


* **Funcionalidades no incluidas:**
  * Establecer horas pasadas dentro de un periodo de gracia si el usuario olvidó fichar (en primera instancia)
  * Establecer turnos por empleado.
  * integracion con sistemas de nóminas
  * control de acceso físico a la empresa (lectores de huellas, etc)
  * envío de notificaciones por correo o sms
  * exportación en excel de los fichajes de los empleados
-
-
-
-
-