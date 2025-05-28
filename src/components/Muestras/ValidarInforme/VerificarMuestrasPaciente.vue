<template>
  <div class="space-y-6">
    <!-- Búsqueda por Cédula -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400">
        Número de Cédula
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
          v-model="cedula"
          type="text"
          placeholder="Ingrese número de cédula"
          class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 pl-[62px] text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
          @keyup.enter="buscarMuestras"
        />
        <button
          @click="buscarMuestras"
          :disabled="!cedula || isLoading"
          class="absolute right-2 top-1/2 -translate-y-1/2 rounded-md bg-brand-600 px-4 py-2 text-sm font-medium text-white hover:bg-brand-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          {{ isLoading ? 'Buscando...' : 'Buscar' }}
        </button>
      </div>
    </div>

    <!-- Resultados de la búsqueda -->
    <div v-if="muestrasEncontradas" class="mt-6">
      <h3 class="text-lg font-medium text-gray-900 dark:text-white mb-4">
        Muestras del paciente: {{ pacienteInfo.nombre }}
      </h3>
      
      <!-- Información del Paciente -->
      <div class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4 mb-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Cédula:</span>
            <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ pacienteInfo.cedula }}</span>
          </div>
          <div>
            <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Teléfono:</span>
            <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ pacienteInfo.telefono }}</span>
          </div>
          <div>
            <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Edad:</span>
            <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ pacienteInfo.edad }} años</span>
          </div>
          <div>
            <span class="text-sm font-medium text-gray-600 dark:text-gray-400">Género:</span>
            <span class="ml-2 text-sm text-gray-900 dark:text-white">{{ pacienteInfo.genero }}</span>
          </div>
        </div>
      </div>

      <!-- Tabla de Muestras -->
      <div class="overflow-hidden rounded-lg border border-gray-200 bg-white dark:border-gray-700 dark:bg-gray-800">
        <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
          <thead class="bg-gray-50 dark:bg-gray-700">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                ID Muestra
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                Tipo de Análisis
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                Fecha de Ingreso
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                Estado
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                Médico Solicitante
              </th>
            </tr>
          </thead>
          <tbody class="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
            <tr v-for="muestra in muestras" :key="muestra.id" class="hover:bg-gray-50 dark:hover:bg-gray-700">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 dark:text-white">
                {{ muestra.id }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-300">
                {{ muestra.tipoAnalisis }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-300">
                {{ muestra.fechaIngreso }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span
                  :class="{
                    'bg-green-100 text-green-800 dark:bg-green-800 dark:text-green-100': muestra.estado === 'Terminado',
                    'bg-yellow-100 text-yellow-800 dark:bg-yellow-800 dark:text-yellow-100': muestra.estado === 'En Proceso',
                    'bg-red-100 text-red-800 dark:bg-red-800 dark:text-red-100': muestra.estado === 'Pendiente'
                  }"
                  class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                >
                  {{ muestra.estado }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-300">
                {{ muestra.medicoSolicitante }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Mensaje cuando no hay resultados -->
    <div v-if="searchPerformed && !muestrasEncontradas" class="text-center py-8">
      <div class="text-gray-500 dark:text-gray-400">
        <svg class="mx-auto h-12 w-12 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p class="text-lg font-medium">No se encontraron muestras</p>
        <p class="text-sm">No hay muestras registradas para la cédula {{ cedula }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const cedula = ref('')
const isLoading = ref(false)
const searchPerformed = ref(false)
const muestrasEncontradas = ref(false)

const pacienteInfo = ref({
  nombre: '',
  cedula: '',
  telefono: '',
  edad: '',
  genero: ''
})

const muestras = ref([
  {
    id: 'L2024-001',
    tipoAnalisis: 'Hemograma Completo',
    fechaIngreso: '15/01/2024',
    estado: 'Terminado',
    medicoSolicitante: 'Dr. García'
  },
  // Más muestras...
])

const buscarMuestras = async () => {
  if (!cedula.value) return
  
  isLoading.value = true
  searchPerformed.value = true
  
  // Remover el setTimeout para hacer instantáneo
  // setTimeout(() => {
    // Datos de ejemplo
    if (cedula.value === '12345678') {
      muestrasEncontradas.value = true
      pacienteInfo.value = {
        nombre: 'Juan Pérez',
        cedula: '12345678',
        telefono: '0123456789',
        edad: '45',
        genero: 'Masculino'
      }
      muestras.value = [
        {
          id: 'L2024-001',
          tipoAnalisis: 'Hemograma Completo',
          fechaIngreso: '15/01/2024',
          estado: 'Terminado',
          medicoSolicitante: 'Dr. García'
        },
        {
          id: 'L2024-002',
          tipoAnalisis: 'Química Sanguínea',
          fechaIngreso: '10/01/2024',
          estado: 'En Proceso',
          medicoSolicitante: 'Dra. Martínez'
        },
        {
          id: 'L2024-003',
          tipoAnalisis: 'Uroanálisis',
          fechaIngreso: '08/01/2024',
          estado: 'Pendiente',
          medicoSolicitante: 'Dr. López'
        }
      ]
    } else {
      muestrasEncontradas.value = false
      muestras.value = []
    }
    isLoading.value = false
  // }, 1000)
}
</script>