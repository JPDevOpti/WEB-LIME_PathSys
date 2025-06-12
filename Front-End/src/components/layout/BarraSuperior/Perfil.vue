<!--
  Componente UserMenu
  Menú de usuario en el encabezado.
  Muestra el perfil del usuario, opciones de perfil y cierre de sesión.
  Incluye soporte para tema oscuro y responsive.
-->
<template>
  <div class="relative" ref="dropdownRef">
    <button
      class="flex items-center text-gray-700 dark:text-gray-400 hover:text-primary-500 dark:hover:text-primary-400 transition-colors duration-200"
      @click.prevent="toggleDropdown"
    >
      <span class="mr-3 overflow-hidden rounded-full h-11 w-11 ring-2 ring-gray-200 dark:ring-gray-700 hover:ring-primary-500 dark:hover:ring-primary-400 transition-all duration-200">
        <img src="/images/user/user-21.jpg" alt="Usuario" class="w-full h-full object-cover" />
      </span>

      <span class="block mr-1 font-medium text-theme-sm">Ana</span>

      <ChevronDownIcon 
        :class="{ 'rotate-180': dropdownOpen }" 
        class="transition-transform duration-200"
      />
    </button>

    <!-- Dropdown Start -->
    <div
      v-if="dropdownOpen"
      class="absolute right-0 mt-[17px] flex w-[260px] flex-col rounded-2xl border border-gray-200 bg-white p-3 shadow-theme-lg dark:border-gray-800 dark:bg-gray-dark animate-fadeIn"
    >
      <div class="p-2">
        <span class="block font-medium text-gray-700 text-theme-sm dark:text-gray-400">
          Ana María Velasquez
        </span>
        <span class="mt-0.5 block text-theme-xs text-gray-500 dark:text-gray-400">
          ana.lime@udea.edu.co
        </span>
      </div>

      <ul class="flex flex-col gap-1 pt-4 pb-3 border-b border-gray-200 dark:border-gray-800">
        <li v-for="item in menuItems" :key="item.href">
          <router-link
            :to="item.href"
            class="flex items-center gap-3 px-3 py-2 font-medium text-gray-700 rounded-lg group text-theme-sm hover:bg-gray-100 hover:text-primary-500 dark:text-gray-400 dark:hover:bg-white/5 dark:hover:text-primary-400 transition-all duration-200"
          >
            <component
              :is="item.icon"
              class="text-gray-500 group-hover:text-primary-500 dark:group-hover:text-primary-400 transition-colors duration-200"
            />
            {{ item.text }}
          </router-link>
        </li>
      </ul>
      <router-link
        to="/signin"
        @click="signOut"
        class="flex items-center gap-3 px-3 py-2 mt-3 font-medium text-gray-700 rounded-lg group text-theme-sm hover:bg-red-50 hover:text-red-500 dark:text-gray-400 dark:hover:bg-red-500/10 dark:hover:text-red-400 transition-all duration-200"
      >
        <LogoutIcon
          class="text-gray-500 group-hover:text-red-500 dark:group-hover:text-red-400 transition-colors duration-200"
        />
        Cerrar sesión
      </router-link>
    </div>
    <!-- Dropdown End -->
  </div>
</template>

<script setup lang="ts">
import { UserCircleIcon, ChevronDownIcon, LogoutIcon, InfoCircleIcon } from '@/icons'
import { RouterLink } from 'vue-router'
import { ref, onMounted, onUnmounted } from 'vue'

const dropdownOpen = ref(false)
const dropdownRef = ref<HTMLDivElement | null>(null)

const menuItems = [
  { href: '/profile', icon: UserCircleIcon, text: 'Editar perfil' },
  { href: '/profile', icon: InfoCircleIcon, text: 'Soporte' },
]

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

const closeDropdown = () => {
  dropdownOpen.value = false
}

const signOut = () => {
  // Implement sign out logic here
  console.log('Cerrando sesión...')
  closeDropdown()
}

const handleClickOutside = (event: MouseEvent) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target as Node)) {
    closeDropdown()
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.2s ease-out;
}
</style>
