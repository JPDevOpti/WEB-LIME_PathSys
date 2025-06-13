# LIME PathSys - Backend

Backend API para el sistema LIME PathSys desarrollado con FastAPI, MongoDB y Python.

## 🚀 Inicio Rápido

### Requisitos Previos

- Python 3.8+
- MongoDB 4.4+
- pip (gestor de paquetes de Python)

### Instalación

1. **Crear entorno virtual:**
```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate     # En Windows
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

4. **Inicializar base de datos:**
```bash
python init_db.py
```

5. **Ejecutar servidor de desarrollo:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📁 Estructura del Proyecto

```
Back-End/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación principal FastAPI
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py      # Configuraciones
│   │   └── database.py      # Conexión MongoDB
│   ├── models/
│   │   ├── __init__.py
│   │   ├── usuario.py       # Modelos de usuario
│   │   └── muestra.py       # Modelos de muestra
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Rutas de autenticación
│   │   ├── usuarios.py      # CRUD usuarios
│   │   └── muestras.py      # CRUD muestras
│   ├── services/            # Lógica de negocio
│   └── utils/               # Utilidades
├── .env.example             # Variables de entorno ejemplo
├── .venv/                   # Entorno virtual
├── init_db.py              # Script inicialización BD
├── requirements.txt         # Dependencias Python
└── README.md               # Este archivo
```

## 🔧 Configuración

### Variables de Entorno (.env)

```env
# MongoDB
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=lime_pathsys

# JWT
SECRET_KEY=tu-clave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# FastAPI
API_V1_STR=/api/v1
PROJECT_NAME="LIME PathSys API"

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]
```

## 📚 API Endpoints

### Autenticación
- `POST /api/v1/auth/login` - Iniciar sesión

### Usuarios
- `GET /api/v1/usuarios/` - Listar usuarios
- `POST /api/v1/usuarios/` - Crear usuario
- `GET /api/v1/usuarios/{id}` - Obtener usuario
- `PUT /api/v1/usuarios/{id}` - Actualizar usuario
- `DELETE /api/v1/usuarios/{id}` - Eliminar usuario

### Muestras
- `GET /api/v1/muestras/` - Listar muestras
- `POST /api/v1/muestras/` - Crear muestra
- `GET /api/v1/muestras/{id}` - Obtener muestra
- `PUT /api/v1/muestras/{id}` - Actualizar muestra
- `DELETE /api/v1/muestras/{id}` - Eliminar muestra
- `GET /api/v1/muestras/estadisticas/resumen` - Estadísticas

## 🧪 Documentación API

Una vez ejecutado el servidor, puedes acceder a:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## 🗄️ Base de Datos

### Colecciones MongoDB

#### usuarios
```json
{
  "_id": "ObjectId",
  "nombre": "string",
  "email": "string",
  "rol": "string",
  "password": "string (hashed)",
  "activo": "boolean",
  "fecha_creacion": "datetime"
}
```

#### muestras
```json
{
  "_id": "ObjectId", 
  "codigo": "string",
  "tipo": "string",
  "ubicacion": "string",
  "fecha_recoleccion": "datetime",
  "estado": "string",
  "observaciones": "string",
  "usuario_id": "string",
  "resultados": "object",
  "fecha_creacion": "datetime"
}
```

## 🧑‍💻 Desarrollo

### Ejecutar en modo desarrollo
```bash
uvicorn app.main:app --reload
```

### Ejecutar tests
```bash
pytest
```

### Formatear código
```bash
black app/
isort app/
```

## 🚀 Producción

### Con Docker
```bash
# Construir imagen
docker build -t lime-pathsys-backend .

# Ejecutar contenedor
docker run -p 8000:8000 lime-pathsys-backend
```

### Con Gunicorn
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 📝 Notas

- El sistema usa JWT para autenticación
- Las contraseñas se almacenan con hash bcrypt
- MongoDB se usa como base de datos principal
- FastAPI proporciona documentación automática de la API
