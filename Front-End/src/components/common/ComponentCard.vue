<!--
  Componente ComponentCard
  Muestra una tarjeta con un encabezado, cuerpo y pie de página.
  Permite configurar el título, descripción, clases adicionales, estado de carga y acciones.
-->
<template>
  <div
    :class="[
      'rounded-2xl border border-gray-200 bg-white dark:border-gray-800 dark:bg-white/[0.03]',
      { 'card-hover': clickable },
      { 'opacity-50 cursor-not-allowed': disabled },
      className,
    ]"
    @click="handleClick"
  >
    <!-- Card Header -->
    <div class="px-6 py-5">
      <div class="flex items-center justify-between">
        <div>
          <h3 class="text-base font-medium text-gray-800 dark:text-white/90">
            {{ title }}
          </h3>
          <p v-if="desc" class="mt-1 text-sm text-gray-500 dark:text-gray-400">
            {{ desc }}
          </p>
        </div>
        <div v-if="$slots.header" class="ml-4">
          <slot name="header"></slot>
        </div>
      </div>
    </div>

    <!-- Card Body -->
    <div 
      class="p-4 border-t border-gray-100 dark:border-gray-800 sm:p-6"
      :class="{ 'bg-gray-50 dark:bg-gray-800/50': loading }"
    >
      <div v-if="loading" class="flex items-center justify-center py-8">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-brand-500"></div>
      </div>
      <div v-else class="space-y-5">
        <slot></slot>
      </div>
    </div>

    <!-- Card Footer -->
    <div v-if="$slots.footer" class="px-6 py-4 border-t border-gray-100 dark:border-gray-800">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  /** Título de la tarjeta */
  title: string
  /** Clases CSS adicionales */
  className?: string
  /** Descripción opcional */
  desc?: string
  /** Si la tarjeta es clickeable */
  clickable?: boolean
  /** Si la tarjeta está deshabilitada */
  disabled?: boolean
  /** Si la tarjeta está en estado de carga */
  loading?: boolean
}

const props = defineProps<Props>()

const emit = defineEmits<{
  (e: 'click', event: MouseEvent): void
}>()

const handleClick = (event: MouseEvent) => {
  if (props.disabled || props.loading) return
  if (props.clickable) {
    emit('click', event)
  }
}
</script>

<style scoped>
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.card-hover {
  position: relative;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform, box-shadow;
  transform: translateY(0);
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}

.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08),
              0 4px 6px -4px rgba(0, 0, 0, 0.05);
}
</style>
