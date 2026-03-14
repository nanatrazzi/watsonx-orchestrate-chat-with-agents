<div align="center">

# Watsonx Orchestrate Chat with Agents

### API REST pour la communication avec IBM Watsonx Orchestrate

[![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Powered-blue?style=for-the-badge&logo=ibm)](https://cloud.ibm.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org)

</div>

---

## Sommaire

- [Vue d'ensemble](#-vue-densemble)
- [Endpoints Disponibles](#-endpoints-disponibles)
- [Comment Obtenir les Identifiants](#-comment-obtenir-les-identifiants)
- [Configuration du Projet](#️-configuration-du-projet)
- [Documentation de l'API](#-documentation-de-lapi)
- [Variables d'Environnement](#-variables-denvironnement)
- [Notes Importantes](#-notes-importantes)

---

## Vue d'ensemble

Cet asset fournit un **service HTTP basé sur FastAPI** qui permet la communication avec **IBM Watson Orchestrate (WxO)** via trois endpoints principaux :

<table>
<tr>
<td width="30%"><b>Endpoint</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td><code>/list_agents</code></td>
<td>Retourne une liste d'agents disponibles dans une instance donnée de watsonx Orchestrate</td>
</tr>
<tr>
<td><code>/get_response</code></td>
<td>Retourne une réponse unique d'un agent WxO</td>
</tr>
<tr>
<td><code>/stream_response</code></td>
<td>Transmet la réponse de l'agent en temps réel en utilisant Server-Sent Events (SSE)</td>
</tr>
</table>

### Liens Utiles

- **Code Source** : [GitHub Repository](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/tree/main/source/rest_api)
- **Endpoints Implémentés** : [Routes Directory](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/blob/main/source/rest_api/routes)

---


#### Créer une Instance de Watsonx Orchestrate

Après vous être connecté à **IBM Cloud**, dans le champ de recherche, tapez `watsonx Orchestrate`.

<div align="center">
<img src="Build_Book_Images/wxo01.jpeg" alt="Rechercher Watsonx Orchestrate" width="800"/>
</div>

Choisissez la **location** de votre instance et le **plan** qui vous convient le mieux

<div align="center">
<img src="Build_Book_Images/wxo02.jpeg" alt="Choisir Location et Plan" width="800"/>
</div>

---

Enfin, saisissez le **nom du service**, optionnellement des **tags** et des **tags de déclenchement**, et sélectionnez un **resource group**.

Acceptez les conditions d'IBM Cloud sur le côté droit de l'écran et cliquez sur **Create**.

<div align="center">
<img src="Build_Book_Images/wxo03.jpeg" alt="Configurer le Service" width="800"/>
</div>

---

Avec votre instance créée, cliquez sur **Launch watsonx Orchestrate**.

<div align="center">
<img src="Build_Book_Images/wxo04.jpeg" alt="Launch Watsonx Orchestrate" width="800"/>
</div>

---

Pour communiquer avec Watsonx Orchestrate via l'API, vous devrez obtenir deux identifiants essentiels :
- `IAM_API_KEY`
- `WXO_INSTANCE_ID`

## Comment obtenir les identifiants de watsonx Orchestrate

Dans l'icône des initiales de votre nom et prénom sur le côté droit de l'interface

<div align="center">
<img src="Build_Book_Images/wxo05.png" alt="Settings" width="800"/>
</div>

Cliquez sur **Settings**.

<div align="center">
<img src="Build_Book_Images/wxo05-b.png" alt="Settings" width="800"/>
</div>

Dans la page de configuration, accédez à l'onglet **API details** 

<div align="center">
<img src="Build_Book_Images/wxo06.png" alt="API Details" width="800"/>
</div>

1. Copiez l'ID de votre instance

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

2. Ensuite, cliquez sur `Generate API Key`

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

Sur la page suivante, cliquez sur **Generate API key**.

Vous serez redirigé vers le catalogue où vous créez, visualisez et travaillez avec les clés API d'IBM Cloud.

<div align="center">
<img src="Build_Book_Images/wxo07.jpeg" alt="Generate API Key" width="800"/>
</div>

> **Qu'est-ce qu'une API Key ?**
> 
> Une API Key est un secret qui permet aux utilisateurs, applications ou services d'accéder à IBM Cloud de manière authentifiée. Elle fonctionne comme un "mot de passe technique" utilisé dans les CLIs, automatisations, pipelines ou intégrations.

---

**Configuration de l'API Key**

**Name (Nom)**

Donnez un nom descriptif à la clé, comme :
- `apikey-wxo`
- `local-development-key`

> **Conseil** : Utilisez des noms qui indiquent l'objectif, le responsable ou l'environnement.

**Description (Optionnel)**

Ici, vous pouvez ajouter une description de votre clé, aidant à son identification.

---

**Lead Action (Action en Cas de Fuite)**

<table>
<tr>
<td width="40%"><b>Option</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>🔘 <b>Disable the leaked key</b>  (recommandé)</td>
<td>La clé est automatiquement désactivée. Bonne option pour la production.</td>
</tr>
<tr>
<td>🔘 <b>Delete the leaked key</b></td>
<td>La clé est supprimée définitivement.</td>
</tr>
<tr>
<td>🔘 <b>Nothing</b></td>
<td>Aucune action n'est prise. Non recommandé.</td>
</tr>
</table>


**API Key Expiration (Expiration)**

Vous pouvez choisir si la clé doit expirer automatiquement.

<table>
<tr>
<td width="40%"><b>Option</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>🔘 <b>Set expiration</b></td>
<td>
Permet de choisir une date future.<br>
-> Idéal pour les accès temporaires, intégrations à court terme, etc.<br>
Lorsqu'elle expire, la clé est automatiquement désactivée.
</td>
</tr>
<tr>
<td>🔘 <b>Sans expiration</b> (par défaut)</td>
<td>La clé n'expire pas.</td>
</tr>
</table>

---

**Session Management (Gestion de Session)**

Définit si cette clé peut être utilisée pour la gestion de sessions dans IBM Cloud CLI.

<table>
<tr>
<td width="20%"><b>Option</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>🔘 <b>Yes</b></td>
<td>Permet d'utiliser la clé pour se connecter au CLI avec <code>ibmcloud login --apikey</code></td>
</tr>
<tr>
<td>🔘 <b>No</b></td>
<td>L'API Key ne pourra pas être utilisée pour se connecter aux sessions CLI. Utilisez cette option lorsque vous souhaitez restreindre la clé uniquement aux appels API spécifiques.</td>
</tr>
</table>

<div align="center">
<img src="Build_Book_Images/wxo08.jpeg" alt="Configurations de l'API Key" width="800"/>
</div>

---
Après avoir tout rempli, cliquez sur **Create**.

<div align="center">
<img src="Build_Book_Images/wxo09.jpeg" alt="Créer API Key" width="800"/>
</div>

> **IMPORTANT** : Profitez de ce moment pour copier ou télécharger votre API Key. La clé sera disponible pendant quelques secondes. Après cette période, il ne sera plus possible de la visualiser à nouveau.

<div align="center">
<img src="Build_Book_Images/wxo10.jpeg" alt="Copier API Key" width="800"/>
</div>

---

Après avoir obtenu les identifiants, vous disposez des deux informations nécessaires pour l'exécution de l'interaction via backend avec le chat de votre agent (watsonx Orchestrate).


1. **Naviguez vers le répertoire du projet** :
   ```bash
   cd ./source/rest_api/
   ```

2. **Configurez les variables d'environnement** :
   - Renommez le fichier `.env_example` en `.env`
   - Remplissez avec vos identifiants :
   
   ```env
   IAM_API_KEY=votre-api-key-ici
   WXO_INSTANCE_ID=votre-instance-id-ici
   ```

3. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Exécutez le serveur** :
   ```bash
   python app.py
   ```

---

### Gestion des Conversations (Thread ID)

> **Important** : Pour maintenir le contexte de la conversation entre plusieurs messages :

- **Premier message** : Effectuez votre premier appel à `/get_response` ou `/stream_response` **sans fournir** de `thread_id` (laissez vide ou omettez de la requête). La réponse inclura une valeur `thread_id`.

- **Messages suivants** : Pour continuer la conversation dans le même contexte, incluez le `thread_id` retourné comme paramètre dans toutes les requêtes suivantes.

Cela permet à l'agent de maintenir le contexte entre les messages.

---

`POST /get_response`

Envoie un message à un agent et reçoit une réponse unique.

**Requête** (paramètres de query) :
```http
POST /get_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Paramètres** :
- `message` (obligatoire) : Le message à envoyer
- `agent_id` (obligatoire) : ID de l'agent
- `thread_id` (optionnel) : ID du thread pour continuer une conversation

**Observations** :
- Pour le premier message, **n'incluez pas** `thread_id`
- Pour les messages suivants, définissez `thread_id` avec la valeur retournée dans la réponse précédente

**Réponse** :
```json
{
  "response": "Agent response here",
  "thread_id": "thread-id-value"
}
```

---

`POST /stream_response`

Envoie un message à un agent WxO et reçoit la réponse de manière continue (SSE).

**Requête** (paramètres de query) :
```http
POST /stream_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Paramètres** :
- `message` (obligatoire) : Le message à envoyer
- `agent_id` (obligatoire) : ID de l'agent
- `thread_id` (optionnel) : ID du thread pour continuer une conversation

**Observations** :
- Pour le premier message, **n'incluez pas** `thread_id`
- Pour les messages suivants, définissez `thread_id` avec la valeur retournée dans la réponse précédente

**Réponse** :
```http
Content-Type: text/event-stream

data: {"chunk": "Response", "thread_id": "thread-id-value"}

data: {"chunk": " chunk", "thread_id": "thread-id-value"}

data: {"chunk": " here", "thread_id": "thread-id-value"}
```

Chaque bloc de données de l'événement est envoyé en temps réel au fur et à mesure que l'agent traite la réponse.

---

**Variables d'Environnement**

<table>
<tr>
<th width="30%">Variable</th>
<th>Description</th>
</tr>
<tr>
<td><code>IAM_API_KEY</code></td>
<td>Clé API d'IBM Cloud IAM</td>
</tr>
<tr>
<td><code>WXO_INSTANCE_ID</code></td>
<td>ID de l'instance de Watsonx Orchestrate</td>
</tr>
</table>

---

**Notes Importantes**

> **Attention** :
> - Assurez-vous que votre **ID d'agent** est valide
> - Votre **clé IAM** doit avoir des permissions suffisantes pour accéder à l'instance
> - L'endpoint `/stream_response` utilise le **streaming (SSE)** pour interagir avec l'agent watsonx Orchestrate en traitant les réponses en temps réel

---

<div align="center">

Vous êtes maintenant prêt à intégrer votre application avec IBM Watson Orchestrate.

**Développé par Nathalia Trazzi**

</div>