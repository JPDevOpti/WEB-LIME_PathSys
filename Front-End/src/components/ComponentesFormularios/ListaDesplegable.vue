<template>
  <div class="relative">
    <label v-if="label" class="mb-1.5 block text-sm font-medium text-gray-700">
      {{ label }}<span v-if="required" class="text-red-500">*</span>
    </label>
    <div class="relative">
      <input
        type="text"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        @focus="showDropdown = true"
        @blur="hideDropdown"
        :placeholder="placeholder"
        :class="inputClasses"
        :required="required"
        ref="inputRef"
        autocomplete="off"
      />
      <button
        type="button"
        @mousedown.prevent="toggleDropdown"
        class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-500"
        tabindex="-1"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </button>
    </div>
    <div
      v-if="showDropdown"
      class="absolute z-50 w-full mt-1 bg-white rounded-md shadow-lg border border-gray-200 max-h-60 overflow-auto"
    >
      <ul class="py-1">
        <li
          v-for="option in filteredOptions"
          :key="option.id || option.nombre || option.value || option.label"
          @mousedown.prevent="selectOption(option)"
          class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer"
        >
          {{ option[labelKey] }}
        </li>
        <li
          v-if="filteredOptions.length === 0"
          class="px-4 py-2 text-sm text-gray-500"
        >
          No se encontraron resultados
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted } from 'vue'

interface Option {
  id?: string | number
  nombre?: string
  value?: string | number
  label?: string
  [key: string]: any
}

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  options: {
    type: Array as () => Option[],
    required: true
  },
  label: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: ''
  },
  required: {
    type: Boolean,
    default: false
  },
  error: {
    type: Boolean,
    default: false
  },
  labelKey: {
    type: String,
    default: 'nombre'
  }
})

const emit = defineEmits(['update:modelValue'])
const showDropdown = ref(false)
const inputRef = ref<HTMLInputElement | null>(null)

const filteredOptions = computed(() => {
  const searchTerm = (props.modelValue || '').toLowerCase()
  return props.options.filter(option => {
    const label = (option[props.labelKey] || '').toLowerCase()
    return label.includes(searchTerm)
  })
})

function selectOption(option: Option) {
  emit('update:modelValue', option[props.labelKey])
  showDropdown.value = false
}

function toggleDropdown() {
  showDropdown.value = !showDropdown.value
  if (showDropdown.value && inputRef.value) {
    inputRef.value.focus()
  }
}

function hideDropdown() {
  setTimeout(() => {
    showDropdown.value = false
  }, 200)
}

const inputClasses = computed(() => {
  const base = "h-11 w-full rounded-lg border bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3"
  if (props.error && props.required && !props.modelValue) {
    return base + ' border-red-500 focus:border-red-500 focus:ring-red-500/10 bg-red-50'
  }
  return base + ' border-gray-300 focus:border-brand-300 focus:ring-brand-500/10'
})
</script>
