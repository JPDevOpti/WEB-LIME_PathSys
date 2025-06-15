<template>
  <div class="space-y-6">
    <!-- Cédula -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Cédula *
      </label>
      <div class="relative">
        <input
          type="text"
          v-model="formData.numeroCedula"
          @input="handleCedulaInput"
          @blur="validateCedula"
          placeholder="Ejemplo: 12345678"
          :class="getCedulaFieldClasses()"
          required
          ref="cedulaInput"
          maxlength="10"
          :disabled="isValidatingCedula"
        />
        <div v-if="isValidatingCedula" class="absolute inset-y-0 right-0 pr-3 flex items-center">
          <svg class="animate-spin h-4 w-4 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        </div>
      </div>
      <div v-if="cedulaErrors.length > 0" class="mt-1 space-y-1">
        <p v-for="error in cedulaErrors" :key="error" class="text-sm text-red-600">
          {{ error }}
        </p>
      </div>
      <div v-if="cedulaWarnings.length > 0" class="mt-1 space-y-1">
        <p v-for="warning in cedulaWarnings" :key="warning" class="text-sm text-yellow-600">
          {{ warning }}
        </p>
      </div>
    </div>

    <!-- Nombre del Paciente -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Nombre del Paciente *
      </label>
      <input
        type="text"
        v-model="formData.nombrePaciente"
        @input="handleNombreInput"
        @blur="validateNombre"
        placeholder="Ingrese el nombre completo del paciente"
        :class="getNombreFieldClasses()"
        required
        ref="nombreInput"
        maxlength="100"
      />
      <div v-if="nombreErrors.length > 0" class="mt-1 space-y-1">
        <p v-for="error in nombreErrors" :key="error" class="text-sm text-red-600">
          {{ error }}
        </p>
      </div>
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
        @input="handleEdadInput"
        @blur="validateEdad"
        placeholder="Ingrese la edad"
        :class="getEdadFieldClasses()"
        required
        ref="edadInput"
        min="0"
        max="150"
      />
      <div v-if="edadErrors.length > 0" class="mt-1 space-y-1">
        <p v-for="error in edadErrors" :key="error" class="text-sm text-red-600">
          {{ error }}
        </p>
      </div>
      <div v-if="edadWarnings.length > 0" class="mt-1 space-y-1">
        <p v-for="warning in edadWarnings" :key="warning" class="text-sm text-yellow-600">
          {{ warning }}
        </p>
      </div>
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
          :disabled="isLoading || isValidatingCedula"
        />
        <button
          @click="handleGuardarClick"
          type="button"
          class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          :disabled="isLoading || isValidatingCedula"
        >
          <svg
            v-if="isLoading || isValidatingCedula"
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
          {{ isLoading ? 'Guardando...' : isValidatingCedula ? 'Validando...' : 'Guardar Paciente' }}
        </button>
      </div>
      
      <!-- Alerta de Validación -->
      <BotonGuardar
        ref="botonGuardarRef"
        :campos="formData"
        :campos-obligatorios="['numeroCedula','nombrePaciente','sexo','edad','entidad','tipoAtencion']"
        :etiquetas="{
          numeroCedula: 'Cédula',
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
                <p class="text-lg font-semibold text-green-900">{{ pacienteGuardado.nombrePaciente }}</p>
                <p class="text-base text-green-800">Cédula: <span class="font-mono font-bold">{{ pacienteGuardado.numeroCedula }}</span></p>
              </div>
              <button 
                @click="copiarCedula"
                class="mt-2 inline-flex items-center px-3 py-1.5 border border-green-300 rounded-md text-xs font-medium text-green-700 bg-white hover:bg-green-50 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-1 transition-colors"
              >
                <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                Copiar Cédula
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script setup lang="ts">
import { reactive, computed, ref, watch } from 'vue'
import 'flatpickr/dist/flatpickr.css'
import ListaDesplegable from '../../ComponentesFormularios/ListaDesplegable.vue'
import BotonGuardar from '../../ComponentesFormularios/BotonGuardar.vue'
import BotonLimpiar from '../../ComponentesFormularios/BotonLimpiar.vue'
import { crearPaciente, buscarPacientePorCedula } from '@/api/pacientes'

// Estados para el componente
const isLoading = ref(false)
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const hasAttemptedSubmit = ref(false)
const showNotification = ref(false)
const progressWidth = ref(100)
const botonGuardarRef = ref<{ validarExternamente: () => boolean } | null>(null)
const showValidationError = ref(false)

// Variable para almacenar los datos del paciente guardado
const pacienteGuardado = ref({
  numeroCedula: '',
  nombrePaciente: '',
  sexo: '',
  edad: '',
  entidad: '',
  tipoAtencion: '',
  observaciones: ''
})

// Estados para validación
const cedulaErrors = ref<string[]>([])
const cedulaWarnings = ref<string[]>([])
const nombreErrors = ref<string[]>([])
const edadErrors = ref<string[]>([])
const edadWarnings = ref<string[]>([])
const isValidatingCedula = ref(false)

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

// Funciones de validación y formateo

// Validación de cédula
const validateCedula = async () => {
  const cedula = formData.numeroCedula.trim()
  cedulaErrors.value = []
  cedulaWarnings.value = []
  
  if (!cedula) {
    if (hasAttemptedSubmit.value) {
      cedulaErrors.value.push('La cédula es obligatoria')
    }
    return
  }
  
  // Validar solo números
  if (!/^\d+$/.test(cedula)) {
    cedulaErrors.value.push('La cédula debe contener solo números')
    return
  }
  
  // Validar longitud mínima
  if (cedula.length < 7) {
    cedulaErrors.value.push('La cédula debe tener al menos 7 dígitos')
    return
  }
  
  // Validar longitud máxima
  if (cedula.length > 10) {
    cedulaErrors.value.push('La cédula no puede tener más de 10 dígitos')
    return
  }
  
  // Advertencias
  if (cedula.length < 8) {
    cedulaWarnings.value.push('La mayoría de cédulas tienen 8 dígitos o más')
  }
  
  // Validar si la cédula ya existe (solo en blur)
  if (cedula.length >= 7 && hasAttemptedSubmit.value) {
    try {
      isValidatingCedula.value = true
      const pacienteExistente = await buscarPacientePorCedula(cedula)
      if (pacienteExistente) {
        cedulaErrors.value.push(`Ya existe un paciente con la cédula ${cedula}: ${pacienteExistente.nombrePaciente}`)
      }
    } catch (error) {
      console.error('Error al validar cédula:', error)
    } finally {
      isValidatingCedula.value = false
    }
  }
}

// Manejo de entrada de cédula
const handleCedulaInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  const value = target.value
  
  // Solo permitir números
  const numericValue = value.replace(/\D/g, '')
  formData.numeroCedula = numericValue
  
  // Validar en tiempo real
  if (numericValue.length > 0) {
    validateCedula()
  } else {
    cedulaErrors.value = []
    cedulaWarnings.value = []
  }
}

// Validación de nombre
const validateNombre = () => {
  const nombre = formData.nombrePaciente.trim()
  nombreErrors.value = []
  
  if (!nombre) {
    if (hasAttemptedSubmit.value) {
      nombreErrors.value.push('El nombre del paciente es obligatorio')
    }
    return
  }
  
  // Validar longitud mínima
  if (nombre.length < 2) {
    nombreErrors.value.push('El nombre debe tener al menos 2 caracteres')
    return
  }
  
  // Validar que contenga al menos dos palabras
  const palabras = nombre.split(/\s+/).filter(p => p.length > 0)
  if (palabras.length < 2) {
    nombreErrors.value.push('Ingrese el nombre completo (nombre y apellido)')
    return
  }
  
  // Validar caracteres válidos (letras, espacios, acentos, guiones)
  if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-']+$/.test(nombre)) {
    nombreErrors.value.push('El nombre solo puede contener letras, espacios, guiones y apostrofes')
    return
  }
}

// Manejo de entrada de nombre
const handleNombreInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  let value = target.value
  
  // Capitalizar primera letra de cada palabra
  value = value.replace(/\b\w/g, (char) => char.toUpperCase())
  formData.nombrePaciente = value
  
  // Validar en tiempo real
  if (value.length > 0) {
    validateNombre()
  } else {
    nombreErrors.value = []
  }
}

// Validación de edad
const validateEdad = () => {
  const edad = parseInt(formData.edad)
  edadErrors.value = []
  edadWarnings.value = []
  
  if (!formData.edad || isNaN(edad)) {
    if (hasAttemptedSubmit.value) {
      edadErrors.value.push('La edad es obligatoria')
    }
    return
  }
  
  if (edad < 0) {
    edadErrors.value.push('La edad no puede ser negativa')
    return
  }
  
  if (edad > 150) {
    edadErrors.value.push('La edad no puede ser mayor a 150 años')
    return
  }
  
  // Advertencias
  if (edad > 120) {
    edadWarnings.value.push('Edad muy alta, verifique que sea correcta')
  } else if (edad === 0) {
    edadWarnings.value.push('¿Es un recién nacido? Considere usar meses si es menor a 1 año')
  }
}

// Manejo de entrada de edad
const handleEdadInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  const value = target.value
  
  // Solo permitir números
  const numericValue = value.replace(/\D/g, '')
  formData.edad = numericValue
  
  // Validar en tiempo real
  if (numericValue.length > 0) {
    validateEdad()
  } else {
    edadErrors.value = []
    edadWarnings.value = []
  }
}

// Funciones para clases CSS
const getCedulaFieldClasses = () => {
  const baseClasses = "h-11 w-full rounded-lg border bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  
  if (cedulaErrors.value.length > 0) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  
  if (cedulaWarnings.value.length > 0) {
    return `${baseClasses} border-yellow-500 focus:border-yellow-500 focus:ring-yellow-500/10 bg-yellow-50`
  }
  
  if (formData.numeroCedula && cedulaErrors.value.length === 0) {
    return `${baseClasses} border-green-500 focus:border-green-500 focus:ring-green-500/10 bg-green-50`
  }
  
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10 bg-white`
}

const getNombreFieldClasses = () => {
  const baseClasses = "h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  
  if (nombreErrors.value.length > 0) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  
  if (formData.nombrePaciente && nombreErrors.value.length === 0) {
    return `${baseClasses} border-green-500 focus:border-green-500 focus:ring-green-500/10 bg-green-50`
  }
  
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10`
}

const getEdadFieldClasses = () => {
  const baseClasses = "h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  
  if (edadErrors.value.length > 0) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  
  if (edadWarnings.value.length > 0) {
    return `${baseClasses} border-yellow-500 focus:border-yellow-500 focus:ring-yellow-500/10 bg-yellow-50`
  }
  
  if (formData.edad && edadErrors.value.length === 0) {
    return `${baseClasses} border-green-500 focus:border-green-500 focus:ring-green-500/10 bg-green-50`
  }
  
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10`
}

// Función para guardar el paciente
const guardarPaciente = async () => {
  isLoading.value = true
  statusMessage.value = ''
  
  // Guardar los datos del paciente antes de limpiar el formulario (para mostrarlos en el mensaje de éxito)
  pacienteGuardado.value = {
    numeroCedula: formData.numeroCedula,
    nombrePaciente: formData.nombrePaciente,
    sexo: formData.sexo,
    edad: formData.edad,
    entidad: formData.entidad,
    tipoAtencion: formData.tipoAtencion,
    observaciones: formData.observaciones
  }
  
  try {
    // Transformar los datos al formato esperado por el backend
    const pacientePayload = {
      numeroCedula: formData.numeroCedula,
      nombrePaciente: formData.nombrePaciente,
      sexo: formData.sexo,
      edad: Number(formData.edad),
      entidad: formData.entidad,
      tipoAtencion: formData.tipoAtencion,
      observaciones: formData.observaciones || undefined
    }
    
    // Debug: Ver qué datos se están enviando
    console.log('Payload enviado:', pacientePayload)
    
    // Llamada a la API para guardar el paciente
    await crearPaciente(pacientePayload)
    
    // Mostrar mensaje de éxito
    statusType.value = 'success'
    statusMessage.value = 'Paciente guardado exitosamente'
    
    // Emitir evento con los datos del paciente guardado
    emit('patient-saved', pacienteGuardado.value)
    
    // Limpiar el formulario automáticamente después de guardar exitosamente
    setTimeout(() => {
      limpiarSoloFormulario()
    }, 100) // Pequeño delay para que el mensaje se muestre antes de limpiar
    
    // Auto-ocultar el mensaje de éxito después de 10 segundos
    setTimeout(() => {
      statusMessage.value = ''
    }, 10000)
    
  } catch (error: any) {
    statusType.value = 'error'
    
    // Manejar errores específicos
    if (error.response?.status === 409) {
      statusMessage.value = `Ya existe un paciente registrado con la cédula ${formData.numeroCedula}`
      cedulaErrors.value = [`Ya existe un paciente con la cédula ${formData.numeroCedula}`]
      if (cedulaInput.value) {
        cedulaInput.value.focus()
      }
    } else if (error.response?.data?.detail) {
      statusMessage.value = `Error: ${error.response.data.detail}`
    } else {
      statusMessage.value = 'Error al guardar el paciente. Intente nuevamente.'
    }
    
    console.error('Error completo:', error)
    if (error.response && error.response.data) {
      console.error('Detalles del error:', error.response.data)
    }
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
  
  // Limpiar estados de validación
  cedulaErrors.value = []
  cedulaWarnings.value = []
  nombreErrors.value = []
  edadErrors.value = []
  edadWarnings.value = []
  
  statusMessage.value = ''
  hasAttemptedSubmit.value = false
  showValidationError.value = false
}

// Función para limpiar solo los datos del formulario (sin afectar mensajes de estado)
const limpiarSoloFormulario = () => {
  formData.numeroCedula = ''
  formData.nombrePaciente = ''
  formData.sexo = ''
  formData.edad = ''
  formData.entidad = ''
  formData.tipoAtencion = ''
  formData.observaciones = ''
  
  // Limpiar estados de validación
  cedulaErrors.value = []
  cedulaWarnings.value = []
  nombreErrors.value = []
  edadErrors.value = []
  edadWarnings.value = []
  
  hasAttemptedSubmit.value = false
  showValidationError.value = false
  // NO limpiar statusMessage para mantener el cartel de éxito visible
}

// Función para manejar errores de validación
const handleValidationError = (camposInvalidos: string[]) => {
  hasAttemptedSubmit.value = true
  console.log('Campos inválidos:', camposInvalidos)
}

// Función para manejar el click del botón guardar
const handleGuardarClick = async () => {
  hasAttemptedSubmit.value = true
  
  // Ejecutar todas las validaciones
  await validateCedula()
  validateNombre()
  validateEdad()
  
  // Verificar si hay errores de validación personalizados
  const hasCustomErrors = cedulaErrors.value.length > 0 || 
                         nombreErrors.value.length > 0 || 
                         edadErrors.value.length > 0
  
  // Trigger validation using the BotonGuardar component
  let isValidBotonGuardar = true
  if (botonGuardarRef.value) {
    isValidBotonGuardar = botonGuardarRef.value.validarExternamente()
  }
  
  if (isValidBotonGuardar && !hasCustomErrors) {
    guardarPaciente()
    showValidationError.value = false
  } else {
    showValidationError.value = true
    
    // Hacer scroll al primer campo con error
    if (cedulaErrors.value.length > 0 && cedulaInput.value) {
      cedulaInput.value.focus()
    } else if (nombreErrors.value.length > 0 && nombreInput.value) {
      nombreInput.value.focus()
    } else if (edadErrors.value.length > 0 && edadInput.value) {
      edadInput.value.focus()
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
    const hasCustomErrors = cedulaErrors.value.length > 0 || 
                           nombreErrors.value.length > 0 || 
                           edadErrors.value.length > 0
    if (isValid && !hasCustomErrors) {
      showValidationError.value = false
    }
  }
}, { deep: true })

// Watch individual para campos específicos
watch(() => formData.numeroCedula, () => {
  if (formData.numeroCedula) {
    validateCedula()
  }
})

watch(() => formData.nombrePaciente, () => {
  if (formData.nombrePaciente) {
    validateNombre()
  }
})

watch(() => formData.edad, () => {
  if (formData.edad) {
    validateEdad()
  }
})

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

// Función para copiar la Cédula del paciente guardado
const copiarCedula = async () => {
  if (pacienteGuardado.value.numeroCedula) {
    try {
      await navigator.clipboard.writeText(pacienteGuardado.value.numeroCedula)
      // Opcional: mostrar feedback visual de que se copió
      console.log('Cédula copiada al portapapeles')
    } catch (err) {
      console.error('Error al copiar la cédula:', err)
    }
  }
}

// Función para copiar la Cédula del paciente (función legacy, mantener por compatibilidad)
const copiarDNI = async () => {
  if (formData.numeroCedula) {
    try {
      await navigator.clipboard.writeText(formData.numeroCedula)
      // Opcional: mostrar feedback visual de que se copió
      console.log('Cédula copiada al portapapeles')
    } catch (err) {
      console.error('Error al copiar la cédula:', err)
    }
  }
}
</script>