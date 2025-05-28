<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-6">
      <!-- Verificadores de muestras en la parte superior -->
      <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
        <ComponentCard title="Verificar Muestras por Código" clickable> 
          <VerificarMuestrasCodigo /> 
        </ComponentCard>
        <ComponentCard title="Verificar Muestras por Paciente" clickable>
          <VerificarMuestraPaciente />
        </ComponentCard>
      </div>

      <!-- Realizador de informe completo en la parte inferior -->
      <ComponentCard title="Realizar Informe Completo" clickable> 
        <RealizarInformeMuestra :muestra-id="''" /> 
      </ComponentCard>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import RealizarInformeMuestra from '@/components/Muestras/RealizarInforme/RealizarInformeMuestra.vue'
import VerificarMuestrasCodigo from '@/components/Muestras/RealizarInforme/VerificarMuestrasCodigo.vue'
import VerificarMuestraPaciente from '@/components/Muestras/RealizarInforme/VerificarMuestrasPaciente.vue'

const currentPageTitle = ref('Realizar Informe')
</script>