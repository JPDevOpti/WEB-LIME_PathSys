<template>
  <div class="space-y-6">
    <!-- Búsqueda por Código de Muestra -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400">
        Código de Muestra
      </label>
      <div class="relative">
        <span
          class="absolute left-0 top-1/2 -translate-y-1/2 border-r border-gray-200 px-3.5 py-3 text-gray-500 dark:border-gray-800 dark:text-gray-400"
        >
          <svg
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M8.33333 14.1667C11.555 14.1667 14.1667 11.555 14.1667 8.33333C14.1667 5.11167 11.555 2.5 8.33333 2.5C5.11167 2.5 2.5 5.11167 2.5 8.33333C2.5 11.555 5.11167 14.1667 8.33333 14.1667Z"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
            <path
              d="M17.5 17.5L13.125 13.125"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
        </span>
        <input
          v-model="codigoMuestra"
          type="text"
          placeholder="Ej: L2024-001"
          class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 pl-[62px] text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
          @keyup.enter="buscarMuestra"
        />
        <button
          @click="buscarMuestra"
          :disabled="!codigoMuestra || isLoading"
          class="absolute right-2 top-1/2 -translate-y-1/2 rounded-md bg-brand-600 px-4 py-2 text-sm font-medium text-white hover:bg-brand-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          {{ isLoading ? 'Buscando...' : 'Buscar' }}
        </button>
      </div>
    </div>

    <!-- Resultado de la búsqueda -->
    <div v-if="muestraEncontrada" class="mt-6">
      <!-- Status de la muestra -->
      <div class="mb-4 flex items-center justify-between">
        <h3 class="text-lg font-medium text-gray-900 dark:text-white">
          Muestra encontrada: {{ muestra.id }}
        </h3>
        <span
          :class="{
            'bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100': muestra.estado === 'Terminado',
            'bg-yellow-100 text-yellow-800 dark:bg-yellow-800 dark:text-yellow-100': muestra.estado === 'En Proceso',
            'bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100': muestra.estado === 'Pendiente'
          }"
          class="inline-flex px-3 py-1 text-sm font-semibold rounded-full"
        >
          {{ muestra.estado }}
        </span>
      </div>
      
      <!-- Información de la Muestra -->
      <div class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700 p-6 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Información del Paciente -->
          <div class="space-y-3">
            <h4 class="text-sm font-semibold text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-700 pb-2">
              Información del Paciente
            </h4>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Nombre:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.paciente.nombre }}</span>
            </div>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Cédula:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.paciente.cedula }}</span>
            </div>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Edad:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.paciente.edad }} años</span>
            </div>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Género:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.paciente.genero }}</span>
            </div>
          </div>

          <!-- Información de la Muestra -->
          <div class="space-y-3">
            <h4 class="text-sm font-semibold text-gray-900 dark:text-white border-b border-gray-200 dark:border-gray-700 pb-2">
              Detalles de la Muestra
            </h4>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Tipo de Análisis:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.tipoAnalisis }}</span>
            </div>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Fecha de Ingreso:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.fechaIngreso }}</span>
            </div>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Médico Solicitante:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.medicoSolicitante }}</span>
            </div>
            <div>
              <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Observaciones:</span>
              <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ muestra.observaciones || 'Sin observaciones' }}</span>
            </div>
          </div>
        </div>

        <!-- Progreso del Análisis -->
        <div class="mt-6">
          <h4 class="text-sm font-semibold text-gray-900 dark:text-white mb-3">Progreso del Análisis</h4>
          <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
            <div
              :class="{
                'bg-red-600': muestra.progreso <= 33,
                'bg-yellow-600': muestra.progreso > 33 && muestra.progreso <= 66,
                'bg-green-600': muestra.progreso > 66
              }"
              class="h-2.5 rounded-full transition-all duration-300"
              :style="`width: ${muestra.progreso}%`"
            ></div>
          </div>
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1">{{ muestra.progreso }}% completado</p>
        </div>
      </div>
    </div>

    <!-- Mensaje cuando no se encuentra la muestra -->
    <div v-if="searchPerformed && !muestraEncontrada" class="text-center py-8">
      <div class="text-gray-500 dark:text-gray-400">
        <svg class="mx-auto h-12 w-12 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 12h6m-3-8a8 8 0 000 16 8 8 0 000-16z" />
        </svg>
        <p class="text-lg font-medium">Muestra no encontrada</p>
        <p class="text-sm">No existe una muestra con el código {{ codigoMuestra }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const codigoMuestra = ref('')
const isLoading = ref(false)
const searchPerformed = ref(false)
const muestraEncontrada = ref(false)

const muestra = ref({
  id: '',
  tipoAnalisis: '',
  fechaIngreso: '',
  estado: '',
  medicoSolicitante: '',
  observaciones: '',
  progreso: 0,
  paciente: {
    nombre: '',
    cedula: '',
    edad: '',
    genero: ''
  }
})

// Base de datos simulada de muestras
const muestrasDB = [
  {
    id: 'L2024-001',
    tipoAnalisis: 'Hemograma Completo',
    fechaIngreso: '15/01/2024',
    estado: 'Terminado',
    medicoSolicitante: 'Dr. García',
    observaciones: 'Muestra procesada exitosamente',
    progreso: 100,
    paciente: {
      nombre: 'Juan Pérez',
      cedula: '12345678',
      edad: '45',
      genero: 'Masculino'
    }
  },
  {
    id: 'L2024-002',
    tipoAnalisis: 'Química Sanguínea',
    fechaIngreso: '10/01/2024',
    estado: 'En Proceso',
    medicoSolicitante: 'Dra. Martínez',
    observaciones: 'En proceso de análisis enzimático',
    progreso: 65,
    paciente: {
      nombre: 'María García',
      cedula: '87654321',
      edad: '32',
      genero: 'Femenino'
    }
  },
  {
    id: 'L2024-003',
    tipoAnalisis: 'Uroanálisis',
    fechaIngreso: '08/01/2024',
    estado: 'Pendiente',
    medicoSolicitante: 'Dr. López',
    observaciones: 'Esperando procesamiento',
    progreso: 20,
    paciente: {
      nombre: 'Carlos Rodríguez',
      cedula: '11223344',
      edad: '28',
      genero: 'Masculino'
    }
  }
]

const buscarMuestra = async () => {
  if (!codigoMuestra.value) return
  
  isLoading.value = true
  searchPerformed.value = true
  
  // Remover el setTimeout para hacer instantáneo
  // setTimeout(() => {
    // Buscar en la base de datos simulada
    const muestraResultado = muestrasDB.find(m => 
      m.id.toLowerCase() === codigoMuestra.value.toLowerCase()
    )
    
    if (muestraResultado) {
      muestraEncontrada.value = true
      muestra.value = { ...muestraResultado }
    } else {
      muestraEncontrada.value = false
    }
    
    isLoading.value = false
  // }, 1000)
}
</script>