from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class MuestraBase(BaseModel):
    codigo: str
    tipo: str
    ubicacion: str
    fecha_recoleccion: datetime
    observaciones: Optional[str] = None

class MuestraCreate(MuestraBase):
    usuario_id: str

class MuestraUpdate(BaseModel):
    codigo: Optional[str] = None
    tipo: Optional[str] = None
    ubicacion: Optional[str] = None
    fecha_recoleccion: Optional[datetime] = None
    estado: Optional[str] = None
    observaciones: Optional[str] = None
    resultados: Optional[Dict[str, Any]] = None

class Muestra(MuestraBase):
    id: str
    estado: str = "pendiente"
    usuario_id: str
    resultados: Optional[Dict[str, Any]] = None
    fecha_creacion: Optional[datetime] = None

    class Config:
        from_attributes = True
