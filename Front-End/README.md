# LIME PathSys - Frontend

Frontend de la aplicación LIME PathSys desarrollado con Vue 3, TypeScript, Vite y Tailwind CSS.

## 🚀 Inicio Rápido

### Requisitos Previos

- Node.js 18+
- npm o yarn

### Instalación

1. **Instalar dependencias:**
```bash
npm install
# o
yarn install
```

2. **Ejecutar servidor de desarrollo:**
```bash
npm run dev
# o
yarn dev
```

3. **Construir para producción:**
```bash
npm run build
# o
yarn build
```

## 📁 Estructura del Proyecto

```
Front-End/
├── public/                  # Archivos estáticos
│   ├── favicon-huam.ico
│   └── images/             # Imágenes y recursos
├── src/
│   ├── App.vue             # Componente raíz
│   ├── main.ts             # Punto de entrada
│   ├── assets/             # Recursos CSS/JS
│   ├── components/         # Componentes Vue
│   │   ├── charts/         # Componentes de gráficos
│   │   ├── common/         # Componentes comunes
│   │   ├── layout/         # Componentes de layout
│   │   ├── Muestras/       # Componentes de muestras
│   │   └── ...
│   ├── composables/        # Composables de Vue
│   ├── icons/              # Iconos SVG
│   ├── router/             # Configuración de rutas
│   ├── types/              # Definiciones TypeScript
│   └── views/              # Páginas/Vistas
│       ├── Inicio.vue
│       ├── Autentificacion/
│       ├── Estadisticas/
│       ├── Muestras/
│       └── ...
├── index.html              # HTML principal
├── package.json            # Dependencias y scripts
├── vite.config.ts          # Configuración Vite
├── tailwind.config.js      # Configuración Tailwind
├── tsconfig.json           # Configuración TypeScript
└── README.md               # Este archivo
```

## 🛠️ Tecnologías

- **Vue 3** - Framework JavaScript progresivo
- **TypeScript** - Tipado estático para JavaScript
- **Vite** - Build tool y dev server
- **Tailwind CSS** - Framework CSS utilitario
- **Vue Router** - Enrutamiento para Vue.js
- **Pinia** - Gestión de estado (si se implementa)

## 📦 Scripts Disponibles

```bash
# Desarrollo
npm run dev          # Servidor de desarrollo

# Construcción
npm run build        # Construir para producción
npm run preview      # Vista previa de la build

# Calidad de código
npm run lint         # Linter ESLint
npm run format       # Formatear con Prettier
npm run type-check   # Verificación de tipos TypeScript
```

## 🎨 Componentes Principales

### Layout
- **Sidebar** - Barra lateral de navegación
- **Header** - Cabecera de la aplicación
- **Breadcrumb** - Navegación de migas de pan

### Muestras
- **ListaMuestras** - Tabla de muestras
- **FormularioMuestra** - Formulario CRUD
- **DetalleMuestra** - Vista detallada

### Estadísticas
- **Dashboard** - Panel principal
- **Gráficos** - Visualizaciones de datos
- **Reportes** - Generación de informes

## 🔧 Configuración

### Variables de Entorno

Crear archivo `.env` en la raíz del proyecto:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_APP_TITLE=LIME PathSys
```

### Tailwind CSS

El proyecto está configurado con Tailwind CSS. Las configuraciones se encuentran en `tailwind.config.js`.

### TypeScript

Configuración en `tsconfig.json` con strict mode habilitado.

## 🌐 Rutas de la Aplicación

```
/                    # Página de inicio
/auth/login          # Iniciar sesión
/auth/register       # Registro
/muestras            # Listado de muestras
/muestras/nueva      # Nueva muestra
/muestras/:id        # Detalle de muestra
/estadisticas        # Dashboard estadísticas
/usuarios            # Gestión de usuarios
/informes            # Generación de informes
```

## 🔌 Integración con Backend

El frontend se conecta con la API backend mediante:

- **Axios** - Cliente HTTP
- **Interceptors** - Manejo de autenticación
- **Error Handling** - Gestión de errores de API

### Configuración API

```typescript
// src/services/api.ts
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})
```

## 🎯 Funcionalidades

### Autenticación
- Login/Logout
- Gestión de tokens JWT
- Rutas protegidas

### Gestión de Muestras
- CRUD completo de muestras  
- Filtrado y búsqueda
- Importación/Exportación
- Estados de workflow

### Dashboard
- Estadísticas en tiempo real
- Gráficos interactivos
- KPIs principales

### Reportes  
- Generación de PDF
- Exportación Excel
- Filtros personalizados

## 🚀 Despliegue

### Build de Producción
```bash
npm run build
```

Los archivos se generan en `dist/` listos para servir.

### Nginx
```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    
    location / {
        root /ruta/a/dist;
        try_files $uri $uri/ /index.html;
    }
    
    location /api {
        proxy_pass http://backend:8000;
    }
}
```

## 🧪 Testing

```bash
# Tests unitarios
npm run test:unit

# Tests e2e  
npm run test:e2e

# Coverage
npm run test:coverage
```

## 📱 Responsive Design

La aplicación está optimizada para:
- ✅ Desktop (1024px+)
- ✅ Tablet (768px - 1023px)  
- ✅ Mobile (320px - 767px)

## 🔧 Desarrollo

### Estructura de Componentes
- Usar Composition API
- Props tipadas con TypeScript
- Emits definidos explícitamente
- Documentar componentes complejos

### Estilo de Código
- ESLint + Prettier configurados
- Convenciones de nomenclatura Vue
- Importaciones organizadas
- Comentarios JSDoc para funciones

## 📞 Soporte

Para problemas o preguntas, contactar al equipo de desarrollo.
