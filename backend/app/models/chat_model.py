from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    prompt: str
    architecture: List[str]
    database: str
    question: str
