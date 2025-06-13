# LIME PathSys

Sistema de gestión de muestras para laboratorio desarrollado con Vue.js (Frontend) y Python/FastAPI (Backend) con MongoDB.

## 🏗️ Arquitectura del Proyecto

```
LIME-PathSys/
├── Front-End/          # Aplicación Vue.js + TypeScript + Tailwind
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
├── Back-End/           # API FastAPI + Python + MongoDB
│   ├── app/
│   ├── requirements.txt
│   ├── init_db.py
│   └── README.md
├── LICENSE
└── README.md           # Este archivo
```

## 🚀 Inicio Rápido

### Prerrequisitos

- **Node.js** 18+ (para el Frontend)
- **Python** 3.8+ (para el Backend)
- **MongoDB** 4.4+ (Base de datos)
- **Git** (Control de versiones)

### Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/LIME-PathSys.git
cd LIME-PathSys
```

### Configurar Backend

1. **Navegar al directorio del backend:**
```bash
cd Back-End
```

2. **Crear entorno virtual:**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate     # Windows
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Inicializar base de datos:**
```bash
python init_db.py
```

6. **Ejecutar servidor:**
```bash
uvicorn app.main:app --reload --port 8000
```

### Configurar Frontend  

1. **Navegar al directorio del frontend:**
```bash
cd Front-End
```

2. **Instalar dependencias:**
```bash
npm install
```

3. **Ejecutar servidor de desarrollo:**
```bash
npm run dev
```

## 🌐 Acceso a la Aplicación

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **Documentación API:** http://localhost:8000/docs

## 📚 Documentación Detallada

- [Frontend README](./Front-End/README.md) - Configuración e información del frontend
- [Backend README](./Back-End/README.md) - Configuración e información del backend

## 🛠️ Tecnologías Utilizadas

### Frontend
- **Vue 3** - Framework JavaScript progresivo
- **TypeScript** - Tipado estático
- **Vite** - Build tool rápido
- **Tailwind CSS** - Framework CSS utilitario
- **Vue Router** - Enrutamiento SPA

### Backend
- **FastAPI** - Framework web Python moderno
- **MongoDB** - Base de datos NoSQL
- **Motor** - Driver MongoDB asíncrono
- **Pydantic** - Validación de datos
- **JWT** - Autenticación basada en tokens
- **Uvicorn** - Servidor ASGI

## 🔧 Funcionalidades Principales

### 👥 Gestión de Usuarios
- Registro e inicio de sesión
- Roles y permisos
- Perfil de usuario

### 🧪 Gestión de Muestras
- CRUD completo de muestras
- Estados de workflow (pendiente, procesada, completada)
- Filtrado y búsqueda avanzada
- Importación/exportación de datos

### 📊 Dashboard y Estadísticas
- Resumen de muestras en tiempo real
- Gráficos interactivos
- KPIs del laboratorio
- Reportes personalizados

### 📱 Interfaz Responsive
- Diseño adaptativo para todos los dispositivos
- Interfaz moderna con Tailwind CSS
- Experiencia de usuario optimizada

## 🔐 Seguridad

- **Autenticación JWT** - Tokens seguros
- **Hashing de contraseñas** - Bcrypt
- **CORS configurado** - Orígenes permitidos
- **Validación de datos** - Pydantic schemas

## 🗄️ Base de Datos

### Colecciones MongoDB

- **usuarios** - Información de usuarios del sistema
- **muestras** - Registro de muestras del laboratorio

## 🧪 Testing

### Backend
```bash
cd Back-End
pytest
```

### Frontend
```bash
cd Front-End
npm run test
```

## 🚀 Despliegue

### Desarrollo
- Frontend: `npm run dev`
- Backend: `uvicorn app.main:app --reload`

### Producción
- Frontend: `npm run build` → servir `dist/`
- Backend: `gunicorn app.main:app` o Docker

## 📦 Scripts Útiles

### Frontend
```bash
npm run dev        # Desarrollo
npm run build      # Construcción
npm run lint       # Linting
npm run format     # Formateo
```

### Backend
```bash
uvicorn app.main:app --reload  # Desarrollo
python init_db.py              # Inicializar BD
pytest                         # Tests
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Equipo de Desarrollo

- **Frontend Developer** - Vue.js, TypeScript, Tailwind CSS
- **Backend Developer** - Python, FastAPI, MongoDB
- **DevOps** - Docker, CI/CD, Deployment

## 📞 Soporte

Para soporte técnico o consultas sobre el proyecto, contactar al equipo de desarrollo.

---

**LIME PathSys** - Sistema de Gestión de Muestras de Laboratorio 🧪