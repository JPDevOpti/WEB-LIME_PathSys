<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Ingresar Nuevo Patologo" clickable>
          <NuevoPatologo />
        </ComponentCard>
      </div>
      <div class="space-y-6">
        <ComponentCard title="Editar Patologo Existente" clickable>
          <EditarPatologo />
        </ComponentCard>

      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import NuevoPatologo from '@/components/NuevosIntegrantes/NuevoPatologo/IngresarNuevoPatologo.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import EditarPatologo from '@/components/NuevosIntegrantes/NuevoPatologo/EditarPatologo.vue'

const currentPageTitle = ref('Nuevo Patologo')
</script>