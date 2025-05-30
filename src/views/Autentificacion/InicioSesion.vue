<!--
  Componente InicioSesion
  Vista de inicio de sesión que permite a los usuarios acceder al sistema.
  
  Características:
  - Formulario de inicio de sesión con validación de email
  - Toggle de visibilidad de contraseña
  - Opción de mantener sesión iniciada
  - Estado de carga durante el envío
  - Soporte para tema oscuro
  - Diseño responsive
  - Animaciones y transiciones suaves
  - Validación visual de campos
-->
<template>
  <FullScreenLayout>
    <!-- Contenedor principal con fondo y centrado -->
    <div class="relative min-h-screen p-6 bg-white z-1 dark:bg-gray-900 sm:p-8 flex flex-col items-center justify-center">
      <!-- Sección de logos y navegación -->
      <div class="w-full max-w-md mx-auto mb-8 text-center">
        <!-- Contenedor de logos con animación al hover -->
        <div class="flex justify-center items-center gap-6 mb-8">
          <router-link to="/" class="inline-block transition-transform duration-300 hover:scale-105">
            <img width="180" height="48" src="/images/logo/banner_huam.png" alt="Logo HUAM" class="mx-auto" />
          </router-link>
          <router-link to="/" class="inline-block transition-transform duration-300 hover:scale-105">
            <img width="140" height="48" src="/images/logo/Logo-LIME-NoFondo.png" alt="Logo LIME" class="mx-auto rounded-md" />
          </router-link>
          <router-link to="/" class="inline-block transition-transform duration-300 hover:scale-105">
            <img width="140" height="48" src="/images/logo/Baner-udea.png" alt="Logo UDEA" class="mx-auto rounded-md" />
          </router-link>
        </div>
        
        <!-- Botón de retorno con animación -->
        <router-link
          to="/"
          class="inline-flex items-center text-sm text-gray-500 transition-all duration-300 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300 mb-4 hover:translate-x-[-4px]"
        >
          <svg
            class="stroke-current mr-2"
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
          >
            <path
              d="M12.7083 5L7.5 10.2083L12.7083 15.4167"
              stroke=""
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          Volver al panel
        </router-link>
      </div>
      
      <!-- Contenedor del formulario con efecto de elevación -->
      <div class="w-full max-w-md mx-auto bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8 transform transition-all duration-300 hover:shadow-xl">
        <!-- Encabezado del formulario -->
        <div class="mb-8 text-center">
          <h1
            class="mb-3 font-semibold text-gray-800 text-title-sm dark:text-white/90 sm:text-title-md"
          >
            Iniciar Sesión
          </h1>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            ¡Ingresa tu correo electrónico y contraseña para iniciar sesión!
          </p>
        </div>
        
        <!-- Formulario de inicio de sesión -->
        <form @submit.prevent="handleSubmit">
          <div class="space-y-6">
            <!-- Campo de email con validación visual -->
            <div class="relative">
              <label
                for="email"
                class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
              >
                Correo Electrónico<span class="text-error-500">*</span>
              </label>
              <div class="relative">
                <input
                  v-model="email"
                  type="email"
                  id="email"
                  name="email"
                  placeholder="info@gmail.com"
                  class="dark:bg-dark-900 h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800 transition-all duration-300"
                  :class="{'border-success-500': email && isValidEmail(email), 'border-error-500': email && !isValidEmail(email)}"
                />
                <!-- Iconos de validación de email -->
                <span v-if="email" class="absolute right-3 top-1/2 -translate-y-1/2">
                  <svg v-if="isValidEmail(email)" class="w-5 h-5 text-success-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <svg v-else class="w-5 h-5 text-error-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </span>
              </div>
            </div>

            <!-- Campo de contraseña con toggle de visibilidad -->
            <div class="relative">
              <label
                for="password"
                class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
              >
                Contraseña<span class="text-error-500">*</span>
              </label>
              <div class="relative">
                <input
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  id="password"
                  placeholder="Ingresa tu contraseña"
                  class="dark:bg-dark-900 h-11 w-full rounded-lg border border-gray-300 bg-transparent py-2.5 pl-4 pr-11 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800 transition-all duration-300"
                  :class="{'border-success-500': password && password.length >= 6}"
                />
                <!-- Botón de toggle de visibilidad de contraseña -->
                <span
                  @click="togglePasswordVisibility"
                  class="absolute z-30 text-gray-500 -translate-y-1/2 cursor-pointer right-4 top-1/2 dark:text-gray-400 transition-colors duration-300 hover:text-gray-700 dark:hover:text-gray-300"
                >
                  <svg
                    v-if="!showPassword"
                    class="fill-current"
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M10.0002 13.8619C7.23361 13.8619 4.86803 12.1372 3.92328 9.70241C4.86804 7.26761 7.23361 5.54297 10.0002 5.54297C12.7667 5.54297 15.1323 7.26762 16.0771 9.70243C15.1323 12.1372 12.7667 13.8619 10.0002 13.8619ZM10.0002 4.04297C6.48191 4.04297 3.49489 6.30917 2.4155 9.4593C2.3615 9.61687 2.3615 9.78794 2.41549 9.94552C3.49488 13.0957 6.48191 15.3619 10.0002 15.3619C13.5184 15.3619 16.5055 13.0957 17.5849 9.94555C17.6389 9.78797 17.6389 9.6169 17.5849 9.45932C16.5055 6.30919 13.5184 4.04297 10.0002 4.04297ZM9.99151 7.84413C8.96527 7.84413 8.13333 8.67606 8.13333 9.70231C8.13333 10.7286 8.96527 11.5605 9.99151 11.5605H10.0064C11.0326 11.5605 11.8646 10.7286 11.8646 9.70231C11.8646 8.67606 11.0326 7.84413 10.0064 7.84413H9.99151Z"
                      fill="currentColor"
                    />
                  </svg>
                  <svg
                    v-else
                    class="fill-current"
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M4.63803 3.57709C4.34513 3.2842 3.87026 3.2842 3.57737 3.57709C3.28447 3.86999 3.28447 4.34486 3.57737 4.63775L4.85323 5.91362C3.74609 6.84199 2.89363 8.06395 2.4155 9.45936C2.3615 9.61694 2.3615 9.78801 2.41549 9.94558C3.49488 13.0957 6.48191 15.3619 10.0002 15.3619C11.255 15.3619 12.4422 15.0737 13.4994 14.5598L15.3625 16.4229C15.6554 16.7158 16.1302 16.7158 16.4231 16.4229C16.716 16.13 16.716 15.6551 16.4231 15.3622L4.63803 3.57709ZM12.3608 13.4212L10.4475 11.5079C10.3061 11.5423 10.1584 11.5606 10.0064 11.5606H9.99151C8.96527 11.5606 8.13333 10.7286 8.13333 9.70237C8.13333 9.5461 8.15262 9.39434 8.18895 9.24933L5.91885 6.97923C5.03505 7.69015 4.34057 8.62704 3.92328 9.70247C4.86803 12.1373 7.23361 13.8619 10.0002 13.8619C10.8326 13.8619 11.6287 13.7058 12.3608 13.4212ZM16.0771 9.70249C15.7843 10.4569 15.3552 11.1432 14.8199 11.7311L15.8813 12.7925C16.6329 11.9813 17.2187 11.0143 17.5849 9.94561C17.6389 9.78803 17.6389 9.61696 17.5849 9.45938C16.5055 6.30925 13.5184 4.04303 10.0002 4.04303C9.13525 4.04303 8.30244 4.17999 7.52218 4.43338L8.75139 5.66259C9.1556 5.58413 9.57311 5.54303 10.0002 5.54303C12.7667 5.54303 15.1323 7.26768 16.0771 9.70249Z"
                      fill="currentColor"
                    />
                  </svg>
                </span>
              </div>
            </div>

            <!-- Opciones adicionales -->
            <div class="flex items-center justify-between">
              <!-- Checkbox de mantener sesión -->
              <div>
                <label
                  for="keepLoggedIn"
                  class="flex items-center text-sm font-normal text-gray-700 cursor-pointer select-none dark:text-gray-400"
                >
                  <div class="relative">
                    <input
                      v-model="keepLoggedIn"
                      type="checkbox"
                      id="keepLoggedIn"
                      class="sr-only"
                    />
                    <div
                      :class="
                        keepLoggedIn
                          ? 'border-brand-500 bg-brand-500'
                          : 'bg-transparent border-gray-300 dark:border-gray-700'
                      "
                      class="mr-3 flex h-5 w-5 items-center justify-center rounded-md border-[1.25px] transition-all duration-300"
                    >
                      <span :class="keepLoggedIn ? 'opacity-100 scale-100' : 'opacity-0 scale-0'" class="transition-all duration-300">
                        <svg
                          width="14"
                          height="14"
                          viewBox="0 0 14 14"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M11.6666 3.5L5.24992 9.91667L2.33325 7"
                            stroke="white"
                            stroke-width="1.94437"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                          />
                        </svg>
                      </span>
                    </div>
                  </div>
                  Mantener sesión iniciada
                </label>
              </div>
              <!-- Enlace de recuperación de contraseña -->
              <router-link
                to="/reset-password"
                class="text-sm text-brand-500 hover:text-brand-600 dark:text-brand-400 transition-colors duration-300"
                >¿Olvidaste tu contraseña?</router-link
              >
            </div>

            <!-- Botón de envío con estado de carga -->
            <div>
              <button
                type="submit"
                :disabled="isLoading"
                class="flex items-center justify-center w-full px-4 py-3 text-sm font-medium text-white transition-all duration-300 rounded-lg bg-brand-500 shadow-theme-xs hover:bg-brand-600 disabled:opacity-70 disabled:cursor-not-allowed"
              >
                <!-- Spinner de carga -->
                <svg v-if="isLoading" class="w-5 h-5 mr-2 animate-spin" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {{ isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </FullScreenLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import FullScreenLayout from '@/components/layout/PantallaBlancaCompleta.vue'

// Estado reactivo para los campos del formulario
const email = ref('')
const password = ref('')
const showPassword = ref(false)
const keepLoggedIn = ref(false)
const isLoading = ref(false)

/**
 * Valida si el email tiene un formato válido
 * @param email - Email a validar
 * @returns boolean - true si el email es válido
 */
const isValidEmail = (email: string) => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}

/**
 * Alterna la visibilidad de la contraseña
 */
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value
}

/**
 * Maneja el envío del formulario
 * Simula una llamada a la API con un delay de 1.5 segundos
 */
const handleSubmit = async () => {
  isLoading.value = true
  try {
    // Simular una llamada a la API
    await new Promise(resolve => setTimeout(resolve, 1500))
    console.log('Formulario enviado', {
      email: email.value,
      password: password.value,
      keepLoggedIn: keepLoggedIn.value,
    })
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
/* Animación de entrada suave para elementos */
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
  animation: fadeIn 0.3s ease-out;
}
</style>
