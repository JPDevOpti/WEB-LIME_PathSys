#!/usr/bin/env python3
"""
Script de inicialización del proyecto LIME PathSys Backend
"""
import asyncio
import sys
import os

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config.database import connect_to_mongo, get_database
from app.config.settings import settings

async def create_indexes():
    """Crear índices para las colecciones"""
    database = get_database()
    
    # Índices para usuarios
    await database.usuarios.create_index("email", unique=True)
    await database.usuarios.create_index("nombre")
    
    # Índices para muestras
    await database.muestras.create_index("codigo", unique=True)
    await database.muestras.create_index("tipo")
    await database.muestras.create_index("estado")
    await database.muestras.create_index("fecha_recoleccion")
    await database.muestras.create_index("usuario_id")
    
    print("✅ Índices creados correctamente")

async def create_sample_data():
    """Crear datos de ejemplo"""
    database = get_database()
    
    # Verificar si ya existen datos
    usuario_count = await database.usuarios.count_documents({})
    if usuario_count > 0:
        print("ℹ️  Ya existen datos en la base de datos")
        return
    
    # Crear usuario administrador
    admin_user = {
        "nombre": "Administrador",
        "email": "admin@limepathsys.com",
        "rol": "admin",
        "password": "hashed_admin123",  # En producción usar hash real
        "activo": True,
        "fecha_creacion": "2024-01-01T00:00:00"
    }
    
    await database.usuarios.insert_one(admin_user)
    print("✅ Usuario administrador creado")
    
    # Crear datos de ejemplo para muestras
    sample_muestras = [
        {
            "codigo": "M001",
            "tipo": "Suelo",
            "ubicacion": "Sector A - Coordenadas: -12.0464, -77.0428",
            "fecha_recoleccion": "2024-01-15T10:00:00",
            "estado": "pendiente",
            "observaciones": "Muestra tomada en condiciones normales",
            "usuario_id": str(admin_user["_id"]) if "_id" in admin_user else "admin",
            "fecha_creacion": "2024-01-15T10:30:00"
        },
        {
            "codigo": "M002",
            "tipo": "Agua",
            "ubicacion": "Río Principal - Punto de muestreo 1",
            "fecha_recoleccion": "2024-01-16T14:30:00",
            "estado": "procesada",
            "observaciones": "Agua con ligera turbidez",
            "usuario_id": str(admin_user["_id"]) if "_id" in admin_user else "admin",
            "resultados": {
                "ph": 7.2,
                "conductividad": 450,
                "turbidez": 12.5
            },
            "fecha_creacion": "2024-01-16T15:00:00"
        }
    ]
    
    await database.muestras.insert_many(sample_muestras)
    print("✅ Muestras de ejemplo creadas")

async def init_database():
    """Inicializar la base de datos"""
    try:
        print("🚀 Inicializando base de datos...")
        await connect_to_mongo()
        print(f"✅ Conectado a MongoDB: {settings.DATABASE_NAME}")
        
        await create_indexes()
        await create_sample_data()
        
        print("🎉 Base de datos inicializada correctamente")
        
    except Exception as e:
        print(f"❌ Error al inicializar la base de datos: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(init_database())
