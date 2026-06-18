from pydantic import BaseModel
from typing import Optional



class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: str = None
    content: str = None
    tag: Optional[str] = None

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    tag: Optional[str] = None

    model_config = {'from_attributes': True}
