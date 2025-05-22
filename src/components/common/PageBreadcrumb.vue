<!--
  Componente PageBreadcrumb
  Muestra un breadcrumb con enlaces y título de la página actual.
  Permite configurar el título de la página.
  Incluye soporte para enlaces y icono de flecha.
-->
<template>
  <!-- Contenedor principal del breadcrumb -->
  <div class="flex flex-wrap items-center justify-between gap-3 mb-6">
    <nav>
      <!-- Lista ordenada para la navegación -->
      <ol class="flex items-center gap-1.5">
        <!-- Enlace a la página principal -->
        <li>
          <router-link
            class="inline-flex items-center gap-1.5 text-sm text-gray-500 dark:text-gray-400"
            to="/"
          >
            Inicio
            <!-- Icono de flecha para separar niveles -->
            <svg
              class="stroke-current"
              width="17"
              height="16"
              viewBox="0 0 17 16"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M6.0765 12.667L10.2432 8.50033L6.0765 4.33366"
                stroke=""
                stroke-width="1.2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </router-link>
        </li>
        <!-- Título de la página actual -->
        <li class="text-sm text-gray-800 dark:text-white/90">
          {{ pageTitle }}
        </li>
      </ol>
    </nav>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'

// Interfaz para las propiedades del componente
interface BreadcrumbProps {
  pageTitle: string  // Título que se mostrará en el breadcrumb
}

// Definición de propiedades
defineProps<BreadcrumbProps>()
</script>
