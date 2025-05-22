<template>
  <div class="space-y-4">
    <div class="flex flex-col gap-4">
      <div class="flex-1">
        <label for="dni" class="block text-sm font-medium text-gray-700 mb-1">
          DNI/Cédula del Paciente
        </label>
        <input
          type="text"
          id="dni"
          v-model="dniPaciente"
          placeholder="Ingrese el DNI o cédula del paciente"
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-brand-500 focus:ring-1 focus:ring-brand-500"
        />
      </div>
      <div class="flex items-end">
        <button
          @click="buscarPaciente"
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
    <div v-if="pacienteEncontrado" class="bg-gray-50 rounded-lg p-4">
      <h3 class="text-lg font-medium text-gray-900 mb-3">Información del Paciente</h3>
      <div class="grid grid-cols-2 gap-4">
        <div>
          <p class="text-sm text-gray-500">Nombre Completo</p>
          <p class="text-base font-medium text-gray-900">{{ pacienteEncontrado.nombre }}</p>
        </div>
        <div>
          <p class="text-sm text-gray-500">DNI/Cédula</p>
          <p class="text-base font-medium text-gray-900">{{ pacienteEncontrado.dni }}</p>
        </div>
        <div>
          <p class="text-sm text-gray-500">Edad</p>
          <p class="text-base font-medium text-gray-900">{{ pacienteEncontrado.edad }} años</p>
        </div>
        <div>
          <p class="text-sm text-gray-500">Género</p>
          <p class="text-base font-medium text-gray-900">{{ pacienteEncontrado.genero }}</p>
        </div>
      </div>

      <!-- Muestras del paciente -->
      <div class="mt-4">
        <h4 class="text-base font-medium text-gray-900 mb-2">Muestras Pendientes</h4>
        <div class="space-y-2">
          <div v-for="muestra in pacienteEncontrado.muestras" :key="muestra.codigo" 
               class="bg-white rounded-lg p-3 border border-gray-200">
            <div class="flex justify-between items-center">
              <div>
                <p class="text-sm font-medium text-gray-900">{{ muestra.codigo }}</p>
                <p class="text-xs text-gray-500">{{ muestra.tipoAnalisis }}</p>
              </div>
              <span :class="[
                'px-2 py-1 rounded-full text-xs font-medium',
                {
                  'bg-warning-50 text-warning-700': muestra.estado === 'Pendiente',
                  'bg-success-50 text-success-700': muestra.estado === 'Completado',
                  'bg-info-50 text-info-700': muestra.estado === 'En Proceso'
                }
              ]">
                {{ muestra.estado }}
              </span>
            </div>
          </div>
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

interface Muestra {
  codigo: string
  tipoAnalisis: string
  estado: string
}

interface Paciente {
  nombre: string
  dni: string
  edad: number
  genero: string
  muestras: Muestra[]
}

const dniPaciente = ref('')
const pacienteEncontrado = ref<Paciente | null>(null)
const error = ref('')

const buscarPaciente = () => {
  // Aquí iría la lógica para buscar el paciente
  // Por ahora, simulamos una búsqueda exitosa
  if (dniPaciente.value) {
    pacienteEncontrado.value = {
      nombre: 'Juan Pérez',
      dni: dniPaciente.value,
      edad: 35,
      genero: 'Masculino',
      muestras: [
        {
          codigo: 'M-2024-001',
          tipoAnalisis: 'Hemograma Completo',
          estado: 'Pendiente'
        },
        {
          codigo: 'M-2024-002',
          tipoAnalisis: 'Perfil Lipídico',
          estado: 'En Proceso'
        }
      ]
    }
    error.value = ''
  } else {
    error.value = 'Por favor, ingrese el DNI o cédula del paciente'
    pacienteEncontrado.value = null
  }
}
</script>