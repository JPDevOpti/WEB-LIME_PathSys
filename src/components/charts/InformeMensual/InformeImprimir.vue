<!--
  Componente Grafico de Barras y Tabla
  Muestra un gráfico de barras con las muestras ingresadas por mes y una tabla con detalles al seleccionar un mes.
-->

<template>
  <div class="space-y-6">
    <!-- Selector de mes -->
    <div class="mb-6 flex flex-col sm:flex-row sm:items-center sm:space-x-6 space-y-2 sm:space-y-0">
      <label for="mes" class="font-medium text-gray-700 min-w-[140px]">Selecciona un mes:</label>
      <select v-model="selectedMonth" id="mes" class="border rounded px-4 py-2 focus:ring focus:border-brand-500 w-full sm:w-auto">
        <option disabled value="">-- Elige un mes --</option>
        <option v-for="(month, idx) in monthsFull" :key="month" :value="idx">{{ month }}</option>
      </select>
    </div>

    <!-- Gráfico de barras (opcional, puedes quitarlo si solo quieres la tabla) -->
    <div class="max-w-full overflow-x-auto custom-scrollbar">
      <div id="chartOne" class="-ml-5 min-w-[650px] xl:min-w-full pl-2">
        <VueApexCharts 
          type="bar" 
          height="180" 
          :options="chartOptions" 
          :series="series" 
        />
      </div>
    </div>

    <!-- Tabla de entidades por pacientes -->
    <div v-if="selectedMonth !== null" class="overflow-x-auto mt-6">
      <div class="mb-4">
        <h2 class="text-xl font-bold text-brand-700 mb-2">Pacientes por entidad - {{ monthsFull[selectedMonth] }}</h2>
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
          <span class="text-base font-semibold block mt-1">{{ monthsFull[selectedMonth] }} 2025</span>
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

// Datos para el gráfico - Serie de pacientes mensuales (total)
const series = ref([
  {
    name: 'Total Pacientes',
    data: entidadesPorMes.map(mes => mes.reduce((acc, entidad) => acc + entidad.ambulatorios + entidad.hospitalizados, 0)),
  },
  {
    name: 'Ambulatorios',
    data: entidadesPorMes.map(mes => mes.reduce((acc, entidad) => acc + entidad.ambulatorios, 0)),
  },
  {
    name: 'Hospitalizados',
    data: entidadesPorMes.map(mes => mes.reduce((acc, entidad) => acc + entidad.hospitalizados, 0)),
  },
])

// Configuración del gráfico
const chartOptions = computed(() => ({
  // Colores usando el esquema LIME del CSS principal
  colors: ['#2974A3', '#5CA6C9', '#8FC8DE'],
  
  // Configuración general del gráfico
  chart: {
    fontFamily: 'Outfit, sans-serif',
    type: 'bar',
    toolbar: {
      show: false,
    },
    animations: {
      enabled: true,
      easing: 'easeinout',
      speed: 800,
    },
  },

  // Configuración de las barras
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '45%',
      borderRadius: 6,
      borderRadiusApplication: 'end',
      distributed: false,
    },
  },

  // Desactiva las etiquetas de datos
  dataLabels: {
    enabled: false,
  },

  // Configuración del trazo de las barras
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent'],
  },

  // Configuración del eje X
  xaxis: {
    categories: monthsFull,
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
    labels: {
      style: {
        fontFamily: 'Outfit, sans-serif',
        fontSize: '12px',
        colors: '#667085',
      },
    },
  },

  // Configuración de la leyenda
  legend: {
    show: true,
    position: 'top',
    horizontalAlign: 'left',
    fontFamily: 'Outfit',
    fontSize: '14px',
    markers: {
      radius: 8,
      width: 12,
      height: 12,
    },
    itemMargin: {
      horizontal: 15,
      vertical: 5,
    },
  },

  // Configuración del eje Y
  yaxis: {
    title: false,
    labels: {
      formatter: (value: number) => value.toLocaleString(),
      style: {
        fontFamily: 'Outfit, sans-serif',
        fontSize: '12px',
        colors: '#667085',
      },
    },
  },

  // Configuración de la cuadrícula
  grid: {
    borderColor: '#e4e7ec',
    strokeDashArray: 3,
    yaxis: {
      lines: {
        show: true,
      },
    },
    xaxis: {
      lines: {
        show: false,
      },
    },
    padding: {
      top: 0,
      right: 10,
      bottom: 0,
      left: 10,
    },
  },

  // Configuración del relleno
  fill: {
    opacity: 0.9,
    type: 'solid',
  },

  // Configuración del tooltip
  tooltip: {
    theme: 'light',
    shared: true,
    intersect: false,
    x: {
      show: true,
      formatter: (value: number) => monthsFull[value - 1] || '',
    },
    y: {
      formatter: (value: number) => `${value.toLocaleString()} pacientes`,
    },
    style: {
      fontFamily: 'Outfit, sans-serif',
      fontSize: '13px',
    },
    marker: {
      show: true,
    },
  },

  // Configuración de estados
  states: {
    hover: {
      filter: {
        type: 'lighten',
        value: 0.15,
      },
    },
    active: {
      filter: {
        type: 'darken',
        value: 0.1,
      },
    },
  },

  // Configuración responsiva
  responsive: [{
    breakpoint: 768,
    options: {
      plotOptions: {
        bar: {
          columnWidth: '60%',
        },
      },
      legend: {
        position: 'bottom',
        horizontalAlign: 'center',
      },
    },
  }],
}))

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
      <title>Informe Mensual de Pacientes - ${mesSeleccionado} 2025</title>
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
          <div class="subtitle">${mesSeleccionado} 2025</div>
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
}
</style>
