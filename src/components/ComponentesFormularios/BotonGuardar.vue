<template>
  <div :class="soloAlerta ? 'w-full' : 'inline-flex flex-col items-start w-full'">
    <button
      v-if="!soloAlerta"
      :type="type"
      :class="computedClass"
      :disabled="isLoading || disabled"
      @click="handleClick"
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
      <slot>{{ isLoading ? 'Guardando...' : 'Guardar' }}</slot>
    </button>
    <transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0 transform scale-95"
      enter-to-class="opacity-100 transform scale-100"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100 transform scale-100"
      leave-to-class="opacity-0 transform scale-95"
    >
      <div v-if="showError" :class="soloAlerta ? 'rounded-lg bg-red-50 border border-red-200 p-4 flex items-start space-x-3 w-full' : 'rounded-lg bg-red-50 border border-red-200 p-4 mt-4 flex items-start space-x-3 w-full'">
        <div class="flex-shrink-0">
          <svg class="w-8 h-8 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <div class="flex-1">
          <p class="font-bold text-lg text-red-800 mb-1">{{ errorMessage }}</p>
          <ul class="list-disc ml-5 mt-1 text-red-700 text-sm">
            <li v-for="campo in camposInvalidos" :key="campo">{{ campo }}</li>
          </ul>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

const props = defineProps({
  isLoading: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  type: { type: String as () => 'button' | 'submit' | 'reset', default: 'button' },
  campos: { type: Object, required: true }, // { nombre: valor, ... }
  camposObligatorios: { type: Array as () => string[], required: true },
  etiquetas: { type: Object, default: () => ({}) }, // { nombre: 'Etiqueta visible', ... }
  clase: { type: String, default: '' },
  soloAlerta: { type: Boolean, default: false },
  mostrarError: { type: Boolean, default: false } // Para controlar la alerta externamente
})

const emit = defineEmits(['guardar', 'validation-error'])

const showError = ref(false)
const errorMessage = ref('Por favor complete todos los campos requeridos')
const camposInvalidos = ref<string[]>([])

const computedClass = computed(() =>
  props.clase || 'inline-flex items-center px-4 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors'
)

function validarCampos() {
  camposInvalidos.value = props.camposObligatorios.filter(
    campo => !props.campos[campo] || String(props.campos[campo]).trim() === ''
  ).map(campo => props.etiquetas[campo] || campo)
  return camposInvalidos.value.length === 0
}

function handleClick() {
  if (!validarCampos()) {
    showError.value = true
    emit('validation-error', camposInvalidos.value)
  } else {
    showError.value = false
    emit('guardar', { ...props.campos })
  }
}

// Función para validar externamente (útil para soloAlerta)
function validarExternamente() {
  const esValido = validarCampos()
  showError.value = !esValido
  if (!esValido) {
    emit('validation-error', camposInvalidos.value)
  }
  return esValido
}

// Exponer la función para uso externo
defineExpose({ validarExternamente })

watch(() => props.campos, () => {
  if (showError.value) validarCampos()
}, { deep: true })

// Watch para mostrarError prop
watch(() => props.mostrarError, (newVal) => {
  if (newVal && !validarCampos()) {
    showError.value = true
  } else if (!newVal) {
    showError.value = false
  }
})
</script>
