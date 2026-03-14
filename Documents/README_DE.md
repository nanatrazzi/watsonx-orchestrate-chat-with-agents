<div align="center">

# Watsonx Orchestrate Chat with Agents

### REST-API für die Kommunikation mit IBM Watsonx Orchestrate

[![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Powered-blue?style=for-the-badge&logo=ibm)](https://cloud.ibm.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org)

</div>

---

## Inhaltsverzeichnis

- [Überblick](#-überblick)
- [Verfügbare Endpoints](#-verfügbare-endpoints)
- [Wie man die Anmeldeinformationen erhält](#-wie-man-die-anmeldeinformationen-erhält)
- [Projektkonfiguration](#️-projektkonfiguration)
- [API-Dokumentation](#-api-dokumentation)
- [Umgebungsvariablen](#-umgebungsvariablen)
- [Wichtige Hinweise](#-wichtige-hinweise)

---

## Überblick

Dieses Asset bietet einen **FastAPI-basierten HTTP-Dienst**, der die Kommunikation mit **IBM Watson Orchestrate (WxO)** über drei Haupt-Endpoints ermöglicht:

<table>
<tr>
<td width="30%"><b>Endpoint</b></td>
<td><b>Beschreibung</b></td>
</tr>
<tr>
<td><code>/list_agents</code></td>
<td>Gibt eine Liste der verfügbaren Agenten in einer bestimmten watsonx Orchestrate-Instanz zurück</td>
</tr>
<tr>
<td><code>/get_response</code></td>
<td>Gibt eine einzelne Antwort von einem WxO-Agenten zurück</td>
</tr>
<tr>
<td><code>/stream_response</code></td>
<td>Überträgt die Antwort des Agenten in Echtzeit mit Server-Sent Events (SSE)</td>
</tr>
</table>

### Nützliche Links

- **Quellcode**: [GitHub Repository](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/tree/main/source/rest_api)
- **Implementierte Endpoints**: [Routes Directory](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/blob/main/source/rest_api/routes)

---


#### Eine Watsonx Orchestrate-Instanz erstellen

Nach der Anmeldung bei **IBM Cloud** geben Sie im Suchfeld `watsonx Orchestrate` ein.

<div align="center">
<img src="Build_Book_Images/wxo01.jpeg" alt="Watsonx Orchestrate suchen" width="800"/>
</div>

Wählen Sie den **Standort** Ihrer Instanz und den **Plan**, der am besten zu Ihnen passt

<div align="center">
<img src="Build_Book_Images/wxo02.jpeg" alt="Standort und Plan wählen" width="800"/>
</div>

---

Geben Sie abschließend den **Dienstnamen** ein, optional **Tags** und **Auslöse-Tags**, und wählen Sie eine **Ressourcengruppe** aus.

Akzeptieren Sie die IBM Cloud-Bedingungen auf der rechten Seite des Bildschirms und klicken Sie auf **Create**.

<div align="center">
<img src="Build_Book_Images/wxo03.jpeg" alt="Dienst konfigurieren" width="800"/>
</div>

---

Klicken Sie nach der Erstellung Ihrer Instanz auf **Launch watsonx Orchestrate**.

<div align="center">
<img src="Build_Book_Images/wxo04.jpeg" alt="Watsonx Orchestrate starten" width="800"/>
</div>

---

Um über die API mit Watsonx Orchestrate zu kommunizieren, müssen Sie zwei wesentliche Anmeldeinformationen erhalten:
- `IAM_API_KEY`
- `WXO_INSTANCE_ID`

## Wie man die watsonx Orchestrate-Anmeldeinformationen erhält

Im Symbol mit den Initialen Ihres Vor- und Nachnamens auf der rechten Seite der Benutzeroberfläche

<div align="center">
<img src="Build_Book_Images/wxo05.png" alt="Einstellungen" width="800"/>
</div>

Klicken Sie auf **Settings**.

<div align="center">
<img src="Build_Book_Images/wxo05-b.png" alt="Einstellungen" width="800"/>
</div>

Gehen Sie auf der Konfigurationsseite zur Registerkarte **API details** 

<div align="center">
<img src="Build_Book_Images/wxo06.png" alt="API-Details" width="800"/>
</div>

1. Kopieren Sie die ID Ihrer Instanz

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API-Details" width="800"/>
</div>

2. Klicken Sie dann auf `Generate API Key`

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API-Details" width="800"/>
</div>

Klicken Sie auf der nächsten Seite auf **Generate API key**.

Sie werden zum Katalog weitergeleitet, wo Sie IBM Cloud-API-Schlüssel erstellen, anzeigen und verwalten.

<div align="center">
<img src="Build_Book_Images/wxo07.jpeg" alt="API-Schlüssel generieren" width="800"/>
</div>

> **Was ist ein API-Schlüssel?**
> 
> Ein API-Schlüssel ist ein Geheimnis, das Benutzern, Anwendungen oder Diensten den authentifizierten Zugriff auf IBM Cloud ermöglicht. Er funktioniert wie ein "technisches Passwort", das in CLIs, Automatisierungen, Pipelines oder Integrationen verwendet wird.

---

**API-Schlüssel-Konfiguration**

**Name**

Geben Sie dem Schlüssel einen beschreibenden Namen, wie:
- `apikey-wxo`
- `local-development-key`

> **Tipp**: Verwenden Sie Namen, die den Zweck, den Verantwortlichen oder die Umgebung angeben.

**Description (Optional)**

Hier können Sie eine Beschreibung Ihres Schlüssels hinzufügen, um die Identifizierung zu erleichtern.

---

**Lead Action (Aktion bei Verlust)**

<table>
<tr>
<td width="40%"><b>Option</b></td>
<td><b>Beschreibung</b></td>
</tr>
<tr>
<td>🔘 <b>Disable the leaked key</b>  (empfohlen)</td>
<td>Der Schlüssel wird automatisch deaktiviert. Gute Option für die Produktion.</td>
</tr>
<tr>
<td>🔘 <b>Delete the leaked key</b></td>
<td>Der Schlüssel wird dauerhaft gelöscht.</td>
</tr>
<tr>
<td>🔘 <b>Nothing</b></td>
<td>Es wird keine Aktion durchgeführt. Nicht empfohlen.</td>
</tr>
</table>


**API Key Expiration (Ablauf)**

Sie können wählen, ob der Schlüssel automatisch ablaufen soll.

<table>
<tr>
<td width="40%"><b>Option</b></td>
<td><b>Beschreibung</b></td>
</tr>
<tr>
<td>🔘 <b>Set expiration</b></td>
<td>
Ermöglicht die Auswahl eines zukünftigen Datums.<br>
-> Ideal für temporäre Zugriffe, kurzfristige Integrationen usw.<br>
Bei Ablauf wird der Schlüssel automatisch deaktiviert.
</td>
</tr>
<tr>
<td>🔘 <b>Kein Ablauf</b> (Standard)</td>
<td>Der Schlüssel läuft nicht ab.</td>
</tr>
</table>

---

**Session Management (Sitzungsverwaltung)**

Legt fest, ob dieser Schlüssel für die Sitzungsverwaltung in IBM Cloud CLI verwendet werden kann.

<table>
<tr>
<td width="20%"><b>Option</b></td>
<td><b>Beschreibung</b></td>
</tr>
<tr>
<td>🔘 <b>Yes</b></td>
<td>Ermöglicht die Verwendung des Schlüssels für die Anmeldung bei CLI mit <code>ibmcloud login --apikey</code></td>
</tr>
<tr>
<td>🔘 <b>No</b></td>
<td>Der API-Schlüssel kann nicht für die Anmeldung bei CLI-Sitzungen verwendet werden. Verwenden Sie diese Option, wenn Sie den Schlüssel nur auf bestimmte API-Aufrufe beschränken möchten.</td>
</tr>
</table>

<div align="center">
<img src="Build_Book_Images/wxo08.jpeg" alt="API-Schlüssel-Konfigurationen" width="800"/>
</div>

---
Klicken Sie nach dem Ausfüllen aller Felder auf **Create**.

<div align="center">
<img src="Build_Book_Images/wxo09.jpeg" alt="API-Schlüssel erstellen" width="800"/>
</div>

> **WICHTIG**: Nutzen Sie diesen Moment, um Ihren API-Schlüssel zu kopieren oder herunterzuladen. Der Schlüssel ist nur für einige Sekunden verfügbar. Nach diesem Zeitraum kann er nicht mehr angezeigt werden.

<div align="center">
<img src="Build_Book_Images/wxo10.jpeg" alt="API-Schlüssel kopieren" width="800"/>
</div>

---

Nach Erhalt der Anmeldeinformationen verfügen Sie über die beiden erforderlichen Informationen für die Ausführung der Backend-Interaktion mit dem Chat Ihres Agenten (watsonx Orchestrate).


1. **Navigieren Sie zum Projektverzeichnis**:
   ```bash
   cd ./source/rest_api/
   ```

2. **Konfigurieren Sie die Umgebungsvariablen**:
   - Benennen Sie die Datei `.env_example` in `.env` um
   - Füllen Sie sie mit Ihren Anmeldeinformationen aus:
   
   ```env
   IAM_API_KEY=ihr-api-key-hier
   WXO_INSTANCE_ID=ihre-instance-id-hier
   ```

3. **Installieren Sie die Abhängigkeiten**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Starten Sie den Server**:
   ```bash
   python app.py
   ```

---

### Gesprächsverwaltung (Thread ID)

> **Wichtig**: Um den Kontext der Konversation zwischen mehreren Nachrichten beizubehalten:

- **Erste Nachricht**: Führen Sie Ihren ersten Aufruf an `/get_response` oder `/stream_response` **ohne Angabe** einer `thread_id` durch (lassen Sie sie leer oder lassen Sie sie in der Anfrage weg). Die Antwort enthält einen `thread_id`-Wert.

- **Folgende Nachrichten**: Um die Konversation im gleichen Kontext fortzusetzen, fügen Sie die zurückgegebene `thread_id` als Parameter in allen nachfolgenden Anfragen hinzu.

Dies ermöglicht es dem Agenten, den Kontext zwischen den Nachrichten beizubehalten.

---

`POST /get_response`

Sendet eine Nachricht an einen Agenten und erhält eine einzelne Antwort.

**Anfrage** (Query-Parameter):
```http
POST /get_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parameter**:
- `message` (erforderlich): Die zu sendende Nachricht
- `agent_id` (erforderlich): ID des Agenten
- `thread_id` (optional): Thread-ID zum Fortsetzen einer Konversation

**Hinweise**:
- Für die erste Nachricht **fügen Sie keine** `thread_id` hinzu
- Für folgende Nachrichten setzen Sie `thread_id` auf den in der vorherigen Antwort zurückgegebenen Wert

**Antwort**:
```json
{
  "response": "Agent response here",
  "thread_id": "thread-id-value"
}
```

---

`POST /stream_response`

Sendet eine Nachricht an einen WxO-Agenten und erhält die Antwort kontinuierlich (SSE).

**Anfrage** (Query-Parameter):
```http
POST /stream_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parameter**:
- `message` (erforderlich): Die zu sendende Nachricht
- `agent_id` (erforderlich): ID des Agenten
- `thread_id` (optional): Thread-ID zum Fortsetzen einer Konversation

**Hinweise**:
- Für die erste Nachricht **fügen Sie keine** `thread_id` hinzu
- Für folgende Nachrichten setzen Sie `thread_id` auf den in der vorherigen Antwort zurückgegebenen Wert

**Antwort**:
```http
Content-Type: text/event-stream

data: {"chunk": "Response", "thread_id": "thread-id-value"}

data: {"chunk": " chunk", "thread_id": "thread-id-value"}

data: {"chunk": " here", "thread_id": "thread-id-value"}
```

Jeder Datenblock des Ereignisses wird in Echtzeit gesendet, während der Agent die Antwort verarbeitet.

---

**Umgebungsvariablen**

<table>
<tr>
<th width="30%">Variable</th>
<th>Beschreibung</th>
</tr>
<tr>
<td><code>IAM_API_KEY</code></td>
<td>IBM Cloud IAM API-Schlüssel</td>
</tr>
<tr>
<td><code>WXO_INSTANCE_ID</code></td>
<td>ID der Watsonx Orchestrate-Instanz</td>
</tr>
</table>

---

**Wichtige Hinweise**

> **Achtung**:
> - Stellen Sie sicher, dass Ihre **Agenten-ID** gültig ist
> - Ihr **IAM-Schlüssel** muss über ausreichende Berechtigungen für den Zugriff auf die Instanz verfügen
> - Der Endpoint `/stream_response` verwendet **Streaming (SSE)**, um mit dem watsonx Orchestrate-Agenten zu interagieren und Antworten in Echtzeit zu verarbeiten

---

<div align="center">

Sie sind jetzt bereit, Ihre Anwendung mit IBM Watson Orchestrate zu integrieren.

**Entwickelt von Nathalia Trazzi**

</div>