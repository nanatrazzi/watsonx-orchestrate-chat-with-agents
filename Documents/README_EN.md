<div align="center">

# Watsonx Orchestrate Chat with Agents

### REST API for communication with IBM Watson Orchestrate

[![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Powered-blue?style=for-the-badge&logo=ibm)](https://cloud.ibm.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org)

</div>

---

## Table of Contents

- [Overview](#-overview)
- [Available Endpoints](#-available-endpoints)
- [How to Obtain Credentials](#-how-to-obtain-credentials)
- [Project Setup](#️-project-setup)
- [API Documentation](#-api-documentation)
- [Environment Variables](#-environment-variables)
- [Important Notes](#-important-notes)

---

## Overview

This asset provides a **FastAPI-based HTTP service** that enables communication with **IBM Watson Orchestrate (WxO)** through three main endpoints:

<table>
<tr>
<td width="30%"><b>Endpoint</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td><code>/list_agents</code></td>
<td>Returns a list of available agents in a given watsonx Orchestrate instance</td>
</tr>
<tr>
<td><code>/get_response</code></td>
<td>Returns a single response from a WxO agent</td>
</tr>
<tr>
<td><code>/stream_response</code></td>
<td>Streams the agent's response in real-time using Server-Sent Events (SSE)</td>
</tr>
</table>

### Useful Links

- **Source Code**: [GitHub Repository](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/tree/main/source/rest_api)
- **Implemented Endpoints**: [Routes Directory](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/blob/main/source/rest_api/routes)

---


#### Create a Watsonx Orchestrate Instance

After logging into **IBM Cloud**, type `watsonx Orchestrate` in the search field.

<div align="center">
<img src="Build_Book_Images/wxo01.jpeg" alt="Search Watsonx Orchestrate" width="800"/>
</div>

Choose the **location** for your instance and the **plan** that best suits your needs

<div align="center">
<img src="Build_Book_Images/wxo02.jpeg" alt="Choose Location and Plan" width="800"/>
</div>

---

Finally, enter the **service name**, optionally **tags** and **access management tags**, and select a **resource group**.

Accept the IBM Cloud terms on the right side of the screen and click **Create**.

<div align="center">
<img src="Build_Book_Images/wxo03.jpeg" alt="Configure Service" width="800"/>
</div>

---

With your instance created, click **Launch watsonx Orchestrate**.

<div align="center">
<img src="Build_Book_Images/wxo04.jpeg" alt="Launch Watsonx Orchestrate" width="800"/>
</div>

---

To communicate with Watsonx Orchestrate via API, you'll need to obtain two essential credentials:
- `IAM_API_KEY`
- `WXO_INSTANCE_ID`

## How to obtain watsonx Orchestrate credentials

Click on the icon with your name and surname initials on the right side of the interface

<div align="center">
<img src="Build_Book_Images/wxo05.png" alt="Settings" width="800"/>
</div>

Click on **Settings**.

<div align="center">
<img src="Build_Book_Images/wxo05-b.png" alt="Settings" width="800"/>
</div>

On the settings page, go to the **API details** tab

<div align="center">
<img src="Build_Book_Images/wxo06.png" alt="API Details" width="800"/>
</div>

1. Copy your instance ID

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

2. Next, click on `Generate API Key`

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

On the next page, click **Generate API key**.

You will be redirected to the catalog where you create, view, and work with IBM Cloud API keys.

<div align="center">
<img src="Build_Book_Images/wxo07.jpeg" alt="Generate API Key" width="800"/>
</div>

> **What is an API Key?**
> 
> An API Key is a secret that allows users, applications, or services to access IBM Cloud in an authenticated manner. It works as a "technical password" used in CLIs, automations, pipelines, or integrations.

---

**API Key Configuration**

**Name**

Give a descriptive name to the key, such as:
- `apikey-wxo`
- `local-development-key`

> **Tip**: Use names that indicate the purpose, responsible party, or environment.

**Description (Optional)**

Here you can add a description of your key, helping with its identification.

---

**Lead Action (Action in Case of Leak)**

<table>
<tr>
<td width="40%"><b>Option</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>🔘 <b>Disable the leaked key</b>  (recommended)</td>
<td>The key is automatically disabled. Good option for production.</td>
</tr>
<tr>
<td>🔘 <b>Delete the leaked key</b></td>
<td>The key is permanently deleted.</td>
</tr>
<tr>
<td>🔘 <b>Nothing</b></td>
<td>No action is taken. Not recommended.</td>
</tr>
</table>


**API Key Expiration**

You can choose whether the key should expire automatically.

<table>
<tr>
<td width="40%"><b>Option</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>🔘 <b>Set expiration</b></td>
<td>
Allows you to choose a future date.<br>
-> Ideal for temporary access, short-term integrations, etc.<br>
When it expires, the key is automatically disabled.
</td>
</tr>
<tr>
<td>🔘 <b>No expiration</b> (default)</td>
<td>The key does not expire.</td>
</tr>
</table>

---

**Session Management**

Defines whether this key can be used for session management in IBM Cloud CLI.

<table>
<tr>
<td width="20%"><b>Option</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>🔘 <b>Yes</b></td>
<td>Allows the key to be used to log in to CLI with <code>ibmcloud login --apikey</code></td>
</tr>
<tr>
<td>🔘 <b>No</b></td>
<td>The API Key cannot be used to log in to CLI sessions. Use when you want to restrict the key only to specific API calls.</td>
</tr>
</table>

<div align="center">
<img src="Build_Book_Images/wxo08.jpeg" alt="API Key Settings" width="800"/>
</div>

---
After filling everything out, click **Create**.

<div align="center">
<img src="Build_Book_Images/wxo09.jpeg" alt="Create API Key" width="800"/>
</div>

> **IMPORTANT**: Take this moment to copy or download your API Key. The key will be available for a few seconds. After this period, it will no longer be possible to view it again.

<div align="center">
<img src="Build_Book_Images/wxo10.jpeg" alt="Copy API Key" width="800"/>
</div>

---

After obtaining the credentials, you now have the two pieces of information needed to execute backend interaction with your agent's chat (watsonx Orchestrate).


1. **Navigate to the project directory**:
   ```bash
   cd ./source/rest_api/
   ```

2. **Configure environment variables**:
   - Rename the `.env_example` file to `.env`
   - Fill in with your credentials:
   
   ```env
   IAM_API_KEY=your-api-key-here
   WXO_INSTANCE_ID=your-instance-id-here
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   ```bash
   python app.py
   ```

---

### Conversation Management (Thread ID)

> **Important**: To maintain conversation context between multiple messages:

- **First message**: Make your first call to `/get_response` or `/stream_response` **without providing** a `thread_id` (leave empty or omit from the request). The response will include a `thread_id` value.

- **Subsequent messages**: To continue the conversation in the same context, include the returned `thread_id` as a parameter in all subsequent requests.

This allows the agent to maintain context between messages.

---

`POST /get_response`

Sends a message to an agent and receives a single response.

**Request** (query parameters):
```http
POST /get_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parameters**:
- `message` (required): The message to be sent
- `agent_id` (required): Agent ID
- `thread_id` (optional): Thread ID to continue a conversation

**Notes**:
- For the first message, **do not include** `thread_id`
- For subsequent messages, set `thread_id` with the value returned in the previous response

**Response**:
```json
{
  "response": "Agent response here",
  "thread_id": "thread-id-value"
}
```

---

`POST /stream_response`

Sends a message to a WxO agent and receives the response continuously (SSE).

**Request** (query parameters):
```http
POST /stream_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parameters**:
- `message` (required): The message to be sent
- `agent_id` (required): Agent ID
- `thread_id` (optional): Thread ID to continue a conversation

**Notes**:
- For the first message, **do not include** `thread_id`
- For subsequent messages, set `thread_id` with the value returned in the previous response

**Response**:
```http
Content-Type: text/event-stream

data: {"chunk": "Response", "thread_id": "thread-id-value"}

data: {"chunk": " chunk", "thread_id": "thread-id-value"}

data: {"chunk": " here", "thread_id": "thread-id-value"}
```

Each event data chunk is sent in real-time as the agent processes the response.

---

**Environment Variables**

<table>
<tr>
<th width="30%">Variable</th>
<th>Description</th>
</tr>
<tr>
<td><code>IAM_API_KEY</code></td>
<td>IBM Cloud IAM API Key</td>
</tr>
<tr>
<td><code>WXO_INSTANCE_ID</code></td>
<td>Watsonx Orchestrate instance ID</td>
</tr>
</table>

---

**Important Notes**

> **Attention**:
> - Make sure your **agent ID** is valid
> - Your **IAM key** must have sufficient permissions to access the instance
> - The `/stream_response` endpoint uses **streaming (SSE)** to interact with the watsonx Orchestrate agent processing responses in real-time

---

<div align="center">

Now you're ready to integrate your application with IBM Watson Orchestrate.

**Developed by Nathalia Trazzi**

</div>