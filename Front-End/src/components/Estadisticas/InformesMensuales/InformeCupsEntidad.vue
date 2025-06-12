<template>
  <div class="space-y-6">
    <!-- Selector de mes, año y entidad -->
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
      <label for="entidad" class="font-medium text-gray-700 min-w-[100px] ml-0 sm:ml-4">Entidad:</label>
      <div class="w-full sm:w-[300px]">
        <ListaDesplegable
          v-model="selectedEntity"
          :options="entidades"
          placeholder="Buscar entidad..."
          :required="true"
          :error="showEntityError"
        />
      </div>
      <button 
        @click="generateReport" 
        class="inline-flex items-center px-6 py-2 bg-brand-500 hover:bg-brand-600 text-white font-semibold rounded-lg shadow transition-colors ml-0 sm:ml-2"
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
        class="inline-flex items-center px-6 py-2 bg-gray-500 hover:bg-gray-600 text-white font-semibold rounded-lg shadow transition-colors ml-0 sm:ml-2"
        title="Limpiar selección y volver a empezar"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
        </svg>
        Limpiar
      </button>
    </div>

    <div v-if="showEntityError" class="text-red-500 text-sm mt-1 mb-4">
      Por favor, selecciona una entidad
    </div>

    <!-- Tabla de CUPS por entidad -->
    <div v-if="showReport" class="overflow-x-auto mt-6">
      <div class="mb-4">
        <h2 class="text-xl font-bold text-brand-700 mb-2">CUPS por entidad - {{ selectedMonth !== null ? monthsFull[selectedMonth] : '' }} {{ selectedYear }}</h2>
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
            <th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">Código</th>
            <th class="px-6 py-3 text-left text-sm font-semibold text-gray-700">CUPS</th>
            <th class="px-6 py-3 text-right text-sm font-semibold text-gray-700">Cantidad</th>
            <th class="px-6 py-3 text-right text-sm font-semibold text-gray-700">Porcentaje</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cups in cupsPorEntidad" :key="cups.nombre" class="even:bg-gray-50">
            <td class="px-6 py-3">{{ cups.codigoCups }}</td>
            <td class="px-6 py-3">{{ cups.nombre }}</td>
            <td class="px-6 py-3 text-right">{{ cups.cantidad }}</td>
            <td class="px-6 py-3 text-right">{{ ((cups.cantidad / totalCups) * 100).toFixed(1) }}%</td>
          </tr>
        </tbody>
        <tfoot>
          <tr class="bg-brand-50 font-bold">
            <td class="px-6 py-3" colspan="2">Total</td>
            <td class="px-6 py-3 text-right">{{ totalCups }}</td>
            <td class="px-6 py-3 text-right">100%</td>
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
          <span class="text-lg font-bold block">INFORME MENSUAL DE PROCEDIMIENTOS ONCOLÓGICOS</span>
          <span class="text-base font-semibold block mt-1">{{ monthsFull[selectedMonth] }} {{ selectedYear }}</span>
        </div>
        <span class="text-sm text-gray-600">{{ new Date().toLocaleDateString() }}</span>
      </div>
      <table class="w-full border border-gray-300 rounded-lg bg-white text-sm">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-4 py-2 text-left font-semibold">Código</th>
            <th class="px-4 py-2 text-left font-semibold">CUPS</th>
            <th class="px-4 py-2 text-right font-semibold">Cantidad</th>
            <th class="px-4 py-2 text-right font-semibold">Porcentaje</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cups in cupsPorEntidad" :key="cups.nombre" class="even:bg-gray-50">
            <td class="px-4 py-2">{{ cups.codigoCups }}</td>
            <td class="px-4 py-2">{{ cups.nombre }}</td>
            <td class="px-4 py-2 text-right">{{ cups.cantidad }}</td>
            <td class="px-4 py-2 text-right">{{ ((cups.cantidad / totalCups) * 100).toFixed(1) }}%</td>
          </tr>
        </tbody>
        <tfoot>
          <tr class="bg-brand-50 font-bold">
            <td class="px-4 py-2" colspan="2">Total</td>
            <td class="px-4 py-2 text-right">{{ totalCups }}</td>
            <td class="px-4 py-2 text-right">100%</td>
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
import { ref, computed } from 'vue'
import VueApexCharts from 'vue3-apexcharts'
import ListaDesplegable from '@/components/ComponentesFormularios/ListaDesplegable.vue'

// Nombres completos de los meses
const monthsFull = [
  'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre',
] as const

// Selector de años (últimos 5 años)
const currentYear = new Date().getFullYear()
const years = Array.from({ length: 5 }, (_, i) => currentYear - i)
const selectedYear = ref(currentYear)

// Lista de entidades
const entidades = [
  { id: 1, nombre: 'Hospital Universitario San Vicente Fundación' },
  { id: 2, nombre: 'IPS Universitaria Sede Medellín' },
  { id: 3, nombre: 'Hospital San Juan de Dios' },
  { id: 4, nombre: 'Clínica León XIII' },
  { id: 5, nombre: 'Hospital Mental de Antioquia' },
  { id: 6, nombre: 'ESE Hospital Marco Fidel Suárez' },
  { id: 7, nombre: 'Hospital La María' },
  { id: 8, nombre: 'Clínica Universitaria Bolivariana' },
]

// Simulación de datos de CUPS por entidad y mes
interface CupsPorEntidad {
  nombre: string
  codigoCups: string
  cantidad: number
  porcentaje: number
}

const cupsPorEntidadMes: Record<string, CupsPorEntidad[][]> = {
  'Hospital Universitario San Vicente Fundación': [
    // Enero
    [
      { nombre: 'Consulta de oncología médica', codigoCups: '890101', cantidad: 85, porcentaje: 25 },
      { nombre: 'Consulta de oncología quirúrgica', codigoCups: '890102', cantidad: 65, porcentaje: 19 },
      { nombre: 'Consulta de radioterapia', codigoCups: '890103', cantidad: 45, porcentaje: 13 },
      { nombre: 'Quimioterapia', codigoCups: '890104', cantidad: 55, porcentaje: 16 },
      { nombre: 'Radioterapia', codigoCups: '890105', cantidad: 40, porcentaje: 12 },
      { nombre: 'Cirugía oncológica', codigoCups: '890106', cantidad: 30, porcentaje: 9 },
      { nombre: 'Procedimientos diagnósticos oncológicos', codigoCups: '890107', cantidad: 25, porcentaje: 7 },
      { nombre: 'Biopsia por aspiración con aguja fina (BAAF)', codigoCups: '890108', cantidad: 35, porcentaje: 10 },
      { nombre: 'Biopsia por punción con aguja gruesa', codigoCups: '890109', cantidad: 28, porcentaje: 8 },
      { nombre: 'Inmunohistoquímica', codigoCups: '890110', cantidad: 42, porcentaje: 12 },
      { nombre: 'Estudio molecular en tejido tumoral', codigoCups: '890111', cantidad: 15, porcentaje: 4 }
    ],
    // Febrero
    [
      { nombre: 'Consulta de oncología médica', codigoCups: '890101', cantidad: 90, porcentaje: 26 },
      { nombre: 'Consulta de oncología quirúrgica', codigoCups: '890102', cantidad: 70, porcentaje: 20 },
      { nombre: 'Consulta de radioterapia', codigoCups: '890103', cantidad: 45, porcentaje: 13 },
      { nombre: 'Quimioterapia', codigoCups: '890104', cantidad: 60, porcentaje: 17 },
      { nombre: 'Radioterapia', codigoCups: '890105', cantidad: 35, porcentaje: 10 },
      { nombre: 'Cirugía oncológica', codigoCups: '890106', cantidad: 25, porcentaje: 7 },
      { nombre: 'Procedimientos diagnósticos oncológicos', codigoCups: '890107', cantidad: 20, porcentaje: 6 },
      { nombre: 'Biopsia por aspiración con aguja fina (BAAF)', codigoCups: '890108', cantidad: 38, porcentaje: 11 },
      { nombre: 'Biopsia por punción con aguja gruesa', codigoCups: '890109', cantidad: 32, porcentaje: 9 },
      { nombre: 'Inmunohistoquímica', codigoCups: '890110', cantidad: 45, porcentaje: 13 },
      { nombre: 'Estudio molecular en tejido tumoral', codigoCups: '890111', cantidad: 18, porcentaje: 5 }
    ]
  ],
  'IPS Universitaria Sede Medellín': [
    // Enero
    [
      { nombre: 'Consulta de oncología médica', codigoCups: '890101', cantidad: 70, porcentaje: 24 },
      { nombre: 'Consulta de oncología quirúrgica', codigoCups: '890102', cantidad: 55, porcentaje: 19 },
      { nombre: 'Consulta de radioterapia', codigoCups: '890103', cantidad: 40, porcentaje: 14 },
      { nombre: 'Quimioterapia', codigoCups: '890104', cantidad: 45, porcentaje: 15 },
      { nombre: 'Radioterapia', codigoCups: '890105', cantidad: 35, porcentaje: 12 },
      { nombre: 'Cirugía oncológica', codigoCups: '890106', cantidad: 25, porcentaje: 9 },
      { nombre: 'Procedimientos diagnósticos oncológicos', codigoCups: '890107', cantidad: 20, porcentaje: 7 },
      { nombre: 'Biopsia por aspiración con aguja fina (BAAF)', codigoCups: '890108', cantidad: 30, porcentaje: 10 },
      { nombre: 'Biopsia por punción con aguja gruesa', codigoCups: '890109', cantidad: 25, porcentaje: 9 },
      { nombre: 'Inmunohistoquímica', codigoCups: '890110', cantidad: 35, porcentaje: 12 },
      { nombre: 'Estudio molecular en tejido tumoral', codigoCups: '890111', cantidad: 12, porcentaje: 4 }
    ],
    // Febrero
    [
      { nombre: 'Consulta de oncología médica', codigoCups: '890101', cantidad: 75, porcentaje: 25 },
      { nombre: 'Consulta de oncología quirúrgica', codigoCups: '890102', cantidad: 60, porcentaje: 20 },
      { nombre: 'Consulta de radioterapia', codigoCups: '890103', cantidad: 40, porcentaje: 13 },
      { nombre: 'Quimioterapia', codigoCups: '890104', cantidad: 50, porcentaje: 17 },
      { nombre: 'Radioterapia', codigoCups: '890105', cantidad: 30, porcentaje: 10 },
      { nombre: 'Cirugía oncológica', codigoCups: '890106', cantidad: 25, porcentaje: 8 },
      { nombre: 'Procedimientos diagnósticos oncológicos', codigoCups: '890107', cantidad: 20, porcentaje: 7 },
      { nombre: 'Biopsia por aspiración con aguja fina (BAAF)', codigoCups: '890108', cantidad: 32, porcentaje: 11 },
      { nombre: 'Biopsia por punción con aguja gruesa', codigoCups: '890109', cantidad: 28, porcentaje: 9 },
      { nombre: 'Inmunohistoquímica', codigoCups: '890110', cantidad: 38, porcentaje: 13 },
      { nombre: 'Estudio molecular en tejido tumoral', codigoCups: '890111', cantidad: 15, porcentaje: 5 }
    ]
  ],
  'Hospital San Juan de Dios': [
    // Enero
    [
      { nombre: 'Consulta de oncología médica', codigoCups: '890101', cantidad: 60, porcentaje: 23 },
      { nombre: 'Consulta de oncología quirúrgica', codigoCups: '890102', cantidad: 45, porcentaje: 17 },
      { nombre: 'Consulta de radioterapia', codigoCups: '890103', cantidad: 35, porcentaje: 13 },
      { nombre: 'Quimioterapia', codigoCups: '890104', cantidad: 40, porcentaje: 15 },
      { nombre: 'Radioterapia', codigoCups: '890105', cantidad: 30, porcentaje: 11 },
      { nombre: 'Cirugía oncológica', codigoCups: '890106', cantidad: 25, porcentaje: 10 },
      { nombre: 'Procedimientos diagnósticos oncológicos', codigoCups: '890107', cantidad: 20, porcentaje: 8 },
      { nombre: 'Biopsia por aspiración con aguja fina (BAAF)', codigoCups: '890108', cantidad: 25, porcentaje: 10 },
      { nombre: 'Biopsia por punción con aguja gruesa', codigoCups: '890109', cantidad: 20, porcentaje: 8 },
      { nombre: 'Inmunohistoquímica', codigoCups: '890110', cantidad: 30, porcentaje: 11 },
      { nombre: 'Estudio molecular en tejido tumoral', codigoCups: '890111', cantidad: 10, porcentaje: 4 }
    ],
    // Febrero
    [
      { nombre: 'Consulta de oncología médica', codigoCups: '890101', cantidad: 65, porcentaje: 24 },
      { nombre: 'Consulta de oncología quirúrgica', codigoCups: '890102', cantidad: 50, porcentaje: 18 },
      { nombre: 'Consulta de radioterapia', codigoCups: '890103', cantidad: 35, porcentaje: 13 },
      { nombre: 'Quimioterapia', codigoCups: '890104', cantidad: 45, porcentaje: 16 },
      { nombre: 'Radioterapia', codigoCups: '890105', cantidad: 30, porcentaje: 11 },
      { nombre: 'Cirugía oncológica', codigoCups: '890106', cantidad: 25, porcentaje: 9 },
      { nombre: 'Procedimientos diagnósticos oncológicos', codigoCups: '890107', cantidad: 20, porcentaje: 7 },
      { nombre: 'Biopsia por aspiración con aguja fina (BAAF)', codigoCups: '890108', cantidad: 28, porcentaje: 10 },
      { nombre: 'Biopsia por punción con aguja gruesa', codigoCups: '890109', cantidad: 22, porcentaje: 8 },
      { nombre: 'Inmunohistoquímica', codigoCups: '890110', cantidad: 32, porcentaje: 12 },
      { nombre: 'Estudio molecular en tejido tumoral', codigoCups: '890111', cantidad: 12, porcentaje: 4 }
    ]
  ]
}

const selectedMonth = ref<number | null>(null)
const selectedEntity = ref('')
const showReport = ref(false)
const isLoading = ref(false)
const showMonthError = ref(false)
const showEntityError = ref(false)

const cupsPorEntidad = computed(() => {
  if (selectedMonth.value === null || !selectedEntity.value) return []
  return cupsPorEntidadMes[selectedEntity.value]?.[selectedMonth.value] || []
})

const totalCups = computed(() =>
  cupsPorEntidad.value.reduce((acc, cups) => acc + cups.cantidad, 0)
)

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
    categories: cupsPorEntidad.value.map(cups => cups.nombre),
    labels: {
      rotate: -45,
      style: {
        fontSize: '12px'
      }
    }
  },
  yaxis: {
    title: {
      text: 'Cantidad de Procedimientos'
    }
  },
  fill: {
    opacity: 1,
    colors: ['#2974A3']
  },
  tooltip: {
    y: {
      formatter: function (val: number) {
        return val + " procedimientos"
      }
    }
  }
}))

const series = computed(() => [
  {
    name: 'Cantidad',
    data: cupsPorEntidad.value.map(cups => cups.cantidad)
  }
])

const generateReport = async () => {
  if (selectedMonth.value === null) {
    showMonthError.value = true
    return
  }
  
  if (!selectedEntity.value) {
    showEntityError.value = true
    return
  }
  
  showMonthError.value = false
  showEntityError.value = false
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
  selectedEntity.value = ''
  showReport.value = false
  showMonthError.value = false
  showEntityError.value = false
}

const imprimir = () => {
  // Verificar que se haya seleccionado un mes y una entidad
  if (selectedMonth.value === null || !selectedEntity.value) {
    alert('Por favor seleccione un mes y una entidad antes de imprimir.');
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
  const entidadSeleccionada = selectedEntity.value;
  const cups = cupsPorEntidad.value;
  const total = totalCups.value;
  const fechaActual = new Date();

  // Generar las filas de la tabla
  const filasCups = cups.map(cups => `
    <tr>
      <td>${cups.codigoCups}</td>
      <td>${cups.nombre}</td>
      <td>${cups.cantidad}</td>
      <td>${((cups.cantidad / total) * 100).toFixed(1)}%</td>
    </tr>
  `).join('');

  // HTML completo para la ventana de impresión
  const printHTML = `
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Informe Mensual de Procedimientos Oncológicos - ${mesSeleccionado} ${selectedYear.value}</title>
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
        
        td:nth-child(2), td:nth-child(3),
        th:nth-child(2), th:nth-child(3) {
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
          <div class="title">INFORME MENSUAL DE PROCEDIMIENTOS ONCOLÓGICOS</div>
          <div class="subtitle">${mesSeleccionado} ${selectedYear.value}</div>
          <div class="subtitle">${entidadSeleccionada}</div>
        </div>
        <div class="date">${fechaActual.toLocaleDateString()}</div>
      </div>
      
      <table>
        <thead>
          <tr>
            <th>Procedimiento Oncológico</th>
            <th>Código</th>
            <th>Cantidad</th>
            <th>Porcentaje</th>
          </tr>
        </thead>
        <tbody>
          ${filasCups}
        </tbody>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>${total}</td>
            <td>${total}</td>
            <td>100%</td>
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
