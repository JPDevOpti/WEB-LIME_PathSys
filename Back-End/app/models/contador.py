from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContadorBase(BaseModel):
    año: int
    ultimo_numero: int = 0

class ContadorCreate(ContadorBase):
    pass

class ContadorUpdate(BaseModel):
    ultimo_numero: Optional[int] = None

class Contador(ContadorBase):
    id: str
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
