<template>
  <div class="space-y-6">
    <!-- Selector de mes y año -->
    <div class="mb-6 flex flex-col sm:flex-row sm:items-center sm:space-x-6 space-y-2 sm:space-y-0">
      <label for="mes" class="font-medium text-gray-700 min-w-[140px]">Selecciona un mes:</label>
      <select 
        v-model="selectedMonth" 
        id="mes" 
        class="border rounded px-4 py-2 focus:ring focus:border-brand-500 w-full sm:w-auto"
        :class="{ 'border-red-500': showMonthError }"
      >
        <option disabled value="">-- Elige un mes --</option>
        <option v-for="(month, idx) in monthsFull" :key="month" :value="idx">{{ month }}</option>
      </select>
      <label for="anio" class="font-medium text-gray-700 min-w-[100px] ml-0 sm:ml-4">Año:</label>
      <select 
        v-model="selectedYear" 
        id="anio" 
        class="border rounded px-4 py-2 focus:ring focus:border-brand-500 w-full sm:w-auto"
      >
        <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
      </select>
      <div class="flex space-x-2 ml-0 sm:ml-4 mt-2 sm:mt-0">
        <button 
          @click="generateReport" 
          class="inline-flex items-center px-6 py-2 bg-brand-500 hover:bg-brand-600 text-white font-semibold rounded-lg shadow transition-colors"
          :disabled="isLoading"
          title="Generar informe con los datos seleccionados"
        >
          <svg v-if="!isLoading" class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          <svg v-else class="animate-spin h-5 w-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ isLoading ? 'Generando...' : 'Generar' }}
        </button>
        <button 
          v-if="showReport"
          @click="clearSelection" 
          class="inline-flex items-center px-6 py-2 bg-gray-500 hover:bg-gray-600 text-white font-semibold rounded-lg shadow transition-colors"
          title="Limpiar selección y volver a empezar"
        >
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
          Limpiar
        </button>
      </div>
    </div>

    <!-- Mensaje de error -->
    <div v-if="showMonthError" class="text-red-500 text-sm mt-1 mb-4">
      Por favor, selecciona un mes para generar el informe
    </div>

    <!-- Tabla de entidades por pacientes -->
    <div v-if="showReport" class="overflow-x-auto mt-6">
      <div class="mb-4">
        <h2 class="text-xl font-bold text-brand-700 mb-2">Pacientes por entidad - {{ selectedMonth !== null ? monthsFull[selectedMonth] : '' }} {{ selectedYear }}</h2>
      </div>

      <!-- Gráfico de barras -->
      <div class="mb-8 bg-white p-4 rounded-lg shadow-sm">
        <apexchart
          type="bar"
          height="350"
          :options="chartOptions"
          :series="series"
        />
      </div>

      <table class="w-full min-w-[400px] border border-gray-200 rounded-lg shadow-sm bg-white">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Entidad</th>
            <th class="px-6 py-3 text-right text-sm font-semibold text-gray-700">Ambulatorios</th>
            <th class="px-6 py-3 text-right text-sm font-semibold text-gray-700">Hospitalizados</th>
            <th class="px-6 py-3 text-right text-sm font-semibold text-gray-700">Total</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entidad in entidadesMesSeleccionado" :key="entidad.nombre" class="even:bg-gray-50">
            <td class="px-6 py-3">{{ entidad.nombre }}</td>
            <td class="px-6 py-3 text-right">{{ entidad.ambulatorios }}</td>
            <td class="px-6 py-3 text-right">{{ entidad.hospitalizados }}</td>
            <td class="px-6 py-3 text-right font-semibold">{{ entidad.ambulatorios + entidad.hospitalizados }}</td>
          </tr>
        </tbody>
        <tfoot>
          <tr class="bg-brand-50 font-bold">
            <td class="px-6 py-3">Total</td>
            <td class="px-6 py-3 text-right">{{ totalAmbulatoriosMes }}</td>
            <td class="px-6 py-3 text-right">{{ totalHospitalizadosMes }}</td>
            <td class="px-6 py-3 text-right">{{ totalPacientesMes }}</td>
          </tr>
        </tfoot>
      </table>
      <!-- Botón de imprimir al final -->
      <div class="flex justify-end mt-8 print:hidden">
        <button @click="imprimir" class="inline-flex items-center px-6 py-2 bg-brand-500 hover:bg-brand-600 text-white font-semibold rounded-lg shadow transition-colors">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2V9a2 2 0 012-2h16a2 2 0 012 2v7a2 2 0 01-2 2h-2m-6 0v4m0 0h4m-4 0H8" />
          </svg>
          Imprimir
        </button>
      </div>
    </div>

    <!-- Bloque de impresión personalizado -->
    <div v-if="selectedMonth !== null" class="hidden print:block print:bg-white print:p-8 print:mx-auto print:w-full print:max-w-3xl">
      <div class="flex items-center justify-between mb-6">
        <img src="/public/images/logo/Baner-udea.png" alt="Logo" class="h-12" style="max-height:48px;max-width:180px;object-fit:contain;" />
        <div class="text-center flex-1">
          <span class="text-lg font-bold block">INFORME MENSUAL DE PACIENTES</span>
          <span class="text-base font-semibold block mt-1">{{ monthsFull[selectedMonth] }} {{ selectedYear }}</span>
        </div>
        <span class="text-sm text-gray-600">{{ new Date().toLocaleDateString() }}</span>
      </div>
      <table class="w-full border border-gray-300 rounded-lg bg-white text-sm">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-4 py-2 text-left font-semibold">Entidad</th>
            <th class="px-4 py-2 text-right font-semibold">Ambulatorios</th>
            <th class="px-4 py-2 text-right font-semibold">Hospitalizados</th>
            <th class="px-4 py-2 text-right font-semibold">Total</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entidad in entidadesMesSeleccionado" :key="entidad.nombre" class="even:bg-gray-50">
            <td class="px-4 py-2">{{ entidad.nombre }}</td>
            <td class="px-4 py-2 text-right">{{ entidad.ambulatorios }}</td>
            <td class="px-4 py-2 text-right">{{ entidad.hospitalizados }}</td>
            <td class="px-4 py-2 text-right font-semibold">{{ entidad.ambulatorios + entidad.hospitalizados }}</td>
          </tr>
        </tbody>
        <tfoot>
          <tr class="bg-brand-50 font-bold">
            <td class="px-4 py-2">Total</td>
            <td class="px-4 py-2 text-right">{{ totalAmbulatoriosMes }}</td>
            <td class="px-4 py-2 text-right">{{ totalHospitalizadosMes }}</td>
            <td class="px-4 py-2 text-right">{{ totalPacientesMes }}</td>
          </tr>
        </tfoot>
      </table>
      <div class="mt-8 text-xs text-gray-500 text-right">
        Generado por el sistema - {{ new Date().toLocaleString() }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Importaciones necesarias de Vue y ApexCharts
import { ref, computed } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

// Nombres completos de los meses
const monthsFull = [
  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre',
] as const

// Selector de años (últimos 5 años)
const currentYear = new Date().getFullYear()
const years = Array.from({ length: 5 }, (_, i) => currentYear - i)
const selectedYear = ref(currentYear)

// Simulación de datos de entidades y pacientes por mes, diferenciando ambulatorios y hospitalizados
interface EntidadMes {
  nombre: string
  ambulatorios: number
  hospitalizados: number
}

const entidadesPorMes: EntidadMes[][] = [
  // Enero
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 45, hospitalizados: 32 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 38, hospitalizados: 28 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 22, hospitalizados: 18 },
    { nombre: 'Clínica León XIII', ambulatorios: 31, hospitalizados: 24 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 15, hospitalizados: 12 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 18, hospitalizados: 14 },
    { nombre: 'Hospital La María', ambulatorios: 25, hospitalizados: 19 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 35, hospitalizados: 27 },
  ],
  // Febrero
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 52, hospitalizados: 38 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 41, hospitalizados: 31 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 28, hospitalizados: 22 },
    { nombre: 'Clínica León XIII', ambulatorios: 34, hospitalizados: 26 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 18, hospitalizados: 15 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 21, hospitalizados: 17 },
    { nombre: 'Hospital La María', ambulatorios: 29, hospitalizados: 23 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 39, hospitalizados: 30 },
  ],
  // Marzo
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 48, hospitalizados: 35 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 36, hospitalizados: 29 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 25, hospitalizados: 20 },
    { nombre: 'Clínica León XIII', ambulatorios: 29, hospitalizados: 23 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 16, hospitalizados: 13 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 19, hospitalizados: 15 },
    { nombre: 'Hospital La María', ambulatorios: 27, hospitalizados: 21 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 33, hospitalizados: 26 },
  ],
  // Abril
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 55, hospitalizados: 42 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 44, hospitalizados: 35 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 32, hospitalizados: 25 },
    { nombre: 'Clínica León XIII', ambulatorios: 37, hospitalizados: 29 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 20, hospitalizados: 16 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 24, hospitalizados: 19 },
    { nombre: 'Hospital La María', ambulatorios: 31, hospitalizados: 25 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 42, hospitalizados: 33 },
  ],
  // Mayo
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 41, hospitalizados: 33 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 33, hospitalizados: 26 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 19, hospitalizados: 16 },
    { nombre: 'Clínica León XIII', ambulatorios: 26, hospitalizados: 21 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 13, hospitalizados: 11 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 16, hospitalizados: 13 },
    { nombre: 'Hospital La María', ambulatorios: 23, hospitalizados: 18 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 29, hospitalizados: 24 },
  ],
  // Junio
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 49, hospitalizados: 37 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 40, hospitalizados: 32 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 27, hospitalizados: 21 },
    { nombre: 'Clínica León XIII', ambulatorios: 33, hospitalizados: 26 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 17, hospitalizados: 14 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 22, hospitalizados: 18 },
    { nombre: 'Hospital La María', ambulatorios: 28, hospitalizados: 22 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 37, hospitalizados: 29 },
  ],
  // Julio
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 58, hospitalizados: 45 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 47, hospitalizados: 38 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 35, hospitalizados: 28 },
    { nombre: 'Clínica León XIII', ambulatorios: 40, hospitalizados: 32 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 23, hospitalizados: 19 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 27, hospitalizados: 22 },
    { nombre: 'Hospital La María', ambulatorios: 34, hospitalizados: 27 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 45, hospitalizados: 36 },
  ],
  // Agosto
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 38, hospitalizados: 30 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 31, hospitalizados: 25 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 18, hospitalizados: 15 },
    { nombre: 'Clínica León XIII', ambulatorios: 24, hospitalizados: 19 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 12, hospitalizados: 10 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 15, hospitalizados: 12 },
    { nombre: 'Hospital La María', ambulatorios: 21, hospitalizados: 17 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 27, hospitalizados: 22 },
  ],
  // Septiembre
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 43, hospitalizados: 34 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 35, hospitalizados: 28 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 23, hospitalizados: 18 },
    { nombre: 'Clínica León XIII', ambulatorios: 28, hospitalizados: 22 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 15, hospitalizados: 12 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 18, hospitalizados: 14 },
    { nombre: 'Hospital La María', ambulatorios: 25, hospitalizados: 20 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 31, hospitalizados: 25 },
  ],
  // Octubre
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 61, hospitalizados: 48 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 50, hospitalizados: 40 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 38, hospitalizados: 30 },
    { nombre: 'Clínica León XIII', ambulatorios: 43, hospitalizados: 34 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 26, hospitalizados: 21 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 30, hospitalizados: 24 },
    { nombre: 'Hospital La María', ambulatorios: 37, hospitalizados: 29 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 48, hospitalizados: 38 },
  ],
  // Noviembre
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 54, hospitalizados: 41 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 43, hospitalizados: 34 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 31, hospitalizados: 24 },
    { nombre: 'Clínica León XIII', ambulatorios: 36, hospitalizados: 28 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 21, hospitalizados: 17 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 25, hospitalizados: 20 },
    { nombre: 'Hospital La María', ambulatorios: 32, hospitalizados: 25 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 40, hospitalizados: 32 },
  ],
  // Diciembre
  [
    { nombre: 'Hospital Universitario San Vicente Fundación', ambulatorios: 47, hospitalizados: 36 },
    { nombre: 'IPS Universitaria Sede Medellín', ambulatorios: 37, hospitalizados: 29 },
    { nombre: 'Hospital San Juan de Dios', ambulatorios: 24, hospitalizados: 19 },
    { nombre: 'Clínica León XIII', ambulatorios: 30, hospitalizados: 23 },
    { nombre: 'Hospital Mental de Antioquia', ambulatorios: 17, hospitalizados: 14 },
    { nombre: 'ESE Hospital Marco Fidel Suárez', ambulatorios: 20, hospitalizados: 16 },
    { nombre: 'Hospital La María', ambulatorios: 26, hospitalizados: 21 },
    { nombre: 'Clínica Universitaria Bolivariana', ambulatorios: 34, hospitalizados: 27 },
  ],
]

const selectedMonth = ref<number | null>(null)
const showReport = ref(false)
const isLoading = ref(false)
const showMonthError = ref(false)

const entidadesMesSeleccionado = computed(() => {
  if (selectedMonth.value === null) return []
  return entidadesPorMes[selectedMonth.value]
})

const totalAmbulatoriosMes = computed(() =>
  entidadesMesSeleccionado.value.reduce((acc, entidad) => acc + entidad.ambulatorios, 0)
)
const totalHospitalizadosMes = computed(() =>
  entidadesMesSeleccionado.value.reduce((acc, entidad) => acc + entidad.hospitalizados, 0)
)
const totalPacientesMes = computed(() => totalAmbulatoriosMes.value + totalHospitalizadosMes.value)

const generateReport = async () => {
  if (selectedMonth.value === null) {
    showMonthError.value = true
    return
  }
  
  showMonthError.value = false
  isLoading.value = true
  
  try {
    // Simulamos una carga para mostrar el estado de carga
    await new Promise(resolve => setTimeout(resolve, 1000))
    showReport.value = true
  } catch (error) {
    console.error('Error al generar el informe:', error)
    alert('Hubo un error al generar el informe. Por favor, intenta de nuevo.')
  } finally {
    isLoading.value = false
  }
}

const clearSelection = () => {
  selectedMonth.value = null
  showReport.value = false
  showMonthError.value = false
}

const imprimir = () => {
  // Verificar que se haya seleccionado un mes
  if (selectedMonth.value === null) {
    alert('Por favor seleccione un mes antes de imprimir.');
    return;
  }

  // Crear una nueva ventana para la impresión
  const printWindow = window.open('', '_blank');
  
  if (!printWindow) {
    alert('No se pudo abrir la ventana de impresión. Verifique que no esté bloqueada por el navegador.');
    return;
  }

  // Obtener los datos actuales
  const mesSeleccionado = monthsFull[selectedMonth.value];
  const entidades = entidadesMesSeleccionado.value;
  const totalAmb = totalAmbulatoriosMes.value;
  const totalHosp = totalHospitalizadosMes.value;
  const totalPac = totalPacientesMes.value;
  const fechaActual = new Date();

  // Generar las filas de la tabla
  const filasEntidades = entidades.map(entidad => `
    <tr>
      <td>${entidad.nombre}</td>
      <td>${entidad.ambulatorios}</td>
      <td>${entidad.hospitalizados}</td>
      <td>${entidad.ambulatorios + entidad.hospitalizados}</td>
    </tr>
  `).join('');

  // HTML completo para la ventana de impresión
  const printHTML = `
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Informe Mensual de Pacientes - ${mesSeleccionado} ${selectedYear}</title>
      <style>
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }
        
        body {
          font-family: Arial, sans-serif;
          background: white;
          color: #333;
          line-height: 1.4;
          padding: 20px;
        }
        
        .header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          margin-bottom: 30px;
          padding-bottom: 20px;
          border-bottom: 2px solid #ddd;
        }
        
        .logo {
          height: 48px;
          max-width: 180px;
          object-fit: contain;
        }
        
        .title-section {
          flex: 1;
          text-align: center;
        }
        
        .title {
          font-size: 18px;
          font-weight: bold;
          color: #333;
          margin-bottom: 5px;
        }
        
        .subtitle {
          font-size: 16px;
          font-weight: 600;
          color: #666;
        }
        
        .date {
          font-size: 12px;
          color: #666;
          white-space: nowrap;
        }
        
        table {
          width: 100%;
          border-collapse: collapse;
          margin: 20px 0;
          font-size: 14px;
        }
        
        th, td {
          border: 1px solid #333;
          padding: 8px 12px;
          text-align: left;
        }
        
        th {
          background-color: #f5f5f5;
          font-weight: bold;
          text-align: center;
        }
        
        td:nth-child(2), td:nth-child(3), td:nth-child(4),
        th:nth-child(2), th:nth-child(3), th:nth-child(4) {
          text-align: right;
        }
        
        tbody tr:nth-child(even) {
          background-color: #f9f9f9;
        }
        
        tfoot tr {
          background-color: #e8f4fd;
          font-weight: bold;
        }
        
        .footer {
          margin-top: 30px;
          text-align: right;
          font-size: 10px;
          color: #666;
        }
        
        @media print {
          body { padding: 0; }
          @page { margin: 15mm; }
        }
      </style>
    </head>
    <body>
      <div class="header">
        <img src="/images/logo/Baner-udea.png" alt="Logo Universidad de Antioquia" class="logo" />
        <div class="title-section">
          <div class="title">INFORME MENSUAL DE PACIENTES</div>
          <div class="subtitle">${mesSeleccionado} ${selectedYear}</div>
        </div>
        <div class="date">${fechaActual.toLocaleDateString()}</div>
      </div>
      
      <table>
        <thead>
          <tr>
            <th>Entidad</th>
            <th>Ambulatorios</th>
            <th>Hospitalizados</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          ${filasEntidades}
        </tbody>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>${totalAmb}</td>
            <td>${totalHosp}</td>
            <td>${totalPac}</td>
          </tr>
        </tfoot>
      </table>
      
      <div class="footer">
        Generado por el sistema - ${fechaActual.toLocaleString()}
      </div>
    </body>
    </html>
  `;

  // Escribir el contenido en la nueva ventana
  printWindow.document.write(printHTML);
  printWindow.document.close();
  
  // Esperar a que se cargue completamente y luego imprimir
  printWindow.onload = () => {
    setTimeout(() => {
      printWindow.print();
      printWindow.close();
    }, 500);
  };
}

// Configuración del gráfico
const chartOptions = computed(() => ({
  chart: {
    type: 'bar',
    height: 350,
    toolbar: {
      show: false
    }
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '55%',
      endingShape: 'rounded'
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent']
  },
  xaxis: {
    categories: entidadesMesSeleccionado.value.map(entidad => entidad.nombre),
    labels: {
      rotate: -45,
      style: {
        fontSize: '12px'
      }
    }
  },
  yaxis: {
    title: {
      text: 'Número de Pacientes'
    }
  },
  fill: {
    opacity: 1,
    colors: ['#2974A3', '#064D5F']
  },
  tooltip: {
    y: {
      formatter: function (val: number) {
        return val + " pacientes"
      }
    }
  },
  legend: {
    position: 'top'
  }
}))

const series = computed(() => [
  {
    name: 'Ambulatorios',
    data: entidadesMesSeleccionado.value.map(entidad => entidad.ambulatorios)
  },
  {
    name: 'Hospitalizados',
    data: entidadesMesSeleccionado.value.map(entidad => entidad.hospitalizados)
  }
])
</script>

<style scoped>
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #2974A3 #f3f4f6;
}

.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #2974A3;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #064D5F;
}

@media print {
  .print\:hidden { display: none !important; }
  .print\:block { display: block !important; }
  
  /* Reset de página para impresión */
  * {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  
  @page {
    margin: 20mm;
    size: A4;
  }
  
  body, html {
    background: #fff !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 100vw !important;
    min-width: 0 !important;
    max-width: 100vw !important;
    overflow: visible !important;
    font-size: 12pt !important;
    line-height: 1.3 !important;
  }
  
  /* Oculta completamente el sidebar usando múltiples selectores */
  aside, 
  nav, 
  header,
  .min-h-screen.xl\\:flex > aside,
  .min-h-screen.xl\\:flex > div:first-child,
  [class*="sidebar"],
  [class*="panel-lateral"],
  [class*="app-sidebar"],
  .fixed.mt-16,
  .fixed.top-0.left-0,
  div[class*="w-\\[290px\\]"],
  div[class*="w-\\[90px\\]"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  
  /* Oculta el header/panel superior */
  .sticky.top-0,
  [class*="panel-superior"],
  [class*="app-header"],
  .border-gray-200.z-99999,
  .bg-white.border-gray-200.z-99999 {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  
  /* Oculta el backdrop */
  [class*="fixed inset-0"][class*="bg-gray-900"] {
    display: none !important;
  }
  
  /* Ajusta el contenido principal para ocupar toda la página */
  .flex-1,
  .flex-1.transition-all,
  main,
  main[role="main"] {
    margin: 0 !important;
    padding: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
    background: #fff !important;
  }
  
  /* Elimina márgenes de layout */
  [class*="lg:ml-[290px]"],
  [class*="lg:ml-[90px]"] {
    margin-left: 0 !important;
  }
  
  /* Oculta elementos de navegación y utilidades */
  .custom-scrollbar, 
  .no-print, 
  button:not([class*="print:block"] button),
  .animate-fadeIn,
  .transition-all,
  [class*="z-99999"] {
    display: none !important;
  }
  
  /* Elimina padding/margin innecesarios */
  .space-y-6, 
  .overflow-x-auto, 
  .mt-6, 
  .mb-4, 
  .p-4,
  .md\\:p-6 {
    margin: 0 !important;
    padding: 0 !important;
  }
  
  /* Ajusta la tabla para impresión */
  table {
    width: 100% !important;
    max-width: 100vw !important;
    min-width: 0 !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    background: #fff !important;
    margin: 0 !important;
    page-break-inside: avoid !important;
    font-size: 13px !important;
  }
  
  th, td {
    padding: 6px 8px !important;
    font-size: 13px !important;
    background: #fff !important;
    color: #222 !important;
  }
  
  .bg-gray-50, .bg-gray-100, .bg-brand-50 {
    background: #fff !important;
  }
  
  /* Elimina cualquier borde visual extra */
  .border, .border-gray-200, .border-gray-300 {
    border-color: #222 !important;
    border-width: 1px !important;
  }
  
  /* Ocultar el gráfico en la impresión */
  .apexcharts-canvas {
    display: none !important;
  }
}

/* Estilos para el gráfico */
:deep(.apexcharts-tooltip) {
  background: #fff;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

:deep(.apexcharts-tooltip-title) {
  background: #f8f9fa;
  border-bottom: 1px solid #ddd;
  font-weight: 600;
}

:deep(.apexcharts-legend-text) {
  font-size: 12px;
  font-weight: 500;
}

:deep(.apexcharts-xaxis-label) {
  font-size: 11px;
}
</style>
