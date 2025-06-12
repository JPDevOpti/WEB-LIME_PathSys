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
          :disabled="!searchCedula || isLoading"
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

      <!-- Nombre del Paciente -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Nombre del Paciente *
        </label>
        <input
          type="text"
          v-model="formData.nombrePaciente"
          placeholder="Ingrese el nombre completo del paciente"
          :class="getFieldClasses('nombrePaciente')"
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

      <!-- Edad -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Edad *
        </label>
        <input
          type="number"
          v-model="formData.edad"
          placeholder="Ingrese la edad"
          :class="getFieldClasses('edad')"
          required
          ref="edadInput"
          min="0"
          max="120"
        />
      </div>

      <!-- Entidad -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Entidad *
        </label>
        <div class="relative">
          <div class="relative">
            <input
              type="text"
              v-model="formData.entidad"
              @focus="showEntidades = true"
              @blur="ocultarEntidades"
              placeholder="Seleccione o escriba la entidad"
              :class="getFieldClasses('entidad')"
              required
              ref="entidadInput"
            />
            <button
              type="button"
              @click="showEntidades = !showEntidades"
              class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-500"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
          </div>
          
          <!-- Lista desplegable de entidades -->
          <div
            v-if="showEntidades"
            class="absolute z-50 w-full mt-1 bg-white rounded-md shadow-lg border border-gray-200 max-h-60 overflow-auto"
          >
            <ul class="py-1">
              <li
                v-for="entidad in entidadesFiltradas"
                :key="entidad.id"
                @mousedown="seleccionarEntidad(entidad)"
                class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer"
              >
                {{ entidad.nombre }}
              </li>
              <li
                v-if="entidadesFiltradas.length === 0"
                class="px-4 py-2 text-sm text-gray-500"
              >
                No se encontraron resultados
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Tipo de Atención -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Tipo de Atención *
        </label>
        <div class="flex items-center space-x-6">
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.tipoAtencion"
              value="ambulatorio"
              class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
              required
            />
            <span class="ml-2 text-sm text-gray-700">Ambulatorio</span>
          </label>
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.tipoAtencion"
              value="hospitalizado"
              class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
              required
            />
            <span class="ml-2 text-sm text-gray-700">Hospitalizado</span>
          </label>
        </div>
        <div v-if="hasAttemptedSubmit && !formData.tipoAtencion" class="mt-1 text-sm text-red-600">
          Por favor seleccione el tipo de atención
        </div>
      </div>

      <!-- Observaciones -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Observaciones
        </label>
        <textarea
          v-model="formData.observaciones"
          placeholder="Observaciones adicionales"
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
          {{ isLoading ? 'Guardando...' : 'Guardar Paciente' }}
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
              ID del paciente: {{ savedPatientId }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed, ref, onMounted, watch, nextTick } from 'vue'

interface FormData {
  numeroCedula: string
  nombrePaciente: string
  sexo: string
  edad: string
  entidad: string
  tipoAtencion: string
  cups: string[]
  observaciones: string
}

interface Entidad {
  id: string
  nombre: string
}

const emit = defineEmits(['update-patient-data', 'patient-saved'])

const formData = reactive<FormData>({
  numeroCedula: '',
  nombrePaciente: '',
  sexo: '',
  edad: '',
  entidad: '',
  tipoAtencion: '',
  cups: [''],
  observaciones: ''
})

const isLoading = ref(false)
const hasAttemptedSubmit = ref(false)
const savedPatientId = ref('')
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const showEntidades = ref(false)
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
const edadInput = ref<HTMLInputElement | null>(null)
const entidadInput = ref<HTMLInputElement | null>(null)

// Lista de entidades (simulada)
const entidades: Entidad[] = [
  { id: '1', nombre: 'Hospital Central' },
  { id: '2', nombre: 'Clínica San Juan' },
  { id: '3', nombre: 'Centro Médico ABC' },
  { id: '4', nombre: 'Hospital del Norte' },
  { id: '5', nombre: 'Clínica del Sur' }
]

// Computed properties
const entidadesFiltradas = computed(() => {
  if (!formData.entidad) return entidades
  const searchTerm = formData.entidad.toLowerCase()
  return entidades.filter(entidad => 
    entidad.nombre.toLowerCase().includes(searchTerm)
  )
})

const isFormValid = computed(() => {
  return (
    formData.numeroCedula.trim() !== '' &&
    formData.nombrePaciente.trim() !== '' &&
    formData.sexo !== '' &&
    formData.edad.trim() !== '' &&
    formData.entidad.trim() !== '' &&
    formData.tipoAtencion !== '' &&
    formData.cups.every(cups => cups.trim() !== '')
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

// Base de datos simulada de pacientes
const pacientesDB = [
  {
    numeroCedula: '12345678',
    nombrePaciente: 'Juan Pérez',
    sexo: 'masculino',
    edad: '35',
    entidad: 'Hospital Central',
    tipoAtencion: 'ambulatorio',
    cups: ['CUPS-001'],
    observaciones: 'Paciente con antecedentes de hipertensión'
  },
  {
    numeroCedula: '87654321',
    nombrePaciente: 'María García',
    sexo: 'femenino',
    edad: '28',
    entidad: 'Clínica San Juan',
    tipoAtencion: 'hospitalizado',
    cups: ['CUPS-002', 'CUPS-003'],
    observaciones: 'Paciente en observación'
  }
]

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

const seleccionarEntidad = (entidad: Entidad) => {
  formData.entidad = entidad.nombre
  showEntidades.value = false
}

const ocultarEntidades = () => {
  setTimeout(() => {
    showEntidades.value = false
  }, 200)
}

const limpiarFormulario = () => {
  Object.keys(formData).forEach(key => {
    const k = key as keyof FormData
    if (k === 'cups') {
      formData[k] = ['']
    } else {
      formData[k] = ''
    }
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
  searchStatus.value = 'Buscando paciente...'
  searchStatusType.value = 'success'

  try {
    // Simular llamada a API
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    const paciente = pacientesDB.find(p => p.numeroCedula === searchCedula.value.trim())
    
    if (paciente) {
      // Actualizar el formulario con los datos del paciente
      Object.assign(formData, paciente)
      pacienteEncontrado.value = true
      searchStatus.value = 'Paciente encontrado'
      searchStatusType.value = 'success'
    } else {
      searchStatus.value = 'No se encontró ningún paciente con esa cédula'
      searchStatusType.value = 'error'
      pacienteEncontrado.value = false
      limpiarFormulario()
    }
  } catch {
    searchStatus.value = 'Error al buscar el paciente'
    searchStatusType.value = 'error'
    pacienteEncontrado.value = false
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
  statusMessage.value = 'Guardando datos del paciente...'
  statusType.value = 'success'

  try {
    // Simular llamada a API
    await new Promise(resolve => setTimeout(resolve, 1500))
    const randomId = Math.random().toString(36).substring(2, 8).toUpperCase()
    savedPatientId.value = randomId
    statusMessage.value = 'Datos del paciente guardados correctamente'
    
    // Mostrar notificación
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

    emit('patient-saved', randomId)
  } catch {
    statusMessage.value = 'Error al guardar los datos del paciente'
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

// Función para copiar desde la notificación y cerrarla
const copyFromNotificationAndClose = async () => {
  await copyToClipboard()
  showNotification.value = false
}

// Función para copiar al portapapeles
const copyToClipboard = async () => {
  try {
    await navigator.clipboard.writeText(savedPatientId.value)
  } catch (err) {
    console.error('Error al copiar:', err)
  }
}
</script>