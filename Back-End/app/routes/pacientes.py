from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Paciente, PacienteCreate, PacienteUpdate
from app.config.database import get_database
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=Paciente)
async def crear_paciente(paciente: PacienteCreate):
    db = get_database()
    
    # Verificar si ya existe un paciente con esa cédula
    existing_patient = await db.pacientes.find_one({"_id": paciente.numeroCedula})
    if existing_patient:
        raise HTTPException(status_code=409, detail="Ya existe un paciente con esta cédula")
    
    # Preparar datos del paciente usando numeroCedula como _id
    paciente_dict = paciente.dict(exclude={"numeroCedula"})
    paciente_dict["_id"] = paciente.numeroCedula
    paciente_dict["fecha_creacion"] = datetime.utcnow()
    
    # Insertar el paciente
    await db.pacientes.insert_one(paciente_dict)
    
    # Retornar el paciente creado
    paciente_dict["id"] = paciente_dict["_id"]
    return Paciente(**paciente_dict)

@router.get("/", response_model=List[Paciente])
async def listar_pacientes():
    db = get_database()
    pacientes = []
    async for doc in db.pacientes.find():
        doc["id"] = doc["_id"]  # _id es ahora la cédula
        pacientes.append(Paciente(**doc))
    return pacientes

@router.get("/cedula/{numero_cedula}", response_model=Paciente)
async def buscar_paciente_por_cedula(numero_cedula: str):
    """Buscar un paciente por número de cédula"""
    db = get_database()
    paciente = await db.pacientes.find_one({"_id": numero_cedula})
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    paciente["id"] = paciente["_id"]  # _id es ahora la cédula
    return Paciente(**paciente)
