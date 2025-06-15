<!-- 
  Componente de demostración para búsqueda y edición de muestras
  Simula la búsqueda y edición de muestras en el front-end
-->

<template>
  <div class="space-y-6">
    <!-- Búsqueda de ID de Muestra -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Buscar por ID de Muestra *
      </label>
      <div class="flex space-x-2">
        <div class="relative flex-1">
          <input
            type="text"
            v-model="searchMuestraId"
            placeholder="Ingrese el ID de la muestra"
            class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            @keyup.enter="buscarMuestra"
            ref="muestraInput"
          />
          <button
            v-if="searchMuestraId"
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
          @click="buscarMuestra"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-400 disabled:hover:bg-gray-400 transition-colors"
          :disabled="!searchMuestraId || isLoading"
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
      <!-- Información del Paciente -->
      <div class="bg-gray-50 rounded-lg p-4 border border-gray-200">
        <h3 class="text-sm font-semibold text-gray-700 mb-3">Información del Paciente</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="mb-1.5 block text-sm font-medium text-gray-600">
              Nombre Completo *
            </label>
            <input
              type="text"
              v-model="formData.paciente.nombre"
              :class="getFieldClasses('paciente.nombre')"
              required
            />
          </div>
          <div>
            <label class="mb-1.5 block text-sm font-medium text-gray-600">
              Cédula *
            </label>
            <input
              type="text"
              v-model="formData.paciente.cedula"
              :class="getFieldClasses('paciente.cedula')"
              required
            />
          </div>
        </div>
      </div>

      <!-- ID de Muestra -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          ID de Muestra *
        </label>
        <input
          type="text"
          v-model="formData.idMuestra"
          class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs"
          readonly
        />
      </div>

      <!-- Médico Solicitante (tipo combobox, igual que patólogo) -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Médico Solicitante *
        </label>
        <div class="relative">
          <input
            type="text"
            v-model="medicoSolicitanteSearch"
            @input="filterMedicos"
            @focus="showMedicosList = true"
            placeholder="Buscar o seleccionar médico"
            class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            required
          />
          <!-- Lista desplegable de médicos -->
          <div
            v-if="showMedicosList && filteredMedicos.length > 0"
            class="absolute z-[9999] w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto"
          >
            <div
              v-for="medico in filteredMedicos"
              :key="medico.value"
              @click="selectMedico(medico)"
              class="px-4 py-2 hover:bg-gray-100 cursor-pointer text-sm"
              :class="{ 'bg-gray-100': formData.medicoSolicitante === medico.value }"
            >
              {{ medico.label }}
            </div>
          </div>
        </div>
      </div>

      <!-- CUPS por Muestra -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          CUPS por Muestra *
        </label>
        <div class="space-y-6">
          <div v-for="(muestra, muestraIndex) in formData.muestras" :key="muestraIndex" class="space-y-2">
            <h4 class="text-sm font-medium text-gray-700">Muestra {{ muestra.numero }}</h4>
            <div v-for="(cups, cupsIndex) in muestra.cups" :key="cupsIndex" class="flex items-center space-x-2">
              <input
                type="text"
                v-model="formData.muestras[muestraIndex].cups[cupsIndex]"
                placeholder="Ingrese el CUPS"
                class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                required
                @keydown.enter.prevent="agregarCupsSiNecesario(muestraIndex, cupsIndex)"
              />
              <button
                v-if="muestra.cups.length > 1"
                @click="eliminarCups(muestraIndex, cupsIndex)"
                type="button"
                class="p-2 text-red-600 hover:text-red-800"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </div>
            <!-- Botón para agregar CUPS debajo de la lista, igual que en AsignarCodigoMuestra.vue -->
            <button
              @click="agregarCups(muestraIndex)"
              type="button"
              class="mt-2 inline-flex items-center px-3 py-1.5 border border-gray-300 rounded-md text-xs font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-1 transition-colors"
            >
              <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              Agregar CUPS
            </button>
          </div>
        </div>
      </div>

      <!-- Observaciones -->
      <div>
        <label class="mb-1.5 block text-sm font-medium text-gray-700">
          Observaciones
        </label>
        <textarea
          v-model="formData.observaciones"
          rows="4"
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
          @click="guardarCambios"
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
          {{ isLoading ? 'Guardando...' : 'Guardar Cambios' }}
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
            <p v-if="statusType === 'success' && savedMuestraId" class="text-xs mt-1 opacity-75">
              ID de la muestra: {{ savedMuestraId }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed, ref, onMounted, watch } from 'vue'

interface FormData {
  idMuestra: string
  paciente: {
    nombre: string
    cedula: string
  }
  medicoSolicitante: string
  observaciones: string
  muestras: {
    numero: number
    cups: string[]
  }[]
}

const formData = reactive<FormData>({
  idMuestra: '',
  paciente: {
    nombre: '',
    cedula: ''
  },
  medicoSolicitante: '',
  observaciones: '',
  muestras: [{
    numero: 1,
    cups: ['']
  }]
})

const isLoading = ref(false)
const hasAttemptedSubmit = ref(false)
const savedMuestraId = ref('')
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const showNotification = ref(false)
const progressWidth = ref(100)

// Estado de búsqueda
const searchMuestraId = ref('')
const searchStatus = ref('')
const searchStatusType = ref<'success' | 'error'>('success')
const muestraEncontrada = ref(false)

// Referencias para los inputs
const muestraInput = ref<HTMLInputElement | null>(null)

// Base de datos simulada de muestras
const muestrasDB = [
  {
    idMuestra: 'M001',
    paciente: {
      nombre: 'Juan Pérez García',
      cedula: '12345678'
    },
    estado: 'en-proceso',
    medicoSolicitante: 'Dr. García',
    observaciones: 'Muestra recibida en condiciones óptimas',
    muestras: [
      { numero: 1, cups: ['CUPS001', 'CUPS002'] }
    ]
  },
  {
    idMuestra: 'M002',
    paciente: {
      nombre: 'María García López',
      cedula: '87654321'
    },
    estado: 'recibida',
    medicoSolicitante: 'Dra. Martínez',
    observaciones: 'Paciente con antecedentes de diabetes',
    muestras: [
      { numero: 1, cups: ['CUPS003'] }
    ]
  }
]

// Computed properties
const isFormValid = computed(() => {
  return (
    formData.idMuestra.trim() !== '' &&
    formData.paciente.nombre.trim() !== '' &&
    formData.paciente.cedula.trim() !== '' &&
    formData.medicoSolicitante.trim() !== '' &&
    formData.muestras.length > 0 &&
    formData.muestras.every(muestra =>
      muestra.cups.length > 0 &&
      muestra.cups.every(cups => cups.trim() !== '')
    )
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

// Lista de médicos solicitantes (puedes editar estos valores)
const medicos = [
  { value: 'dr-jimenez', label: 'Dr. Jiménez Herrera (JH)' },
  { value: 'dra-morales', label: 'Dra. Morales Castro (MC)' },
  { value: 'dr-vargas', label: 'Dr. Vargas Mendez (VM)' },
  { value: 'dra-restrepo', label: 'Dra. Restrepo Vega (RV)' },
  { value: 'dr-sandoval', label: 'Dr. Sandoval Lima (SL)' },
  { value: 'dra-herrera', label: 'Dra. Herrera Cruz (HC)' }
]

const medicoSolicitanteSearch = ref('')
const showMedicosList = ref(false)
const filteredMedicos = ref(medicos)

// Filtrar médicos según búsqueda
const filterMedicos = () => {
  const search = medicoSolicitanteSearch.value.toLowerCase()
  filteredMedicos.value = medicos.filter(medico =>
    medico.label.toLowerCase().includes(search)
  )
}

// Seleccionar médico de la lista
const selectMedico = (medico: { value: string; label: string }) => {
  formData.medicoSolicitante = medico.label
  medicoSolicitanteSearch.value = medico.label
  showMedicosList.value = false
}

// Sincronizar input con valor seleccionado
watch(
  () => formData.medicoSolicitante,
  (val) => {
    medicoSolicitanteSearch.value = val
  }
)

// Cerrar la lista al hacer clic fuera
onMounted(() => {
  document.addEventListener('click', (e) => {
    const target = e.target as HTMLElement
    if (!target.closest('.relative')) {
      showMedicosList.value = false
    }
  })
})

// Methods
const getFieldClasses = (field: string) => {
  const baseClasses = 'h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10'
  const errorClasses = hasAttemptedSubmit.value && !(formData as any)[field] ? 'border-red-300' : 'border-gray-300'
  return `${baseClasses} ${errorClasses}`
}

const getTextareaClasses = (field: string) => {
  const baseClasses = 'w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none'
  const errorClasses = hasAttemptedSubmit.value && !(formData as any)[field] ? 'border-red-300' : 'border-gray-300'
  return `${baseClasses} ${errorClasses}`
}

const limpiarFormulario = () => {
  formData.idMuestra = ''
  formData.paciente.nombre = ''
  formData.paciente.cedula = ''
  formData.medicoSolicitante = ''
  formData.observaciones = ''
  formData.muestras = [{ numero: 1, cups: [''] }]
  hasAttemptedSubmit.value = false
  statusMessage.value = ''
  savedMuestraId.value = ''
}

const limpiarBusqueda = () => {
  searchMuestraId.value = ''
  searchStatus.value = ''
  muestraEncontrada.value = false
  limpiarFormulario()
}

const buscarMuestra = async () => {
  if (!searchMuestraId.value.trim()) {
    searchStatus.value = 'Por favor ingrese un ID de muestra'
    searchStatusType.value = 'error'
    return
  }

  isLoading.value = true
  searchStatus.value = 'Buscando muestra...'
  searchStatusType.value = 'success'

  try {
    // Simular llamada a API
    await new Promise(resolve => setTimeout(resolve, 500))
    
    const muestra = muestrasDB.find(m => m.idMuestra === searchMuestraId.value.trim())
    
    if (muestra) {
      // Si la muestra no tiene la propiedad 'muestras', inicialízala
      if (!muestra.muestras) {
        muestra.muestras = [{ numero: 1, cups: [''] }]
      }
      Object.assign(formData, muestra)
      muestraEncontrada.value = true
      searchStatus.value = 'Muestra encontrada'
      searchStatusType.value = 'success'
    } else {
      searchStatus.value = 'No se encontró ninguna muestra con ese ID'
      searchStatusType.value = 'error'
      muestraEncontrada.value = false
      limpiarFormulario()
    }
  } catch {
    searchStatus.value = 'Error al buscar la muestra'
    searchStatusType.value = 'error'
    muestraEncontrada.value = false
  } finally {
    isLoading.value = false
  }
}

const guardarCambios = async () => {
  hasAttemptedSubmit.value = true
  
  if (!isFormValid.value) {
    statusMessage.value = 'Por favor complete todos los campos requeridos'
    statusType.value = 'error'
    return
  }

  isLoading.value = true
  statusMessage.value = 'Guardando datos de la muestra...'
  statusType.value = 'success'

  try {
    // Simular llamada a API
    await new Promise(resolve => setTimeout(resolve, 1500))
    const randomId = Math.random().toString(36).substring(2, 8).toUpperCase()
    savedMuestraId.value = randomId
    statusMessage.value = 'Datos de la muestra guardados correctamente'
    
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
  } catch {
    statusMessage.value = 'Error al guardar los datos de la muestra'
    statusType.value = 'error'
  } finally {
    isLoading.value = false
  }
}

// Métodos para CUPS
const agregarCups = (muestraIndex: number) => {
  formData.muestras[muestraIndex].cups.push('')
}

const eliminarCups = (muestraIndex: number, cupsIndex: number) => {
  formData.muestras[muestraIndex].cups.splice(cupsIndex, 1)
}

const agregarCupsSiNecesario = (muestraIndex: number, cupsIndex: number) => {
  const currentCups = formData.muestras[muestraIndex].cups[cupsIndex]
  if (currentCups.trim() !== '') {
    agregarCups(muestraIndex)
  }
}

// Focus en el primer campo al montar
onMounted(() => {
  if (muestraInput.value) {
    muestraInput.value.focus()
  }
})
</script>