<!--
  Componente PorcentajeAvance
  Muestra un gráfico circular con el porcentaje de avance de muestras activas
  y métricas adicionales como promesa media, muestras activas y muestras del día.
-->
<template>
  <!-- Contenedor principal con soporte para tema oscuro y efectos hover -->
  <div
    class="rounded-2xl border border-gray-200 bg-gray-100 transition-all duration-300 hover:shadow-lg dark:border-gray-800 dark:bg-white/[0.03]"
  >
    <!-- Sección superior con título y menú de opciones -->
    <div
      class="px-5 pt-5 bg-white shadow-default rounded-2xl pb-11 dark:bg-gray-900 sm:px-6 sm:pt-6"
    >
      <!-- Encabezado con título y menú desplegable -->
      <div class="flex justify-between items-center">
        <div>
          <h3 class="text-lg font-semibold text-gray-800 dark:text-white/90">Oportunidad de Atención</h3>
          <p class="mt-1 text-gray-500 text-theme-sm dark:text-gray-400">
            Porcentaje de muestras procesadas dentro del tiempo de oportunidad
          </p>
        </div>
        <!-- Menú de opciones con icono y efectos hover -->
        <div class="relative group">
          <DropdownMenu :menu-items="menuItems">
            <template #icon>
              <svg
                class="transition-colors duration-300 group-hover:text-primary-600 dark:group-hover:text-primary-400"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M10.2441 6C10.2441 5.0335 11.0276 4.25 11.9941 4.25H12.0041C12.9706 4.25 13.7541 5.0335 13.7541 6C13.7541 6.9665 12.9706 7.75 12.0041 7.75H11.9941C11.0276 7.75 10.2441 6.9665 10.2441 6ZM10.2441 18C10.2441 17.0335 11.0276 16.25 11.9941 16.25H12.0041C12.9706 16.25 13.7541 17.0335 13.7541 18C13.7541 18.9665 12.9706 19.75 12.0041 19.75H11.9941C11.0276 19.75 10.2441 18.9665 10.2441 18ZM11.9941 10.25C11.0276 10.25 10.2441 11.0335 10.2441 12C10.2441 12.9665 11.0276 13.75 11.9941 13.75H12.0041C12.9706 13.75 13.7541 12.9665 13.7541 12C13.7541 11.0335 12.9706 10.25 12.0041 10.25H11.9941Z"
                  fill="currentColor"
                />
              </svg>
            </template>
          </DropdownMenu>
        </div>
      </div>

      <!-- Gráfico circular con animaciones y efectos hover -->
      <div class="relative max-h-[195px]">
        <div id="chartTwo" class="h-full">
          <div class="radial-bar-chart">
            <VueApexCharts 
              type="radialBar" 
              height="330" 
              :options="chartOptions" 
              :series="series"
              class="transition-all duration-500 hover:scale-105" 
            />
          </div>
        </div>
        <!-- Indicador de porcentaje de crecimiento -->
        <span
          class="absolute left-1/2 top-[85%] -translate-x-1/2 -translate-y-[85%] rounded-full bg-success-50 px-3 py-1 text-xs font-medium text-success-600 transition-all duration-300 hover:bg-success-100 dark:bg-success-500/15 dark:text-success-500 dark:hover:bg-success-500/25"
          >+5.2%</span 
        >
      </div>
      <!-- Descripción del gráfico -->
      <p class="mx-auto mt-1.5 w-full max-w-[380px] text-center text-sm text-gray-500 transition-colors duration-300 dark:text-gray-400 sm:text-base">
        Progreso en el cumplimiento de tiempos de oportunidad
      </p>
    </div>

    <!-- Sección de métricas con efectos hover y animaciones -->
    <div class="flex items-center justify-center gap-5 px-6 py-3.5 sm:gap-8 sm:py-5">
      <!-- Métrica: Tiempo promedio de procesamiento -->
      <div class="group transition-all duration-300 hover:scale-105">
        <p class="mb-1 text-center text-gray-500 text-theme-xs transition-colors duration-300 group-hover:text-gray-700 dark:text-gray-400 dark:group-hover:text-gray-300 sm:text-sm">
          Tiempo promedio
        </p>
        <p
          class="flex items-center justify-center gap-1 text-base font-semibold text-gray-800 transition-colors duration-300 group-hover:text-primary-600 dark:text-white/90 dark:group-hover:text-primary-400 sm:text-lg"
        >
          4.2
          <span class="text-sm text-gray-500">días</span>
        </p>
      </div>

      <!-- Separador vertical -->
      <div class="w-px bg-gray-200 h-7 dark:bg-gray-800"></div>

      <!-- Métrica: Muestras dentro de oportunidad -->
      <div class="group transition-all duration-300 hover:scale-105">
        <p class="mb-1 text-center text-gray-500 text-theme-xs transition-colors duration-300 group-hover:text-gray-700 dark:text-gray-400 dark:group-hover:text-gray-300 sm:text-sm">
          Dentro de oportunidad
        </p>
        <p
          class="flex items-center justify-center gap-1 text-base font-semibold text-gray-800 transition-colors duration-300 group-hover:text-primary-600 dark:text-white/90 dark:group-hover:text-primary-400 sm:text-lg"
        >
          285
          <svg
            class="transition-transform duration-300 group-hover:translate-y-[-2px]"
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M7.60141 2.33683C7.73885 2.18084 7.9401 2.08243 8.16435 2.08243C8.16475 2.08243 8.16516 2.08243 8.16556 2.08243C8.35773 2.08219 8.54998 2.15535 8.69664 2.30191L12.6968 6.29924C12.9898 6.59203 12.9899 7.0669 12.6971 7.3599C12.4044 7.6529 11.9295 7.65306 11.6365 7.36027L8.91435 4.64004L8.91435 13.5C8.91435 13.9142 8.57856 14.25 8.16435 14.25C7.75013 14.25 7.41435 13.9142 7.41435 13.5L7.41435 4.64442L4.69679 7.36025C4.4038 7.65305 3.92893 7.6529 3.63613 7.35992C3.34333 7.06693 3.34348 6.59206 3.63646 6.29926L7.60141 2.33683Z"
              fill="#039855"
            />
          </svg>
        </p>
      </div>

      <!-- Separador vertical -->
      <div class="w-px bg-gray-200 h-7 dark:bg-gray-800"></div>

      <!-- Métrica: Muestras fuera de oportunidad -->
      <div class="group transition-all duration-300 hover:scale-105">
        <p class="mb-1 text-center text-gray-500 text-theme-xs transition-colors duration-300 group-hover:text-gray-700 dark:text-gray-400 dark:group-hover:text-gray-300 sm:text-sm">
          Fuera de oportunidad
        </p>
        <p
          class="flex items-center justify-center gap-1 text-base font-semibold text-gray-800 transition-colors duration-300 group-hover:text-primary-600 dark:text-white/90 dark:group-hover:text-primary-400 sm:text-lg"
        >
          45
          <svg
            class="transition-transform duration-300 group-hover:translate-y-[-2px]"
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M7.26816 13.6632C7.4056 13.8192 7.60686 13.9176 7.8311 13.9176C7.83148 13.9176 7.83187 13.9176 7.83226 13.9176C8.02445 13.9178 8.21671 13.8447 8.36339 13.6981L12.3635 9.70076C12.6565 9.40797 12.6567 8.9331 12.3639 8.6401C12.0711 8.34711 11.5962 8.34694 11.3032 8.63973L8.5811 11.36L8.5811 2.5C8.5811 2.08579 8.24531 1.75 7.8311 1.75C7.41688 1.75 7.0811 2.08579 7.0811 2.5L7.0811 11.3556L4.36354 8.63975C4.07055 8.34695 3.59568 8.3471 3.30288 8.64009C3.01008 8.93307 3.01023 9.40794 3.30321 9.70075L7.26816 13.6632Z"
              fill="#D92D20"
            />
          </svg>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import DropdownMenu from '../common/DropdownMenu.vue'
import VueApexCharts from 'vue3-apexcharts'

// Opciones del menú desplegable
const menuItems = [
  { 
    label: 'Ver informe detallado', 
    onClick: () => console.log('Ver informe detallado clicked'),
    icon: 'chart-bar'
  },
  { 
    label: 'Exportar datos', 
    onClick: () => console.log('Exportar datos clicked'),
    icon: 'download'
  },
  { 
    label: 'Configuración', 
    onClick: () => console.log('Configuración clicked'),
    icon: 'cog'
  }
]

// Props del componente
const props = defineProps({
  value: {
    type: Number,
    default: 86.36, // Porcentaje de muestras dentro de oportunidad
  },
})

// Serie de datos para el gráfico
const series = computed(() => [props.value])

// Configuración del gráfico circular
const chartOptions = {
  colors: ['#3D8D5B'],
  chart: {
    fontFamily: 'Outfit, sans-serif',
    sparkline: {
      enabled: true,
    },
    // Configuración de animaciones
    animations: {
      enabled: true,
      easing: 'easeinout',
      speed: 800,
      animateGradually: {
        enabled: true,
        delay: 150
      },
      dynamicAnimation: {
        enabled: true,
        speed: 350
      }
    }
  },
  // Opciones de visualización del gráfico circular
  plotOptions: {
    radialBar: {
      startAngle: -90,
      endAngle: 90,
      hollow: {
        size: '80%',
      },
      track: {
        background: '#E4E7EC',
        strokeWidth: '100%',
        margin: 5,
      },
      dataLabels: {
        name: {
          show: false,
        },
        value: {
          fontSize: '36px',
          fontWeight: '600',
          offsetY: 60,
          color: '#1D2939',
          formatter: function (val: number) {
            return val.toFixed(2) + '%'
          },
        },
      },
    },
  },
  // Configuración del gradiente
  fill: {
    type: 'gradient',
    gradient: {
      shade: 'dark',
      type: 'horizontal',
      shadeIntensity: 0.5,
      gradientToColors: ['#7FCB97'],
      inverseColors: true,
      opacityFrom: 1,
      opacityTo: 1,
      stops: [0, 100]
    }
  },
  // Estilo de la línea del gráfico
  stroke: {
    lineCap: 'round',
    width: 2
  },
  labels: ['Oportunidad'],
  // Estados del gráfico
  states: {
    hover: {
      filter: {
        type: 'darken',
        value: 0.9
      }
    }
  }
}
</script>

<style scoped>
/* Estilos del contenedor del gráfico */
.radial-bar-chart {
  width: 100%;
  max-width: 330px;
  margin: 0 auto;
  transition: transform 0.3s ease;
}

/* Efecto hover en el gráfico */
.radial-bar-chart:hover {
  transform: scale(1.05);
}

/* Animación de pulso para elementos importantes */
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
</style>
