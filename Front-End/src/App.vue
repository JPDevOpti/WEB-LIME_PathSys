<template>
  <ThemeProvider>
    <SidebarProvider>
      <RouterView />
    </SidebarProvider>
  </ThemeProvider>
</template>

<script setup lang="ts">
import ThemeProvider from './components/layout/ControladorTema.vue'
import SidebarProvider from './components/layout/ControlPanelLateral.vue'
</script>
