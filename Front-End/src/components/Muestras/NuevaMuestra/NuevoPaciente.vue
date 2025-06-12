<template>
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
        :class="getFieldClasses('numeroCedula', true)"
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
        :class="getFieldClasses('nombrePaciente', true)"
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
        :class="getFieldClasses('edad', true)"
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
      <ListaDesplegable
        v-model="formData.entidad"
        :options="entidades"
        label=""
        placeholder="Seleccione o escriba la entidad"
        :required="true"
        :error="hasAttemptedSubmit && !formData.entidad"
      />
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
    <div class="flex flex-col pt-6">
      <!-- Fila de Botones -->
      <div class="flex items-center justify-end space-x-3 mb-4">
        <BotonLimpiar 
          @limpiar="limpiarFormulario"
          :disabled="isLoading"
        />
        <button
          @click="handleGuardarClick"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
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
      
      <!-- Alerta de Validación -->
      <BotonGuardar
        ref="botonGuardarRef"
        :campos="formData"
        :campos-obligatorios="['numeroCedula','nombrePaciente','sexo','edad','entidad','tipoAtencion']"
        :etiquetas="{
          numeroCedula: 'Número de Cédula',
          nombrePaciente: 'Nombre del Paciente',
          sexo: 'Sexo',
          edad: 'Edad',
          entidad: 'Entidad',
          tipoAtencion: 'Tipo de Atención'
        }"
        :solo-alerta="true"
        :mostrar-error="showValidationError"
        @validation-error="handleValidationError"
      />
    </div>

    <!-- Mensaje de Estado -->
    <div v-if="statusMessage" :class="statusMessageClasses" class="mt-6">
      <div class="flex items-center space-x-3">
        <div class="flex-shrink-0">
          <svg
            :class="statusIconClass"
            class="w-8 h-8"
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
        </div>
        <div class="flex-1">
          <p class="font-bold text-lg">{{ statusMessage }}</p>
          <div v-if="statusType === 'success'" class="mt-3">
            <div class="bg-white bg-opacity-50 rounded-md border border-green-300 p-3">
              <p class="text-sm font-medium text-green-800 mb-2">Datos del Paciente Registrado:</p>
              <div class="space-y-1">
                <p class="text-lg font-semibold text-green-900">{{ formData.nombrePaciente }}</p>
                <p class="text-base text-green-800">Número de Cédula: <span class="font-mono font-bold">{{ formData.numeroCedula }}</span></p>
              </div>
              <button 
                @click="copiarDNI"
                class="mt-2 inline-flex items-center px-3 py-1.5 border border-green-300 rounded-md text-xs font-medium text-green-700 bg-white hover:bg-green-50 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-1 transition-colors"
              >
                <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                Copiar Número de Cédula
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Notificación Emergente Centrada -->
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="opacity-0 transform scale-95"
      enter-to-class="opacity-100 transform scale-100"
      leave-active-class="transition ease-in duration-200"
      leave-from-class="opacity-100 transform scale-100"
      leave-to-class="opacity-0 transform scale-95"
    >
      <div
        v-if="showNotification"
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
      >
        <!-- Overlay oscuro -->
        <div 
          class="absolute inset-0 bg-black bg-opacity-50"
          @click="showNotification = false"
        ></div>
        
        <!-- Modal de notificación -->
        <div
          class="relative bg-white rounded-2xl shadow-2xl border-l-4 border-green-500 p-8 max-w-md w-full"
        >
          <div class="text-center">
            <!-- Ícono de éxito -->
            <div class="mx-auto flex items-center justify-center w-16 h-16 rounded-full bg-green-100 mb-4">
              <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            
            <!-- Título -->
            <h3 class="text-2xl font-bold text-gray-900 mb-2">¡Paciente Registrado!</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              El paciente <strong class="text-brand-600">{{ formData.nombrePaciente }}</strong>
            </p>
            <p class="text-gray-600 mb-1">
              con Número de Cédula
            </p>
            <p class="text-lg font-semibold text-brand-600 font-mono mb-4">
              {{ formData.numeroCedula }}
            </p>
            <p class="text-gray-600 mb-6">
              se ha registrado correctamente en el sistema.
            </p>
            
            <!-- Timestamp -->
            <div class="flex items-center justify-center text-sm text-gray-500 mb-6">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {{ new Date().toLocaleTimeString() }}
            </div>
            
            <!-- Barra de progreso -->
            <div class="w-full bg-gray-200 rounded-full h-2 mb-6">
              <div 
                class="bg-green-500 h-2 rounded-full transition-all duration-75 ease-linear"
                :style="{ width: progressWidth + '%' }"
              ></div>
            </div>
            
            <!-- Botón de cerrar -->
            <button
              @click="showNotification = false"
              class="w-full inline-flex items-center justify-center px-6 py-3 border border-transparent rounded-lg text-base font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-3 focus:ring-green-500 focus:ring-offset-2 transition-colors"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
              Entendido
            </button>
          </div>
          
          <!-- Botón X en la esquina -->
          <button
            @click="showNotification = false"
            class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 transition-colors p-2 rounded-full hover:bg-gray-100"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed, ref, watch } from 'vue'
import 'flatpickr/dist/flatpickr.css'
import ListaDesplegable from '../../ComponentesFormularios/ListaDesplegable.vue'
import BotonGuardar from '../../ComponentesFormularios/BotonGuardar.vue'
import BotonLimpiar from '../../ComponentesFormularios/BotonLimpiar.vue'

// Estados para el componente
const isLoading = ref(false)
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const hasAttemptedSubmit = ref(false)
const showNotification = ref(false)
const progressWidth = ref(100)
const botonGuardarRef = ref<{ validarExternamente: () => boolean } | null>(null)
const showValidationError = ref(false)

// Entidades disponibles
const entidades = [
  { id: 'ESSALUD', nombre: 'ESSALUD' },
  { id: 'MINSA', nombre: 'MINSA' },
  { id: 'FFAA', nombre: 'FFAA' },
  { id: 'PNP', nombre: 'PNP' },
  { id: 'SIS', nombre: 'SIS' },
  { id: 'PRIVADO', nombre: 'PRIVADO' },
  { id: 'OTRO', nombre: 'OTRO' }
]

// Datos del formulario reactivos
const formData = reactive({
  numeroCedula: '',
  nombrePaciente: '',
  sexo: '',
  edad: '',
  entidad: '',
  tipoAtencion: '',
  observaciones: '',
})

// Referencias a los inputs
const cedulaInput = ref<HTMLInputElement | null>(null)
const nombreInput = ref<HTMLInputElement | null>(null)
const edadInput = ref<HTMLInputElement | null>(null)

// Clases para el mensaje de estado
const statusMessageClasses = computed(() => {
  return statusType.value === 'success'
    ? 'rounded-lg bg-green-50 border border-green-200 p-4'
    : 'rounded-lg bg-red-50 border border-red-200 p-4'
})

const statusIconClass = computed(() => {
  return statusType.value === 'success' ? 'text-green-600' : 'text-red-600'
})

// Función para guardar el paciente
const guardarPaciente = async () => {
  isLoading.value = true
  statusMessage.value = ''
  try {
    statusType.value = 'success'
    statusMessage.value = 'Paciente guardado exitosamente'
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
    emit('patient-saved', { ...formData })
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al guardar el paciente. Intente nuevamente.'
    console.error('Error:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para limpiar el formulario
const limpiarFormulario = () => {
  formData.numeroCedula = ''
  formData.nombrePaciente = ''
  formData.sexo = ''
  formData.edad = ''
  formData.entidad = ''
  formData.tipoAtencion = ''
  formData.observaciones = ''
  
  statusMessage.value = ''
  hasAttemptedSubmit.value = false
  showValidationError.value = false
}

// Función para manejar errores de validación
const handleValidationError = (camposInvalidos: string[]) => {
  hasAttemptedSubmit.value = true
  console.log('Campos inválidos:', camposInvalidos)
}

// Función para manejar el click del botón guardar
const handleGuardarClick = () => {
  // Trigger validation using the BotonGuardar component
  if (botonGuardarRef.value) {
    const isValid = botonGuardarRef.value.validarExternamente()
    if (isValid) {
      guardarPaciente()
      showValidationError.value = false
    } else {
      showValidationError.value = true
    }
  }
}

// Emitir los datos del formulario para poder usarlos en el componente padre
const emit = defineEmits(['update-patient-data', 'patient-saved'])

// Watch para emitir cambios
watch(formData, (newData) => {
  emit('update-patient-data', newData)
}, { deep: true, immediate: true })

// Watch para ocultar errores de validación cuando el formulario se vuelve válido
watch(formData, () => {
  if (showValidationError.value && botonGuardarRef.value) {
    const isValid = botonGuardarRef.value.validarExternamente()
    if (isValid) {
      showValidationError.value = false
    }
  }
}, { deep: true })

// Función para obtener clases CSS condicionales para campos requeridos
const getFieldClasses = (fieldName: keyof typeof formData, isRequired = false) => {
  const baseClasses = "h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  
  if (isRequired && hasAttemptedSubmit.value && !formData[fieldName]) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10`
}

// Función específica para textareas
const getTextareaClasses = (fieldName: keyof typeof formData, isRequired = false) => {
  const baseClasses = "w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3 resize-none"
  
  if (isRequired && hasAttemptedSubmit.value && !formData[fieldName]) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10`
}

// Función para copiar el Número de Cédula del paciente
const copiarDNI = async () => {
  if (formData.numeroCedula) {
    try {
      await navigator.clipboard.writeText(formData.numeroCedula)
      // Opcional: mostrar feedback visual de que se copió
      console.log('Número de Cédula copiado al portapapeles')
    } catch (err) {
      console.error('Error al copiar el Número de Cédula:', err)
    }
  }
}
</script>