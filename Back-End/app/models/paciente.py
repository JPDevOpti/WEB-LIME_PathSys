from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PacienteBase(BaseModel):
    nombrePaciente: str = Field(..., description="Nombre completo del Paciente")
    sexo: str # Podría ser un Enum si los valores son estrictamente 'masculino' o 'femenino'
    edad: int = Field(..., ge=0, le=120, description="Edad del paciente")
    entidad: str = Field(..., description="Entidad de salud del paciente")
    tipoAtencion: str # Podría ser un Enum: 'ambulatorio', 'hospitalizado'
    observaciones: Optional[str] = None

class PacienteCreate(PacienteBase):
    numeroCedula: str = Field(..., description="Número de Cédula del Paciente que será usado como _id")

class PacienteUpdate(BaseModel):
    nombrePaciente: Optional[str] = None
    sexo: Optional[str] = None
    edad: Optional[int] = Field(None, ge=0, le=120)
    entidad: Optional[str] = None
    tipoAtencion: Optional[str] = None
    observaciones: Optional[str] = None

class Paciente(PacienteBase):
    id: str = Field(alias="_id")  # El _id será el número de cédula
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True
