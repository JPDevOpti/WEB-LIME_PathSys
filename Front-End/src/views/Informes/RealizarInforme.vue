<template>
  <AdminLayout>
    <PageBreadcrumb :pageTitle="currentPageTitle" />
    <div class="space-y-6">
      <!-- Verificadores de muestras en la parte superior -->
      <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
        <ComponentCard title="Verificar Muestras por Código" clickable> 
          <VerificarMuestrasCodigo 
            @muestra-encontrada="handleMuestraEncontrada"
            @limpiar-campos="handleLimpiarCampos"
            :codigo-externo="codigoMuestraSeleccionado"
          /> 
        </ComponentCard>
        <ComponentCard title="Verificar Muestras por Paciente" clickable>
          <VerificarMuestrasPaciente
            @muestra-encontrada="handleMuestraEncontrada"
            @limpiar-campos="handleLimpiarCampos"
            :dni-externo="dniPacienteSeleccionado"
          />
        </ComponentCard>
      </div>

      <ComponentCard title="Realizar Informe" clickable>
        <RealizarInformeMuestra 
          :muestra-id="muestraSeleccionada.idMuestra"
          :datos-muestra="muestraSeleccionada"
          @informe-guardado="handleInformeGuardado"
          @previsualizar-informe="handlePrevisualizar"
          @cancelar="handleCancelar"
        />
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
import VerificarMuestrasCodigo from '@/components/Muestras/ComponentesMuestras/VerificarMuestrasCodigo.vue'
import VerificarMuestrasPaciente from '@/components/Muestras/ComponentesMuestras/VerificarMuestrasPaciente.vue'

const currentPageTitle = ref('Realizar Informe')

interface MuestraData {
  idMuestra: string;
  paciente: {
    nombre: string;
    cedula: string;
  };
  tipoAnalisisTexto: string;
  estadoTexto: string;
  medicoSolicitanteTexto: string;
  fechaIngresoTexto: string;
  resultadoMacro: string;
  resultadoMicro: string;
  resultadoMetodo: string;
  diagnostico: string;
}

const muestraSeleccionada = ref<MuestraData>({
  idMuestra: '',
  paciente: {
    nombre: '',
    cedula: ''
  },
  tipoAnalisisTexto: '',
  estadoTexto: '',
  medicoSolicitanteTexto: '',
  fechaIngresoTexto: '',
  resultadoMacro: '',
  resultadoMicro: '',
  resultadoMetodo: '',
  diagnostico: ''
})

const codigoMuestraSeleccionado = ref('')
const dniPacienteSeleccionado = ref('')

const handleMuestraEncontrada = (muestra: MuestraData) => {
  muestraSeleccionada.value = muestra
  codigoMuestraSeleccionado.value = muestra.idMuestra
  dniPacienteSeleccionado.value = muestra.paciente.cedula
}

const handleLimpiarCampos = () => {
  muestraSeleccionada.value = {
    idMuestra: '',
    paciente: {
      nombre: '',
      cedula: ''
    },
    tipoAnalisisTexto: '',
    estadoTexto: '',
    medicoSolicitanteTexto: '',
    fechaIngresoTexto: '',
    resultadoMacro: '',
    resultadoMicro: '',
    resultadoMetodo: '',
    diagnostico: ''
  }
}

const handleInformeGuardado = (data: any) => {
  console.log('Informe guardado:', data)
}

const handlePrevisualizar = (data: any) => {
  console.log('Previsualizar informe:', data)
}

const handleCancelar = () => {
  handleLimpiarCampos()
}
</script>