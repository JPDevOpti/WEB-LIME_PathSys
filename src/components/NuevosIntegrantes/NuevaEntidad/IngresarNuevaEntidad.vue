<template>
  <div class="space-y-6">
    <!-- Nombre de la Entidad -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Nombre de la Entidad *
      </label>
      <input
        type="text"
        v-model="formData.nombreEntidad"
        placeholder="Ej: Hospital Central"
        :class="getFieldClasses('nombreEntidad', true)"
        required
        ref="nombreEntidadInput"
      />
    </div>

    <!-- Tipo de Entidad -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Tipo de Entidad *
      </label>
      <select
        v-model="formData.tipoEntidad"
        :class="getFieldClasses('tipoEntidad', true)"
        required
        ref="tipoEntidadInput"
      >
        <option value="">Seleccione un tipo</option>
        <option value="Hospital">Hospital</option>
        <option value="Clínica">Clínica</option>
        <option value="Centro Médico">Centro Médico</option>
        <option value="Laboratorio">Laboratorio</option>
        <option value="Otro">Otro</option>
      </select>
    </div>

    <!-- RUC / NIT / Código -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        RUC / NIT / Código de la Entidad *
      </label>
      <input
        type="text"
        v-model="formData.ruc"
        placeholder="Ej: 12345678901"
        :class="getFieldClasses('ruc', true)"
        required
        ref="rucInput"
      />
    </div>

    <!-- Dirección -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Dirección *
      </label>
      <input
        type="text"
        v-model="formData.direccion"
        placeholder="Ej: Av. Principal 1234, Ciudad"
        :class="getFieldClasses('direccion', true)"
        required
        ref="direccionInput"
      />
    </div>

    <!-- Teléfono -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Teléfono
      </label>
      <input
        type="tel"
        v-model="formData.telefono"
        placeholder="Ej: 987654321"
        :class="getFieldClasses('telefono')"
        ref="telefonoInput"
      />
    </div>

    <!-- Email -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Email
      </label>
      <input
        type="email"
        v-model="formData.email"
        placeholder="Ej: contacto@entidad.com"
        :class="getFieldClasses('email')"
        ref="emailInput"
      />
    </div>

    <!-- Responsable / Representante -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Responsable / Representante
      </label>
      <input
        type="text"
        v-model="formData.responsable"
        placeholder="Nombre del responsable o representante legal"
        :class="getFieldClasses('responsable')"
        ref="responsableInput"
      />
    </div>

    <!-- Observaciones -->
    <div>
      <label class="mb-1.5 block text-sm font-medium text-gray-700">
        Observaciones
      </label>
      <textarea
        v-model="formData.observaciones"
        placeholder="Observaciones adicionales sobre la entidad"
        rows="3"
        :class="getTextareaClasses('observaciones')"
      ></textarea>
    </div>

    <!-- Botones de Acción -->
    <div class="flex items-center justify-end space-x-3 pt-6">
      <button
        @click="limpiarFormulario"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 focus:border-gray-400 transition-colors"
        :disabled="isLoading"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Limpiar
      </button>

      <button
        @click="guardarEntidad"
        type="button"
        class="inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        :disabled="isLoading"
      >
        <svg
          v-if="isLoading"
          class="animate-spin -ml-1 mr-2 h-4 w-4 text-white"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <svg
          v-else
          class="w-4 h-4 mr-2"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"
          />
        </svg>
        {{ isLoading ? 'Guardando...' : 'Guardar Entidad' }}
      </button>
    </div>

    <!-- Mensaje de Estado -->
    <div v-if="statusMessage" :class="statusMessageClasses" class="mt-6">
      <div class="flex items-center space-x-3">
        <div class="flex-shrink-0">
          <svg
            :class="statusIconClass"
            class="w-8 h-8"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              v-if="statusType === 'success'"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
            <path
              v-else
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </div>
        <div class="flex-1">
          <p class="font-bold text-lg">{{ statusMessage }}</p>
          <div v-if="statusType === 'success'" class="mt-3">
            <div class="bg-white bg-opacity-50 rounded-md border border-green-300 p-3">
              <p class="text-sm font-medium text-green-800 mb-2">Datos de la Entidad Registrada:</p>
              <div class="space-y-1">
                <p class="text-lg font-semibold text-green-900">{{ formData.nombreEntidad }}</p>
                <p class="text-base text-green-800">Tipo: <span class="font-semibold">{{ formData.tipoEntidad }}</span></p>
                <p class="text-base text-green-800">RUC/NIT: <span class="font-mono font-bold">{{ formData.ruc }}</span></p>
                <p class="text-base text-green-800">Dirección: <span class="font-semibold">{{ formData.direccion }}</span></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed, ref } from 'vue'

const isLoading = ref(false)
const statusMessage = ref('')
const statusType = ref<'success' | 'error'>('success')
const hasAttemptedSubmit = ref(false)

const formData = reactive({
  nombreEntidad: '',
  tipoEntidad: '',
  ruc: '',
  direccion: '',
  telefono: '',
  email: '',
  responsable: '',
  observaciones: ''
})

const nombreEntidadInput = ref<HTMLInputElement | null>(null)
const tipoEntidadInput = ref<HTMLSelectElement | null>(null)
const rucInput = ref<HTMLInputElement | null>(null)
const direccionInput = ref<HTMLInputElement | null>(null)
const telefonoInput = ref<HTMLInputElement | null>(null)
const emailInput = ref<HTMLInputElement | null>(null)
const responsableInput = ref<HTMLInputElement | null>(null)

const isFormValid = computed(() => {
  return !!(
    formData.nombreEntidad.trim() &&
    formData.tipoEntidad.trim() &&
    formData.ruc.trim() &&
    formData.direccion.trim()
  )
})

const statusMessageClasses = computed(() => {
  return statusType.value === 'success'
    ? 'rounded-lg bg-green-50 border border-green-200 p-4'
    : 'rounded-lg bg-red-50 border border-red-200 p-4'
})

const statusIconClass = computed(() => {
  return statusType.value === 'success' ? 'text-green-600' : 'text-red-600'
})

const limpiarFormulario = () => {
  formData.nombreEntidad = ''
  formData.tipoEntidad = ''
  formData.ruc = ''
  formData.direccion = ''
  formData.telefono = ''
  formData.email = ''
  formData.responsable = ''
  formData.observaciones = ''
  statusMessage.value = ''
  hasAttemptedSubmit.value = false
  nombreEntidadInput.value?.focus()
}

const guardarEntidad = async () => {
  hasAttemptedSubmit.value = true
  if (!isFormValid.value) {
    statusType.value = 'error'
    statusMessage.value = 'Por favor complete todos los campos obligatorios (*)'
    if (!formData.nombreEntidad.trim()) nombreEntidadInput.value?.focus()
    else if (!formData.tipoEntidad.trim()) tipoEntidadInput.value?.focus()
    else if (!formData.ruc.trim()) rucInput.value?.focus()
    else if (!formData.direccion.trim()) direccionInput.value?.focus()
    return
  }
  isLoading.value = true
  statusMessage.value = ''
  try {
    // Aquí iría la lógica para enviar los datos a un backend
    // await api.registrarEntidad(formData)
    const dataToSave = { ...formData }
    console.log('Datos de la entidad a guardar:', dataToSave)
    await new Promise(resolve => setTimeout(resolve, 1000))
    statusType.value = 'success'
    statusMessage.value = 'Entidad guardada exitosamente'
  } catch (error) {
    statusType.value = 'error'
    statusMessage.value = 'Error al guardar la entidad. Intente nuevamente.'
    console.error('Error al guardar entidad:', error)
  } finally {
    isLoading.value = false
  }
}

const getFieldClasses = (fieldName: keyof typeof formData, isRequired = false) => {
  const baseClasses = "h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  let fieldIsInvalid = false;
  if (isRequired && hasAttemptedSubmit.value && !formData[fieldName]) {
    fieldIsInvalid = true
  }
  if (fieldIsInvalid) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10`
}

const getTextareaClasses = (fieldName: keyof typeof formData, isRequired = false) => {
  const baseClasses = "w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3 resize-none"
  if (isRequired && hasAttemptedSubmit.value && !formData[fieldName]) {
    return `${baseClasses} border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50`
  }
  return `${baseClasses} border-gray-300 focus:border-brand-300 focus:ring-brand-500/10`
}
</script>