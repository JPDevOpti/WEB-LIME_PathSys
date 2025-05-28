<template>
  <div class="space-y-6">
    <!-- Búsqueda de Muestra -->
    <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-lg p-6">
      <div class="mb-4">
        <h3 class="text-lg font-semibold text-blue-800 mb-2 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
          Asignación de Patólogo a Muestra
        </h3>
        <p class="text-sm text-blue-600">Ingrese el código de la muestra para asignar un patólogo</p>
      </div>

      <div>
        <label class="mb-2 block text-sm font-medium text-gray-700">
          Código de Muestra *
        </label>
        <div class="relative">
          <span class="absolute left-0 top-1/2 -translate-y-1/2 border-r border-gray-200 px-3.5 py-3 text-blue-500">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
            </svg>
          </span>
          <input
            v-model="codigoMuestra"
            type="text"
            placeholder="Ejemplo: M001"
            class="h-12 w-full rounded-lg border border-gray-300 bg-white px-4 py-3 pl-[62px] text-sm text-gray-800 shadow-sm placeholder:text-gray-400 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
            @keyup.enter="buscarMuestra"
            :disabled="isLoading"
          />
          <div class="absolute right-2 top-1/2 -translate-y-1/2 flex items-center space-x-2">
            <button
              v-if="codigoMuestra.trim()"
              @click="codigoMuestra = ''"
              type="button"
              class="rounded-lg bg-gray-100 p-2 text-gray-500 hover:bg-gray-200 transition-colors"
              title="Limpiar campo"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <button
              @click="buscarMuestra"
              :disabled="!codigoMuestra.trim() || isLoading"
              class="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
              {{ isLoading ? 'Buscando...' : 'Buscar' }}
            </button>
          </div>
        </div>

        <!-- Resultado de la búsqueda -->
        <div v-if="searchPerformed" class="mt-4">
          <!-- Muestra encontrada -->
          <div v-if="muestraEncontrada" class="rounded-lg bg-emerald-50 border border-emerald-200 p-4">
            <div class="flex items-start space-x-3">
              <div class="flex-shrink-0">
                <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div class="flex-1">
                <h4 class="text-sm font-semibold text-emerald-800 mb-2">¡Muestra encontrada!</h4>
                <div class="mt-3 flex items-center space-x-2">
                  <span class="inline-flex items-center px-3 py-1.5 bg-emerald-100 text-emerald-800 text-xs font-medium rounded-md">
                    <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                    Muestra Lista para Asignar Patólogo
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Muestra no encontrada -->
          <div v-else class="rounded-lg bg-amber-50 border border-amber-200 p-4">
            <div class="flex items-start space-x-3">
              <div class="flex-shrink-0">
                <svg class="w-6 h-6 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                </svg>
              </div>
              <div class="flex-1">
                <h4 class="text-sm font-semibold text-amber-800 mb-1">Muestra no encontrada</h4>
                <p class="text-xs text-amber-600">
                  No existe una muestra registrada con el código <strong>{{ codigoMuestra }}</strong>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Formulario de Asignación de Patólogo (se muestra si la muestra es encontrada) -->
    <div v-if="muestraEncontrada" class="space-y-6">
      <div class="bg-white border border-gray-200 rounded-lg p-6">
        <h3 class="text-lg font-semibold text-gray-800 mb-4 flex items-center">
          <svg class="w-5 h-5 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          Asignar Patólogo a la Muestra
        </h3>

        <!-- Información de la Muestra -->
        <div class="bg-gray-50 rounded-lg p-4 border border-gray-200 mb-6">
          <h4 class="text-sm font-semibold text-gray-700 mb-3">Información de la Muestra</h4>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Código de Muestra</label>
              <input
                type="text"
                :value="muestraInfo.codigo"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Número de Caso</label>
              <input
                type="text"
                :value="muestraInfo.numeroCaso"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Nombre del Paciente</label>
              <input
                type="text"
                :value="muestraInfo.paciente.nombre"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Cédula del Paciente</label>
              <input
                type="text"
                :value="muestraInfo.paciente.cedula"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div class="md:col-span-2">
              <label class="mb-1.5 block text-sm font-medium text-gray-600">CUPS</label>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="cups in muestraInfo.cups"
                  :key="cups"
                  class="inline-flex items-center px-3 py-1.5 bg-gray-100 text-gray-700 text-sm font-medium rounded-md"
                >
                  {{ cups }}
                </span>
              </div>
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Entidad</label>
              <input
                type="text"
                :value="muestraInfo.entidad"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
          </div>
        </div>

        <!-- Selección de Patólogo -->
        <div class="mb-6">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">Patólogo Asignado *</label>
          <div class="relative">
            <input
              type="text"
              v-model="patologoSearch"
              @input="filterPatologos"
              @focus="showPatologosList = true"
              placeholder="Buscar o seleccionar patólogo"
              class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            />
            <!-- Lista desplegable de patólogos -->
            <div
              v-if="showPatologosList && filteredPatologos.length > 0"
              class="absolute z-[9999] w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto"
            >
              <div
                v-for="patologo in filteredPatologos"
                :key="patologo.value"
                @click="selectPatologo(patologo)"
                class="px-4 py-2 hover:bg-gray-100 cursor-pointer text-sm"
                :class="{ 'bg-gray-100': formData.patologoAsignado === patologo.value }"
              >
                {{ patologo.label }}
              </div>
            </div>
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="flex justify-end space-x-4">
          <button
            @click="limpiarFormulario"
            type="button"
            class="inline-flex items-center px-6 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
            Limpiar
          </button>
          <button
            @click="asignarPatologo"
            type="button"
            class="inline-flex items-center px-6 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:bg-gray-400 disabled:hover:bg-gray-400 disabled:cursor-not-allowed transition-colors"
            :disabled="!isFormValid"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            Asignar Patólogo
          </button>
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
            <h3 class="text-2xl font-bold text-gray-900 mb-2">¡Patólogo Asignado!</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              El patólogo ha sido asignado correctamente a la muestra
            </p>
            <p class="text-lg font-semibold text-brand-600 mb-1">
              {{ muestraInfo.codigo }}
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
            
            <!-- Botón de cierre -->
            <button
              @click="showNotification = false"
              class="w-full inline-flex items-center justify-center px-6 py-3 border border-green-300 rounded-lg text-base font-medium text-green-700 bg-green-50 hover:bg-green-100 focus:outline-none focus:ring-3 focus:ring-green-500 focus:ring-offset-2 transition-colors"
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
import { ref, reactive, computed, onMounted } from 'vue'

interface MuestraInfo {
  codigo: string
  numeroCaso: string
  paciente: {
    nombre: string
    cedula: string
  }
  cups: string[]
  entidad: string
}

// Estado del formulario
const codigoMuestra = ref('')
const isLoading = ref(false)
const searchPerformed = ref(false)
const muestraEncontrada = ref(false)
const showNotification = ref(false)
const progressWidth = ref(100)

// Información de la muestra
const muestraInfo = ref<MuestraInfo>({
  codigo: '',
  numeroCaso: '',
  paciente: {
    nombre: '',
    cedula: ''
  },
  cups: [],
  entidad: ''
})

// Datos del formulario
const formData = reactive({
  patologoAsignado: ''
})

// Lista de patólogos
const patologos = [
  { value: 'dr-jimenez', label: 'Dr. Jiménez Herrera (JH)' },
  { value: 'dra-morales', label: 'Dra. Morales Castro (MC)' },
  { value: 'dr-vargas', label: 'Dr. Vargas Mendez (VM)' },
  { value: 'dra-restrepo', label: 'Dra. Restrepo Vega (RV)' },
  { value: 'dr-sandoval', label: 'Dr. Sandoval Lima (SL)' },
  { value: 'dra-herrera', label: 'Dra. Herrera Cruz (HC)' }
]

// Estado para el combobox de patólogos
const patologoSearch = ref('')
const showPatologosList = ref(false)
const filteredPatologos = ref(patologos)

// Base de datos simulada de muestras
const muestrasDB: Record<string, MuestraInfo> = {
  'M001': {
    codigo: 'M001',
    numeroCaso: 'C001',
    paciente: {
      nombre: 'Juan Pérez García',
      cedula: '12345678'
    },
    cups: ['CUPS001', 'CUPS002', 'CUPS003'],
    entidad: 'ESSALUD'
  },
  'M002': {
    codigo: 'M002',
    numeroCaso: 'C002',
    paciente: {
      nombre: 'María López Silva',
      cedula: '87654321'
    },
    cups: ['CUPS004', 'CUPS005'],
    entidad: 'MINSA'
  }
}

// Validación del formulario
const isFormValid = computed(() => {
  return !!(
    muestraEncontrada.value &&
    formData.patologoAsignado
  )
})

// Función para buscar muestra
const buscarMuestra = async () => {
  if (!codigoMuestra.value.trim()) return

  isLoading.value = true
  searchPerformed.value = true

  try {
    const muestra = muestrasDB[codigoMuestra.value]
    
    if (muestra) {
      muestraEncontrada.value = true
      muestraInfo.value = { ...muestra }
    } else {
      muestraEncontrada.value = false
      muestraInfo.value = {
        codigo: '',
        numeroCaso: '',
        paciente: {
          nombre: '',
          cedula: ''
        },
        cups: [],
        entidad: ''
      }
    }
  } catch (error) {
    console.error('Error al buscar muestra:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para limpiar el formulario
const limpiarFormulario = () => {
  codigoMuestra.value = ''
  searchPerformed.value = false
  muestraEncontrada.value = false
  muestraInfo.value = {
    codigo: '',
    numeroCaso: '',
    paciente: {
      nombre: '',
      cedula: ''
    },
    cups: [],
    entidad: ''
  }
  formData.patologoAsignado = ''
  patologoSearch.value = ''
  showNotification.value = false
  progressWidth.value = 100
}

// Función para filtrar patólogos
const filterPatologos = () => {
  const search = patologoSearch.value.toLowerCase()
  filteredPatologos.value = patologos.filter(patologo => 
    patologo.label.toLowerCase().includes(search)
  )
}

// Función para seleccionar patólogo
const selectPatologo = (patologo: { value: string; label: string }) => {
  formData.patologoAsignado = patologo.value
  patologoSearch.value = patologo.label
  showPatologosList.value = false
}

// Función para asignar patólogo
const asignarPatologo = () => {
  if (!isFormValid.value) return

  // Mostrar notificación
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
  emit('patologo-asignado', {
    codigoMuestra: muestraInfo.value.codigo,
    patologo: formData.patologoAsignado
  })
}

// Emits
const emit = defineEmits<{
  'patologo-asignado': [data: { codigoMuestra: string; patologo: string }]
}>()

// Exponer funciones para uso externo
defineExpose({
  limpiarFormulario,
  buscarMuestra
})

// Cerrar la lista al hacer clic fuera
onMounted(() => {
  document.addEventListener('click', (e) => {
    const target = e.target as HTMLElement
    if (!target.closest('.relative')) {
      showPatologosList.value = false
    }
  })
})
</script>