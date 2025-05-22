<!-- 
  Este componente permite modificar los datos de una muestra existente.
  Muestra información del paciente en modo solo lectura (ID muestra, nombre y cédula)
  y permite editar campos como el tipo de análisis y otros datos relevantes de la muestra.
  Se utiliza para actualizar la información de muestras ya registradas en el sistema.
-->

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

    <!-- Tipo de Análisis -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Tipo de Análisis *
      </label>
      <div class="relative z-20 bg-transparent">
        <select
          v-model="formData.tipoAnalisis"
          class="h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
          :class="{ 'text-gray-800': formData.tipoAnalisis }"
          required
        >
          <option value="" disabled>Seleccione el tipo de análisis</option>
          <option value="hemograma-completo">Hemograma Completo</option>
          <option value="quimica-sanguinea">Química Sanguínea</option>
          <option value="uroanalisis">Uroanálisis</option>
          <option value="coprologia">Coprología</option>
          <option value="parasitologia">Parasitología</option>
          <option value="microbiologia">Microbiología</option>
          <option value="inmunologia">Inmunología</option>
          <option value="hormonal">Perfil Hormonal</option>
          <option value="otro">Otro</option>
        </select>
        <span
          class="absolute z-30 text-gray-500 -translate-y-1/2 pointer-events-none right-4 top-1/2"
        >
          <svg
            class="stroke-current"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4.79175 7.396L10.0001 12.6043L15.2084 7.396"
              stroke=""
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </span>
      </div>
    </div>

    <!-- Estado de la Muestra -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Estado de la Muestra *
      </label>
      <div class="relative z-20 bg-transparent">
        <select
          v-model="formData.estado"
          class="h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
          :class="{ 'text-gray-800': formData.estado }"
          required
        >
          <option value="" disabled>Seleccione el estado</option>
          <option value="recibida">Recibida</option>
          <option value="en-proceso">En Proceso</option>
          <option value="analizada">Analizada</option>
          <option value="terminada">Terminada</option>
          <option value="entregada">Entregada</option>
          <option value="rechazada">Rechazada</option>
        </select>
        <span
          class="absolute z-30 text-gray-500 -translate-y-1/2 pointer-events-none right-4 top-1/2"
        >
          <svg
            class="stroke-current"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4.79175 7.396L10.0001 12.6043L15.2084 7.396"
              stroke=""
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </span>
      </div>
    </div>

    <!-- Médico Solicitante -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Médico Solicitante *
      </label>
      <div class="relative z-20 bg-transparent">
        <select
          v-model="formData.medicoSolicitante"
          class="h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
          :class="{ 'text-gray-800': formData.medicoSolicitante }"
          required
        >
          <option value="" disabled>Seleccione el médico</option>
          <option value="dr-garcia">Dr. García Pérez</option>
          <option value="dra-martinez">Dra. Martínez López</option>
          <option value="dr-rodriguez">Dr. Rodríguez Silva</option>
          <option value="dra-torres">Dra. Torres Ruiz</option>
          <option value="dr-fernandez">Dr. Fernández Díaz</option>
          <option value="otro">Otro médico</option>
        </select>
        <span
          class="absolute z-30 text-gray-500 -translate-y-1/2 pointer-events-none right-4 top-1/2"
        >
          <svg
            class="stroke-current"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4.79175 7.396L10.0001 12.6043L15.2084 7.396"
              stroke=""
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </span>
      </div>
    </div>

    <!-- Fecha de Ingreso -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Fecha y Hora de Ingreso *
      </label>
      <div class="relative">
        <flat-pickr
          v-model="formData.fechaIngreso"
          :config="fechaIngresoConfig"
          class="h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pl-4 pr-11 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
          placeholder="Fecha y hora de ingreso"
        />
        <span
          class="absolute text-gray-500 -translate-y-1/2 pointer-events-none right-3 top-1/2"
        >
          <svg
            class="fill-current"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M3.04175 9.99984C3.04175 6.15686 6.1571 3.0415 10.0001 3.0415C13.8431 3.0415 16.9584 6.15686 16.9584 9.99984C16.9584 13.8428 13.8431 16.9582 10.0001 16.9582C6.1571 16.9582 3.04175 13.8428 3.04175 9.99984ZM10.0001 1.5415C5.32867 1.5415 1.54175 5.32843 1.54175 9.99984C1.54175 14.6712 5.32867 18.4582 10.0001 18.4582C14.6715 18.4582 18.4584 14.6712 18.4584 9.99984C18.4584 5.32843 14.6715 1.5415 10.0001 1.5415ZM9.99998 10.7498C9.58577 10.7498 9.24998 10.4141 9.24998 9.99984V5.4165C9.24998 5.00229 9.58577 4.6665 9.99998 4.6665C10.4142 4.6665 10.75 5.00229 10.75 5.4165V9.24984H13.3334C13.7476 9.24984 14.0834 9.58562 14.0834 9.99984C14.0834 10.4141 13.7476 10.7498 13.3334 10.7498H10.0001H9.99998Z"
              fill=""
            />
          </svg>
        </span>
      </div>
    </div>

    <!-- Prioridad -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Prioridad
      </label>
      <div class="relative z-20 bg-transparent">
        <select
          v-model="formData.prioridad"
          class="h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
          :class="{ 'text-gray-800': formData.prioridad }"
        >
          <option value="" disabled>Seleccione la prioridad</option>
          <option value="baja">Baja</option>
          <option value="normal">Normal</option>
          <option value="alta">Alta</option>
          <option value="urgente">Urgente</option>
        </select>
        <span
          class="absolute z-30 text-gray-500 -translate-y-1/2 pointer-events-none right-4 top-1/2"
        >
          <svg
            class="stroke-current"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M4.79175 7.396L10.0001 12.6043L15.2084 7.396"
              stroke=""
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </span>
      </div>
    </div>

    <!-- Observaciones -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Observaciones
      </label>
      <textarea
        v-model="formData.observaciones"
        placeholder="Observaciones sobre la muestra o el análisis"
        rows="4"
        class="w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
      ></textarea>
    </div>

    <!-- Botones de Acción -->
    <div class="flex items-center justify-end space-x-3 pt-6">
      <button
        @click="cancelarEdicion"
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
        @click="actualizarMuestra"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
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
        {{ isLoading ? 'Actualizando...' : 'Actualizar Muestra' }}
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
            <h3 class="text-2xl font-bold text-gray-900 mb-2">¡Muestra Actualizada!</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              La muestra <strong class="text-brand-600">{{ formData.idMuestra }}</strong>
            </p>
            <p class="text-gray-600 mb-1">
              del paciente
            </p>
            <p class="text-lg font-semibold text-brand-600 mb-1">
              {{ formData.paciente.nombre }}
            </p>
            <p class="text-gray-600 mb-1">
              ha sido actualizada al estado:
            </p>
            <p class="text-lg font-semibold text-green-600 capitalize mb-4">
              {{ formData.estado.replace('-', ' ') }}
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
import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'
import type { BaseOptions } from 'flatpickr/dist/types/options'

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
  idMuestra: '',
  paciente: {
    nombre: '',
    cedula: ''
  },
  tipoAnalisis: '',
  estado: '',
  medicoSolicitante: '',
  prioridad: 'normal',
  fechaIngreso: '',
  observaciones: '',
  resultados: ''
})

// Validación del formulario
const isFormValid = computed(() => {
  return !!(
    formData.idMuestra &&
    formData.tipoAnalisis &&
    formData.estado &&
    formData.medicoSolicitante &&
    formData.fechaIngreso
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
      tipoAnalisis: 'hemograma-completo',
      estado: 'en-proceso',
      medicoSolicitante: 'dr-garcia',
      prioridad: 'normal',
      fechaIngreso: '2024-01-15T10:30:00',
      observaciones: 'Muestra recibida en condiciones óptimas',
      resultados: ''
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

// Función para actualizar la muestra
const actualizarMuestra = async () => {
  if (!isFormValid.value) {
    statusType.value = 'error'
    statusMessage.value = 'Por favor complete todos los campos requeridos'
    return
  }

  isLoading.value = true
  statusMessage.value = ''

  try {
    
    statusType.value = 'success'
    statusMessage.value = 'Muestra actualizada exitosamente'
    
    // Mostrar notificación emergente
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
    emit('muestra-updated', { ...formData })
    
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al actualizar la muestra. Intente nuevamente.'
    console.error('Error:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para cancelar la edición
const cancelarEdicion = () => {
  emit('cancel-edit')
}

// Configuración de flatpickr mejorada
const fechaIngresoConfig: Partial<BaseOptions> = {
  dateFormat: 'Y-m-d H:i',
  altInput: true,
  altFormat: 'd/m/Y H:i',
  enableTime: true,
  time_24hr: true,
  minuteIncrement: 1,
  defaultDate: new Date(),
  locale: {
    firstDayOfWeek: 1,
    weekdays: {
      shorthand: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
      longhand: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    },
    months: {
      shorthand: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
      longhand: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    }
  },
  allowInput: true,
  disableMobile: false
}

// Emits
const emit = defineEmits(['muestra-updated', 'cancel-edit'])

// Cargar datos al montar el componente
onMounted(() => {
  cargarMuestra()
})
</script>