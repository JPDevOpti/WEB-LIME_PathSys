<!--
  Componente HeaderLogo
  Muestra el logo de la aplicación en el encabezado.
  Permite navegar a la página de inicio.
  Incluye soporte para tema oscuro y responsive.
-->
<template>
  <router-link to="/" class="lg:hidden">
    <img class="dark:hidden" src="/images/logo/Logo-LIME-NoFondo.png" alt="Logo" width="150" height="40" />
    <img class="hidden dark:block" src="/images/logo/logo-dark.svg" alt="Logo" width="150" height="40" />
  </router-link>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
AppSidebar