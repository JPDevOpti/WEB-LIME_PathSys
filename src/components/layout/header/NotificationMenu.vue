<!--
  Componente NotificationMenu
  Menú de notificaciones para el sistema de control de muestras.
  Muestra alertas sobre muestras urgentes, resultados listos y cambios de estado.
  Incluye soporte para tema oscuro y responsive.
-->
<template>
  <div class="relative" ref="dropdownRef">
    <button
      class="relative flex items-center justify-center text-gray-500 transition-colors bg-white border border-gray-200 rounded-full hover:text-dark-900 h-11 w-11 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-800 dark:bg-gray-900 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white"
      @click="toggleDropdown"
      aria-label="Notificaciones"
      :aria-expanded="dropdownOpen"
    >
      <span
        :class="{ hidden: !notifying, flex: notifying }"
        class="absolute right-0 top-0.5 z-1 h-2 w-2 rounded-full bg-orange-400"
      >
        <span class="absolute inline-flex w-full h-full bg-orange-400 rounded-full opacity-75 -z-1 animate-ping"></span>
      </span>
      <span class="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-500 text-[10px] font-medium text-white" v-if="unreadCount > 0">
        {{ unreadCount }}
      </span>
      <svg
        class="fill-current transform transition-transform duration-200 hover:scale-110"
        width="22"
        height="22"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M12 2C11.2044 2 10.4413 2.31607 9.87868 2.87868C9.31607 3.44129 9 4.20435 9 5V5.29C6.89162 5.57962 5.07962 7.39162 4.79 9.5L4.5 14.5H4C3.73478 14.5 3.48043 14.6054 3.29289 14.7929C3.10536 14.9804 3 15.2348 3 15.5C3 15.7652 3.10536 16.0196 3.29289 16.2071C3.48043 16.3946 3.73478 16.5 4 16.5H5H19H20C20.2652 16.5 20.5196 16.3946 20.7071 16.2071C20.8946 16.0196 21 15.7652 21 15.5C21 15.2348 20.8946 14.9804 20.7071 14.7929C20.5196 14.6054 20.2652 14.5 20 14.5H19.5V9.5C19.5 7.39162 17.688 5.57962 15.5796 5.29V5C15.5796 4.20435 15.2635 3.44129 14.7009 2.87868C14.1383 2.31607 13.3752 2 12.5796 2H12Z"
          fill="currentColor"
        />
        <path
          d="M12 18.5C12.8284 18.5 13.5 17.8284 13.5 17H10.5C10.5 17.8284 11.1716 18.5 12 18.5Z"
          fill="currentColor"
        />
        <path
          d="M12 2C11.2044 2 10.4413 2.31607 9.87868 2.87868C9.31607 3.44129 9 4.20435 9 5V5.29C6.89162 5.57962 5.07962 7.39162 4.79 9.5L4.5 14.5H4C3.73478 14.5 3.48043 14.6054 3.29289 14.7929C3.10536 14.9804 3 15.2348 3 15.5C3 15.7652 3.10536 16.0196 3.29289 16.2071C3.48043 16.3946 3.73478 16.5 4 16.5H5H19H20C20.2652 16.5 20.5196 16.3946 20.7071 16.2071C20.8946 16.0196 21 15.7652 21 15.5C21 15.2348 20.8946 14.9804 20.7071 14.7929C20.5196 14.6054 20.2652 14.5 20 14.5H19.5V9.5C19.5 7.39162 17.688 5.57962 15.5796 5.29V5C15.5796 4.20435 15.2635 3.44129 14.7009 2.87868C14.1383 2.31607 13.3752 2 12.5796 2H12Z"
          stroke="currentColor"
          stroke-width="1.5"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>

    <div
      v-if="dropdownOpen"
      class="absolute -right-[240px] mt-[17px] flex h-[480px] w-[350px] flex-col rounded-2xl border border-gray-200 bg-white p-3 shadow-theme-lg dark:border-gray-800 dark:bg-gray-dark sm:w-[361px] lg:right-0"
      role="menu"
      aria-label="Menú de notificaciones"
    >
      <div class="flex items-center justify-between pb-3 mb-3 border-b border-gray-100 dark:border-gray-800">
        <h5 class="text-lg font-semibold text-gray-800 dark:text-white/90">Notificaciones</h5>
        <button @click="closeDropdown" class="text-gray-500 dark:text-gray-400" aria-label="Cerrar notificaciones">
          <svg class="fill-current" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M6.21967 7.28131C5.92678 6.98841 5.92678 6.51354 6.21967 6.22065C6.51256 5.92775 6.98744 5.92775 7.28033 6.22065L11.999 10.9393L16.7176 6.22078C17.0105 5.92789 17.4854 5.92788 17.7782 6.22078C18.0711 6.51367 18.0711 6.98855 17.7782 7.28144L13.0597 12L17.7782 16.7186C18.0711 17.0115 18.0711 17.4863 17.7782 17.7792C17.4854 18.0721 17.0105 18.0721 16.7176 17.7792L11.999 13.0607L7.28033 17.7794C6.98744 18.0722 6.51256 18.0722 6.21967 17.7794C5.92678 17.4865 5.92678 17.0116 6.21967 16.7187L10.9384 12L6.21967 7.28131Z" fill=""/>
          </svg>
        </button>
      </div>

      <ul class="flex flex-col h-auto overflow-y-auto custom-scrollbar">
        <li v-for="notification in notifications" :key="notification.id" @click="handleItemClick(notification)">
          <a
            class="flex gap-3 rounded-lg border-b border-gray-100 p-3 px-4.5 py-3 hover:bg-gray-100 dark:border-gray-800 dark:hover:bg-white/5"
            :class="{ 'bg-blue-50 dark:bg-blue-900/20': !notification.read }"
            href="#"
          >
            <span class="relative block w-full h-10 rounded-full z-1 max-w-10">
              <span :class="getStatusColor(notification.type)" class="flex h-10 w-10 items-center justify-center rounded-full">
                <svg class="h-5 w-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="getStatusIcon(notification.type)" />
                </svg>
              </span>
            </span>

            <span class="block">
              <span class="mb-1.5 block text-theme-sm text-gray-500 dark:text-gray-400">
                <span class="font-medium text-gray-800 dark:text-white/90">
                  {{ notification.title }}
                </span>
                {{ notification.message }}
              </span>

              <span class="flex items-center gap-2 text-gray-500 text-theme-xs dark:text-gray-400">
                <span>{{ notification.type }}</span>
                <span class="w-1 h-1 bg-gray-400 rounded-full"></span>
                <span>{{ notification.time }}</span>
              </span>
            </span>
          </a>
        </li>
      </ul>

      <button
        @click="clearNotifications"
        class="mt-3 flex items-center justify-center gap-2 rounded-lg border border-gray-300 bg-white p-3 text-theme-sm font-medium text-gray-700 shadow-theme-xs hover:bg-gray-50 hover:text-gray-800 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-white/[0.03] dark:hover:text-gray-200"
      >
        <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M19 7L18.1327 19.1425C18.0579 20.1891 17.187 21 16.1378 21H7.86224C6.81296 21 5.94208 20.1891 5.86732 19.1425L5 7M10 11V17M14 11V17M15 7V4C15 3.44772 14.5523 3 14 3H10C9.44772 3 9 3.44772 9 4V7M4 7H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Limpiar notificaciones
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'

interface Notification {
  id: number
  title: string
  message: string
  type: 'urgente' | 'resultado' | 'estado' | 'sistema'
  time: string
  read: boolean
}

const dropdownOpen = ref(false)
const notifying = ref(false)
const dropdownRef = ref<HTMLElement | null>(null)

const notifications = ref<Notification[]>([
  {
    id: 1,
    title: 'Muestra Urgente',
    message: 'La muestra M-2024-108 requiere atención inmediata',
    type: 'urgente',
    time: '2 min atrás',
    read: false
  },
  {
    id: 2,
    title: 'Resultado Listo',
    message: 'Los resultados de la muestra M-2024-109 están disponibles',
    type: 'resultado',
    time: '15 min atrás',
    read: false
  },
  {
    id: 3,
    title: 'Cambio de Estado',
    message: 'La muestra M-2024-110 ha sido validada',
    type: 'estado',
    time: '1 hora atrás',
    read: true
  },
  {
    id: 4,
    title: 'Sistema',
    message: 'Se ha completado la sincronización de datos',
    type: 'sistema',
    time: '2 horas atrás',
    read: true
  }
])

const unreadCount = computed(() => {
  return notifications.value.filter(n => !n.read).length
})

const getStatusColor = (type: string) => {
  const colors = {
    urgente: 'bg-red-500',
    resultado: 'bg-green-500',
    estado: 'bg-blue-500',
    sistema: 'bg-gray-500'
  }
  return colors[type as keyof typeof colors] || 'bg-gray-500'
}

const getStatusIcon = (type: string) => {
  const icons = {
    urgente: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z',
    resultado: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z',
    estado: 'M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
    sistema: 'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z'
  }
  return icons[type as keyof typeof icons] || icons.sistema
}

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
  notifying.value = false
}

const closeDropdown = () => {
  dropdownOpen.value = false
}

const handleClickOutside = (event: MouseEvent) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    closeDropdown()
  }
}

const handleItemClick = (notification: Notification) => {
  notification.read = true
  notifying.value = unreadCount.value > 0
  // Aquí podrías navegar a la página de la muestra
  closeDropdown()
}

const clearNotifications = () => {
  notifications.value = []
  notifying.value = false
  closeDropdown()
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
