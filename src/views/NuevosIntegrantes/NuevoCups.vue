<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Ingresar Nuevo Cups" clickable>
          <NuevoPatologo />
        </ComponentCard>
      </div>
      <div class="space-y-6">
        <ComponentCard title="Editar Cups Existente" clickable>
          <EditarPatologo />
        </ComponentCard>

      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '../../components/common/PageBreadcrumb.vue'
import AdminLayout from '../../components/layout/AdminLayout.vue'
import NuevoPatologo from '../../components/NuevosIntegrantes/NuevoCups/IngresarNuevoCups.vue'
import ComponentCard from '../../components/common/ComponentCard.vue'
import EditarPatologo from '../../components/NuevosIntegrantes/NuevoCups/EditarCups.vue'

const currentPageTitle = ref('Nuevo Cups')
</script>