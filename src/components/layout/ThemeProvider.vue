<template>
  <slot></slot>
</template>

<script setup lang="ts">
import { ref, provide, onMounted } from 'vue'

const isDarkMode = ref(false)

onMounted(() => {
      document.documentElement.classList.remove('dark')
})

provide('theme', {
  isDarkMode,
  toggleTheme: () => {}
})
</script>

<script lang="ts">
import { inject } from 'vue'

export function useTheme() {
  const theme = inject('theme')
  if (!theme) {
    throw new Error('useTheme must be used within a ThemeProvider')
  }
  return theme
}
</script>
