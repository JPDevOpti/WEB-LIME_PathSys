<!--
  Componente HeaderLogo
  Muestra el logo de la aplicación en el encabezado.
  Permite navegar a la página de inicio.
  Incluye soporte para tema oscuro y responsive.
-->
<template>
  <router-link to="/" class="lg:hidden">
    <img class="dark:hidden" src="/images/logo/banner_huam.png" alt="Logo" />
    <img class="hidden dark:block" src="/images/logo/logo-dark.svg" alt="Logo" />
  </router-link>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>
AppSidebar