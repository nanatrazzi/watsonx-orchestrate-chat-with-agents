<div align="center">

# Watsonx Orchestrate Chat with Agents

### API REST para comunicação com IBM Watsonx Orchestrate

[![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Powered-blue?style=for-the-badge&logo=ibm)](https://cloud.ibm.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org)

</div>

---

## Indice

- [Visão Geral](#-visão-geral)
- [Endpoints Disponíveis](#-endpoints-disponíveis)
- [Como Obter as Credenciais](#-como-obter-as-credenciais)
- [Configuração do Projeto](#️-configuração-do-projeto)
- [Documentação da API](#-documentação-da-api)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [Notas Importantes](#-notas-importantes)

---

## Visão Geral

Este asset fornece um **serviço HTTP baseado em FastAPI** que permite a comunicação com o **IBM Watson Orchestrate (WxO)** por meio de três endpoints principais:

<table>
<tr>
<td width="30%"><b>Endpoint</b></td>
<td><b>Descrição</b></td>
</tr>
<tr>
<td><code>/list_agents</code></td>
<td>Retorna uma lista de agentes disponíveis em uma determinada instância de watsonx Orchestrate</td>
</tr>
<tr>
<td><code>/get_response</code></td>
<td>Retorna uma única resposta de um agente WxO</td>
</tr>
<tr>
<td><code>/stream_response</code></td>
<td>Transmite a resposta do agente em tempo real usando Server-Sent Events (SSE)</td>
</tr>
</table>

### Links Úteis

- **Código Fonte**: [GitHub Repository](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/tree/main/source/rest_api)
- **Endpoints Implementados**: [Routes Directory](https://github.com/nanatrazzi/watsonx-orchestrate-chat-with-agents/blob/main/source/rest_api/routes)

---


#### Criar uma Instância do Watsonx Orchestrate

Após fazer login na **IBM Cloud**, no campo de pesquisa digite `watsonx Orchestrate`.

<div align="center">
<img src="Build_Book_Images/wxo01.jpeg" alt="Pesquisar Watsonx Orchestrate" width="800"/>
</div>

Escolha a **location** de sua instância e o **plano** que lhe atende melhor

<div align="center">
<img src="Build_Book_Images/wxo02.jpeg" alt="Escolher Location e Plan" width="800"/>
</div>

---

Por fim, digite o **nome do serviço**, opcionalmente **tags** e **tags de acionamento**, e selecione um **resource group**.

Aceite os termos da IBM Cloud ao lado direito da tela e clique em **Create**.

<div align="center">
<img src="Build_Book_Images/wxo03.jpeg" alt="Configurar Serviço" width="800"/>
</div>

---

Com sua instância criada, clique em **Launch watsonx Orchestrate**.

<div align="center">
<img src="Build_Book_Images/wxo04.jpeg" alt="Launch Watsonx Orchestrate" width="800"/>
</div>

---

Para se comunicar com o Watsonx Orchestrate via API, você precisará obter duas credenciais essenciais:
- `IAM_API_KEY`
- `WXO_INSTANCE_ID`

## Como obter as credenciais do watsonx Orchestrate

No ícone da sigla de seu nome e sobrenome ao lado direito da interface

<div align="center">
<img src="Build_Book_Images/wxo05.png" alt="Settings" width="800"/>
</div>

Clique em **Settings**.

<div align="center">
<img src="Build_Book_Images/wxo05-b.png" alt="Settings" width="800"/>
</div>

Na página de configuração e entre na aba **API details** 

<div align="center">
<img src="Build_Book_Images/wxo06.png" alt="API Details" width="800"/>
</div>

1. Copie o ID de sua instância

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

2. Em seguida, clique em `Generate API Key`

<div align="center">
<img src="Build_Book_Images/wxo06-b.png" alt="API Details" width="800"/>
</div>

Na próxima página, clique em **Generate API key**.

Você será redirecionado para o catálogo onde você cria, visualiza e trabalha com chaves de API da IBM Cloud.

<div align="center">
<img src="Build_Book_Images/wxo07.jpeg" alt="Generate API Key" width="800"/>
</div>

> **O que é uma API Key?**
> 
> Uma API Key é um segredo que permite que usuários, aplicações ou serviços acessem a IBM Cloud de forma autenticada. Ela funciona como uma "senha técnica" usada em CLIs, automações, pipelines ou integrações.

---

**Configuração da API Key**

**Name (Nome)**

Dê um nome descritivo para a chave, como:
- `apikey-wxo`
- `local-development-key`

> **Dica**: Use nomes que indiquem o propósito, responsável ou ambiente.

**Description (Opcional)**

Aqui você pode adicionar uma descrição da sua chave, ajudando na identificação dela.

---

**Lead Action (Ação em Caso de Vazamento)**

<table>
<tr>
<td width="40%"><b>Opção</b></td>
<td><b>Descrição</b></td>
</tr>
<tr>
<td>🔘 <b>Disable the leaked key</b>  (recomendado)</td>
<td>A chave é automaticamente desativada. Boa opção para produção.</td>
</tr>
<tr>
<td>🔘 <b>Delete the leaked key</b></td>
<td>A chave é deletada permanentemente.</td>
</tr>
<tr>
<td>🔘 <b>Nothing</b></td>
<td>Nenhuma ação é tomada. Não recomendado.</td>
</tr>
</table>


**API Key Expiration (Expiração)**

Você pode escolher se a chave deve expirar automaticamente.

<table>
<tr>
<td width="40%"><b>Opção</b></td>
<td><b>Descrição</b></td>
</tr>
<tr>
<td>🔘 <b>Set expiration</b></td>
<td>
Permite escolher uma data futura.<br>
-> Ideal para acessos temporários, integrações de curto prazo, etc.<br>
Quando expirar, a chave é automaticamente desabilitada.
</td>
</tr>
<tr>
<td>🔘 <b>Sem expiração</b> (default)</td>
<td>A chave não expira.</td>
</tr>
</table>

---

**Session Management (Gerenciamento de Sessão)**

Define se esta chave pode ser usada para gerenciamento de sessões no IBM Cloud CLI.

<table>
<tr>
<td width="20%"><b>Opção</b></td>
<td><b>Descrição</b></td>
</tr>
<tr>
<td>🔘 <b>Yes</b></td>
<td>Permite que a chave seja usada para fazer login no CLI com <code>ibmcloud login --apikey</code></td>
</tr>
<tr>
<td>🔘 <b>No</b></td>
<td>A API Key não poderá ser usada para login em sessões CLI. Use quando desejar restringir a chave apenas para chamadas específicas de API.</td>
</tr>
</table>

<div align="center">
<img src="Build_Book_Images/wxo08.jpeg" alt="Configurações da API Key" width="800"/>
</div>

---
Após preencher tudo, clique em **Create**.

<div align="center">
<img src="Build_Book_Images/wxo09.jpeg" alt="Criar API Key" width="800"/>
</div>

> **IMPORTANTE**: Aproveite esse momento para copiar ou fazer o download sua API Key. A chave ficará disponível por alguns segundos. Após esse período, não será mais possível visualizá-la novamente.

<div align="center">
<img src="Build_Book_Images/wxo10.jpeg" alt="Copiar API Key" width="800"/>
</div>

---

Após obter as credenciais, você já possui as duas informações necessárias para a execução da interação via backend com o chat do seu agent (watsonx Orchestrate).


1. **Navegue até o diretório do projeto**:
   ```bash
   cd ./source/rest_api/
   ```

2. **Configure as variáveis de ambiente**:
   - Altere o nome do arquivo `.env_example` para `.env`
   - Preencha com suas credenciais:
   
   ```env
   IAM_API_KEY=sua-api-key-aqui
   WXO_INSTANCE_ID=seu-instance-id-aqui
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o servidor**:
   ```bash
   python app.py
   ```

---

### Gerenciamento de Conversas (Thread ID)

> **Importante**: Para manter o contexto da conversa entre múltiplas mensagens:

- **Primeira mensagem**: Faça sua primeira chamada para `/get_response` ou `/stream_response` **sem fornecer** um `thread_id` (deixe vazio ou omita da requisição). A resposta incluirá um valor `thread_id`.

- **Mensagens subsequentes**: Para continuar a conversa no mesmo contexto, inclua o `thread_id` retornado como parâmetro em todas as requisições subsequentes.

Isso permite que o agente mantenha o contexto entre as mensagens.

---

`POST /get_response`

Envia uma mensagem para um agente e recebe uma resposta única.

**Requisição** (parâmetros de query):
```http
POST /get_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parâmetros**:
- `message` (obrigatório): A mensagem a ser enviada
- `agent_id` (obrigatório): ID do agente
- `thread_id` (opcional): ID da thread para continuar uma conversa

**Observações**:
- Para a primeira mensagem, **não inclua** `thread_id`
- Para mensagens seguintes, defina `thread_id` com o valor retornado na resposta anterior

**Resposta**:
```json
{
  "response": "Agent response here",
  "thread_id": "thread-id-value"
}
```

---

`POST /stream_response`

Envia uma mensagem para um agente WxO e recebe a resposta de forma contínua (SSE).

**Requisição** (parâmetros de query):
```http
POST /stream_response?message=Hello&agent_id=your-agent-id[&thread_id=optional-thread-id]
```

**Parâmetros**:
- `message` (obrigatório): A mensagem a ser enviada
- `agent_id` (obrigatório): ID do agente
- `thread_id` (opcional): ID da thread para continuar uma conversa

**Observações**:
- Para a primeira mensagem, **não inclua** `thread_id`
- Para mensagens seguintes, defina `thread_id` com o valor retornado na resposta anterior

**Resposta**:
```http
Content-Type: text/event-stream

data: {"chunk": "Response", "thread_id": "thread-id-value"}

data: {"chunk": " chunk", "thread_id": "thread-id-value"}

data: {"chunk": " here", "thread_id": "thread-id-value"}
```

Cada bloco de dados do evento é enviado em tempo real conforme o agente processa a resposta.

---

**Variáveis de Ambiente**

<table>
<tr>
<th width="30%">Variável</th>
<th>Descrição</th>
</tr>
<tr>
<td><code>IAM_API_KEY</code></td>
<td>Chave de API do IBM Cloud IAM</td>
</tr>
<tr>
<td><code>WXO_INSTANCE_ID</code></td>
<td>ID da instância do Watsonx Orchestrate</td>
</tr>
</table>

---

**Notas Importantes**

> **Atenção**:
> - Certifique-se de que seu **ID do agente** seja válido
> - Sua **chave IAM** deve ter permissões suficientes para acessar a instância
> - O endpoint `/stream_response` usa **streaming (SSE)** para interagir com o agente watsonx Orchestrate processando respostas em tempo real

---

<div align="center">

Agora você está pronto para integrar seu aplicativo com o IBM Watson Orchestrate.

**Desenvolvido por Nathalia Trazzi**

</div>
