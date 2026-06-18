from pydantic import BaseModel
from typing import Optional



class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    id: int
    title: str
    content: str
    tag: Optional[str] = None

    model_config = {
        'from_atributes': True
    }
