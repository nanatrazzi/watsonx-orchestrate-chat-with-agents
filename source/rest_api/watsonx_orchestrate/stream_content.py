import json
from models.models import AgentResponse

def stream_content(response):
    """
    Function responsible to stream content from a response iterable, formatting each chunk as a Server-Sent Event (SSE).

    Args:
        response (Iterable[dict]): An iterable of response chunks, where each chunk is a dictionary
            containing the keys "answer" and "thread_id".

    Yields:
        str: A formatted string in SSE format containing the serialized AgentResponse object.
    """
    for chunk in response:
        data = AgentResponse(response=chunk["answer"], thread_id=chunk["thread_id"])
        yield f"data: {data.model_dump_json()}\n\n"


def stream_response_from_wxo_agent(response):
    """
    Function responsible to processes a streaming response from watsonx Orchestrate agent and deliver a message content.

    Args:
        response (requests.Response): A streamed HTTP response object from watsonx Orchestrate API.

    Returns:
        dict: A dictionary containing:
            - "answer" (str): A partial piece of the agent's response text.
            - "thread_id" (str): The thread ID associated with the conversation.
    """
    for line in response.iter_lines():
                if line:
                    try:
                        decoded = line.decode("utf-8")
                        event_data = json.loads(decoded)
                        if event_data.get("event") == "message.delta":
                            answer = event_data["data"]["delta"]["content"][0]["text"]
                            thread_id = event_data["data"].get("thread_id", "")
                            yield {"answer": answer, "thread_id": thread_id}
                    except json.JSONDecodeError:
                        continue