from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class CupsItem(BaseModel):
    code: str
    cantidad: int = 1

class MuestraIndividual(BaseModel):
    numero: int
    region_cuerpo: str
    cups: List[CupsItem]

class MuestraBase(BaseModel):
    medico_solicitante: Optional[str] = None
    fecha_ingreso: datetime
    observaciones: Optional[str] = None
    # Agregar nombre del paciente y entidad
    nombre_paciente: str
    entidad: str
    muestras: List[MuestraIndividual]  # Múltiples muestras por solicitud

class MuestraCreate(MuestraBase):
    codigo_muestra: Optional[str] = Field(None, description="Código único de la muestra (se genera automáticamente si no se proporciona)")
    usuario_id: str
    paciente_id: str  # ID del paciente asociado (cédula)

class MuestraUpdate(BaseModel):
    medico_solicitante: Optional[str] = None
    fecha_ingreso: Optional[datetime] = None
    estado: Optional[str] = None
    patologo: Optional[str] = None
    observaciones: Optional[str] = None
    resultados: Optional[Dict[str, Any]] = None

class Muestra(MuestraBase):
    id: str = Field(alias="_id")  # El _id será el codigo_muestra
    estado: str = "En proceso"  # Cambiar estado por defecto a "En proceso"
    patologo: str = "Pendiente"  # Campo patólogo por defecto en "Pendiente"
    usuario_id: str
    paciente_id: str  # Cédula del paciente
    resultados: Optional[Dict[str, Any]] = None
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None
    codigo_solicitud: Optional[str] = None  # Para compatibilidad con frontend

    class Config:
        from_attributes = True
        populate_by_name = True
