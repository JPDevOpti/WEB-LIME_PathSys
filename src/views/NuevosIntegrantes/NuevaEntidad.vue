<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Ingresar Nueva Entidad" clickable>
          <NuevaEntidad />
        </ComponentCard>
      </div>
      <div class="space-y-6">
        <ComponentCard title="Editar Entidad Existente" clickable>
          <EditarEntidad />
        </ComponentCard>

      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import NuevaEntidad from '@/components/NuevosIntegrantes/NuevaEntidad/IngresarNuevaEntidad.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import EditarEntidad from '@/components/NuevosIntegrantes/NuevaEntidad/EditarEntidad.vue'

const currentPageTitle = ref('Nuevo Patologo')
</script>