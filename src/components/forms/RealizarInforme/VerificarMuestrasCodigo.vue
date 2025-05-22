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
          placeholder="Ingrese el código de la muestra"
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-brand-500 focus:ring-1 focus:ring-brand-500"
        />
      </div>
      <div class="flex items-end">
        <button
          @click="buscarMuestra"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-brand-500"
        >
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          Buscar
        </button>
      </div>
    </div>

    <!-- Resultados de la búsqueda -->
    <div v-if="muestraEncontrada" class="bg-gray-50 rounded-lg p-4">
      <h3 class="text-lg font-medium text-gray-900 mb-3">Información de la Muestra</h3>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <p class="text-sm text-gray-500">Código</p>
          <p class="text-base font-medium text-gray-900">{{ muestraEncontrada.codigo }}</p>
        </div>
        <div>
          <p class="text-sm text-gray-500">Paciente</p>
          <p class="text-base font-medium text-gray-900">{{ muestraEncontrada.paciente }}</p>
        </div>
        <div>
          <p class="text-sm text-gray-500">Tipo de Análisis</p>
          <p class="text-base font-medium text-gray-900">{{ muestraEncontrada.tipoAnalisis }}</p>
        </div>
        <div>
          <p class="text-sm text-gray-500">Estado</p>
          <p class="text-base font-medium text-gray-900">{{ muestraEncontrada.estado }}</p>
        </div>
      </div>
    </div>

    <!-- Mensaje de error -->
    <div v-if="error" class="bg-red-50 rounded-lg p-4">
      <p class="text-sm text-red-700">{{ error }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const codigoMuestra = ref('')
const muestraEncontrada = ref(null)
const error = ref('')

const buscarMuestra = () => {
  // Aquí iría la lógica para buscar la muestra
  // Por ahora, simulamos una búsqueda exitosa
  if (codigoMuestra.value) {
    muestraEncontrada.value = {
      codigo: codigoMuestra.value,
      paciente: 'Juan Pérez',
      tipoAnalisis: 'Hemograma Completo',
      estado: 'Pendiente'
    }
    error.value = ''
  } else {
    error.value = 'Por favor, ingrese un código de muestra'
    muestraEncontrada.value = null
  }
}
</script> 