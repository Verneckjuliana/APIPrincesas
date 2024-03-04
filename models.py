from typing import Optional
from pydantic import BaseModel

class Princesa(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    filme: str