<template>
  <div class="space-y-4">
    <div class="flex gap-4">
      <div class="flex-1">
        <label for="codigo" class="block text-sm font-medium text-gray-700 mb-1">
          Código de Muestra
        </label>
        <input
          type="text"
          id="codigo"
          v-model="codigoMuestra"
          placeholder="Ej: 2024-0001"
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-brand-500 focus:ring-1 focus:ring-brand-500"
          @keyup.enter="buscarMuestra"
        />
      </div>
      <div class="flex items-end gap-2">
        <button
          @click="buscarMuestra"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-500"
        >
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          Buscar
        </button>
        <button
          @click="limpiarCampos"
          class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
        >
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
          Limpiar
        </button>
      </div>
    </div>

    <!-- Mensaje de éxito -->
    <div v-if="muestraEncontrada" class="mt-6">
      <div class="flex items-center justify-between mb-2">
        <h2 class="text-lg font-semibold">Muestra encontrada: {{ codigoMuestra }}</h2>
        <span class="px-3 py-1 rounded-full bg-green-100 text-green-700 text-xs font-semibold">Terminado</span>
      </div>
      <div class="bg-gray-50 rounded-lg border border-gray-200 p-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Información del Paciente -->
          <div>
            <h3 class="font-semibold mb-2 text-gray-700">Información del Paciente</h3>
            <div class="text-sm text-gray-800 space-y-1">
              <div><span class="font-medium">Nombre:</span> Juan Pérez</div>
              <div><span class="font-medium">Cédula:</span> 12345678</div>
              <div><span class="font-medium">Edad:</span> 45 años</div>
              <div><span class="font-medium">Género:</span> Masculino</div>
            </div>
          </div>
          <!-- Detalles de la Muestra -->
          <div>
            <h3 class="font-semibold mb-2 text-gray-700">Detalles de la Muestra</h3>
            <div class="text-sm text-gray-800 space-y-1">
              <div><span class="font-medium">Tipo de Análisis:</span> Hemograma Completo</div>
              <div><span class="font-medium">Fecha de Ingreso:</span> 15/01/2024</div>
              <div><span class="font-medium">Médico Solicitante:</span> Dr. García</div>
              <div><span class="font-medium">Observaciones:</span> Muestra procesada exitosamente</div>
            </div>
          </div>
        </div>
        <!-- Progreso del Análisis -->
        <div class="mt-6">
          <h4 class="text-sm font-medium text-gray-700 mb-1">Progreso del Análisis</h4>
          <div class="w-full bg-gray-200 rounded-full h-2.5 mb-1">
            <div class="bg-green-500 h-2.5 rounded-full" style="width: 100%"></div>
          </div>
          <div class="text-xs text-green-700 font-medium">100% completado</div>
        </div>
      </div>
    </div>

    <!-- Mensaje de error -->
    <div v-if="error" class="bg-red-50 rounded-lg p-4 border border-red-200">
      <div class="flex items-center">
        <svg class="w-5 h-5 text-red-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p class="text-sm text-red-700">{{ error }}</p>
      </div>
    </div>
    <div v-if="!muestraEncontrada && error === '' && codigoMuestra && busquedaRealizada" class="bg-yellow-50 rounded-lg p-4 border border-yellow-200 mt-4">
      <div class="flex items-center">
        <svg class="w-5 h-5 text-yellow-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p class="text-sm text-yellow-700">No se ha encontrado la muestra</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

interface MuestraCompleta {
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

const codigoMuestra = ref('')
const muestraEncontrada = ref(false)
const error = ref('')
const busquedaRealizada = ref(false)

const props = defineProps<{ codigoExterno?: string }>()

// Definir emits
const emit = defineEmits<{
  'muestra-encontrada': [muestra: MuestraCompleta]
  'limpiar-campos': []
}>()

watch(() => props.codigoExterno, (nuevoCodigo) => {
  if (nuevoCodigo && nuevoCodigo !== codigoMuestra.value) {
    codigoMuestra.value = nuevoCodigo
    buscarMuestra()
  }
})

const buscarMuestra = () => {
  busquedaRealizada.value = true
  // Aquí iría la lógica para buscar la muestra
  // Por ahora, simulamos una búsqueda exitosa
  if (codigoMuestra.value) {
    // Simulación: solo existe la muestra 2024-0001
    if (codigoMuestra.value === '2024-0001') {
      const muestra: MuestraCompleta = {
        idMuestra: codigoMuestra.value,
        paciente: {
          nombre: 'Juan Pérez',
          cedula: '12345678'
        },
        tipoAnalisisTexto: 'Hemograma Completo',
        estadoTexto: 'Pendiente',
        medicoSolicitanteTexto: 'Dr. García Pérez',
        fechaIngresoTexto: new Date().toLocaleString(),
        resultadoMacro: '',
        resultadoMicro: '',
        resultadoMetodo: '',
        diagnostico: ''
      }
      muestraEncontrada.value = true
      error.value = ''
      emit('muestra-encontrada', muestra)
    } else {
      muestraEncontrada.value = false
      error.value = ''
    }
  } else {
    error.value = 'Por favor, ingrese un código de muestra'
    muestraEncontrada.value = false
  }
}

const limpiarCampos = () => {
  codigoMuestra.value = ''
  muestraEncontrada.value = false
  error.value = ''
  busquedaRealizada.value = false
  // Emitir evento para limpiar campos en el componente padre
  emit('limpiar-campos')
}
</script> 