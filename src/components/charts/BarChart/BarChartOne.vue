<!--
  Componente Grafico de Barras
  Muestra un gráfico de barras con las muestras ingresadas por mes.
-->

<template>
  <!-- Contenedor principal con scroll horizontal para responsividad -->
  <div class="max-w-full overflow-x-auto custom-scrollbar">
    <!-- Contenedor del gráfico con ancho mínimo en móvil y completo en xl -->
    <div id="chartOne" class="-ml-5 min-w-[650px] xl:min-w-full pl-2">
      <!-- Componente de gráfico de barras de ApexCharts -->
      <VueApexCharts 
        type="bar" 
        height="180" 
        :options="chartOptions" 
        :series="series" 
      />
    </div>
  </div>
</template>

<script setup lang="ts">
// Importaciones necesarias de Vue y ApexCharts
import { ref, computed } from 'vue'
import VueApexCharts from 'vue3-apexcharts'

// Interfaces para tipado
interface ChartData {
  name: string
  data: number[]
}

// Datos para el gráfico - Serie de ventas mensuales
const series = ref<ChartData[]>([
  {
    name: 'Muestras',
    data: [168, 385, 201, 298, 187, 195, 291, 110, 215, 390, 280, 112],
  },
])

// Meses del año para el eje X
const months = [
  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
] as const

// Configuración del gráfico
const chartOptions = computed(() => ({
  // Color de las barras
  colors: ['#465fff'],
  
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
      columnWidth: '39%',
      borderRadius: 5,
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
    width: 4,
    colors: ['transparent'],
  },

  // Configuración del eje X
  xaxis: {
    categories: months,
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
      },
    },
  },

  // Configuración de la leyenda
  legend: {
    show: true,
    position: 'top',
    horizontalAlign: 'left',
    fontFamily: 'Outfit',
    markers: {
      radius: 99,
    },
    itemMargin: {
      horizontal: 10,
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
      },
    },
  },

  // Configuración de la cuadrícula
  grid: {
    yaxis: {
      lines: {
        show: true,
      },
    },
    padding: {
      top: 0,
      right: 0,
      bottom: 0,
      left: 0,
    },
  },

  // Configuración del relleno
  fill: {
    opacity: 1,
    type: 'solid',
  },

  // Configuración del tooltip
  tooltip: {
    theme: 'light',
    x: {
      show: false,
    },
    y: {
      formatter: (value: number) => value.toLocaleString(),
    },
    style: {
      fontFamily: 'Outfit, sans-serif',
      fontSize: '12px',
    },
  },

  // Configuración de estados
  states: {
    hover: {
      filter: {
        type: 'lighten',
        value: 0.1,
      },
    },
    active: {
      filter: {
        type: 'darken',
        value: 0.1,
      },
    },
  },
}))
</script>

<style scoped>
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #465fff #f3f4f6;
}

.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #465fff;
  border-radius: 3px;
}
</style>
