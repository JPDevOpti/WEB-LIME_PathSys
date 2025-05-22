<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Modificar Datos Demográficos" clickable>
          <ModificarDatosDemograficos />
        </ComponentCard>
      </div>
      <div class="space-y-6">
        <ComponentCard title="Modificar Datos de Muestra" clickable>
          <ModificarDatosMuestra :muestra-id="'L2024-001'" />
        </ComponentCard>

      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import ModificarDatosDemograficos from '@/components/forms/EditarMuestra/ModificarDatosPaciente.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import ModificarDatosMuestra from '@/components/forms/EditarMuestra/ModificarDatosMuestra.vue'
import VerMuestrasPaciente from '@/components/forms/EditarMuestra/VerMuestrasPaciente.vue'


const currentPageTitle = ref('Gestión de Muestras')
</script>