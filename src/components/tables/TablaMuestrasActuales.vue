<template>
  <div class="space-y-4">
    <!-- Barra de búsqueda y filtros -->
    <div class="bg-white rounded-xl border border-gray-200 p-4">
      <div class="flex flex-col gap-4">
        <!-- Fila de búsqueda -->
        <div class="flex flex-col sm:flex-row sm:items-center gap-3">
          <div class="relative flex-1">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Buscar por ID de muestra o cédula del paciente..."
              class="h-11 w-full pl-10 pr-4 rounded-lg border border-gray-300 bg-transparent py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            />
          </div>
        </div>

        <!-- Fila de filtros -->
        <div class="flex flex-col sm:flex-row sm:items-center gap-3">
          <div class="flex flex-col sm:flex-row gap-3 flex-1">
            <!-- Filtro por año -->
            <div class="w-full sm:w-auto">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Año
              </label>
              <select
                v-model="selectedYear"
                class="h-11 w-full sm:w-32 appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
              >
                <option value="">Todos</option>
                <option v-for="year in availableYears" :key="year" :value="year">
                  {{ year }}
                </option>
              </select>
            </div>

            <!-- Filtro por mes -->
            <div class="w-full sm:w-auto">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Mes
              </label>
              <select
                v-model="selectedMonth"
                class="h-11 w-full sm:w-40 appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                :disabled="!selectedYear"
              >
                <option value="">Todos</option>
                <option v-for="month in availableMonths" :key="month.value" :value="month.value">
                  {{ month.name }}
                </option>
              </select>
            </div>

            <!-- Filtro por tipo de análisis -->
            <div class="w-full sm:w-auto">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Tipo de Análisis
              </label>
              <select
                v-model="selectedAnalisis"
                class="h-11 w-full sm:w-48 appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
              >
                <option value="">Todos</option>
                <option v-for="analisis in tiposAnalisis" :key="analisis" :value="analisis">
                  {{ analisis }}
                </option>
              </select>
            </div>

            <!-- Filtro por estado -->
            <div class="w-full sm:w-auto">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Estado
              </label>
              <select
                v-model="selectedEstado"
                class="h-11 w-full sm:w-40 appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
              >
                <option value="">Todos</option>
                <option v-for="estado in estados" :key="estado" :value="estado">
                  {{ estado }}
                </option>
              </select>
            </div>
          </div>

          <!-- Contador y botón limpiar -->
          <div class="flex items-center gap-3">
            <span class="text-sm text-gray-500">
              {{ filteredMuestras.length }} de {{ muestras.length }} muestras
            </span>
            <button
              v-if="hasActiveFilters"
              @click="clearAllFilters"
              class="inline-flex items-center px-3 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 transition-colors"
            >
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
              Limpiar filtros
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tabla -->
    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white">
      <!-- Acciones en lote -->
      <div v-if="selectedMuestras.length > 0" class="p-4 border-b border-gray-200 bg-gray-50">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="text-sm text-gray-600">
              {{ selectedMuestras.length }} muestras seleccionadas
            </span>
            <select
              v-model="accionEnLote"
              class="h-9 rounded-lg border border-gray-300 bg-white px-3 py-1.5 text-sm text-gray-700 focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-500/10"
            >
              <option value="">Acciones en lote</option>
              <option value="completado">Marcar como Completado</option>
              <option value="en-proceso">Marcar como En Proceso</option>
              <option value="pendiente">Marcar como Pendiente</option>
              <option value="validado">Marcar como Validado</option>
            </select>
            <button
              v-if="accionEnLote"
              @click="aplicarAccionEnLote"
              class="inline-flex items-center px-3 py-1.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 transition-colors"
            >
              Aplicar
            </button>
          </div>
          <button
            @click="selectedMuestras = []"
            class="text-gray-500 hover:text-gray-700"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>

      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <table class="min-w-full">
          <thead>
            <tr class="border-b border-gray-200">
              <th class="px-5 py-3 text-left w-1/24 sm:px-6">
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    :checked="isAllSelected"
                    @change="toggleSelectAll"
                    class="h-4 w-4 rounded border-gray-300 text-brand-500 focus:ring-brand-500"
                  />
                </div>
              </th>
              <th 
                v-for="column in columns" 
                :key="column.key"
                class="px-5 py-3 text-left sm:px-6"
                :class="column.class"
              >
                <button
                  class="flex items-center gap-1 font-medium text-gray-500 text-theme-xs hover:text-gray-700"
                  @click="sortBy(column.key)"
                >
                  {{ column.label }}
                  <svg
                    v-if="sortKey === column.key"
                    class="w-4 h-4"
                    :class="{ 'transform rotate-180': sortOrder === 'desc' }"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="(muestra, index) in paginatedMuestras"
              :key="index"
              class="border-t border-gray-100 hover:bg-gray-50 transition-colors"
            >
              <td class="px-5 py-4 sm:px-6">
                <input
                  type="checkbox"
                  :checked="selectedMuestras.includes(muestra.id)"
                  @change="toggleSelect(muestra.id)"
                  class="h-4 w-4 rounded border-gray-300 text-brand-500 focus:ring-brand-500"
                />
              </td>
              <td class="px-5 py-4 sm:px-6">
                <div class="flex items-center gap-3">
                  <div class="h-[32px] w-[32px] flex items-center justify-center bg-blue-50 rounded-md">
                    <svg
                      class="w-6 h-6 text-blue-600"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      viewBox="0 0 24 24"
                    >
                      <rect x="6" y="4" width="12" height="2" rx="1" stroke="currentColor" />
                      <rect x="6" y="6" width="12" height="14" rx="3" stroke="currentColor" />
                      <rect x="9" y="12" width="6" height="4" rx="0" stroke="currentColor" />
                    </svg>
                  </div>
                  <div>
                    <span class="block font-medium text-gray-800 text-theme-sm">
                      <span v-html="highlightText(muestra.id, searchQuery)"></span>
                    </span>
                    <span class="block text-gray-500 text-theme-xs">
                      {{ muestra.tipoMuestra }}
                    </span>
                  </div>
                </div>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <div>
                  <p class="text-gray-800 text-theme-sm">{{ muestra.paciente }}</p>
                  <p class="text-gray-500 text-theme-xs">
                    <span v-html="highlightText(muestra.dni, searchQuery)"></span>
                  </p>
                </div>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <p class="text-gray-800 text-theme-sm">{{ muestra.analisis }}</p>
                <p class="text-gray-500 text-theme-xs">{{ muestra.medico }}</p>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <span
                  :class="[
                    'rounded-full px-2 py-0.5 text-theme-xs font-medium',
                    {
                      'bg-success-50 text-success-700': muestra.estado === 'Completado',
                      'bg-warning-50 text-warning-700': muestra.estado === 'En Proceso',
                      'bg-error-50 text-error-700': muestra.estado === 'Pendiente',
                      'bg-success-50 text-info-700': muestra.estado === 'Validado',
                    },
                  ]"
                >
                  {{ muestra.estado }}
                </span>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <p class="text-gray-800 text-theme-sm">{{ formatDate(muestra.fechaRecepcion) }}</p>
                <p class="text-gray-500 text-theme-xs">{{ muestra.horaRecepcion }}</p>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <div class="flex gap-2">
                  <button 
                    @click="mostrarDetallesMuestra(muestra)"
                    class="text-brand-500 hover:text-brand-600 p-1 rounded-md hover:bg-brand-50 transition-colors"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  <button 
                    @click="editarMuestra(muestra)"
                    class="text-brand-500 hover:text-brand-600 p-1 rounded-md hover:bg-brand-50 transition-colors"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
            <!-- Mensaje cuando no hay resultados -->
            <tr v-if="filteredMuestras.length === 0">
              <td colspan="7" class="px-5 py-8 text-center">
                <div class="flex flex-col items-center">
                  <svg class="w-12 h-12 text-gray-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>
                  </svg>
                  <p class="text-gray-500 text-theme-sm font-medium">
                    {{ hasActiveFilters ? 'No se encontraron muestras con los filtros aplicados' : 'No hay muestras disponibles' }}
                  </p>
                  <p v-if="hasActiveFilters" class="text-gray-400 text-theme-xs mt-1">
                    Intente con otros criterios de búsqueda
                  </p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal de Detalles -->
      <transition
        enter-active-class="transition ease-out duration-300"
        enter-from-class="opacity-0 transform scale-95"
        enter-to-class="opacity-100 transform scale-100"
        leave-active-class="transition ease-in duration-200"
        leave-from-class="opacity-100 transform scale-100"
        leave-to-class="opacity-0 transform scale-95"
      >
        <div
          v-if="muestraSeleccionada"
          class="fixed inset-0 z-50 flex items-center justify-center p-4"
        >
          <!-- Overlay oscuro -->
          <div 
            class="absolute inset-0 bg-black bg-opacity-50"
            @click="muestraSeleccionada = null"
          ></div>
          
          <!-- Modal -->
          <div
            class="relative bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto"
          >
            <!-- Encabezado -->
            <div class="sticky top-0 z-10 bg-white border-b border-gray-200 px-6 py-4 rounded-t-2xl">
              <div class="flex items-center justify-between">
                <h3 class="text-xl font-semibold text-gray-900">
                  Detalles de la Muestra
                </h3>
                <button
                  @click="muestraSeleccionada = null"
                  class="text-gray-400 hover:text-gray-600 transition-colors"
                >
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Contenido -->
            <div class="p-6 space-y-6">
              <!-- ID y Estado -->
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="text-lg font-medium text-gray-900">{{ muestraSeleccionada.id }}</h4>
                  <p class="text-sm text-gray-500">{{ muestraSeleccionada.tipoMuestra }}</p>
                </div>
                <span
                  :class="[
                    'rounded-full px-3 py-1 text-sm font-medium',
                    {
                      'bg-success-50 text-success-700': muestraSeleccionada.estado === 'Completado',
                      'bg-warning-50 text-warning-700': muestraSeleccionada.estado === 'En Proceso',
                      'bg-error-50 text-error-700': muestraSeleccionada.estado === 'Pendiente',
                      'bg-info-50 text-info-700': muestraSeleccionada.estado === 'Validado',
                    },
                  ]"
                >
                  {{ muestraSeleccionada.estado }}
                </span>
              </div>

              <!-- Información del Paciente -->
              <div class="bg-gray-50 rounded-xl p-4">
                <h5 class="text-sm font-medium text-gray-700 mb-3">Información del Paciente</h5>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <p class="text-sm text-gray-500">Nombre</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.paciente }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">DNI/Cédula</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.dni }}</p>
                  </div>
                </div>
              </div>

              <!-- Información del Análisis -->
              <div class="bg-gray-50 rounded-xl p-4">
                <h5 class="text-sm font-medium text-gray-700 mb-3">Información del Análisis</h5>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <p class="text-sm text-gray-500">Tipo de Análisis</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.analisis }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">Médico Solicitante</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.medico }}</p>
                  </div>
                </div>
              </div>

              <!-- Información de Recepción -->
              <div class="bg-gray-50 rounded-xl p-4">
                <h5 class="text-sm font-medium text-gray-700 mb-3">Información de Recepción</h5>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <p class="text-sm text-gray-500">Fecha de Recepción</p>
                    <p class="text-base font-medium text-gray-900">{{ formatDate(muestraSeleccionada.fechaRecepcion) }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">Hora de Recepción</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.horaRecepcion }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Pie del Modal -->
            <div class="sticky bottom-0 bg-white border-t border-gray-200 px-6 py-4 rounded-b-2xl">
              <div class="flex justify-end gap-3">
                <button
                  @click="muestraSeleccionada = null"
                  class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-brand-500/10"
                >
                  Cerrar
                </button>
                <button
                  @click="editarMuestra(muestraSeleccionada)"
                  class="inline-flex items-center px-4 py-2 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20"
                >
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                  Editar Muestra
                </button>
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- Paginación -->
      <div class="px-5 py-4 border-t border-gray-200">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500">Mostrando</span>
            <select
              v-model="itemsPerPage"
              class="h-9 rounded-lg border border-gray-300 bg-white px-3 py-1.5 text-sm text-gray-700 focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-500/10"
            >
              <option :value="5">5</option>
              <option :value="10">10</option>
              <option :value="20">20</option>
              <option :value="50">50</option>
            </select>
            <span class="text-sm text-gray-500">de {{ filteredMuestras.length }} resultados</span>
          </div>
          <div class="flex items-center gap-2">
            <button
              @click="currentPage--"
              :disabled="currentPage === 1"
              class="inline-flex items-center px-3 py-1.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-brand-500/10 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Anterior
            </button>
            <span class="text-sm text-gray-500">
              Página {{ currentPage }} de {{ totalPages }}
            </span>
            <button
              @click="currentPage++"
              :disabled="currentPage === totalPages"
              class="inline-flex items-center px-3 py-1.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-brand-500/10 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'

// Estados para búsqueda y filtros
const searchQuery = ref('')
const selectedYear = ref('')
const selectedMonth = ref('')
const selectedAnalisis = ref('')
const selectedEstado = ref('')

// Estados para ordenamiento
const sortKey = ref('id')
const sortOrder = ref('asc')

// Estados para paginación
const currentPage = ref(1)
const itemsPerPage = ref(10)

// Estados para selección en lote
const selectedMuestras = ref([])
const accionEnLote = ref('')

// Estado para el modal de detalles
const muestraSeleccionada = ref(null)

// Definición de columnas
const columns = [
  { key: 'id', label: 'ID Muestra', class: 'w-2/11' },
  { key: 'paciente', label: 'Paciente', class: 'w-2/11' },
  { key: 'analisis', label: 'Tipo de Análisis', class: 'w-2/11' },
  { key: 'estado', label: 'Estado', class: 'w-2/11' },
  { key: 'fechaRecepcion', label: 'Fecha Recepción', class: 'w-2/11' },
  { key: 'acciones', label: 'Acciones', class: 'w-1/11' }
]

const muestras = ref([
  {
    id: 'M-2024-001',
    tipoMuestra: 'Sangre',
    paciente: 'Juan Pérez',
    dni: '12345678',
    analisis: 'Hemograma Completo',
    medico: 'Dr. García',
    estado: 'Completado',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '09:30'
  },
  {
    id: 'M-2024-002',
    tipoMuestra: 'Orina',
    paciente: 'María López',
    dni: '87654321',
    analisis: 'Uroanálisis',
    medico: 'Dra. Martínez',
    estado: 'En Proceso',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '10:15'
  },
  {
    id: 'M-2024-003',
    tipoMuestra: 'Heces',
    paciente: 'Carlos Ruiz',
    dni: '23456789',
    analisis: 'Coprológico',
    medico: 'Dr. Sánchez',
    estado: 'Pendiente',
    fechaRecepcion: '2024-02-15',
    horaRecepcion: '11:00'
  },
  {
    id: 'M-2024-004',
    tipoMuestra: 'Sangre',
    paciente: 'Ana Torres',
    dni: '34567890',
    analisis: 'Perfil Lipídico',
    medico: 'Dra. Rodríguez',
    estado: 'Validado',
    fechaRecepcion: '2024-01-10',
    horaRecepcion: '11:45'
  },
  {
    id: 'M-2023-005',
    tipoMuestra: 'Sangre',
    paciente: 'Roberto Díaz',
    dni: '45678901',
    analisis: 'Glucosa',
    medico: 'Dr. Fernández',
    estado: 'En Proceso',
    fechaRecepcion: '2023-12-05',
    horaRecepcion: '12:30'
  }
])

// Computed property para obtener años disponibles
const availableYears = computed(() => {
  const years = muestras.value.map(muestra => new Date(muestra.fechaRecepcion).getFullYear())
  return [...new Set(years)].sort((a, b) => b - a)
})

// Computed property para obtener meses disponibles para el año seleccionado
const availableMonths = computed(() => {
  if (!selectedYear.value) return []
  
  const months = [
    { value: '01', name: 'Enero' },
    { value: '02', name: 'Febrero' },
    { value: '03', name: 'Marzo' },
    { value: '04', name: 'Abril' },
    { value: '05', name: 'Mayo' },
    { value: '06', name: 'Junio' },
    { value: '07', name: 'Julio' },
    { value: '08', name: 'Agosto' },
    { value: '09', name: 'Septiembre' },
    { value: '10', name: 'Octubre' },
    { value: '11', name: 'Noviembre' },
    { value: '12', name: 'Diciembre' }
  ]
  
  // Filtrar meses que tienen muestras en el año seleccionado
  const availableMonthNumbers = muestras.value
    .filter(muestra => new Date(muestra.fechaRecepcion).getFullYear() == selectedYear.value)
    .map(muestra => new Date(muestra.fechaRecepcion).getMonth() + 1)
    .map(month => month.toString().padStart(2, '0'))
  
  const uniqueMonths = [...new Set(availableMonthNumbers)]
  
  return months.filter(month => uniqueMonths.includes(month.value))
})

// Watch para limpiar el mes cuando cambia el año
watch(selectedYear, () => {
  selectedMonth.value = ''
})

// Computed property para filtrar y ordenar las muestras
const filteredMuestras = computed(() => {
  let filtered = muestras.value
  
  // Filtrar por búsqueda de texto
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase().trim()
    filtered = filtered.filter(muestra => {
      return muestra.id.toLowerCase().includes(query) || 
             muestra.dni.toLowerCase().includes(query)
    })
  }
  
  // Filtrar por año
  if (selectedYear.value) {
    filtered = filtered.filter(muestra => {
      return new Date(muestra.fechaRecepcion).getFullYear() == selectedYear.value
    })
  }
  
  // Filtrar por mes
  if (selectedMonth.value) {
    filtered = filtered.filter(muestra => {
      const month = (new Date(muestra.fechaRecepcion).getMonth() + 1).toString().padStart(2, '0')
      return month === selectedMonth.value
    })
  }

  // Filtrar por tipo de análisis
  if (selectedAnalisis.value) {
    filtered = filtered.filter(muestra => muestra.analisis === selectedAnalisis.value)
  }

  // Filtrar por estado
  if (selectedEstado.value) {
    filtered = filtered.filter(muestra => muestra.estado === selectedEstado.value)
  }
  
  // Ordenar
  filtered.sort((a, b) => {
    let aValue = a[sortKey.value]
    let bValue = b[sortKey.value]

    if (sortKey.value === 'fechaRecepcion') {
      aValue = new Date(a.fechaRecepcion)
      bValue = new Date(b.fechaRecepcion)
    }

    if (aValue < bValue) return sortOrder.value === 'asc' ? -1 : 1
    if (aValue > bValue) return sortOrder.value === 'asc' ? 1 : -1
    return 0
  })
  
  return filtered
})

// Computed property para verificar si hay filtros activos
const hasActiveFilters = computed(() => {
  return searchQuery.value || selectedYear.value || selectedMonth.value || selectedAnalisis.value || selectedEstado.value
})

// Computed properties para paginación
const totalPages = computed(() => {
  return Math.ceil(filteredMuestras.value.length / itemsPerPage.value)
})

const paginatedMuestras = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredMuestras.value.slice(start, end)
})

// Computed property para selección en lote
const isAllSelected = computed(() => {
  return paginatedMuestras.value.length > 0 && 
         paginatedMuestras.value.every(m => selectedMuestras.value.includes(m.id))
})

// Funciones para selección en lote
const toggleSelectAll = () => {
  if (isAllSelected.value) {
    selectedMuestras.value = selectedMuestras.value.filter(
      id => !paginatedMuestras.value.some(m => m.id === id)
    )
  } else {
    const newSelected = paginatedMuestras.value.map(m => m.id)
    selectedMuestras.value = [...new Set([...selectedMuestras.value, ...newSelected])]
  }
}

const toggleSelect = (id) => {
  const index = selectedMuestras.value.indexOf(id)
  if (index === -1) {
    selectedMuestras.value.push(id)
  } else {
    selectedMuestras.value.splice(index, 1)
  }
}

// Función para aplicar acción en lote
const aplicarAccionEnLote = () => {
  if (!accionEnLote.value) return

  muestras.value = muestras.value.map(muestra => {
    if (selectedMuestras.value.includes(muestra.id)) {
      return { ...muestra, estado: accionEnLote.value }
    }
    return muestra
  })

  selectedMuestras.value = []
  accionEnLote.value = ''
}

// Función para ordenar
const sortBy = (key) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

// Watch para resetear la página cuando cambian los filtros
watch([searchQuery, selectedYear, selectedMonth, selectedAnalisis, selectedEstado], () => {
  currentPage.value = 1
})

// Watch para resetear la página cuando cambia el número de items por página
watch(itemsPerPage, () => {
  currentPage.value = 1
})

// Función para limpiar todos los filtros
const clearAllFilters = () => {
  searchQuery.value = ''
  selectedYear.value = ''
  selectedMonth.value = ''
  selectedAnalisis.value = ''
  selectedEstado.value = ''
  currentPage.value = 1
}

// Función para resaltar texto coincidente
const highlightText = (text, query) => {
  if (!query) return text
  
  const regex = new RegExp(`(${query})`, 'gi')
  return text.replace(regex, '<mark class="bg-yellow-200 px-1 rounded">$1</mark>')
}

// Función para formatear fecha
const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}

// Función para mostrar los detalles de la muestra
const mostrarDetallesMuestra = (muestra) => {
  muestraSeleccionada.value = muestra
}

const router = useRouter()

// Función para editar la muestra
const editarMuestra = (muestra) => {
  router.push(`/editar-muestra/${muestra.id}`)
  muestraSeleccionada.value = null
}
</script>

<style scoped>
/* Estilos para el highlight */
:deep(mark) {
  background-color: rgb(254 240 138);
  padding: 0.125rem 0.25rem;
  border-radius: 0.25rem;
}

/* Custom scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  height: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

/* Estilos para el ordenamiento */
.sort-icon {
  transition: transform 0.2s ease-in-out;
}

.sort-icon.rotate {
  transform: rotate(180deg);
}

/* Estilos para el scroll del modal */
.modal-content {
  scrollbar-width: thin;
  scrollbar-color: #cbd5e1 #f1f5f9;
}

.modal-content::-webkit-scrollbar {
  width: 8px;
}

.modal-content::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.modal-content::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}

.modal-content::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
</style>