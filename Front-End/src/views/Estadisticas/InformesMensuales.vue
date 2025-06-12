<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">
      <ComponentCard title="Informe de entidades"> <InformeEntidades /> </ComponentCard>
      <ComponentCard title="Informe de cups por entidad"> <InformeCupsEntidad /> </ComponentCard>
      <ComponentCard title="Informe de cancer por entidad"> <InformeCancerEntidades /> </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import ComponentCard from "@/components/common/ComponentCard.vue";
import PageBreadcrumb from "@/components/common/PageBreadcrumb.vue";
import AdminLayout from "@/components/layout/AdminLayout.vue";
import InformeEntidades from "@/components/Estadisticas/InformesMensuales/InformeEntidades.vue"
import InformeCupsEntidad from "@/components/Estadisticas/InformesMensuales/InformeCupsEntidad.vue"
import InformeCancerEntidades from "@/components/Estadisticas/InformesMensuales/InformeCancerEntidades.vue"
import { ref } from "vue";
const currentPageTitle = ref("Estadisticas");
</script>
