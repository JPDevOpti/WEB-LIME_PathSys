<template>
  <div class="space-y-6">
    <!-- Búsqueda de Cédula -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Buscar por Cédula *
      </label>
      <div class="flex space-x-2">
        <div class="relative flex-1">
          <input
            type="text"
            v-model="searchCedula"
            placeholder="Ingrese el número de cédula"
            class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            @keyup.enter="buscarPaciente"
            ref="cedulaInput"
          />
          <button
            v-if="searchCedula"
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
          @click="buscarPaciente"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-400 disabled:hover:bg-gray-400 transition-colors"
          :disabled="isLoading"
        >
          <svg
            v-if="isLoading"
            class="animate-spin -ml-1 mr-2 h-4 w-4 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <svg
            v-else
            class="w-4 h-4 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          {{ isLoading ? 'Buscando...' : 'Buscar' }}
        </button>
      </div>
      <!-- Mensaje de estado de búsqueda -->
      <div v-if="searchStatus" :class="searchStatusClasses" class="mt-2">
        <div class="flex items-start space-x-2">
          <svg
            :class="searchStatusIconClass"
            class="w-5 h-5 mt-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              v-if="searchStatusType === 'success'"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
            <path
              v-else
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p class="text-sm">{{ searchStatus }}</p>
        </div>
      </div>
    </div>

    <!-- Formulario -->
    <div class="space-y-6">
      <!-- Número de Cédula -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Número de Cédula *
        </label>
        <input
          type="text"
          v-model="formData.numeroCedula"
          placeholder="Ej: 12345678"
          :class="getFieldClasses('numeroCedula')"
          required
          ref="cedulaInput"
        />
      </div>

      <!-- Nombre del Patólogo -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Nombre del Patólogo *
        </label>
        <input
          type="text"
          v-model="formData.nombreCompleto"
          placeholder="Ingrese el nombre completo del patólogo"
          :class="getFieldClasses('nombreCompleto')"
          required
          ref="nombreInput"
        />
      </div>

      <!-- Sexo -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Sexo *
        </label>
        <div class="flex items-center space-x-6">
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.sexo"
              value="masculino"
              class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
              required
            />
            <span class="ml-2 text-sm text-gray-700">Masculino</span>
          </label>
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.sexo"
              value="femenino"
              class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
              required
            />
            <span class="ml-2 text-sm text-gray-700">Femenino</span>
          </label>
        </div>
        <div v-if="hasAttemptedSubmit && !formData.sexo" class="mt-1 text-sm text-red-600">
          Por favor seleccione el sexo
        </div>
      </div>

      <!-- Email -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Email *
        </label>
        <input
          type="email"
          v-model="formData.email"
          placeholder="Ej: correo@ejemplo.com"
          :class="getFieldClasses('email')"
          required
          ref="emailInput"
        />
      </div>

      <!-- Teléfono -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Teléfono
        </label>
        <input
          type="tel"
          v-model="formData.telefono"
          placeholder="Ej: 987654321"
          :class="getFieldClasses('telefono')"
          ref="telefonoInput"
        />
      </div>

      <!-- Especialidad -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Especialidad *
        </label>
        <input
          type="text"
          v-model="formData.especialidad"
          placeholder="Ej: Anatomía Patológica"
          :class="getFieldClasses('especialidad')"
          required
          ref="especialidadInput"
        />
      </div>

      <!-- Número de Registro Médico -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Número de Registro Médico (RNE/CMP) *
        </label>
        <input
          type="text"
          v-model="formData.registroMedico"
          placeholder="Ej: 12345"
          :class="getFieldClasses('registroMedico')"
          required
          ref="registroMedicoInput"
        />
      </div>

      <!-- Firma del Patólogo -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Firma del Patólogo
        </label>
        <Dropzone
          :uploadUrl="'/api/upload-signature'"
          :dropzoneId="dropzoneId"
          @file-added="handleFirmaFile"
        />
        <div v-if="firmaPatologoFile" class="mt-2 text-sm text-gray-600">
          Archivo seleccionado: {{ firmaPatologoFile.name }}
        </div>
      </div>

      <!-- Observaciones -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Observaciones
        </label>
        <textarea
          v-model="formData.observaciones"
          placeholder="Observaciones adicionales sobre el patólogo"
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
          @click="guardarPaciente"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-400 disabled:hover:bg-gray-400 transition-colors"
          :disabled="isLoading || !isFormValid"
        >
          <svg
            v-if="isLoading"
            class="animate-spin -ml-1 mr-2 h-4 w-4 text-white"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <svg
            v-else
            class="w-4 h-4 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"
            />
          </svg>
          {{ isLoading ? 'Guardando...' : 'Guardar Patólogo' }}
        </button>
      </div>

      <!-- Mensaje de Estado -->
      <div v-if="statusMessage" :class="statusMessageClasses" class="mt-4">
        <div class="flex items-start space-x-2">
          <svg
            :class="statusIconClass"
            class="w-5 h-5 mt-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              v-if="statusType === 'success'"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
            <path
              v-else
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <div>
            <p class="font-medium text-sm">{{ statusMessage }}</p>
            <p v-if="statusType === 'success' && savedPatientId" class="text-xs mt-1 opacity-75">
              ID del patólogo: {{ savedPatientId }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Dropzone from '@/components/Muestras/NuevaMuestra/Dropzone.vue' // Import Dropzone correcto
import { reactive, computed, ref, onMounted, watch } from 'vue'

interface FormData {
  numeroCedula: string
  nombreCompleto: string
  sexo: string
  email: string
  telefono: string
  especialidad: string
  registroMedico: string
  observaciones: string
  firmaPatologoUrl?: string
}

const emit = defineEmits(['update-patient-data', 'patologo-saved'])

const formData = reactive<FormData>({
  numeroCedula: '',
  nombreCompleto: '',
  sexo: '',
  email: '',
  telefono: '',
  especialidad: '',
  registroMedico: '',
  observaciones: '',
  firmaPatologoUrl: ''
})
const firmaPatologoFile = ref<File | null>(null)

const isLoading = ref(false)
const hasAttemptedSubmit = ref(false)
const savedPatientId = ref('')
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const showNotification = ref(false)
const progressWidth = ref(100)

// Estado de búsqueda
const searchCedula = ref('')
const searchStatus = ref('')
const searchStatusType = ref<'success' | 'error'>('success')
const pacienteEncontrado = ref(false)

// Referencias para los inputs
const cedulaInput = ref<HTMLInputElement | null>(null)
const nombreInput = ref<HTMLInputElement | null>(null)
const emailInput = ref<HTMLInputElement | null>(null)
const telefonoInput = ref<HTMLInputElement | null>(null)
const especialidadInput = ref<HTMLInputElement | null>(null)
const registroMedicoInput = ref<HTMLInputElement | null>(null)

// Base de datos simulada de patólogos
const patologoDB = [
  {
    numeroCedula: '12345678',
    nombreCompleto: 'Dra. Ana Patóloga',
    sexo: 'femenino',
    email: 'ana@patologia.com',
    telefono: '987654321',
    especialidad: 'Anatomía Patológica',
    registroMedico: 'CMP12345',
    observaciones: 'Especialista en biopsias'
  }
]

// Computed properties
const isFormValid = computed(() => {
  return (
    formData.numeroCedula.trim() !== '' &&
    formData.nombreCompleto.trim() !== '' &&
    formData.sexo !== '' &&
    formData.email.trim() !== '' &&
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim()) &&
    formData.especialidad.trim() !== '' &&
    formData.registroMedico.trim() !== ''
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

// Methods
const getFieldClasses = (field: keyof FormData) => {
  const baseClasses = 'h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10'
  const errorClasses = hasAttemptedSubmit.value && !formData[field] ? 'border-red-300' : 'border-gray-300'
  return `${baseClasses} ${errorClasses}`
}

const getTextareaClasses = (field: keyof FormData) => {
  const baseClasses = 'w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none'
  const errorClasses = hasAttemptedSubmit.value && !formData[field] ? 'border-red-300' : 'border-gray-300'
  return `${baseClasses} ${errorClasses}`
}

const limpiarFormulario = () => {
  Object.keys(formData).forEach(key => {
    const k = key as keyof FormData
    formData[k] = ''
  })
  hasAttemptedSubmit.value = false
  statusMessage.value = ''
  savedPatientId.value = ''
}

const limpiarBusqueda = () => {
  searchCedula.value = ''
  searchStatus.value = ''
  pacienteEncontrado.value = false
  limpiarFormulario()
}

const buscarPaciente = async () => {
  if (!searchCedula.value.trim()) {
    searchStatus.value = 'Por favor ingrese un número de cédula'
    searchStatusType.value = 'error'
    return
  }
  isLoading.value = true
  searchStatus.value = 'Buscando patólogo...'
  searchStatusType.value = 'success'
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    const patologo = patologoDB.find(p => p.numeroCedula === searchCedula.value.trim())
    if (patologo) {
      Object.assign(formData, patologo)
      searchStatus.value = 'Patólogo encontrado'
      searchStatusType.value = 'success'
    } else {
      searchStatus.value = 'No se encontró ningún patólogo con esa cédula'
      searchStatusType.value = 'error'
      limpiarFormulario()
    }
  } catch {
    searchStatus.value = 'Error al buscar el patólogo'
    searchStatusType.value = 'error'
  } finally {
    isLoading.value = false
  }
}

const guardarPaciente = async () => {
  hasAttemptedSubmit.value = true
  if (!isFormValid.value) {
    statusMessage.value = 'Por favor complete todos los campos requeridos'
    statusType.value = 'error'
    return
  }
  isLoading.value = true
  statusMessage.value = 'Guardando datos del patólogo...'
  statusType.value = 'success'
  try {
    await new Promise(resolve => setTimeout(resolve, 1500))
    statusMessage.value = 'Datos del patólogo guardados correctamente'
    showNotification.value = true
    progressWidth.value = 100
    const duration = 5000
    const interval = 50
    const decrement = (interval / duration) * 100
    const progressInterval = setInterval(() => {
      progressWidth.value -= decrement
      if (progressWidth.value <= 0) {
        clearInterval(progressInterval)
        showNotification.value = false
        progressWidth.value = 100
      }
    }, interval)
    emit('patologo-saved')
  } catch {
    statusMessage.value = 'Error al guardar los datos del patólogo'
    statusType.value = 'error'
  } finally {
    isLoading.value = false
  }
}

// Watch para emitir cambios y mostrar notificación
watch(formData, (newData) => {
  emit('update-patient-data', newData)
  
  // Mostrar notificación solo si hay cambios y el formulario es válido
  if (isFormValid.value && !isLoading.value) {
    showNotification.value = true
    progressWidth.value = 100
    
    // Iniciar barra de progreso
    const duration = 5000 // 5 segundos
    const interval = 50 // Update every 50ms
    const decrement = (interval / duration) * 100

    const progressInterval = setInterval(() => {
      progressWidth.value -= decrement
      if (progressWidth.value <= 0) {
        clearInterval(progressInterval)
        showNotification.value = false
        progressWidth.value = 100
      }
    }, interval)
  }
}, { deep: true })

// Focus en el primer campo al montar
onMounted(() => {
  if (cedulaInput.value) {
    cedulaInput.value.focus()
  }
})

const handleFirmaFile = (file: File) => {
  firmaPatologoFile.value = file
}

const dropzoneId = 'firmaDropzonePatologo'; // id fijo y consistente para el Dropzone
</script>