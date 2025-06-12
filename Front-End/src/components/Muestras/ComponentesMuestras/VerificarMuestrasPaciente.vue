<template>
  <div class="space-y-4">
    <div class="flex flex-col gap-4 sm:flex-row">
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
          @keyup.enter="buscarPaciente"
        />
      </div>
      <div class="flex items-end sm:ml-4 gap-2">
        <button
          @click="buscarPaciente"
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

    <!-- Resultados de la búsqueda -->
    <div v-if="pacienteEncontrado" class="bg-gray-50 rounded-lg border border-gray-200 p-6 mt-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Información del Paciente -->
        <div>
          <h3 class="font-semibold mb-2 text-gray-700">Información del Paciente</h3>
          <div class="text-sm text-gray-800 space-y-1">
            <div><span class="font-medium">Nombre:</span> {{ pacienteEncontrado.nombre }}</div>
            <div><span class="font-medium">DNI/Cédula:</span> {{ pacienteEncontrado.dni }}</div>
            <div><span class="font-medium">Edad:</span> {{ pacienteEncontrado.edad }} años</div>
            <div><span class="font-medium">Género:</span> {{ pacienteEncontrado.genero }}</div>
          </div>
        </div>
        <!-- Muestras del Paciente -->
        <div>
          <h3 class="font-semibold mb-2 text-gray-700">Muestras del Paciente</h3>
          <div class="space-y-2">
            <div v-for="muestra in pacienteEncontrado.muestras" 
                 :key="muestra.codigo" 
                 @click="seleccionarMuestra(muestra)"
                 class="bg-white rounded-lg p-3 border border-gray-200 hover:border-brand-500 hover:shadow-md cursor-pointer transition-all duration-200"
            >
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
    </div>

    <!-- Mensaje de error -->
    <div v-if="error" class="bg-red-50 rounded-lg p-4">
      <p class="text-sm text-red-700">{{ error }}</p>
    </div>
    <div v-if="!pacienteEncontrado && error === '' && dniPaciente && busquedaRealizada" class="bg-yellow-50 rounded-lg p-4 border border-yellow-200 mt-4">
      <div class="flex items-center">
        <svg class="w-5 h-5 text-yellow-600 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p class="text-sm text-yellow-700">No se ha encontrado el paciente</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

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

const dniPaciente = ref('')
const pacienteEncontrado = ref<Paciente | null>(null)
const error = ref('')
const busquedaRealizada = ref(false)
const props = defineProps<{ dniExterno?: string }>()

// Definir emits
const emit = defineEmits<{
  'muestra-encontrada': [muestra: MuestraCompleta]
  'limpiar-campos': []
}>()

watch(() => props.dniExterno, (nuevoDni) => {
  if (nuevoDni && nuevoDni !== dniPaciente.value) {
    dniPaciente.value = nuevoDni
    buscarPaciente()
  }
})

const buscarPaciente = () => {
  busquedaRealizada.value = true
  // Aquí iría la lógica para buscar el paciente
  // Por ahora, simulamos una búsqueda exitosa
  if (dniPaciente.value) {
    // Simulación: solo existe el paciente con dni 12345678
    if (dniPaciente.value === '12345678') {
      pacienteEncontrado.value = {
        nombre: 'Juan Pérez',
        dni: dniPaciente.value,
        edad: 35,
        genero: 'Masculino',
        muestras: [
          {
            codigo: '2024-0001',
            tipoAnalisis: 'Hemograma Completo',
            estado: 'Pendiente'
          },
          {
            codigo: '2024-0002',
            tipoAnalisis: 'Perfil Lipídico',
            estado: 'En Proceso'
          }
        ]
      }
      error.value = ''
    } else {
      pacienteEncontrado.value = null
      error.value = ''
    }
  } else {
    error.value = 'Por favor, ingrese el DNI o cédula del paciente'
    pacienteEncontrado.value = null
  }
}

const seleccionarMuestra = (muestra: Muestra) => {
  if (!pacienteEncontrado.value) return

  const muestraCompleta: MuestraCompleta = {
    idMuestra: muestra.codigo,
    paciente: {
      nombre: pacienteEncontrado.value.nombre,
      cedula: pacienteEncontrado.value.dni
    },
    tipoAnalisisTexto: muestra.tipoAnalisis,
    estadoTexto: muestra.estado,
    medicoSolicitanteTexto: 'Dr. García Pérez', // Esto vendría de la API
    fechaIngresoTexto: new Date().toLocaleString(), // Esto vendría de la API
    resultadoMacro: '',
    resultadoMicro: '',
    resultadoMetodo: '',
    diagnostico: ''
  }

  emit('muestra-encontrada', muestraCompleta)
}

const limpiarCampos = () => {
  dniPaciente.value = ''
  pacienteEncontrado.value = null
  error.value = ''
  busquedaRealizada.value = false
  emit('limpiar-campos')
}
</script>