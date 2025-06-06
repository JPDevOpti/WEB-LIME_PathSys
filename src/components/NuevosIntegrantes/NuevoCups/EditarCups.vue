<template>
  <div class="space-y-6">
    <!-- Búsqueda por Nombre de Entidad -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Buscar por Nombre de Entidad *
      </label>
      <div class="flex space-x-2">
        <div class="relative flex-1">
          <input
            type="text"
            v-model="searchNombre"
            placeholder="Ingrese el nombre de la entidad"
            class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            @keyup.enter="buscarEntidad"
            ref="nombreEntidadInput"
          />
          <button
            v-if="searchNombre"
            @click="limpiarBusqueda"
            type="button"
            class="absolute inset-y-0 right-0 flex items-center px-3 text-gray-400 hover:text-gray-600"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <button
          @click="buscarEntidad"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-400 disabled:hover:bg-gray-400 transition-colors"
          :disabled="isLoading"
        >
          <svg v-if="isLoading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <svg v-else class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          {{ isLoading ? 'Buscando...' : 'Buscar' }}
        </button>
      </div>
      <div v-if="searchStatus" :class="searchStatusClasses" class="mt-2">
        <div class="flex items-start space-x-2">
          <svg :class="searchStatusIconClass" class="w-5 h-5 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="searchStatusType === 'success'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <p class="text-sm">{{ searchStatus }}</p>
        </div>
      </div>
    </div>

    <!-- Formulario de Entidad -->
    <div class="space-y-6">
      <!-- Nombre de la Entidad -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Nombre de la Entidad *</label>
        <input
          type="text"
          v-model="formData.nombreEntidad"
          placeholder="Ej: Hospital Central"
          :class="getFieldClasses('nombreEntidad')"
          required
          ref="nombreEntidadInput"
        />
      </div>
      <!-- Tipo de Entidad -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Tipo de Entidad *</label>
        <select
          v-model="formData.tipoEntidad"
          :class="getFieldClasses('tipoEntidad')"
          required
          ref="tipoEntidadInput"
        >
          <option value="" disabled>Seleccione un tipo</option>
          <option value="Hospital">Hospital</option>
          <option value="Clínica">Clínica</option>
          <option value="Centro de Salud">Centro de Salud</option>
          <option value="Laboratorio">Laboratorio</option>
          <option value="Otro">Otro</option>
        </select>
      </div>
      <!-- RUC/NIT -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">RUC / NIT *</label>
        <input
          type="text"
          v-model="formData.ruc"
          placeholder="Ej: 12345678901"
          :class="getFieldClasses('ruc')"
          required
          ref="rucInput"
        />
      </div>
      <!-- Dirección -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Dirección *</label>
        <input
          type="text"
          v-model="formData.direccion"
          placeholder="Ej: Av. Principal 123, Ciudad"
          :class="getFieldClasses('direccion')"
          required
          ref="direccionInput"
        />
      </div>
      <!-- Teléfono -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Teléfono</label>
        <input
          type="tel"
          v-model="formData.telefono"
          placeholder="Ej: 987654321"
          :class="getFieldClasses('telefono')"
          ref="telefonoInput"
        />
      </div>
      <!-- Email -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Email *</label>
        <input
          type="email"
          v-model="formData.email"
          placeholder="Ej: correo@ejemplo.com"
          :class="getFieldClasses('email')"
          required
          ref="emailInput"
        />
      </div>
      <!-- Responsable -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Responsable</label>
        <input
          type="text"
          v-model="formData.responsable"
          placeholder="Nombre del responsable de la entidad"
          :class="getFieldClasses('responsable')"
          ref="responsableInput"
        />
      </div>
      <!-- Observaciones -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">Observaciones</label>
        <textarea
          v-model="formData.observaciones"
          placeholder="Observaciones adicionales sobre la entidad"
          rows="3"
          :class="getTextareaClasses('observaciones')"
        ></textarea>
      </div>
      <!-- Botones de Acción -->
      <div class="flex items-center justify-end space-x-3 pt-6">
        <button
          @click="limpiarFormulario"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 focus:border-gray-400 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-400 disabled:border-gray-200 transition-colors"
          :disabled="isLoading"
        >
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Limpiar
        </button>
        <button
          @click="guardarEntidad"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-400 disabled:hover:bg-gray-400 transition-colors"
          :disabled="isLoading || !isFormValid"
        >
          <svg v-if="isLoading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          </svg>
          <svg v-else class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
          </svg>
          {{ isLoading ? 'Guardando...' : 'Guardar Entidad' }}
        </button>
      </div>
      <div v-if="statusMessage" :class="statusMessageClasses" class="mt-4">
        <div class="flex items-start space-x-2">
          <svg :class="statusIconClass" class="w-5 h-5 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="statusType === 'success'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <div>
            <p class="font-medium text-sm">{{ statusMessage }}</p>
            <p v-if="statusType === 'success' && savedEntidadId" class="text-xs mt-1 opacity-75">
              ID de la entidad: {{ savedEntidadId }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed, ref } from 'vue'

interface EntidadForm {
  nombreEntidad: string
  tipoEntidad: string
  ruc: string
  direccion: string
  telefono: string
  email: string
  responsable: string
  observaciones: string
}

const emit = defineEmits(['update-entidad-data', 'entidad-saved'])

const formData = reactive<EntidadForm>({
  nombreEntidad: '',
  tipoEntidad: '',
  ruc: '',
  direccion: '',
  telefono: '',
  email: '',
  responsable: '',
  observaciones: ''
})

const isLoading = ref(false)
const hasAttemptedSubmit = ref(false)
const savedEntidadId = ref('')
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')

const searchNombre = ref('')
const searchStatus = ref('')
const searchStatusType = ref<'success' | 'error'>('success')

const nombreEntidadInput = ref<HTMLInputElement | null>(null)
const tipoEntidadInput = ref<HTMLSelectElement | null>(null)
const rucInput = ref<HTMLInputElement | null>(null)
const direccionInput = ref<HTMLInputElement | null>(null)
const telefonoInput = ref<HTMLInputElement | null>(null)
const emailInput = ref<HTMLInputElement | null>(null)
const responsableInput = ref<HTMLInputElement | null>(null)

// Simulada base de datos de entidades
const entidadDB = [
  {
    nombreEntidad: 'Hospital Central',
    tipoEntidad: 'Hospital',
    ruc: '12345678901',
    direccion: 'Av. Principal 123',
    telefono: '987654321',
    email: 'hospital@central.com',
    responsable: 'Dr. Juan Pérez',
    observaciones: 'Entidad principal de la ciudad.'
  }
]

const isFormValid = computed(() => {
  return (
    formData.nombreEntidad.trim() !== '' &&
    formData.tipoEntidad !== '' &&
    formData.ruc.trim() !== '' &&
    formData.direccion.trim() !== '' &&
    formData.email.trim() !== '' &&
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim())
  )
})

const statusMessageClasses = computed(() => ({
  'p-4 rounded-lg': true,
  'bg-green-50 text-green-800': statusType.value === 'success',
  'bg-red-50 text-red-800': statusType.value === 'error'
}))

const statusIconClass = computed(() => ({
  'text-green-500': statusType.value === 'success',
  'text-red-500': statusType.value === 'error'
}))

const searchStatusClasses = computed(() => ({
  'p-3 rounded-lg': true,
  'bg-green-50 text-green-800': searchStatusType.value === 'success',
  'bg-red-50 text-red-800': searchStatusType.value === 'error'
}))

const searchStatusIconClass = computed(() => ({
  'text-green-500': searchStatusType.value === 'success',
  'text-red-500': searchStatusType.value === 'error'
}))

const getFieldClasses = (field: keyof EntidadForm) => {
  const baseClasses = 'h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10'
  const errorClasses = hasAttemptedSubmit.value && !formData[field] ? 'border-red-300' : 'border-gray-300'
  return `${baseClasses} ${errorClasses}`
}

const getTextareaClasses = (field: keyof EntidadForm) => {
  const baseClasses = 'w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none'
  const errorClasses = hasAttemptedSubmit.value && !formData[field] ? 'border-red-300' : 'border-gray-300'
  return `${baseClasses} ${errorClasses}`
}

const limpiarFormulario = () => {
  Object.keys(formData).forEach(key => {
    const k = key as keyof EntidadForm
    formData[k] = ''
  })
  hasAttemptedSubmit.value = false
  statusMessage.value = ''
  savedEntidadId.value = ''
}

const limpiarBusqueda = () => {
  searchNombre.value = ''
  searchStatus.value = ''
  limpiarFormulario()
}

const buscarEntidad = async () => {
  if (!searchNombre.value.trim()) {
    searchStatus.value = 'Por favor ingrese un nombre de entidad'
    searchStatusType.value = 'error'
    return
  }
  isLoading.value = true
  searchStatus.value = 'Buscando entidad...'
  searchStatusType.value = 'success'
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    const entidad = entidadDB.find(e => e.nombreEntidad.toLowerCase() === searchNombre.value.trim().toLowerCase())
    if (entidad) {
      Object.assign(formData, entidad)
      searchStatus.value = 'Entidad encontrada'
      searchStatusType.value = 'success'
    } else {
      searchStatus.value = 'No se encontró ninguna entidad con ese nombre'
      searchStatusType.value = 'error'
      limpiarFormulario()
    }
  } catch {
    searchStatus.value = 'Error al buscar la entidad'
    searchStatusType.value = 'error'
  } finally {
    isLoading.value = false
  }
}

const guardarEntidad = async () => {
  hasAttemptedSubmit.value = true
  if (!isFormValid.value) {
    statusMessage.value = 'Por favor complete todos los campos requeridos'
    statusType.value = 'error'
    return
  }
  isLoading.value = true
  statusMessage.value = 'Guardando datos de la entidad...'
  statusType.value = 'success'
  try {
    await new Promise(resolve => setTimeout(resolve, 1500))
    statusMessage.value = 'Datos de la entidad guardados correctamente'
    savedEntidadId.value = formData.ruc
    emit('entidad-saved')
  } catch {
    statusMessage.value = 'Error al guardar los datos de la entidad'
    statusType.value = 'error'
  } finally {
    isLoading.value = false
  }
}
</script>