<template>
  <div class="space-y-6">
    <!-- ID de Muestra (Solo lectura) -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        ID de Muestra
      </label>
      <input
        type="text"
        v-model="formData.idMuestra"
        class="h-11 w-full rounded-lg border border-gray-300 bg-gray-100 px-4 py-2.5 text-sm text-gray-500 shadow-theme-xs cursor-not-allowed"
        readonly
      />
    </div>

    <!-- Información del Paciente (Solo lectura) -->
    <div class="bg-gray-50 rounded-lg p-4 border border-gray-200">
      <h3 class="text-sm font-semibold text-gray-700 mb-3">Información del Paciente</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="mb-1.5 block text-sm font-medium text-gray-600">
            Nombre Completo
          </label>
          <input
            type="text"
            v-model="formData.paciente.nombre"
            class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
            readonly
          />
        </div>
        <div>
          <label class="mb-1.5 block text-sm font-medium text-gray-600">
            Cédula
          </label>
          <input
            type="text"
            v-model="formData.paciente.cedula"
            class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
            readonly
          />
        </div>
      </div>
    </div>

    <!-- Información de la Muestra (Solo lectura) -->
    <div class="bg-gray-50 rounded-lg p-4 border border-gray-200">
      <h3 class="text-sm font-semibold text-gray-700 mb-3">Información de la Muestra</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="mb-1.5 block text-sm font-medium text-gray-600">Tipo de Análisis</label>
          <input
            type="text"
            v-model="formData.tipoAnalisisTexto"
            class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
            readonly
          />
        </div>
        <div>
          <label class="mb-1.5 block text-sm font-medium text-gray-600">Estado</label>
          <input
            type="text"
            v-model="formData.estadoTexto"
            class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
            readonly
          />
        </div>
        <div>
          <label class="mb-1.5 block text-sm font-medium text-gray-600">Médico Solicitante</label>
          <input
            type="text"
            v-model="formData.medicoSolicitanteTexto"
            class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
            readonly
          />
        </div>
        <div>
          <label class="mb-1.5 block text-sm font-medium text-gray-600">Fecha de Ingreso</label>
          <input
            type="text"
            v-model="formData.fechaIngresoTexto"
            class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
            readonly
          />
        </div>
      </div>
    </div>

    <!-- Resultados de Análisis -->
    <div class="bg-blue-50 rounded-lg p-4 border border-blue-200">
      <h3 class="text-sm font-semibold text-blue-700 mb-4">Resultados de Análisis</h3>
      
      <!-- Prueba 1 -->
      <div class="mb-4">
        <div class="flex items-center justify-between mb-2">
          <label class="text-sm font-medium text-gray-700">Prueba 1</label>
          <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            Código: {{ formData.codigoPrueba1 }}
          </span>
        </div>
        <textarea
          v-model="formData.resultadoPrueba1"
          placeholder="Ingrese los resultados de la prueba 1"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
        ></textarea>
      </div>

      <!-- Prueba 2 -->
      <div class="mb-4">
        <div class="flex items-center justify-between mb-2">
          <label class="text-sm font-medium text-gray-700">Prueba 2</label>
          <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            Código: {{ formData.codigoPrueba2 }}
          </span>
        </div>
        <textarea
          v-model="formData.resultadoPrueba2"
          placeholder="Ingrese los resultados de la prueba 2"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
        ></textarea>
      </div>

      <!-- Prueba 3 -->
      <div class="mb-4">
        <div class="flex items-center justify-between mb-2">
          <label class="text-sm font-medium text-gray-700">Prueba 3</label>
          <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            Código: {{ formData.codigoPrueba3 }}
          </span>
        </div>
        <textarea
          v-model="formData.resultadoPrueba3"
          placeholder="Ingrese los resultados de la prueba 3"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
        ></textarea>
      </div>

      <!-- Diagnóstico Final -->
      <div>
        <label class="mb-2 block text-sm font-medium text-gray-700">
          Diagnóstico Final *
        </label>
        <textarea
          v-model="formData.diagnosticoFinal"
          placeholder="Ingrese el diagnóstico final basado en los resultados de las pruebas"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
          required
        ></textarea>
      </div>
    </div>

    <!-- Botones de Acción -->
    <div class="flex items-center justify-end space-x-3 pt-6">
      <button
        @click="cancelar"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 focus:border-gray-400 transition-colors"
        :disabled="isLoading"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
        Cancelar
      </button>

      <button
        @click="previsualizar"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-brand-300 rounded-lg text-sm font-medium text-brand-600 bg-brand-50 hover:bg-brand-100 focus:outline-none focus:ring-3 focus:ring-brand-300/30 focus:border-brand-400 transition-colors"
        :disabled="isLoading || !diagnosticoFinalCompleto"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
        </svg>
        Previsualizar
      </button>

      <button
        @click="guardarInforme"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        :disabled="isLoading || !diagnosticoFinalCompleto"
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
        {{ isLoading ? 'Guardando...' : 'Guardar Informe' }}
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
            <h3 class="text-2xl font-bold text-gray-900 mb-2">¡Informe Guardado!</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              El informe para la muestra
            </p>
            <p class="text-lg font-semibold text-brand-600 mb-4">
              {{ formData.idMuestra }}
            </p>
            <p class="text-gray-600 mb-6">
              se ha guardado correctamente en el sistema.
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
import { reactive, computed, ref, onMounted } from 'vue'

// Estados para el componente
const isLoading = ref(false)
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const showNotification = ref(false)
const progressWidth = ref(100)

// Props para recibir el ID de la muestra a editar
const props = defineProps({
  muestraId: {
    type: String,
    required: true
  }
})

const formData = reactive({
  // Datos de solo lectura
  idMuestra: '',
  paciente: {
    nombre: '',
    cedula: ''
  },
  tipoAnalisisTexto: '',
  estadoTexto: '',
  medicoSolicitanteTexto: '',
  fechaIngresoTexto: '',
  
  // Códigos de prueba
  codigoPrueba1: '',
  codigoPrueba2: '',
  codigoPrueba3: '',
  
  // Campos editables para los análisis
  resultadoPrueba1: '',
  resultadoPrueba2: '',
  resultadoPrueba3: '',
  diagnosticoFinal: ''
})

// Validación: al menos el diagnóstico final debe estar completo
const diagnosticoFinalCompleto = computed(() => {
  return formData.diagnosticoFinal.trim().length > 0
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

// Función para cargar los datos de la muestra
const cargarMuestra = async () => {
  if (!props.muestraId) return

  isLoading.value = true

  try {
    
    // Datos simulados de la muestra
    const muestraData = {
      idMuestra: props.muestraId,
      paciente: {
        nombre: 'Juan Pérez García',
        cedula: '12345678'
      },
      tipoAnalisisTexto: 'Hemograma Completo',
      estadoTexto: 'En Proceso',
      medicoSolicitanteTexto: 'Dr. García Pérez',
      fechaIngresoTexto: '15/01/2024 10:30',
      
      // Códigos de prueba generados automáticamente
      codigoPrueba1: 'LAB-HEM-001',
      codigoPrueba2: 'LAB-HEM-002', 
      codigoPrueba3: 'LAB-HEM-003',
      
      // Resultados vacíos para editar
      resultadoPrueba1: '',
      resultadoPrueba2: '',
      resultadoPrueba3: '',
      diagnosticoFinal: ''
    }
    
    // Asignar datos al formulario
    Object.assign(formData, muestraData)
    
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al cargar los datos de la muestra'
    console.error('Error:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para guardar el informe
const guardarInforme = async () => {
  if (!diagnosticoFinalCompleto.value) {
    statusType.value = 'error'
    statusMessage.value = 'Por favor complete el diagnóstico final'
    return
  }

  isLoading.value = true
  statusMessage.value = ''

  try {
    // Simular llamada a API
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    statusType.value = 'success'
    statusMessage.value = 'Informe guardado exitosamente'
    
    // Mostrar notificación emergente mejorada
    showNotification.value = true
    progressWidth.value = 100
    
    // Crear barra de progreso para auto-cierre
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
    
    // Emitir evento de éxito
    emit('informe-guardado', {
      muestraId: formData.idMuestra,
      resultados: {
        prueba1: formData.resultadoPrueba1,
        prueba2: formData.resultadoPrueba2,
        prueba3: formData.resultadoPrueba3,
        diagnosticoFinal: formData.diagnosticoFinal
      }
    })
    
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al guardar el informe. Intente nuevamente.'
    console.error('Error:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para previsualizar
const previsualizar = () => {
  emit('previsualizar-informe', {
    muestraId: formData.idMuestra,
    paciente: formData.paciente,
    tipoAnalisis: formData.tipoAnalisisTexto,
    medicoSolicitante: formData.medicoSolicitanteTexto,
    fechaIngreso: formData.fechaIngresoTexto,
    resultados: {
      prueba1: {
        codigo: formData.codigoPrueba1,
        resultado: formData.resultadoPrueba1
      },
      prueba2: {
        codigo: formData.codigoPrueba2,
        resultado: formData.resultadoPrueba2
      },
      prueba3: {
        codigo: formData.codigoPrueba3,
        resultado: formData.resultadoPrueba3
      }
    },
    diagnosticoFinal: formData.diagnosticoFinal
  })
}

// Función para cancelar
const cancelar = () => {
  emit('cancelar')
}

// Emits
const emit = defineEmits(['informe-guardado', 'previsualizar-informe', 'cancelar'])

// Cargar datos al montar el componente
onMounted(() => {
  cargarMuestra()
})
</script>