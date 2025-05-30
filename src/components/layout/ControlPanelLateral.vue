<!--
  Componente SidebarProvider
  Proveedor de estado global para el sidebar de la aplicación.
  - Inicializa y proporciona el estado global del sidebar
  - Permite compartir el estado entre componentes relacionados
  - Maneja la lógica de expansión/colapso del sidebar
-->
<template>
  <slot></slot>
</template>

<script setup lang="ts">
import { useSidebarProvider } from '@/composables/ControlBarraLateral'

// Inicializa el proveedor de estado del sidebar
useSidebarProvider()
</script>
