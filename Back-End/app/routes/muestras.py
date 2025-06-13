from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Muestra, MuestraCreate, MuestraUpdate
from app.config.database import get_database
from datetime import datetime

router = APIRouter()

async def generar_codigo_consecutivo(db, año: int = None) -> str:
    """Generar código consecutivo con formato año-xxxxxx"""
    if año is None:
        año = datetime.now().year
    
    # Buscar o crear el contador para el año actual
    contador = await db.contadores.find_one({"año": año})
    
    if not contador:
        # Crear nuevo contador para el año
        nuevo_contador = {
            "año": año,
            "ultimo_numero": 1,
            "fecha_creacion": datetime.utcnow()
        }
        await db.contadores.insert_one(nuevo_contador)
        numero = 1
    else:
        # Incrementar el contador
        numero = contador["ultimo_numero"] + 1
        await db.contadores.update_one(
            {"año": año},
            {
                "$set": {
                    "ultimo_numero": numero,
                    "fecha_actualizacion": datetime.utcnow()
                }
            }
        )
    
    # Formatear el código con 6 dígitos
    codigo = f"{año}-{numero:06d}"
    return codigo

@router.post("/", response_model=Muestra)
async def crear_solicitud_muestras(muestra: MuestraCreate):
    """Crear una nueva solicitud de muestras"""
    db = get_database()
    
    # Verificar que el paciente existe usando la cédula como _id
    paciente = await db.pacientes.find_one({"_id": muestra.paciente_id})
    if not paciente:
        raise HTTPException(status_code=404, detail=f"Paciente con cédula {muestra.paciente_id} no encontrado")
    
    # Generar código automáticamente si no se proporciona
    if hasattr(muestra, 'codigo_muestra') and muestra.codigo_muestra:
        codigo_muestra = muestra.codigo_muestra
        # Verificar si ya existe una muestra con este código
        existing_muestra = await db.muestras.find_one({"_id": codigo_muestra})
        if existing_muestra:
            raise HTTPException(status_code=409, detail="Ya existe una muestra con este código")
    else:
        # Generar código automáticamente
        codigo_muestra = await generar_codigo_consecutivo(db)
    
    # Crear la muestra usando el codigo_muestra como _id
    muestra_dict = muestra.dict(exclude={"codigo_muestra"} if hasattr(muestra, 'codigo_muestra') else set())
    muestra_dict["_id"] = codigo_muestra
    muestra_dict["fecha_creacion"] = datetime.utcnow()
    muestra_dict["estado"] = "pendiente"
    
    # Insertar la muestra
    await db.muestras.insert_one(muestra_dict)
    
    # Retornar la muestra creada con el código generado
    muestra_dict["id"] = codigo_muestra
    muestra_dict["codigo_solicitud"] = codigo_muestra  # Para compatibilidad con frontend
    
    return Muestra(**muestra_dict)

@router.get("/", response_model=List[Muestra])
async def listar_muestras():
    """Listar todas las solicitudes de muestras"""
    db = get_database()
    muestras = []
    async for doc in db.muestras.find():
        doc["id"] = doc["_id"]  # _id es ahora el código de muestra
        muestras.append(Muestra(**doc))
    return muestras

@router.get("/{codigo_muestra}", response_model=Muestra)
async def obtener_muestra(codigo_muestra: str):
    """Obtener una solicitud de muestra específica por código"""
    db = get_database()
    muestra = await db.muestras.find_one({"_id": codigo_muestra})
    if not muestra:
        raise HTTPException(status_code=404, detail="Muestra no encontrada")
    muestra["id"] = muestra["_id"]
    return Muestra(**muestra)

@router.put("/{codigo_muestra}", response_model=Muestra)
async def actualizar_muestra(codigo_muestra: str, muestra_update: MuestraUpdate):
    """Actualizar una muestra"""
    db = get_database()
    
    # Crear diccionario solo con campos no nulos
    update_data = {k: v for k, v in muestra_update.dict().items() if v is not None}
    update_data["fecha_actualizacion"] = datetime.utcnow()
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")
    
    result = await db.muestras.update_one(
        {"_id": codigo_muestra}, 
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Muestra no encontrada")
    
    # Obtener la muestra actualizada
    updated_muestra = await db.muestras.find_one({"_id": codigo_muestra})
    updated_muestra["id"] = updated_muestra["_id"]
    
    return Muestra(**updated_muestra)

@router.delete("/{codigo_muestra}")
async def eliminar_muestra(codigo_muestra: str):
    """Eliminar una muestra"""
    db = get_database()
    result = await db.muestras.delete_one({"_id": codigo_muestra})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Muestra no encontrada")
    
    return {"message": "Muestra eliminada correctamente"}

@router.get("/estadisticas/resumen")
async def obtener_estadisticas():
    """Obtener estadísticas generales de las muestras"""
    db = get_database()
    
    total_muestras = await db.muestras.count_documents({})
    muestras_pendientes = await db.muestras.count_documents({"estado": "pendiente"})
    muestras_procesadas = await db.muestras.count_documents({"estado": "procesada"})
    muestras_completadas = await db.muestras.count_documents({"estado": "completada"})
    
    return {
        "total_muestras": total_muestras,
        "muestras_pendientes": muestras_pendientes,
        "muestras_procesadas": muestras_procesadas,
        "muestras_completadas": muestras_completadas
    }
