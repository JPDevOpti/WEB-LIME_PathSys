# WEB-LIS_PathSys

This project is a web-based Laboratory Information System (LIS) with PathSys integration.

## Flujo de Trabajo con Ramas

Este proyecto utiliza el siguiente flujo de ramas para mantener un desarrollo organizado:

### 🌿 Ramas Principales

- **`main`** - Código estable y listo para producción
- **`desarrollo`** - Rama principal de desarrollo donde se integran nuevas características
- **`produccion`** - Rama para preparar y probar releases antes de production

### 📋 Flujo de Trabajo Recomendado

1. **Desarrollo de nuevas características:**

   ```bash
   git checkout desarrollo
   git checkout -b feature/nueva-caracteristica
   # Desarrollar la característica
   git add .
   git commit -m "feat: agregar nueva característica"
   git push origin feature/nueva-caracteristica
   ```

2. **Integración a desarrollo:**
   - Crear Pull Request de `feature/nueva-caracteristica` → `desarrollo`
   - Revisar y aprobar
   - Merge a `desarrollo`

3. **Preparar para producción:**

   ```bash
   git checkout produccion
   git merge desarrollo
   git push origin produccion
   ```

4. **Deploy a producción:**

   ```bash
   git checkout main
   git merge produccion
   git push origin main
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

## Getting Started

This is the initial setup of the project.
