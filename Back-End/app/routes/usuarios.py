from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from bson import ObjectId
from app.config.database import get_database

router = APIRouter()

class Usuario(BaseModel):
    id: str = None
    nombre: str
    email: str
    rol: str
    activo: bool = True

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    rol: str
    password: str

class UsuarioUpdate(BaseModel):
    nombre: str = None
    email: str = None
    rol: str = None
    activo: bool = None

@router.get("/", response_model=List[Usuario])
async def obtener_usuarios():
    """Obtener todos los usuarios"""
    database = get_database()
    usuarios = []
    async for usuario in database.usuarios.find():
        usuario["id"] = str(usuario["_id"])
        del usuario["_id"]
        del usuario["password"]  # No devolver la contraseña
        usuarios.append(Usuario(**usuario))
    return usuarios

@router.post("/", response_model=Usuario)
async def crear_usuario(usuario: UsuarioCreate):
    """Crear un nuevo usuario"""
    database = get_database()
    
    # Verificar si el email ya existe
    existing_user = await database.usuarios.find_one({"email": usuario.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    # Hash de la contraseña (implementar hash real)
    usuario_dict = usuario.dict()
    usuario_dict["password"] = f"hashed_{usuario.password}"  # Implementar hash real
    
    result = await database.usuarios.insert_one(usuario_dict)
    
    # Obtener el usuario creado
    created_user = await database.usuarios.find_one({"_id": result.inserted_id})
    created_user["id"] = str(created_user["_id"])
    del created_user["_id"]
    del created_user["password"]
    
    return Usuario(**created_user)

@router.get("/{usuario_id}", response_model=Usuario)
async def obtener_usuario(usuario_id: str):
    """Obtener un usuario por ID"""
    database = get_database()
    usuario = await database.usuarios.find_one({"_id": ObjectId(usuario_id)})
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    usuario["id"] = str(usuario["_id"])
    del usuario["_id"]
    del usuario["password"]
    
    return Usuario(**usuario)

@router.put("/{usuario_id}", response_model=Usuario)
async def actualizar_usuario(usuario_id: str, usuario_update: UsuarioUpdate):
    """Actualizar un usuario"""
    database = get_database()
    
    # Crear diccionario solo con campos no nulos
    update_data = {k: v for k, v in usuario_update.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")
    
    result = await database.usuarios.update_one(
        {"_id": ObjectId(usuario_id)}, 
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Obtener el usuario actualizado
    updated_user = await database.usuarios.find_one({"_id": ObjectId(usuario_id)})
    updated_user["id"] = str(updated_user["_id"])
    del updated_user["_id"]
    del updated_user["password"]
    
    return Usuario(**updated_user)

@router.delete("/{usuario_id}")
async def eliminar_usuario(usuario_id: str):
    """Eliminar un usuario"""
    database = get_database()
    result = await database.usuarios.delete_one({"_id": ObjectId(usuario_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return {"message": "Usuario eliminado correctamente"}
