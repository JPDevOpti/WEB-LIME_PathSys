<!--
  Componente MuestrasUrgentes
  Tabla interactiva que muestra las muestras médicas urgentes del sistema.
  Permite filtrar por especialista, ordenar por columnas y exportar a CSV.
  Incluye estados visuales, soporte para tema oscuro y diseño responsive.
-->
<template>
  <div
    class="overflow-hidden rounded-2xl border border-gray-200 bg-white px-4 pb-3 pt-4 transition-all duration-300 hover:shadow-lg dark:border-gray-800 dark:bg-white/[0.03] sm:px-6"
  >
    <!-- Encabezado con título y filtro de especialista -->
    <div class="flex flex-col gap-2 mb-4 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <h3 class="text-lg font-semibold text-gray-800 dark:text-white/90">Muestras Urgentes</h3>
        <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">Total: {{ muestrasUrgentes.length }} muestras</p>
      </div>
      <!-- Selector de especialista -->
      <div class="w-full sm:w-auto relative">
        <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1.5">
          Especialista
        </label>
        <select
          v-model="especialistaSeleccionado"
          class="h-11 w-full sm:w-40 appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 pr-11 text-sm text-gray-800 shadow-theme-xs transition-all duration-300 hover:border-primary-500 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:text-gray-300 dark:hover:border-primary-400"
        >
          <option value="">Todos</option>
          <option v-for="especialista in especialistasUnicos" :key="especialista" :value="especialista">
            {{ especialista }}
          </option>
        </select>
        <!-- Icono del selector -->
        <div class="absolute inset-y-0 right-0 top-7 flex items-center pr-3 pointer-events-none">
          <svg class="h-5 w-5 text-gray-400 transition-colors duration-300 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </div>
    </div>

    <!-- Tabla de muestras con scroll horizontal -->
    <div class="max-w-full overflow-x-auto custom-scrollbar">
      <table class="min-w-full">
        <!-- Encabezados de columna con ordenamiento -->
        <thead>
          <tr class="border-t border-gray-100 dark:border-gray-800">
            <th 
              v-for="columna in columnas" 
              :key="columna.campo"
              class="py-3 text-left cursor-pointer transition-colors duration-300 hover:bg-gray-50 dark:hover:bg-gray-800/50"
              @click="ordenarPor(columna.campo)"
            >
              <p class="font-medium text-gray-500 text-theme-xs flex items-center gap-1">
                {{ columna.titulo }}
                <span v-if="ordenCampo === columna.campo" class="transition-transform duration-300">
                  {{ ordenAsc ? '▲' : '▼' }}
                </span>
              </p>
            </th>
          </tr>
        </thead>
        <!-- Cuerpo de la tabla con datos de muestras -->
        <tbody>
          <tr
            v-for="(muestra, index) in muestrasUrgentes"
            :key="index"
            class="border-t border-gray-100 transition-all duration-300 hover:bg-gray-50 dark:border-gray-800 dark:hover:bg-gray-800/50"
          >
            <!-- ID y tipo de muestra -->
            <td class="py-3 whitespace-nowrap">
              <div class="flex items-center gap-3">
                <div class="h-[50px] w-[50px] flex items-center justify-center bg-blue-50 rounded-md transition-colors duration-300 group-hover:bg-blue-100 dark:bg-blue-900/20 dark:group-hover:bg-blue-900/30">
                  <svg
                    class="w-8 h-8 text-brand-700 transition-colors duration-300 dark:text-blue-400"
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
                  <p class="font-medium text-gray-800 text-theme-sm dark:text-white/90">
                    {{ muestra.id }}
                  </p>
                  <span class="text-gray-500 text-theme-xs dark:text-gray-400">{{ muestra.tipoMuestra }}</span>
                </div>
              </div>
            </td>
            <!-- Datos del paciente -->
            <td class="py-3 whitespace-nowrap">
              <div>
                <p class="font-medium text-gray-800 text-theme-sm dark:text-white/90">{{ muestra.paciente }}</p>
                <span class="text-gray-500 text-theme-xs dark:text-gray-400">{{ muestra.dni }}</span>
              </div>
            </td>
            <!-- Tipo de análisis -->
            <td class="py-3 whitespace-nowrap">
              <div>
                <p class="text-gray-800 text-theme-sm dark:text-white/90">{{ muestra.analisis }}</p>
              </div>
            </td>
            <!-- Especialista -->
            <td class="py-3 whitespace-nowrap">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ muestra.medico }}</p>
            </td>
            <!-- Fecha de ingreso -->
            <td class="py-3 whitespace-nowrap">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ muestra.fechaIngreso }}</p>
            </td>
            <!-- Días en el sistema -->
            <td class="py-3 whitespace-nowrap">
              <p class="text-gray-500 text-theme-sm dark:text-gray-400">{{ calcularDiasEnSistema(muestra.fechaIngreso) }}</p>
            </td>
            <!-- Estado con indicador visual -->
            <td class="py-3 whitespace-nowrap">
              <span
                :class="{
                  'rounded-full px-2 py-0.5 text-theme-xs font-medium transition-all duration-300': true,
                  'bg-success-50 text-success-600 dark:bg-success-500/15 dark:text-success-500': muestra.estado === 'Completado',
                  'bg-warning-50 text-warning-600 dark:bg-warning-500/15 dark:text-warning-500': muestra.estado === 'En Proceso',
                  'bg-blue-50 text-blue-600 dark:bg-blue-500/15 dark:text-blue-500': muestra.estado === 'Validado',
                  'bg-error-50 text-error-600 dark:bg-error-500/15 dark:text-error-500': muestra.estado === 'Pendiente',
                  'bg-red-100 text-red-700 dark:bg-red-500/15 dark:text-red-500 animate-pulse': muestra.estado === 'Urgente',
                }"
              >
                {{ muestra.estado }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pie de tabla con contador y botón de exportación -->
    <div class="flex items-center justify-between mt-4">
      <div class="text-sm text-gray-500 dark:text-gray-400">
        Mostrando {{ muestrasUrgentes.length }} de {{ muestrasUrgentes.length }} resultados
      </div>
      <div class="flex gap-2">
        <button
          class="px-3 py-1 text-sm font-medium text-gray-700 transition-colors duration-300 rounded-lg hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800"
          @click="exportarCSV"
        >
          Exportar CSV
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// Datos de ejemplo de muestras médicas
const muestras = ref([
  {
    id: 'M-2024-108',
    tipoMuestra: 'Sangre',
    paciente: 'María García',
    dni: '12345678',
    analisis: 'Hemograma Completo',
    medico: 'Dr. López',
    fecha: '2024-03-21',
    estado: 'Completado',
    fechaIngreso: '2024-03-19',
  },
  {
    id: 'M-2024-109',
    tipoMuestra: 'Orina',
    paciente: 'Juan Rodríguez',
    dni: '87654321',
    analisis: 'Uroanálisis',
    medico: 'Dra. Martínez',
    fecha: '2024-03-21',
    estado: 'Urgente',
    fechaIngreso: '2024-03-20',
  },
  {
    id: 'M-2024-110',
    tipoMuestra: 'Sangre',
    paciente: 'Ana Torres',
    dni: '23456789',
    analisis: 'Perfil Lipídico',
    medico: 'Dr. Fernández',
    fecha: '2024-03-21',
    estado: 'Validado',
    fechaIngreso: '2024-03-21',
  },
  {
    id: 'M-2024-111',
    tipoMuestra: 'Heces',
    paciente: 'Carlos Mendez',
    dni: '34567890',
    analisis: 'Coprológico',
    medico: 'Dra. Silva',
    fecha: '2024-03-21',
    estado: 'Urgente',
    fechaIngreso: '2024-03-18',
  },
  {
    id: 'M-2024-112',
    tipoMuestra: 'Sangre',
    paciente: 'Roberto Díaz',
    dni: '45678901',
    analisis: 'Glucosa en Ayunas',
    medico: 'Dr. Ramírez',
    fecha: '2024-03-21',
    estado: 'Completado',
    fechaIngreso: '2024-03-21',
  },
])

// Estado para ordenamiento y filtrado
const ordenCampo = ref('id')
const ordenAsc = ref(true)
const especialistaSeleccionado = ref('')

// Lista de especialistas únicos para el filtro
const especialistasUnicos = computed<string[]>(() => {
  const set = new Set<string>()
  muestras.value.forEach(m => {
    if (m.estado === 'Urgente') set.add(m.medico)
  })
  return Array.from(set)
})

// Función para ordenar la tabla por columna
type CampoOrdenable = 'id' | 'paciente' | 'analisis' | 'medico' | 'fechaIngreso' | 'diasSistema' | 'estado'

function ordenarPor(campo: CampoOrdenable, asc = true) {
  if (ordenCampo.value === campo) {
    ordenAsc.value = !ordenAsc.value
  } else {
    ordenCampo.value = campo
    ordenAsc.value = asc
  }
}

// Calcula los días que una muestra lleva en el sistema
function calcularDiasEnSistema(fechaIngreso: string) {
  const fechaIngresoDate = new Date(fechaIngreso)
  const hoy = new Date()
  const diffTime = hoy.getTime() - fechaIngresoDate.getTime()
  return Math.floor(diffTime / (1000 * 60 * 60 * 24))
}

// Muestras filtradas y ordenadas
const muestrasUrgentes = computed(() => {
  const arr = muestras.value.filter(m => m.estado === 'Urgente' &&
    (especialistaSeleccionado.value === '' || m.medico === especialistaSeleccionado.value))
  return arr.slice().sort((a, b) => {
    let aVal, bVal
    if (ordenCampo.value === 'diasSistema') {
      aVal = calcularDiasEnSistema(a.fechaIngreso)
      bVal = calcularDiasEnSistema(b.fechaIngreso)
    } else {
      aVal = a[ordenCampo.value as keyof Muestra]
      bVal = b[ordenCampo.value as keyof Muestra]
    }
    if (aVal == null) return 1
    if (bVal == null) return -1
    if (typeof aVal === 'string' && typeof bVal === 'string') {
      aVal = aVal.toLowerCase()
      bVal = bVal.toLowerCase()
    }
    if (aVal < bVal) return ordenAsc.value ? -1 : 1
    if (aVal > bVal) return ordenAsc.value ? 1 : -1
    return 0
  })
})

// Configuración de columnas de la tabla
const columnas: { campo: CampoOrdenable; titulo: string }[] = [
  { campo: 'id', titulo: 'ID Muestra' },
  { campo: 'paciente', titulo: 'Paciente' },
  { campo: 'analisis', titulo: 'Tipo de Análisis' },
  { campo: 'medico', titulo: 'Especialista' },
  { campo: 'fechaIngreso', titulo: 'Fecha de Ingreso' },
  { campo: 'diasSistema', titulo: 'Días en el sistema' },
  { campo: 'estado', titulo: 'Estado' }
]

// Función para exportar datos a CSV
function exportarCSV() {
  const headers = ['ID', 'Paciente', 'DNI', 'Análisis', 'Especialista', 'Fecha Ingreso', 'Días', 'Estado']
  const data = muestrasUrgentes.value.map(m => [
    m.id,
    m.paciente,
    m.dni,
    m.analisis,
    m.medico,
    m.fechaIngreso,
    calcularDiasEnSistema(m.fechaIngreso),
    m.estado
  ])
  
  const csvContent = [
    headers.join(','),
    ...data.map(row => row.join(','))
  ].join('\n')
  
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' })
  const link = document.createElement('a')
  link.href = URL.createObjectURL(blob)
  link.download = `muestras-urgentes-${new Date().toISOString().split('T')[0]}.csv`
  link.click()
}

interface Muestra {
  id: string
  tipoMuestra: string
  paciente: string
  dni: string
  analisis: string
  medico: string
  fecha: string
  estado: string
  fechaIngreso: string
}
</script>

<style scoped>
/* Animación de pulso para estados urgentes */
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Estilos personalizados para el scrollbar horizontal */
.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>