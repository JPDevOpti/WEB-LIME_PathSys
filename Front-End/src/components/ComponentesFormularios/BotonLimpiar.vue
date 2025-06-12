<template>
  <button
    @click="handleLimpiar"
    type="button"
    :class="buttonClasses"
    :disabled="disabled"
  >
    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path 
        stroke-linecap="round" 
        stroke-linejoin="round" 
        stroke-width="2" 
        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" 
      />
    </svg>
    {{ etiqueta }}
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'

// Props del componente
interface Props {
  etiqueta?: string
  disabled?: boolean
  clase?: string
}

const props = withDefaults(defineProps<Props>(), {
  etiqueta: 'Limpiar',
  disabled: false,
  clase: ''
})

// Eventos emitidos
const emit = defineEmits<{
  limpiar: []
}>()

// Clases CSS del botón
const buttonClasses = computed(() => {
  const baseClasses = "inline-flex items-center px-4 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 focus:border-gray-400 transition-colors"
  
  if (props.disabled) {
    return `${baseClasses} opacity-50 cursor-not-allowed`
  }
  
  return props.clase ? `${baseClasses} ${props.clase}` : baseClasses
})

// Función para manejar el click del botón
const handleLimpiar = () => {
  if (!props.disabled) {
    emit('limpiar')
  }
}
</script>
