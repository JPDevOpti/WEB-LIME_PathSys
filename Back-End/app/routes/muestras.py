from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime
from app.config.database import get_database

router = APIRouter()

class Muestra(BaseModel):
    id: str = None
    codigo: str
    tipo: str
    ubicacion: str
    fecha_recoleccion: datetime
    estado: str = "pendiente"
    observaciones: str = None
    usuario_id: str
    resultados: dict = None
    fecha_creacion: datetime = None

class MuestraCreate(BaseModel):
    codigo: str
    tipo: str
    ubicacion: str
    fecha_recoleccion: datetime
    observaciones: str = None
    usuario_id: str

class MuestraUpdate(BaseModel):
    codigo: str = None
    tipo: str = None
    ubicacion: str = None
    fecha_recoleccion: datetime = None
    estado: str = None
    observaciones: str = None
    resultados: dict = None

class MuestraFilter(BaseModel):
    tipo: str = None
    estado: str = None
    usuario_id: str = None
    fecha_inicio: datetime = None
    fecha_fin: datetime = None

@router.get("/", response_model=List[Muestra])
async def obtener_muestras(
    tipo: Optional[str] = None,
    estado: Optional[str] = None,
    usuario_id: Optional[str] = None
):
    """Obtener todas las muestras con filtros opcionales"""
    database = get_database()
    
    # Construir filtro
    filtro = {}
    if tipo:
        filtro["tipo"] = tipo
    if estado:
        filtro["estado"] = estado
    if usuario_id:
        filtro["usuario_id"] = usuario_id
    
    muestras = []
    async for muestra in database.muestras.find(filtro):
        muestra["id"] = str(muestra["_id"])
        del muestra["_id"]
        muestras.append(Muestra(**muestra))
    
    return muestras

@router.post("/", response_model=Muestra)
async def crear_muestra(muestra: MuestraCreate):
    """Crear una nueva muestra"""
    database = get_database()
    
    # Verificar si el código ya existe
    existing_muestra = await database.muestras.find_one({"codigo": muestra.codigo})
    if existing_muestra:
        raise HTTPException(status_code=400, detail="El código de muestra ya existe")
    
    # Crear muestra con fecha de creación
    muestra_dict = muestra.dict()
    muestra_dict["fecha_creacion"] = datetime.utcnow()
    muestra_dict["estado"] = "pendiente"
    
    result = await database.muestras.insert_one(muestra_dict)
    
    # Obtener la muestra creada
    created_muestra = await database.muestras.find_one({"_id": result.inserted_id})
    created_muestra["id"] = str(created_muestra["_id"])
    del created_muestra["_id"]
    
    return Muestra(**created_muestra)

@router.get("/{muestra_id}", response_model=Muestra)
async def obtener_muestra(muestra_id: str):
    """Obtener una muestra por ID"""
    database = get_database()
    muestra = await database.muestras.find_one({"_id": ObjectId(muestra_id)})
    
    if not muestra:
        raise HTTPException(status_code=404, detail="Muestra no encontrada")
    
    muestra["id"] = str(muestra["_id"])
    del muestra["_id"]
    
    return Muestra(**muestra)

@router.put("/{muestra_id}", response_model=Muestra)
async def actualizar_muestra(muestra_id: str, muestra_update: MuestraUpdate):
    """Actualizar una muestra"""
    database = get_database()
    
    # Crear diccionario solo con campos no nulos
    update_data = {k: v for k, v in muestra_update.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")
    
    result = await database.muestras.update_one(
        {"_id": ObjectId(muestra_id)}, 
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Muestra no encontrada")
    
    # Obtener la muestra actualizada
    updated_muestra = await database.muestras.find_one({"_id": ObjectId(muestra_id)})
    updated_muestra["id"] = str(updated_muestra["_id"])
    del updated_muestra["_id"]
    
    return Muestra(**updated_muestra)

@router.delete("/{muestra_id}")
async def eliminar_muestra(muestra_id: str):
    """Eliminar una muestra"""
    database = get_database()
    result = await database.muestras.delete_one({"_id": ObjectId(muestra_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Muestra no encontrada")
    
    return {"message": "Muestra eliminada correctamente"}

@router.get("/estadisticas/resumen")
async def obtener_estadisticas():
    """Obtener estadísticas generales de las muestras"""
    database = get_database()
    
    total_muestras = await database.muestras.count_documents({})
    muestras_pendientes = await database.muestras.count_documents({"estado": "pendiente"})
    muestras_procesadas = await database.muestras.count_documents({"estado": "procesada"})
    muestras_completadas = await database.muestras.count_documents({"estado": "completada"})
    
    # Estadísticas por tipo
    pipeline = [
        {"$group": {"_id": "$tipo", "count": {"$sum": 1}}}
    ]
    tipos_stats = []
    async for doc in database.muestras.aggregate(pipeline):
        tipos_stats.append({"tipo": doc["_id"], "cantidad": doc["count"]})
    
    return {
        "total_muestras": total_muestras,
        "muestras_pendientes": muestras_pendientes,
        "muestras_procesadas": muestras_procesadas,
        "muestras_completadas": muestras_completadas,
        "por_tipo": tipos_stats
    }
