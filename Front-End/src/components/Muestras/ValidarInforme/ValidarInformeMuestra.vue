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

    <!-- Resultados de Análisis (Editable) -->
    <div class="bg-blue-50 rounded-lg p-4 border border-blue-200">
      <h3 class="text-sm font-semibold text-blue-700 mb-4">Resultados de Análisis (Informe)</h3>
      
      <!-- Corte Macro -->
      <div class="mb-4">
        <div class="flex items-center justify-between mb-2">
          <label class="text-sm font-medium text-gray-700">Corte Macro</label>
          <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            Código: {{ formData.codigoCorteMacro }}
          </span>
        </div>
        <textarea
          v-model="formData.resultadoCorteMacro"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
          placeholder="Ingrese la descripción del corte macro"
        ></textarea>
      </div>

      <!-- Corte Micro -->
      <div class="mb-4">
        <div class="flex items-center justify-between mb-2">
          <label class="text-sm font-medium text-gray-700">Corte Micro</label>
          <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            Código: {{ formData.codigoCorteMicro }}
          </span>
        </div>
        <textarea
          v-model="formData.resultadoCorteMicro"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
          placeholder="Ingrese la descripción del corte micro"
        ></textarea>
      </div>

      <!-- Método -->
      <div class="mb-4">
        <div class="flex items-center justify-between mb-2">
          <label class="text-sm font-medium text-gray-700">Método</label>
          <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
            Código: {{ formData.codigoMetodo }}
          </span>
        </div>
        <textarea
          v-model="formData.resultadoMetodo"
          rows="4"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
          placeholder="Ingrese la descripción del método utilizado"
        ></textarea>
      </div>

      <!-- Diagnóstico Final -->
      <div>
        <label class="mb-2 block text-sm font-medium text-gray-700">
          Diagnóstico Final
        </label>
        <textarea
          v-model="formData.diagnosticoFinal"
          rows="6"
          class="w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 resize-none"
          placeholder="Ingrese el diagnóstico final"
        ></textarea>
      </div>
      <!-- Campo: ¿Cáncer? Sí / No -->
      <div class="mt-4">
        <label class="mb-2 block text-sm font-medium text-gray-700">
          ¿Cáncer?
        </label>
        <div class="flex items-center space-x-6">
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.cancer"
              :value="'si'"
              class="form-radio h-5 w-5 text-red-600"
            >
            <span class="ml-2 text-sm text-gray-700">Sí</span>
          </label>
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.cancer"
              :value="'no'"
              class="form-radio h-5 w-5 text-green-600"
            >
            <span class="ml-2 text-sm text-gray-700">No</span>
          </label>
          <label class="inline-flex items-center">
            <input
              type="radio"
              v-model="formData.cancer"
              :value="'no_aplica'"
              class="form-radio h-5 w-5 text-blue-600"
            >
            <span class="ml-2 text-sm text-gray-700">No aplica</span>
          </label>
        </div>
      </div>
    </div>

    <!-- Validación del Informe -->
    <div class="bg-yellow-50 rounded-lg p-4 border border-yellow-200">
      <h3 class="text-sm font-semibold text-yellow-700 mb-4">Validación del Informe</h3>
      
      <!-- Estado de validación -->
      <div class="mb-4">
        <label class="mb-2 block text-sm font-medium text-gray-700">
          Estado de Validación *
        </label>
        <div class="flex items-center space-x-4">
          <label class="inline-flex items-center">
            <input 
              type="radio" 
              v-model="formData.estadoValidacion" 
              value="aprobado" 
              class="form-radio h-5 w-5 text-green-600"
            >
            <span class="ml-2 text-sm text-gray-700">Aprobado</span>
          </label>
          <label class="inline-flex items-center">
            <input 
              type="radio" 
              v-model="formData.estadoValidacion" 
              value="requiere_cambios" 
              class="form-radio h-5 w-5 text-yellow-600"
            >
            <span class="ml-2 text-sm text-gray-700">Requiere cambios</span>
          </label>
        </div>
      </div>

      <!-- Comentarios de validación (solo visible si requiere cambios) -->
      <div v-if="formData.estadoValidacion === 'requiere_cambios'">
        <label class="mb-2 block text-sm font-medium text-gray-700">
          Comentarios de Validación *
        </label>
        <textarea
          v-model="formData.comentariosValidacion"
          placeholder="Ingrese sus comentarios sobre los cambios requeridos"
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
        @click="guardarValidacion"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        :disabled="isLoading || !validacionCompleta"
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
            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        {{ isLoading ? 'Guardando...' : 'Guardar Validación' }}
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
          class="relative bg-white rounded-2xl shadow-2xl border-l-4"
          :class="notificationBorderClass"
        >
          <div class="text-center p-8 max-w-md w-full">
            <!-- Ícono -->
            <div class="mx-auto flex items-center justify-center w-16 h-16 rounded-full mb-4"
                 :class="notificationIconBgClass">
              <svg class="w-10 h-10" :class="notificationIconClass" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path 
                  v-if="formData.estadoValidacion === 'aprobado'"
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="2.5" 
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" 
                />
                <path 
                  v-else-if="formData.estadoValidacion === 'rechazado'"
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="2.5" 
                  d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" 
                />
                <path 
                  v-else
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="2.5" 
                  d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" 
                />
              </svg>
            </div>
            
            <!-- Título -->
            <h3 class="text-2xl font-bold text-gray-900 mb-2">{{ notificationTitle }}</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              El informe para la muestra
            </p>
            <p class="text-lg font-semibold mb-4" :class="notificationTextClass">
              {{ formData.idMuestra }}
            </p>
            <p class="text-gray-600 mb-6">
              ha sido {{ notificationStatusText }}.
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
                class="h-2 rounded-full transition-all duration-75 ease-linear"
                :class="notificationProgressClass"
                :style="{ width: progressWidth + '%' }"
              ></div>
            </div>
            
            <!-- Botón de cerrar -->
            <button
              @click="showNotification = false"
              class="w-full inline-flex items-center justify-center px-6 py-3 border border-transparent rounded-lg text-base font-medium text-white transition-colors"
              :class="notificationButtonClass"
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

// Props para recibir el ID de la muestra a validar
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
    cedula: '',
    edad: '',
    sexo: '',
    fechaNacimiento: ''
  },
  tipoAnalisisTexto: '',
  estadoTexto: '',
  medicoSolicitanteTexto: '',
  fechaIngresoTexto: '',
  fechaResultadoTexto: '',
  
  // Códigos de secciones
  codigoCorteMacro: '',
  codigoCorteMicro: '',
  codigoMetodo: '',
  
  // Resultados editables
  resultadoCorteMacro: '',
  resultadoCorteMicro: '',
  resultadoMetodo: '',
  diagnosticoFinal: '',
  
  // Nuevo campo: ¿Cáncer?
  cancer: '',
  
  // Campos para la validación
  estadoValidacion: '',
  comentariosValidacion: ''
})

// Modificar la validación para que solo requiera comentarios si es requiere_cambios
const validacionCompleta = computed(() => {
  if (formData.estadoValidacion === 'requiere_cambios') {
    return formData.estadoValidacion && formData.comentariosValidacion.trim().length > 0
  }
  return formData.estadoValidacion === 'aprobado'
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

// Clases dinámicas para la notificación según el estado de validación
const notificationBorderClass = computed(() => {
  const classes: Record<string, string> = {
    'aprobado': 'border-green-500',
    'rechazado': 'border-red-500',
    'requiere_cambios': 'border-yellow-500'
  }
  return classes[formData.estadoValidacion as keyof typeof classes] || 'border-gray-500'
})

const notificationIconBgClass = computed(() => {
  const classes: Record<string, string> = {
    'aprobado': 'bg-green-100',
    'rechazado': 'bg-red-100',
    'requiere_cambios': 'bg-yellow-100'
  }
  return classes[formData.estadoValidacion as keyof typeof classes] || 'bg-gray-100'
})

const notificationIconClass = computed(() => {
  const classes: Record<string, string> = {
    'aprobado': 'text-green-600',
    'rechazado': 'text-red-600',
    'requiere_cambios': 'text-yellow-600'
  }
  return classes[formData.estadoValidacion as keyof typeof classes] || 'text-gray-600'
})

const notificationTextClass = computed(() => {
  const classes: Record<string, string> = {
    'aprobado': 'text-green-600',
    'rechazado': 'text-red-600',
    'requiere_cambios': 'text-yellow-600'
  }
  return classes[formData.estadoValidacion as keyof typeof classes] || 'text-gray-600'
})

const notificationProgressClass = computed(() => {
  const classes: Record<string, string> = {
    'aprobado': 'bg-green-500',
    'rechazado': 'bg-red-500',
    'requiere_cambios': 'bg-yellow-500'
  }
  return classes[formData.estadoValidacion as keyof typeof classes] || 'bg-gray-500'
})

const notificationButtonClass = computed(() => {
  const classes: Record<string, string> = {
    'aprobado': 'bg-green-600 hover:bg-green-700 focus:ring-green-500',
    'rechazado': 'bg-red-600 hover:bg-red-700 focus:ring-red-500',
    'requiere_cambios': 'bg-yellow-600 hover:bg-yellow-700 focus:ring-yellow-500'
  }
  return classes[formData.estadoValidacion as keyof typeof classes] || 'bg-gray-600 hover:bg-gray-700 focus:ring-gray-500'
})

const notificationTitle = computed(() => {
  const titles: Record<string, string> = {
    'aprobado': '¡Informe Aprobado!',
    'rechazado': 'Informe Rechazado',
    'requiere_cambios': 'Informe Requiere Cambios'
  }
  return titles[formData.estadoValidacion as keyof typeof titles] || 'Validación Completada'
})

const notificationStatusText = computed(() => {
  const texts: Record<string, string> = {
    'aprobado': 'aprobado exitosamente',
    'rechazado': 'rechazado',
    'requiere_cambios': 'marcado para revisión'
  }
  return texts[formData.estadoValidacion as keyof typeof texts] || 'procesado'
})

// Función para cargar los datos del informe
const cargarInforme = async () => {
  isLoading.value = true

  try {
    // Simulación de carga de datos desde la API
    const informeData = {
      idMuestra: props.muestraId || 'L2024-0586',
      paciente: {
        nombre: 'María Fernanda Rodríguez Álvarez',
        cedula: '1723456789',
        edad: '42 años',
        sexo: 'Femenino',
        fechaNacimiento: '12/05/1982'
      },
      tipoAnalisisTexto: 'Biopsia de Mama',
      estadoTexto: 'Pendiente de Validación',
      medicoSolicitanteTexto: 'Dra. Gabriela Salazar - Cirugía General',
      fechaIngresoTexto: '18/07/2024 09:15',
      fechaResultadoTexto: '19/07/2024 14:30',
      
      // Códigos de secciones
      codigoCorteMacro: 'MAC-001',
      codigoCorteMicro: 'MIC-001',
      codigoMetodo: 'MET-001',
      
      // Resultados iniciales
      resultadoCorteMacro: 'Muestra de tejido mamario derecho, de 2.5 x 1.8 x 1.2 cm, con superficie externa irregular y coloración blanco-grisácea. Al corte se observa una lesión nodular de 1.5 cm de diámetro, de consistencia firme y coloración blanco-amarillenta.',
      resultadoCorteMicro: 'Se observa proliferación de células epiteliales atípicas con núcleos hipercromáticos y pleomórficos. Se identifican mitosis atípicas y pérdida de la arquitectura normal del tejido. El estroma muestra desmoplasia moderada.',
      resultadoMetodo: 'Tinción con Hematoxilina-Eosina. Inmunohistoquímica positiva para receptores de estrógeno y progesterona. Ki-67 elevado (30%).',
      diagnosticoFinal: 'Carcinoma ductal infiltrante de mama, grado II (moderadamente diferenciado). Tamaño tumoral: 1.5 cm. Margen quirúrgico libre de tumor. Ganglios linfáticos negativos para metástasis (0/3).',
      // Valor por defecto para cáncer
      cancer: ''
    }
    
    // Asignar datos al formulario
    Object.assign(formData, informeData)
    
    console.log('Datos cargados:', formData)
    
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al cargar los datos del informe'
    console.error('Error:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para guardar la validación del informe
const guardarValidacion = async () => {
  if (!validacionCompleta.value) {
    statusType.value = 'error'
    statusMessage.value = 'Por favor complete todos los campos de validación'
    return
  }

  isLoading.value = true
  statusMessage.value = ''

  try {
    // Simular llamada a API
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    statusType.value = 'success'
    statusMessage.value = 'Validación guardada exitosamente'
    
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
    
    // Emitir evento de validación completada
    emit('validacion-completada', {
      muestraId: formData.idMuestra,
      estadoValidacion: formData.estadoValidacion,
      comentariosValidacion: formData.comentariosValidacion
    })
    
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al guardar la validación. Intente nuevamente.'
    console.error('Error:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para cancelar
const cancelar = () => {
  emit('cancelar')
}

// Emits
const emit = defineEmits(['validacion-completada', 'cancelar'])

// Cargar datos al montar el componente
onMounted(() => {
  cargarInforme()
})
</script>