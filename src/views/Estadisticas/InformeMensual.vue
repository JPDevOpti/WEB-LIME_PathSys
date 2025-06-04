<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-5 sm:space-y-6">
      <ComponentCard title="Informe Mensual"> <InformeMensual /> </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup>
import ComponentCard from "@/components/common/ComponentCard.vue";
import PageBreadcrumb from "@/components/common/PageBreadcrumb.vue";
import AdminLayout from "@/components/layout/AdminLayout.vue";
import InformeMensual from "@/components/charts/InformeMensual/InformeImprimir.vue"
import { ref } from "vue";
const currentPageTitle = ref("Estadisticas");
</script>
