from typing import List
from pydantic import BaseModel


class AgentResponse(BaseModel):
    response: str
    thread_id: str

class AgentListResponse(BaseModel):
    agents: List[dict]