<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
      <div class="space-y-6">
        <ComponentCard title="Asignar Codigo a una Muestra" clickable>
          <AsignarCodigoMuestra 
            ref="asignarCodigoRef"
            :nuevo-paciente-guardado="nuevoPacienteGuardado"
            @reset-nuevo-paciente="resetNuevoPaciente"
          />
        </ComponentCard>
        <ComponentCard title="Asignar Patologo a Muestra" clickable>
          <AsignarPatologoMuestra />
        </ComponentCard>
      </div>
      <div class="space-y-6">
        <ComponentCard title="Ingresar Nuevo Paciente" clickable>
          <NuevoPaciente @patient-saved="handlePatientSaved" />
        </ComponentCard>
      </div>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PageBreadcrumb from '@/components/common/PageBreadcrumb.vue'
import AdminLayout from '@/components/layout/AdminLayout.vue'
import NuevoPaciente from '@/components/Muestras/NuevaMuestra/NuevoPaciente.vue'
import ComponentCard from '@/components/common/ComponentCard.vue'
import AsignarCodigoMuestra from '@/components/Muestras/NuevaMuestra/AsignarCodigoMuestra.vue'
import AsignarPatologoMuestra from '@/components/Muestras/NuevaMuestra/AsignarPatologoMuestra.vue'

interface PacienteData {
  numeroCedula: string
  nombrePaciente: string
  sexo: string
  edad: string | number
  entidad: string
  tipoAtencion: string
  observaciones: string
}

const currentPageTitle = ref('Nueva Muestra')
const asignarCodigoRef = ref()
const nuevoPacienteGuardado = ref<PacienteData | null>(null)

// Función que se ejecuta cuando se guarda un nuevo paciente
const handlePatientSaved = (pacienteData: PacienteData) => {
  console.log('Nuevo paciente guardado:', pacienteData)
  
  // Pasar los datos del paciente guardado al componente de asignar código
  nuevoPacienteGuardado.value = {
    numeroCedula: pacienteData.numeroCedula,
    nombrePaciente: pacienteData.nombrePaciente,
    sexo: pacienteData.sexo,
    edad: pacienteData.edad,
    entidad: pacienteData.entidad,
    tipoAtencion: pacienteData.tipoAtencion,
    observaciones: pacienteData.observaciones
  }
  
  // Opcional: hacer scroll al componente de asignar código
  setTimeout(() => {
    if (asignarCodigoRef.value?.$el) {
      asignarCodigoRef.value.$el.scrollIntoView({ 
        behavior: 'smooth', 
        block: 'start' 
      })
    }
  }, 100)
}

// Función para resetear el estado del nuevo paciente
const resetNuevoPaciente = () => {
  nuevoPacienteGuardado.value = null
}
</script>