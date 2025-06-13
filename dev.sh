#!/bin/bash

# Script de desarrollo para LIME PathSys
# Uso: ./dev.sh [frontend|backend|full|setup|clean]

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para mostrar ayuda
show_help() {
    echo -e "${BLUE}LIME PathSys - Script de Desarrollo${NC}"
    echo ""
    echo "Uso: ./dev.sh [comando]"
    echo ""
    echo "Comandos disponibles:"
    echo "  setup     - Configurar el entorno de desarrollo"
    echo "  frontend  - Ejecutar solo el frontend"
    echo "  backend   - Ejecutar solo el backend"
    echo "  full      - Ejecutar frontend y backend"
    echo "  docker    - Ejecutar con Docker Compose"
    echo "  test      - Ejecutar tests"
    echo "  clean     - Limpiar archivos temporales"
    echo "  help      - Mostrar esta ayuda"
    echo ""
}

# Función para setup inicial
setup_project() {
    echo -e "${YELLOW}🚀 Configurando proyecto LIME PathSys...${NC}"
    
    # Verificar si MongoDB está corriendo
    if ! pgrep -x "mongod" > /dev/null; then
        echo -e "${YELLOW}⚠️  MongoDB no está corriendo. Inicia MongoDB primero.${NC}"
    else
        echo -e "${GREEN}✅ MongoDB está corriendo${NC}"
    fi
    
    # Setup Backend
    echo -e "${BLUE}📦 Configurando Backend...${NC}"
    cd Back-End
    
    if [ ! -d ".venv" ]; then
        echo "Creando entorno virtual..."
        python -m venv .venv
    fi
    
    echo "Activando entorno virtual..."
    source .venv/bin/activate
    
    echo "Instalando dependencias Python..."
    pip install -r requirements.txt
    
    # Crear .env si no existe
    if [ ! -f ".env" ]; then
        echo "Creando archivo .env..."
        cp .env.example .env
        echo -e "${YELLOW}📝 Edita el archivo Back-End/.env con tus configuraciones${NC}"
    fi
    
    cd ..
    
    # Setup Frontend
    echo -e "${BLUE}📦 Configurando Frontend...${NC}"
    cd Front-End
    
    if [ ! -d "node_modules" ]; then
        echo "Instalando dependencias Node.js..."
        npm install
    else
        echo "Dependencias ya instaladas, actualizando..."
        npm update
    fi
    
    cd ..
    
    echo -e "${GREEN}🎉 Proyecto configurado correctamente!${NC}"
    echo -e "${YELLOW}💡 Ahora puedes usar: ./dev.sh full${NC}"
}

# Función para ejecutar frontend
run_frontend() {
    echo -e "${BLUE}🌐 Iniciando Frontend...${NC}"
    cd Front-End
    npm run dev
}

# Función para ejecutar backend
run_backend() {
    echo -e "${BLUE}🔧 Iniciando Backend...${NC}"
    cd Back-End
    
    # Activar entorno virtual
    source .venv/bin/activate
    
    # Inicializar BD si es necesario
    if [ "$1" = "--init-db" ]; then
        echo "Inicializando base de datos..."
        python init_db.py
    fi
    
    # Ejecutar servidor
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
}

# Función para ejecutar ambos
run_full() {
    echo -e "${BLUE}🚀 Iniciando proyecto completo...${NC}"
    
    # Verificar que todo esté configurado
    if [ ! -d "Back-End/.venv" ] || [ ! -d "Front-End/node_modules" ]; then
        echo -e "${YELLOW}⚠️  Proyecto no configurado. Ejecutando setup...${NC}"
        setup_project
    fi
    
    # Iniciar backend en background
    echo -e "${BLUE}🔧 Iniciando Backend...${NC}"
    cd Back-End
    source .venv/bin/activate
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
    BACKEND_PID=$!
    cd ..
    
    # Esperar un poco para que el backend inicie
    sleep 3
    
    # Iniciar frontend
    echo -e "${BLUE}🌐 Iniciando Frontend...${NC}"
    cd Front-End
    npm run dev &
    FRONTEND_PID=$!
    cd ..
    
    echo -e "${GREEN}✅ Servicios iniciados:${NC}"
    echo -e "${GREEN}   - Backend: http://localhost:8000${NC}"
    echo -e "${GREEN}   - Frontend: http://localhost:5173${NC}"
    echo -e "${GREEN}   - API Docs: http://localhost:8000/docs${NC}"
    echo ""
    echo -e "${YELLOW}Presiona Ctrl+C para detener ambos servicios${NC}"
    
    # Función para cleanup
    cleanup() {
        echo -e "\n${YELLOW}🛑 Deteniendo servicios...${NC}"
        kill $BACKEND_PID 2>/dev/null || true
        kill $FRONTEND_PID 2>/dev/null || true
        echo -e "${GREEN}✅ Servicios detenidos${NC}"
        exit 0
    }
    
    # Capturar Ctrl+C
    trap cleanup INT
    
    # Esperar
    wait
}

# Función para ejecutar con Docker
run_docker() {
    echo -e "${BLUE}🐳 Iniciando con Docker Compose...${NC}"
    
    if ! command -v docker-compose &> /dev/null; then
        echo -e "${RED}❌ Docker Compose no está instalado${NC}"
        exit 1
    fi
    
    docker-compose up --build
}

# Función para ejecutar tests
run_tests() {
    echo -e "${BLUE}🧪 Ejecutando tests...${NC}"
    
    # Tests Backend
    echo -e "${BLUE}Backend Tests:${NC}"
    cd Back-End
    source .venv/bin/activate
    pytest --verbose
    cd ..
    
    # Tests Frontend (si existen)
    echo -e "${BLUE}Frontend Tests:${NC}"
    cd Front-End
    if [ -f "package.json" ] && grep -q "test" package.json; then
        npm run test
    else
        echo -e "${YELLOW}No hay tests configurados para el frontend${NC}"
    fi
    cd ..
}

# Función para limpiar
clean_project() {
    echo -e "${BLUE}🧹 Limpiando proyecto...${NC}"
    
    # Limpiar Backend
    echo "Limpiando Backend..."
    find Back-End -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
    find Back-End -name "*.pyc" -delete 2>/dev/null || true
    
    # Limpiar Frontend
    echo "Limpiando Frontend..."
    rm -rf Front-End/dist 2>/dev/null || true
    rm -rf Front-End/.vite 2>/dev/null || true
    
    # Limpiar logs
    find . -name "*.log" -delete 2>/dev/null || true
    
    echo -e "${GREEN}✅ Proyecto limpiado${NC}"
}

# Función principal
main() {
    case "$1" in
        "setup")
            setup_project
            ;;
        "frontend")
            run_frontend
            ;;
        "backend")
            run_backend $2
            ;;
        "full")
            run_full
            ;;
        "docker")
            run_docker
            ;;
        "test")
            run_tests
            ;;
        "clean")
            clean_project
            ;;
        "help"|"--help"|"-h")
            show_help
            ;;
        "")
            echo -e "${YELLOW}⚠️  No se especificó comando${NC}"
            show_help
            ;;
        *)
            echo -e "${RED}❌ Comando desconocido: $1${NC}"
            show_help
            exit 1
            ;;
    esac
}

# Ejecutar función principal
main "$@"
