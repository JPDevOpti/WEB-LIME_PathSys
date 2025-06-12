<!--
  Componente DropdownMenu
  Menú desplegable con animaciones y submenús.
  Permite configurar el botón, el menú, los items y la posición.
  Incluye soporte para accesibilidad y eventos de clic.
-->
<template>
  <!-- Contenedor principal del menú desplegable -->
  <div 
    class="relative" 
    v-click-outside="closeDropdown" 
    ref="dropdown"
    @keydown.esc="closeDropdown"
    @keydown.tab="handleTab"
  >
    <!-- Botón que activa el menú desplegable -->
    <button 
      @click="toggleDropdown" 
      :class="buttonClass"
      :aria-expanded="open"
      :aria-controls="menuId"
      :aria-haspopup="true"
      :aria-label="ariaLabel"
    >
      <!-- Slot para personalizar el icono del botón -->
      <slot name="icon">
        <!-- Icono por defecto (tres puntos verticales) -->
        <svg
          class="fill-current"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M5.99902 10.245C6.96552 10.245 7.74902 11.0285 7.74902 11.995V12.005C7.74902 12.9715 6.96552 13.755 5.99902 13.755C5.03253 13.755 4.24902 12.9715 4.24902 12.005V11.995C4.24902 11.0285 5.03253 10.245 5.99902 10.245ZM17.999 10.245C18.9655 10.245 19.749 11.0285 19.749 11.995V12.005C19.749 12.9715 18.9655 13.755 17.999 13.755C17.0325 13.755 16.249 12.9715 16.249 12.005V11.995C16.249 11.0285 17.0325 10.245 17.999 10.245ZM13.749 11.995C13.749 11.0285 12.9655 10.245 11.999 10.245C11.0325 10.245 10.249 11.0285 10.249 11.995V12.005C10.249 12.9715 11.0325 13.755 11.999 13.755C12.9655 13.755 13.749 12.9715 13.749 12.005V11.995Z"
            fill="currentColor"
          />
        </svg>
      </slot>
    </button>

    <!-- Menú desplegable con animaciones -->
    <Transition
      enter-active-class="transition duration-100 ease-out"
      enter-from-class="transform scale-95 opacity-0"
      enter-to-class="transform scale-100 opacity-100"
      leave-active-class="transition duration-75 ease-in"
      leave-from-class="transform scale-100 opacity-100"
      leave-to-class="transform scale-95 opacity-0"
    >
      <div 
        v-if="open" 
        :id="menuId"
        :class="[
          menuClass,
          position === 'right' ? 'right-0' : 'left-0',
          position === 'top' ? 'bottom-full top-auto' : 'top-full'
        ]"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="dropdown-button"
      >
        <!-- Slot para personalizar el contenido del menú -->
        <slot name="menu">
          <!-- Items del menú por defecto -->
          <template v-for="(item, index) in menuItems" :key="index">
            <!-- Submenú (menú anidado) -->
            <div v-if="item.submenu" class="relative group">
              <button
                :class="[itemClass, 'w-full flex justify-between items-center']"
                @click="toggleSubmenu(index)"
                :aria-expanded="openSubmenus[index]"
                :aria-controls="`submenu-${index}`"
              >
                {{ item.label }}
                <!-- Icono de flecha para submenú -->
                <svg 
                  class="w-4 h-4 ml-2 transform transition-transform"
                  :class="{ 'rotate-180': openSubmenus[index] }"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
              </button>
              <!-- Contenedor del submenú -->
              <div
                v-if="openSubmenus[index]"
                :id="`submenu-${index}`"
                class="absolute left-full top-0 w-48 p-2 space-y-1 bg-white border border-gray-200 rounded-2xl shadow-lg dark:border-gray-800 dark:bg-gray-dark"
                role="menu"
              >
                <!-- Items del submenú -->
                <template v-for="(subItem, subIndex) in item.submenu" :key="`sub-${subIndex}`">
                  <!-- Enlace de router para navegación -->
                  <router-link
                    v-if="subItem.to"
                    :to="subItem.to"
                    @click="handleMenuItemClick(subItem.onClick)"
                    :class="itemClass"
                    role="menuitem"
                  >
                    {{ subItem.label }}
                  </router-link>
                  <!-- Botón normal para acciones -->
                  <button
                    v-else
                    @click="handleMenuItemClick(subItem.onClick)"
                    :class="itemClass"
                    role="menuitem"
                  >
                    {{ subItem.label }}
                  </button>
                </template>
              </div>
            </div>

            <!-- Item de menú regular (sin submenú) -->
            <template v-else>
              <!-- Enlace de router para navegación -->
              <router-link
                v-if="item.to"
                :to="item.to"
                @click="handleMenuItemClick(item.onClick)"
                :class="itemClass"
                role="menuitem"
              >
                {{ item.label }}
              </router-link>

              <!-- Botón normal para acciones -->
              <button
                v-else
                @click="handleMenuItemClick(item.onClick)"
                :class="itemClass"
                role="menuitem"
              >
                {{ item.label }}
              </button>
            </template>
          </template>
        </slot>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import vClickOutside from './v-click-outside.vue'

// Función para generar un ID único para el menú
const generateId = () => {
  return 'dropdown-' + Math.random().toString(36).substr(2, 9)
}

// Interfaz para definir la estructura de un item del menú
interface MenuItem {
  label: string        // Texto que se muestra en el menú
  to?: string         // Ruta para navegación (opcional)
  onClick?: () => void // Función a ejecutar al hacer clic (opcional)
  submenu?: MenuItem[] // Submenú anidado (opcional)
}

// Interfaz para las propiedades del componente
interface Props {
  menuItems: MenuItem[]  // Lista de items del menú
  buttonClass?: string   // Clases CSS para el botón
  menuClass?: string     // Clases CSS para el menú
  itemClass?: string     // Clases CSS para los items
  position?: 'left' | 'right' | 'top'  // Posición del menú
  ariaLabel?: string     // Etiqueta para accesibilidad
}

// Definición de propiedades con valores por defecto
const props = withDefaults(defineProps<Props>(), {
  menuItems: () => [],
  buttonClass: 'text-gray-500 dark:text-gray-400',
  menuClass: 'absolute z-40 w-40 p-2 space-y-1 bg-white border border-gray-200 rounded-2xl shadow-lg dark:border-gray-800 dark:bg-gray-dark',
  itemClass: 'flex w-full px-3 py-2 font-medium text-left text-gray-500 rounded-lg text-theme-xs hover:bg-gray-100 hover:text-gray-700 dark:text-gray-400 dark:hover:bg-white/5 dark:hover:text-gray-300',
  position: 'right',
  ariaLabel: 'Menu desplegable'
})

// Estado del componente
const menuId = computed(() => generateId())  // ID único para el menú
const open = ref(false)  // Estado de apertura del menú
const openSubmenus = ref<Record<number, boolean>>({})  // Estado de submenús abiertos

// Función para alternar la apertura del menú
const toggleDropdown = () => {
  open.value = !open.value
  if (!open.value) {
    openSubmenus.value = {}  // Cierra todos los submenús al cerrar el menú principal
  }
}

// Función para cerrar el menú
const closeDropdown = () => {
  open.value = false
  openSubmenus.value = {}
}

// Función para alternar la apertura de un submenú
const toggleSubmenu = (index: number) => {
  openSubmenus.value[index] = !openSubmenus.value[index]
}

// Función para manejar el clic en un item del menú
const handleMenuItemClick = (callback?: () => void) => {
  if (typeof callback === 'function') {
    callback()  // Ejecuta la función de callback si existe
  }
  closeDropdown()  // Cierra el menú después de la acción
}

// Función para manejar la navegación por teclado
const handleTab = (event: KeyboardEvent) => {
  if (open.value && !event.shiftKey) {
    const focusableElements = document.querySelectorAll(
      `#${menuId.value} button, #${menuId.value} a`
    )
    if (focusableElements.length > 0) {
      event.preventDefault()
      ;(focusableElements[0] as HTMLElement).focus()
    }
  }
}
</script>

<script lang="ts">
// Registro de la directiva personalizada para detectar clics fuera del menú
export default {
  directives: {
    clickOutside: vClickOutside,
  },
}
</script>
