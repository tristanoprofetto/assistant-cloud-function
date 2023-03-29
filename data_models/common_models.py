from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel

 
class IncommingRequest(BaseModel):
    id: str
    message: str


class ChatResponse(BaseModel):
    id: str
    object: str = None
    created: int = None
    model: str = None
    usage: Dict[None]
    choices: List[Dict[None]]


class ChatChoicesResponse(BaseModel):
    message: Dict[str, str]
    finish_reason: str
    index: int
 

class ChatUsageResponse(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int