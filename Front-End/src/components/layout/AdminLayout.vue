<!--
  Componente AdminLayout
  Layout principal para la aplicación de administración.
  Incluye barra lateral, encabezado, contenido y fondo.
  Permite expandir y contraer la barra lateral.
  Utiliza el componente AppSidebar y AppHeader.
-->
<template>
  <div class="min-h-screen xl:flex bg-gray-50 dark:bg-gray-900">
    <app-sidebar />
    <Backdrop />
    <div
      class="flex-1 transition-all duration-300 ease-in-out"
      :class="[
        isExpanded || isHovered ? 'lg:ml-[290px]' : 'lg:ml-[90px]',
        'animate-fadeIn'
      ]"
    >
      <app-header />
      <main 
        class="p-4 mx-auto max-w-(--breakpoint-2xl) md:p-6"
        role="main"
      >
        <div class="animate-fadeIn">
          <slot></slot>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import AppSidebar from './PanelLateral.vue'
import AppHeader from './PanelSuperior.vue'
import { useSidebar } from '@/composables/ControlBarraLateral'
import Backdrop from './Backdrop.vue'
import { onMounted, onUnmounted } from 'vue'

const { isExpanded, isHovered } = useSidebar()

// Manejo de teclas de acceso rápido
const handleKeyPress = (event: KeyboardEvent) => {
  // Alt + S para toggle sidebar
  if (event.altKey && event.key === 's') {
    isExpanded.value = !isExpanded.value
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleKeyPress)
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleKeyPress)
})
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.3s ease-out;
}

/* Mejora del scroll */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

/* Mejora de selección de texto */
::selection {
  background: #3b82f6;
  color: white;
}

/* Mejora de focus */
:focus-visible {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
}
</style>
