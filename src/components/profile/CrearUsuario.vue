<template>
  <div class="flex gap-6">
    <!-- Selector de tipo de usuario -->
    <div class="w-64 p-5 border border-gray-200 rounded-2xl dark:border-gray-800">
      <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 mb-4">
        Tipo de Usuario
      </h4>
      <div class="space-y-2">
        <button
          v-for="type in tiposUsuario"
          :key="type.value"
          @click="tipoUsuarioSeleccionado = type.value"
          class="w-full text-left px-4 py-2 rounded-lg transition-colors"
          :class="tipoUsuarioSeleccionado === type.value ? 
            'bg-brand-500 text-white' : 
            'bg-gray-100 text-gray-700 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700'"
        >
          {{ type.label }}
        </button>
      </div>
    </div>

    <!-- Formulario de creación -->
    <div class="flex-1">
      <div class="p-5 mb-6 border border-gray-200 rounded-2xl dark:border-gray-800 lg:p-6">
        <div class="flex flex-col gap-6 lg:flex-row lg:items-start lg:justify-between">
          <div class="w-full">
            <!-- Sección de foto de perfil solo para administrativo y patólogo -->
            <div v-if="['administrativo', 'patologo'].includes(tipoUsuarioSeleccionado)" class="flex flex-col items-center w-full gap-6 mb-6 xl:flex-row">
              <div class="relative w-20 h-20 overflow-hidden border border-gray-200 rounded-full dark:border-gray-800 group">
                <img :src="previewImage || '/images/user/owner.jpg'" alt="user" class="w-full h-full object-cover" />
                <div class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer" @click="triggerFileInput">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <input
                  ref="fileInput"
                  type="file"
                  accept="image/*"
                  class="hidden"
                  @change="handleFileChange"
                />
              </div>
              <div>
                <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 lg:mb-3">
                  Crear Nuevo {{ tipoUsuarioSeleccionado ? tiposUsuario.find(t => t.value === tipoUsuarioSeleccionado)?.label : 'Usuario' }}
                </h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                  Haz clic en la imagen para cambiar la foto de perfil
                </p>
              </div>
            </div>

            <!-- Título sin foto para entidad y CUPS -->
            <div v-else class="mb-6">
              <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90">
                Crear Nuevo {{ tipoUsuarioSeleccionado ? tiposUsuario.find(t => t.value === tipoUsuarioSeleccionado)?.label : 'Usuario' }}
              </h4>
            </div>

            <!-- Formulario Administrativo -->
            <form v-if="tipoUsuarioSeleccionado === 'administrativo'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre Completo</label>
                <input v-model="nuevoUsuario.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Documento de Identidad</label>
                <input v-model="nuevoUsuario.document" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 1234567890" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
                <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Celular</label>
                <input v-model="nuevoUsuario.phone" type="tel" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 3001234567" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Fecha de Ingreso</label>
                <input v-model="nuevoUsuario.startDate" type="date" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear Usuario Administrativo</button>
              </div>
            </form>

            <!-- Formulario Patólogo -->
            <form v-if="tipoUsuarioSeleccionado === 'patologo'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre Completo</label>
                <input v-model="nuevoUsuario.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Documento de Identidad</label>
                <input v-model="nuevoUsuario.document" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 1234567890" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
                <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Celular</label>
                <input v-model="nuevoUsuario.phone" type="tel" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 3001234567" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Especialidad</label>
                <input v-model="nuevoUsuario.specialty" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: Anatomía Patológica" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Registro Médico</label>
                <input v-model="nuevoUsuario.medicalLicense" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 12345" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Estado</label>
                <div class="flex items-center space-x-4 mt-2">
                  <label class="inline-flex items-center">
                    <input
                      type="radio"
                      v-model="nuevoUsuario.isActive"
                      :value="true"
                      class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
                      required
                    />
                    <span class="ml-2 text-sm text-gray-700">Activo</span>
                  </label>
                  <label class="inline-flex items-center">
                    <input
                      type="radio"
                      v-model="nuevoUsuario.isActive"
                      :value="false"
                      class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
                      required
                    />
                    <span class="ml-2 text-sm text-gray-700">Inactivo</span>
                  </label>
                </div>
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Fecha de Ingreso</label>
                <input 
                  v-model="nuevoUsuario.startDate" 
                  type="date" 
                  required 
                  class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" 
                />
              </div>
              <div class="col-span-2">
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Firma del Patólogo</label>
                <Dropzone
                  :uploadUrl="'/api/upload-signature'"
                  @file-added="handleFirmaFile"
                  id="firmaDropzonePatologo" 
                />
                <div v-if="firmaPatologoFile" class="mt-2 text-sm text-gray-600">
                  Archivo seleccionado: {{ firmaPatologoFile.name }}
                </div>
              </div>
              <div class="col-span-2">
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Observaciones</label>
                <textarea
                  v-model="nuevoUsuario.observaciones"
                  placeholder="Observaciones adicionales sobre el patólogo"
                  rows="3"
                  class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs resize-none"
                ></textarea>
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear Patólogo</button>
              </div>
            </form>

            <!-- Formulario Entidad -->
            <form v-if="tipoUsuarioSeleccionado === 'entidad'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre de la Entidad</label>
                <input v-model="nuevoUsuario.entityName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">NIT</label>
                <input v-model="nuevoUsuario.nit" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Dirección</label>
                <input v-model="nuevoUsuario.address" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</label>
                <input v-model="nuevoUsuario.phone" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
                <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Tipo de Entidad</label>
                <select v-model="nuevoUsuario.entityType" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                  <option value="">Seleccione un tipo</option>
                  <option value="hospital">Hospital</option>
                  <option value="clinica">Clínica</option>
                  <option value="laboratorio">Laboratorio</option>
                  <option value="ips">IPS</option>
                </select>
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear Entidad</button>
              </div>
            </form>

            <!-- Formulario CUPS -->
            <form v-if="tipoUsuarioSeleccionado === 'cups'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Código CUPS</label>
                <input v-model="nuevoUsuario.cupsCode" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre del Procedimiento</label>
                <input v-model="nuevoUsuario.cupsName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Categoría</label>
                <select v-model="nuevoUsuario.cupsCategory" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                  <option value="">Seleccione una categoría</option>
                  <option value="diagnostico">Diagnóstico</option>
                  <option value="terapeutico">Terapéutico</option>
                  <option value="quirurgico">Quirúrgico</option>
                  <option value="procedimiento">Procedimiento</option>
                </select>
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Descripción</label>
                <textarea v-model="nuevoUsuario.cupsDescription" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" rows="3"></textarea>
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear CUPS</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div v-if="usuarioCreado" class="p-4 mt-4 rounded-lg bg-green-50 text-green-800 border border-green-200">
        {{ mensajeExito }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import Dropzone from '@/components/Muestras/NuevaMuestra/Dropzone.vue'

const tiposUsuario = [
  { value: 'administrativo', label: 'Administrativo' },
  { value: 'patologo', label: 'Patólogo' },
  { value: 'entidad', label: 'Entidad' },
  { value: 'cups', label: 'CUPS' }
]

const tipoUsuarioSeleccionado = ref('')

const firmaPatologoFile = ref<File | null>(null)

const nuevoUsuario = ref({
  // Campos comunes
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  role: '',
  specialty: '',
  
  // Campos específicos para administrativo
  document: '',
  startDate: '',
  
  // Campos específicos para entidad
  entityName: '',
  nit: '',
  address: '',
  entityType: '',
  
  // Campos específicos para patólogo
  medicalLicense: '',
  observaciones: '',
  firmaPatologoUrl: '',
  isActive: true,
  startDate: '',
  
  // Campos específicos para CUPS
  cupsCode: '',
  cupsName: '',
  cupsCategory: '',
  cupsDescription: ''
})

const usuarioCreado = ref(false)

const mensajeExito = computed(() => {
  switch (tipoUsuarioSeleccionado.value) {
    case 'administrativo':
      return 'Usuario administrativo creado exitosamente.'
    case 'patologo':
      return 'Patólogo creado exitosamente.'
    case 'entidad':
      return 'Entidad creada exitosamente.'
    case 'cups':
      return 'CUPS creado exitosamente.'
    default:
      return 'Registro creado exitosamente.'
  }
})

// Validación de correo electrónico
const validarEmail = (email: string) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return regex.test(email)
}

// Validación de teléfono
const validarTelefono = (telefono: string) => {
  const regex = /^\+?[\d\s-]{10,}$/
  return regex.test(telefono)
}

// Manejo de errores
const errores = ref({
  email: '',
  phone: '',
  general: ''
})

// Función mejorada de creación
const crearUsuario = async () => {
  try {
    // Validaciones
    if (!validarEmail(nuevoUsuario.value.email)) {
      errores.value.email = 'Correo electrónico inválido'
      return
    }
    if (!validarTelefono(nuevoUsuario.value.phone)) {
      errores.value.phone = 'Formato de teléfono inválido'
      return
    }

    // Llamada a API
    const response = await api.crearUsuario(nuevoUsuario.value)
    
    if (response.success) {
      usuarioCreado.value = true
      setTimeout(() => {
        usuarioCreado.value = false
        // Limpiar formulario según el tipo
        nuevoUsuario.value = {
          firstName: '',
          lastName: '',
          email: '',
          phone: '',
          role: '',
          specialty: '',
          entityName: '',
          nit: '',
          address: '',
          entityType: '',
          medicalLicense: '',
          cupsCode: '',
          cupsName: '',
          cupsCategory: '',
          cupsDescription: '',
          document: '',
          startDate: '',
          observaciones: '',
          firmaPatologoUrl: '',
          isActive: true
        }
      }, 3000)
    }
  } catch (error) {
    errores.value.general = 'Error al crear usuario'
  }
}

const fileInput = ref<HTMLInputElement | null>(null)
const previewImage = ref<string | null>(null)

const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    // Validar tipo de archivo
    if (!file.type.startsWith('image/')) {
      alert('Por favor, selecciona un archivo de imagen válido')
      return
    }
    
    // Validar tamaño (máximo 2MB)
    if (file.size > 2 * 1024 * 1024) {
      alert('La imagen no debe superar los 2MB')
      return
    }
    
    // Crear preview
    const reader = new FileReader()
    reader.onload = (e) => {
      previewImage.value = e.target?.result as string
    }
    reader.readAsDataURL(file)
  }
}

// Manejar el archivo de la firma desde el evento del Dropzone
const handleFirmaFile = (file: File) => {
  firmaPatologoFile.value = file
  // Opcionalmente, podrías mostrar una vista previa o el nombre del archivo
  console.log('Firma recibida:', file.name)
}
</script>

<style scoped>
.edit-button-modern {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  color: white;
  background-color: #3b82f6;
  border: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.edit-button-modern:hover {
  background-color: #2563eb;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
  transform: translateY(-1px);
}
.edit-button-modern:active {
  transform: translateY(1px);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}
.dark .edit-button-modern {
  background-color: #4f46e5;
}
.dark .edit-button-modern:hover {
  background-color: #4338ca;
}
</style>
