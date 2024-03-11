from typing import Optional
from pydantic import BaseModel

class Princesa(BaseModel):
    id: Optional[int] = None
    nome: str | None = None
    idade: int | None = None
    filme: str | None = None