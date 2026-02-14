import os, json, requests
from dotenv import load_dotenv
from .stream_content import stream_response_from_wxo_agent

load_dotenv()

IAM_API_KEY = os.getenv("IAM_API_KEY")
WXO_INSTANCE_ID = os.getenv("WXO_INSTANCE_ID")

# Change us-south to according the region where your instance is on IBM Cloud. (e.g: us-south, eu-de, us-east, au-syd, ca-to, br-sao)
REGION_IBM_CLOUD = "us-south"
IAM_API_KEY = ""
WXO_INSTANCE_ID = ""

base_url = f"https://api.{REGION_IBM_CLOUD}.watson-orchestrate.cloud.ibm.com/instances/{WXO_INSTANCE_ID}/v1/orchestrate"

def list_all_agents():
    """
    Function responsible to retrieve a list of all agents from watsonx Orchestrate.

    Returns:
        dict: A dictionary with a single key "agents", mapping to a list of dictionaries.
        Each dictionary contains:
            - "agent_id" (str): The unique identifier of the agent.
            - "name" (str): The display name of the agent.
    """
    headers = {
        'IAM-API_KEY': IAM_API_KEY,
        'Content-Type': 'application/json'
    }
    url = f"{base_url}/agents"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.content.decode("utf-8"))

    data = response.json()
    return {"agents": [{"agent_id": agent["id"], "name": agent["display_name"]} for agent in data]}

def get_agent_response(message: str, agent_id: str, thread_id: str = None):
    """
    Function responsivle to sends a message to a specified agent and retrieves the response via a streaming API.

    Args
    --------
        message (str): The user's message to be sent to the agent.
        agent_id (str): The unique identifier of the agent to receive the message.
        thread_id (str, optional): An optional thread ID to maintain conversation context.

    Returns:
        dict: A dictionary containing:
            - "response" (str): The agent's reply message.
            - "thread_id" (str): The thread ID associated with the conversation.
    """

    payload = {
        "message": {"role": "user", "content": message},
        "additional_properties": {},
        "context": {},
        "agent_id": agent_id
    }
    if thread_id:
        payload["thread_id"] = thread_id

    headers = {
        'IAM-API_KEY': IAM_API_KEY,
        'Content-Type': 'application/json'
    }
    url = f"{base_url}/runs/stream"

    response = requests.post(url, headers=headers, data=json.dumps(payload), stream=True)
    if response.status_code != 200:
        raise Exception(response.content.decode("utf-8"))

    answer = ""
    for line in response.iter_lines():
        if line:
            try:
                decoded = line.decode("utf-8")
                event_data = json.loads(decoded)
                if event_data.get("event") == "message.created":
                    answer = event_data["data"]["message"]["content"][0]["text"]
                    thread_id = event_data["data"].get("thread_id", "")
                    break
            except json.JSONDecodeError:
                continue
    return {"response": answer, "thread_id": thread_id}

def stream_agent_response(message: str, agent_id: str, thread_id: str = None):
    """
    Function responsible to send a message to a specified agent and returns a streaming response handler.

    This function constructs a payload with the user's message and agent ID, optionally including
    a thread ID to maintain conversation context. It sends a POST request to the `/runs/stream`
    endpoint and returns the result of the streaming response handler.

    Args:
        message (str): The user's message to be sent to the agent.
        agent_id (str): The unique identifier of the agent to receive the message.
        thread_id (str, optional): An optional thread ID to maintain conversation context.

    Raises:
        Exception: If the API response status code is not 200, an exception is raised with the
        decoded error message.

    Returns:
        Generator: A generator object returned by `stream_response_from_wxo_agent`, which yields
        streamed response data from the agent.
    """

    payload = {
        "message": {"role": "user", "content": message},
        "additional_properties": {},
        "context": {},
        "agent_id": agent_id
    }
    if thread_id:
        payload["thread_id"] = thread_id

    headers = {
        'IAM-API_KEY': IAM_API_KEY,
        'Content-Type': 'application/json'
    }

    url = f"{base_url}/runs/stream"
    response = requests.post(url, headers=headers, data=json.dumps(payload), stream=True)

    if response.status_code != 200:
        raise Exception(response.content.decode("utf-8"))

    return stream_response_from_wxo_agent(response)