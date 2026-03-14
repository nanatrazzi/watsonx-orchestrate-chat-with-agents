<div align="center">

# Watsonx Orchestrate Chat with Agents

### API REST para comunicación con IBM Watsonx Orchestrate

[![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Powered-blue?style=for-the-badge&logo=ibm)](https://cloud.ibm.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org)

</div>

---

## Índice

- [Visión General](#-visión-general)
- [Endpoints Disponibles](#-endpoints-disponibles)
- [Cómo Obtener las Credenciales](#-cómo-obtener-las-credenciales)
- [Configuración del Proyecto](#️-configuración-del-proyecto)
- [Documentación de la API](#-documentación-de-la-api)
- [Variables de Entorno](#-variables-de-entorno)
- [Notas Importantes](#-notas-importantes)

---

## Visión General

Este asset proporciona un **servicio HTTP basado en FastAPI** que permite la comunicación con **IBM Watson Orchestrate (WxO)** a través de tres endpoints principales:

<table>
<tr>
<td width="30%"><b>Endpoint</b></td>
<td><b>Descripción</b></td>
</tr>
<tr>
<td><code>/list_agents</code></td>
<td>Devuelve una lista de agentes disponibles en una determinada instancia de watsonx Orchestrate</td>
</tr>
<tr>
<td><code>/get_response</code></td>
<td>Devuelve una única respuesta de un agente WxO</td>
</tr>
<tr>
<td><code>/stream_response</code></td>
<td>Transmite la respuesta del agente en tiempo real usando Server-Sent Events (SSE)</td>
</tr>
</table>

### Enlaces Útiles

- **Código Fuente**: [GitHub Repository](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/tree/main/source/rest_api)
- **Endpoints Implementados**: [Routes Directory](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/blob/main/source/rest_api/routes)

---


#### Crear una Instancia de Watsonx Orchestrate

Después de iniciar sesión en **IBM Cloud**, en el campo de búsqueda escriba `watsonx Orchestrate`.

<div align="center">
<img src="Build_Book_Images/wxo01.jpeg" alt="Buscar Watsonx Orchestrate" width="800"/>
</div>

Elija la **location** de su instancia y el **plan** que mejor le convenga

<div align="center">
<img src="Build_Book_Images/wxo02.jpeg" alt="Elegir Location y Plan" width="800"/>
</div>

---

Por último, escriba el **nombre del servicio**, opcionalmente **tags** y **tags de activación**, y seleccione un **resource group**.

Acepte los términos de IBM Cloud en el lado derecho de la pantalla y haga clic en **Create**.

<div align="center">
<img src="Build_Book_Images/wxo03.jpeg" alt="Configurar Servicio" width="800"/>
</div>

---

Con su instancia creada, haga clic en **Launch watsonx Orchestrate**.

<div align="center">
<img src="Build_Book_Images/wxo04.jpeg" alt="Launch Watsonx Orchestrate" width="800"/>
</div>

---

Para comunicarse con Watsonx Orchestrate vía API, necesitará obtener dos credenciales esenciales:
- `IAM_API_KEY`
- `WXO_INSTANCE_ID`

## Cómo obtener las credenciales de watsonx Orchestrate

En el ícono de las iniciales de su nombre y apellido en el lado derecho de la interfaz

<div align="center">
<img src="Build_Book_Images/wxo05.png" alt="Settings" width="800"/>
</div>

Haga clic en **Settings**.

<div align="center">
<img src="Build_Book_Images/wxo05-b.png" alt="Settings" width="800"/>
</div>

En la página de configuración entre en la pestaña **API details** 

<div align="center">
<img src="Build_Book_Images/wxo06.png" alt="API Details" width="800"/>
</div>

1. Copie el ID de su instancia

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

2. A continuación, haga clic en `Generate API Key`

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

En la siguiente página, haga clic en **Generate API key**.

Será redirigido al catálogo donde crea, visualiza y trabaja con claves de API de IBM Cloud.

<div align="center">
<img src="Build_Book_Images/wxo07.jpeg" alt="Generate API Key" width="800"/>
</div>

> **¿Qué es una API Key?**
> 
> Una API Key es un secreto que permite que usuarios, aplicaciones o servicios accedan a IBM Cloud de forma autenticada. Funciona como una "contraseña técnica" usada en CLIs, automatizaciones, pipelines o integraciones.

---

**Configuración de la API Key**

**Name (Nombre)**

Dé un nombre descriptivo a la clave, como:
- `apikey-wxo`
- `local-development-key`

> **Consejo**: Use nombres que indiquen el propósito, responsable o entorno.

**Description (Opcional)**

Aquí puede agregar una descripción de su clave, ayudando en su identificación.

---

**Lead Action (Acción en Caso de Filtración)**

<table>
<tr>
<td width="40%"><b>Opción</b></td>
<td><b>Descripción</b></td>
</tr>
<tr>
<td>🔘 <b>Disable the leaked key</b>  (recomendado)</td>
<td>La clave se desactiva automáticamente. Buena opción para producción.</td>
</tr>
<tr>
<td>🔘 <b>Delete the leaked key</b></td>
<td>La clave se elimina permanentemente.</td>
</tr>
<tr>
<td>🔘 <b>Nothing</b></td>
<td>No se toma ninguna acción. No recomendado.</td>
</tr>
</table>


**API Key Expiration (Expiración)**

Puede elegir si la clave debe expirar automáticamente.

<table>
<tr>
<td width="40%"><b>Opción</b></td>
<td><b>Descripción</b></td>
</tr>
<tr>
<td>🔘 <b>Set expiration</b></td>
<td>
Permite elegir una fecha futura.<br>
-> Ideal para accesos temporales, integraciones de corto plazo, etc.<br>
Cuando expire, la clave se deshabilitará automáticamente.
</td>
</tr>
<tr>
<td>🔘 <b>Sin expiración</b> (default)</td>
<td>La clave no expira.</td>
</tr>
</table>

---

**Session Management (Gestión de Sesión)**

Define si esta clave puede ser usada para gestión de sesiones en IBM Cloud CLI.

<table>
<tr>
<td width="20%"><b>Opción</b></td>
<td><b>Descripción</b></td>
</tr>
<tr>
<td>🔘 <b>Yes</b></td>
<td>Permite que la clave sea usada para iniciar sesión en CLI con <code>ibmcloud login --apikey</code></td>
</tr>
<tr>
<td>🔘 <b>No</b></td>
<td>La API Key no podrá ser usada para iniciar sesión en sesiones CLI. Use cuando desee restringir la clave solo para llamadas específicas de API.</td>
</tr>
</table>

<div align="center">
<img src="Build_Book_Images/wxo08.jpeg" alt="Configuraciones de la API Key" width="800"/>
</div>

---
Después de completar todo, haga clic en **Create**.

<div align="center">
<img src="Build_Book_Images/wxo09.jpeg" alt="Crear API Key" width="800"/>
</div>

> **IMPORTANTE**: Aproveche este momento para copiar o descargar su API Key. La clave estará disponible por algunos segundos. Después de este período, no será posible visualizarla nuevamente.

<div align="center">
<img src="Build_Book_Images/wxo10.jpeg" alt="Copiar API Key" width="800"/>
</div>

---

Después de obtener las credenciales, ya posee las dos informaciones necesarias para la ejecución de la interacción vía backend con el chat de su agente (watsonx Orchestrate).


1. **Navegue hasta el directorio del proyecto**:
   ```bash
   cd ./source/rest_api/
   ```

2. **Configure las variables de entorno**:
   - Cambie el nombre del archivo `.env_example` a `.env`
   - Complete con sus credenciales:
   
   ```env
   IAM_API_KEY=su-api-key-aqui
   WXO_INSTANCE_ID=su-instance-id-aqui
   ```

3. **Instale las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecute el servidor**:
   ```bash
   python app.py
   ```

---

### Gestión de Conversaciones (Thread ID)

> **Importante**: Para mantener el contexto de la conversación entre múltiples mensajes:

- **Primer mensaje**: Haga su primera llamada a `/get_response` o `/stream_response` **sin proporcionar** un `thread_id` (déjelo vacío u omítalo de la solicitud). La respuesta incluirá un valor `thread_id`.

- **Mensajes subsiguientes**: Para continuar la conversación en el mismo contexto, incluya el `thread_id` devuelto como parámetro en todas las solicitudes subsiguientes.

Esto permite que el agente mantenga el contexto entre los mensajes.

---

`POST /get_response`

Envía un mensaje a un agente y recibe una respuesta única.

**Solicitud** (parámetros de query):
```http
POST /get_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parámetros**:
- `message` (obligatorio): El mensaje a ser enviado
- `agent_id` (obligatorio): ID del agente
- `thread_id` (opcional): ID del thread para continuar una conversación

**Observaciones**:
- Para el primer mensaje, **no incluya** `thread_id`
- Para mensajes siguientes, defina `thread_id` con el valor devuelto en la respuesta anterior

**Respuesta**:
```json
{
  "response": "Agent response here",
  "thread_id": "thread-id-value"
}
```

---

`POST /stream_response`

Envía un mensaje a un agente WxO y recibe la respuesta de forma continua (SSE).

**Solicitud** (parámetros de query):
```http
POST /stream_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parámetros**:
- `message` (obligatorio): El mensaje a ser enviado
- `agent_id` (obligatorio): ID del agente
- `thread_id` (opcional): ID del thread para continuar una conversación

**Observaciones**:
- Para el primer mensaje, **no incluya** `thread_id`
- Para mensajes siguientes, defina `thread_id` con el valor devuelto en la respuesta anterior

**Respuesta**:
```http
Content-Type: text/event-stream

data: {"chunk": "Response", "thread_id": "thread-id-value"}

data: {"chunk": " chunk", "thread_id": "thread-id-value"}

data: {"chunk": " here", "thread_id": "thread-id-value"}
```

Cada bloque de datos del evento se envía en tiempo real conforme el agente procesa la respuesta.

---

**Variables de Entorno**

<table>
<tr>
<th width="30%">Variable</th>
<th>Descripción</th>
</tr>
<tr>
<td><code>IAM_API_KEY</code></td>
<td>Clave de API de IBM Cloud IAM</td>
</tr>
<tr>
<td><code>WXO_INSTANCE_ID</code></td>
<td>ID de la instancia de Watsonx Orchestrate</td>
</tr>
</table>

---

**Notas Importantes**

> **Atención**:
> - Asegúrese de que su **ID del agente** sea válido
> - Su **clave IAM** debe tener permisos suficientes para acceder a la instancia
> - El endpoint `/stream_response` usa **streaming (SSE)** para interactuar con el agente watsonx Orchestrate procesando respuestas en tiempo real

---

<div align="center">

Ahora está listo para integrar su aplicación con IBM Watson Orchestrate.

**Desarrollado por Nathalia Trazzi**

</div>