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

    <!-- Nombre del Patólogo -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Nombre del Patólogo *
      </label>
      <input
        type="text"
        v-model="formData.nombreCompleto"
        placeholder="Ingrese el nombre completo del patólogo"
        :class="getFieldClasses('nombreCompleto', true)"
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
        :class="getFieldClasses('email', true)"
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
        :class="getFieldClasses('especialidad', true)"
        required
        ref="especialidadInput"
      />
      <!-- Podría ser un select si hay especialidades predefinidas -->
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
        :class="getFieldClasses('registroMedico', true)"
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
        @file-added="handleFirmaFile"
        id="firmaDropzonePatologo" 
      />
      <div v-if="firmaPatologoFile" class="mt-2 text-sm text-gray-600">
        Archivo seleccionado: {{ firmaPatologoFile.name }}
      </div>
      <!-- Aquí podrías añadir una validación si la firma es requerida -->
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
        class="inline-flex items-center px-4 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 focus:border-gray-400 transition-colors"
        :disabled="isLoading"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Limpiar
      </button>

      <button
        @click="guardarPatologo"
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
        {{ isLoading ? 'Guardando...' : 'Guardar Patólogo' }}
      </button>
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
              <p class="text-sm font-medium text-green-800 mb-2">Datos del Patólogo Registrado:</p>
              <div class="space-y-1">
                <p class="text-lg font-semibold text-green-900">{{ formData.nombreCompleto }}</p>
                <p class="text-base text-green-800">Número de Cédula: <span class="font-mono font-bold">{{ formData.numeroCedula }}</span></p>
                <p class="text-base text-green-800">Especialidad: <span class="font-semibold">{{ formData.especialidad }}</span></p>
                <p class="text-base text-green-800">Reg. Médico: <span class="font-mono font-bold">{{ formData.registroMedico }}</span></p>
              </div>
              <button 
                @click="copiarCedula"
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
            <h3 class="text-2xl font-bold text-gray-900 mb-2">¡Patólogo Registrado!</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              El patólogo <strong class="text-brand-600">{{ formData.nombreCompleto }}</strong>
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
import Dropzone from '@/components/Muestras/NuevaMuestra/Dropzone.vue' // Import Dropzone correcto
// No se necesita flatpickr para este formulario
// import 'flatpickr/dist/flatpickr.css' 

// Estados para el componente
const isLoading = ref(false)
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const hasAttemptedSubmit = ref(false)
const showNotification = ref(false)
const progressWidth = ref(100)
// showEntidades ya no es necesario
const firmaPatologoFile = ref<File | null>(null)

const formData = reactive({
  numeroCedula: '',
  nombreCompleto: '',
  sexo: '',
  email: '',
  telefono: '',
  especialidad: '',
  registroMedico: '',
  observaciones: '',
  firmaPatologoUrl: '', // Campo para la URL de la firma o referencia
})

// Referencias a los inputs
const cedulaInput = ref<HTMLInputElement | null>(null)
const nombreInput = ref<HTMLInputElement | null>(null)
const emailInput = ref<HTMLInputElement | null>(null)
const telefonoInput = ref<HTMLInputElement | null>(null)
const especialidadInput = ref<HTMLInputElement | null>(null)
const registroMedicoInput = ref<HTMLInputElement | null>(null)
// edadInput y entidadInput ya no son necesarios

// Lista de entidades ya no es necesaria

// Validación del formulario
const isFormValid = computed(() => {
  return !!(
    formData.numeroCedula.trim() &&
    formData.nombreCompleto.trim() &&
    formData.sexo &&
    formData.email.trim() && // Validar que el email no esté vacío
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim()) && // Validación básica de formato de email
    formData.especialidad.trim() &&
    formData.registroMedico.trim()
  )
})

// Clases para el mensaje de estado
const statusMessageClasses = computed(() => {
  return statusType.value === 'success'
    ? 'rounded-lg bg-green-50 border border-green-200 p-4'
    : 'rounded-lg bg-red-50 border border-red-200 p-4'
})

const statusIconClass = computed(() => {
  return statusType.value === 'success' ? 'text-green-600' : 'text-red-600'
})

// Función para guardar el patólogo
const guardarPatologo = async () => {
  hasAttemptedSubmit.value = true
  
  if (!formData.email.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email.trim())) {
    statusType.value = 'error'
    statusMessage.value = 'Por favor ingrese un email válido.'
    emailInput.value?.focus()
    return
  }

  if (!isFormValid.value) {
    statusType.value = 'error'
    statusMessage.value = 'Por favor complete todos los campos requeridos (*)'
    // Enfocar el primer campo inválido podría ser una mejora aquí
    if (!formData.numeroCedula.trim()) cedulaInput.value?.focus()
    else if (!formData.nombreCompleto.trim()) nombreInput.value?.focus()
    else if (!formData.sexo) { /* No hay input directo para enfocar para radio buttons */ }
    else if (!formData.email.trim()) emailInput.value?.focus()
    else if (!formData.especialidad.trim()) especialidadInput.value?.focus()
    else if (!formData.registroMedico.trim()) registroMedicoInput.value?.focus()
    return
  }

  isLoading.value = true
  statusMessage.value = ''

  try {
    // Aquí iría la lógica para enviar los datos a un backend
    // await api.registrarPatologo(formData)
    const dataToSave = { ...formData }
    if (firmaPatologoFile.value) {
      // Lógica para manejar el archivo de la firma, por ejemplo, subirlo y obtener una URL
      // Por ahora, solo lo incluimos en el log o lo guardamos como nombre de archivo
      console.log('Archivo de firma seleccionado:', firmaPatologoFile.value.name)
      // dataToSave.firmaPatologoUrl = await uploadFileAndGetURL(firmaPatologoFile.value); // Ejemplo
    }
    console.log('Datos del patólogo a guardar:', dataToSave)
    
    // Simulación de guardado exitoso
    await new Promise(resolve => setTimeout(resolve, 1000));

    statusType.value = 'success'
    statusMessage.value = 'Patólogo guardado exitosamente'
    
    // Mostrar notificación emergente
    showNotification.value = true
    progressWidth.value = 100
    
    const duration = 5000 // 5 segundos
    const interval = 50 // Update every 50ms
    const decrement = (interval / duration) * 100
    
    const progressInterval = setInterval(() => {
      progressWidth.value -= decrement
      if (progressWidth.value <= 0) {
        clearInterval(progressInterval)
        showNotification.value = false
        progressWidth.value = 100 // Reset for next time
      }
    }, interval)
    
    // Emitir evento de éxito
    emit('patologo-saved', { ...formData })
    // limpiarFormulario() // Opcional: limpiar el formulario después de guardar
    
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al guardar el patólogo. Intente nuevamente.'
    console.error('Error al guardar patólogo:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para limpiar el formulario
const limpiarFormulario = () => {
  formData.numeroCedula = ''
  formData.nombreCompleto = ''
  formData.sexo = ''
  formData.email = ''
  formData.telefono = ''
  formData.especialidad = ''
  formData.registroMedico = ''
  formData.observaciones = ''
  formData.firmaPatologoUrl = '' // Limpiar campo de firma
  firmaPatologoFile.value = null // Limpiar el archivo de firma
  
  statusMessage.value = ''
  hasAttemptedSubmit.value = false
  cedulaInput.value?.focus() // Enfocar el primer campo al limpiar
}

// Emitir los datos del formulario para poder usarlos en el componente padre
const emit = defineEmits(['update-patologo-data', 'patologo-saved'])

// Watch para emitir cambios
watch(formData, (newData) => {
  emit('update-patologo-data', newData)
}, { deep: true, immediate: true })

// Función para obtener clases CSS condicionales para campos requeridos
const getFieldClasses = (fieldName: keyof typeof formData, isRequired = false) => {
  const baseClasses = "h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  
  let fieldIsInvalid = false;
  if (fieldName === 'email') {
    fieldIsInvalid = isRequired && hasAttemptedSubmit.value && (!formData[fieldName].trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData[fieldName].trim()));
  } else {
    fieldIsInvalid = isRequired && hasAttemptedSubmit.value && !formData[fieldName];
  }

  if (fieldIsInvalid) {
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

// Función para copiar el Número de Cédula del patólogo
const copiarCedula = async () => {
  if (formData.numeroCedula) {
    try {
      await navigator.clipboard.writeText(formData.numeroCedula)
      // Opcional: mostrar feedback visual de que se copió
      console.log('Número de Cédula copiado al portapapeles')
      // Podrías añadir una pequeña notificación temporal aquí
      // Ejemplo: showToast('¡Número de Cédula copiado!')
    } catch (err) {
      console.error('Error al copiar el Número de Cédula:', err)
    }
  }
}

// Manejar el archivo de la firma desde el evento del Dropzone
const handleFirmaFile = (file: File) => {
  firmaPatologoFile.value = file
  // Opcionalmente, podrías mostrar una vista previa o el nombre del archivo
  console.log('Firma recibida:', file.name)
}

// Lógica de entidades filtradas, seleccionarEntidad y ocultarEntidades ya no son necesarias
</script>