from pydantic import BaseModel
from typing import Any


class Message(BaseModel):
    number: int
    messageId: Any  
    contacts: dict
    name: str
    text: str
