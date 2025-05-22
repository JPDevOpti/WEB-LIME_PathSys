<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Asignar Codigo a una Muestra" clickable>
          <AsignarCodigoMuestra />
        </ComponentCard>
        <ComponentCard title="Asignar Patologo a Muestra" clickable>
          <AsignarPatologoMuestra />
        </ComponentCard>
      </div>
      <div class="space-y-6">
        <ComponentCard title="Ingresar Nuevo Paciente" clickable>
          <DefaultInputs />
        </ComponentCard>
        <ComponentCard title="Verificar Muestras" clickable> 
          <VerMuestrasPaciente /> 
        </ComponentCard>

      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import DefaultInputs from '@/components/forms/NuevaMuestra/DatosDemograficos.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import VerMuestrasPaciente from '@/components/forms/NuevaMuestra/VerMuestrasPaciente.vue'
import AsignarCodigoMuestra from '@/components/forms/NuevaMuestra/AsignarCodigoMuestra.vue'
import AsignarPatologoMuestra from '@/components/forms/NuevaMuestra/AsignarPatologoMuestra.vue'

const currentPageTitle = ref('Nueva Muestra')
</script>