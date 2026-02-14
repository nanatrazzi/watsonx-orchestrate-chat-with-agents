import json
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from typing import Optional
from models.models import AgentListResponse, AgentResponse
from watsonx_orchestrate.functions import *

router = APIRouter()

@router.get("/list_agents", response_model=AgentListResponse)
async def list_agents():
    """
    Endpoint responsible to retrieve a list of all available agents.

    Returns:
        AgentListResponse: A response model containing a list of agents with their IDs and names.

    """
    try:
        return list_all_agents()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/get_response", response_model=AgentResponse)
async def get_response(message: str, agent_id: str, thread_id: Optional[str] = None):
    """
    Endpoint responsible to send a message to a specified agent and retrieve its response.

    Args:
        message (str): The user's message to be sent to the agent.
        agent_id (str): The unique identifier of the agent to respond.
        thread_id (Optional[str]): An optional thread ID to maintain conversation context.

    Returns:
            AgentResponse: A response model containing the agent's reply and the thread ID.

    """
    try:
        return get_agent_response(message, agent_id, thread_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/stream_response", response_model=AgentResponse, response_class=StreamingResponse, 
            responses={200: {"content": {"text/event-stream": {"schema": {"$ref": "#/components/schemas/AgentResponse"}}},
                            "description": "A streaming response of answer."}})
async def stream_response(message: str, agent_id: str, thread_id: Optional[str] = None):

    """ 
    Function responsible to stream SSE response by aggregating responses from watsonx Orchestrate.

    Args:
        message (str): The user message to be processed by the agent.
        agent_id (str): Identifier of the agent that will handle the request.
        thread_id (Optional[str]): Optional conversation thread ID. If not provided, it will be resolved dynamically.

    Returns:
        StreamingResponse: A streaming HTTP response with `text/event-stream` media type, 
        sending incremental JSON payloads containing:
            - answer (str): Partial or complete response text.
            - thread_id (str): The resolved thread identifier for the conversation.
    """
    async def event_stream():
        buffer = ""
        resolved_thread_id = thread_id

        for chunk in stream_agent_response(message, agent_id, thread_id):
            if isinstance(chunk, dict) and chunk.get("thread_id"):
                resolved_thread_id = chunk["thread_id"]

            part = chunk.get("answer", "")
            buffer += part

            if (
                buffer.endswith(" ")
                or buffer.endswith(".")
                or buffer.endswith("?")
                or buffer.endswith("!")
                or buffer.endswith(",")
            ):
                yield f"data: {json.dumps({'answer': buffer, 'thread_id': resolved_thread_id})}\n\n"
                buffer = ""

        if buffer:
            yield f"data: {json.dumps({'answer': buffer, 'thread_id': resolved_thread_id})}\n\n"

    try:
        return StreamingResponse(event_stream(), media_type="text/event-stream")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))