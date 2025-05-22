// Importaciones necesarias de Vue para manejar estado reactivo, ciclo de vida y sistema de inyección
import { ref, computed, onMounted, onUnmounted, provide, inject } from 'vue'
import type { Ref } from 'vue'

// Interfaz que define la estructura del contexto del sidebar
interface SidebarContextType {
  isExpanded: Ref<boolean>                      // Controla si el sidebar está expandido
  isMobileOpen: Ref<boolean>                    // Controla si el sidebar está abierto en vista móvil
  isHovered: Ref<boolean>                       // Controla si el mouse está sobre el sidebar
  activeItem: Ref<string | null>                // Almacena el ítem activo actual
  openSubmenu: Ref<string | null>               // Almacena el submenú abierto actual
  toggleSidebar: () => void                     // Función para alternar el estado del sidebar
  toggleMobileSidebar: () => void               // Función para alternar el estado en móvil
  setIsHovered: (isHovered: boolean) => void    // Función para establecer el estado de hover
  setActiveItem: (item: string | null) => void  // Función para establecer el ítem activo
  toggleSubmenu: (item: string) => void         // Función para alternar submenús
}

// Símbolo único para la inyección de dependencias
const SidebarSymbol = Symbol()

// Función principal que provee el contexto del sidebar
export function useSidebarProvider() {
  // Estados reactivos del sidebar
  const isExpanded = ref(true)                    // Sidebar expandido por defecto
  const isMobileOpen = ref(false)                 // Sidebar móvil cerrado por defecto
  const isMobile = ref(false)                     // Estado de detección móvil
  const isHovered = ref(false)                    // Estado de hover
  const activeItem = ref<string | null>(null)     // Item activo
  const openSubmenu = ref<string | null>(null)    // Submenú abierto

  // Función para manejar cambios de tamaño de ventana
  const handleResize = () => {
    const mobile = window.innerWidth < 768    // Detecta si es vista móvil (< 768px)
    isMobile.value = mobile
    if (!mobile) {
      isMobileOpen.value = false              // Cierra el sidebar móvil en desktop
    }
  }

  // Configuración de eventos al montar el componente
  onMounted(() => {
    handleResize()                                  // Verifica el tamaño inicial
    window.addEventListener('resize', handleResize) // Escucha cambios de tamaño
  })

  // Limpieza de eventos al desmontar
  onUnmounted(() => {
    window.removeEventListener('resize', handleResize)
  })

  // Función para alternar el estado del sidebar
  const toggleSidebar = () => {
    if (isMobile.value) {
      isMobileOpen.value = !isMobileOpen.value    // Toggle en móvil
    } else {
      isExpanded.value = !isExpanded.value        // Toggle en desktop
    }
  }

  // Función específica para alternar el sidebar en móvil
  const toggleMobileSidebar = () => {
    isMobileOpen.value = !isMobileOpen.value
  }

  // Función para establecer el estado de hover
  const setIsHovered = (value: boolean) => {
    isHovered.value = value
  }

  // Función para establecer el ítem activo
  const setActiveItem = (item: string | null) => {
    activeItem.value = item
  }

  // Función para alternar submenús
  const toggleSubmenu = (item: string) => {
    openSubmenu.value = openSubmenu.value === item ? null : item
  }

  // Creación del contexto con todos los estados y funciones
  const context: SidebarContextType = {
    isExpanded: computed(() => (isMobile.value ? false : isExpanded.value)), // Computed para manejar expansión en móvil
    isMobileOpen,
    isHovered,
    activeItem,
    openSubmenu,
    toggleSidebar,
    toggleMobileSidebar,
    setIsHovered,
    setActiveItem,
    toggleSubmenu,
  }

  // Provee el contexto para los componentes hijos
  provide(SidebarSymbol, context)

  return context
}

// Función para consumir el contexto del sidebar en componentes hijos
export function useSidebar(): SidebarContextType {
  const context = inject<SidebarContextType>(SidebarSymbol)
  if (!context) {
    throw new Error(
      'useSidebar must be used within a component that has SidebarProvider as an ancestor',
    )
  }
  return context
}
