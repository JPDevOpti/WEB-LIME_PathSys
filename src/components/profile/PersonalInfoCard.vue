<template>
  <div>
    <div class="p-5 mb-6 border border-gray-200 rounded-2xl dark:border-gray-800 lg:p-6">
      <div class="flex flex-col gap-6 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <div class="flex flex-col items-center w-full gap-6 mb-6 xl:flex-row">
            <div
              class="w-20 h-20 overflow-hidden border border-gray-200 rounded-full dark:border-gray-800"
            >
              <img src="/images/user/owner.jpg" alt="user" />
            </div>
            <div>
              <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 lg:mb-3">
                Información del Personal
              </h4>
            </div>
          </div>

          <div v-if="currentRole === 'admin'" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.admin.firstName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Apellido</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.admin.lastName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">
                Correo Electrónico
              </p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">
                {{ userData.admin.email }}
              </p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.admin.phone }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Rol</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.admin.role }}</p>
            </div>
          </div>

          <div v-if="currentRole === 'dataentry'" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.dataentry.firstName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Apellido</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.dataentry.lastName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">
                Correo Electrónico
              </p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">
                {{ userData.dataentry.email }}
              </p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.dataentry.phone }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Rol</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.dataentry.role }}</p>
            </div>
          </div>

          <div v-if="currentRole === 'transcriber'" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.transcriber.firstName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Apellido</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.transcriber.lastName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">
                Correo Electrónico
              </p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">
                {{ userData.transcriber.email }}
              </p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.transcriber.phone }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Rol</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.transcriber.role }}</p>
            </div>
          </div>

          <div v-if="currentRole === 'specialist'" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.specialist.firstName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Apellido</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.specialist.lastName }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">
                Correo Electrónico
              </p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">
                {{ userData.specialist.email }}
              </p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.specialist.phone }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Rol</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">{{ userData.specialist.role }}</p>
            </div>

            <div>
              <p class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Especialidad</p>
              <p class="text-sm font-medium text-gray-800 dark:text-white/90">Anatomía Patológica</p>
            </div>
          </div>
        </div>

        <div class="flex flex-col gap-2">
          <button @click="isProfileInfoModal = true" class="edit-button-modern">
            <svg
              class="edit-icon"
              width="16"
              height="16"
              viewBox="0 0 18 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M15.0911 2.78206C14.2125 1.90338 12.7878 1.90338 11.9092 2.78206L4.57524 10.116C4.26682 10.4244 4.0547 10.8158 3.96468 11.2426L3.31231 14.3352C3.25997 14.5833 3.33653 14.841 3.51583 15.0203C3.69512 15.1996 3.95286 15.2761 4.20096 15.2238L7.29355 14.5714C7.72031 14.4814 8.11172 14.2693 8.42013 13.9609L15.7541 6.62695C16.6327 5.74827 16.6327 4.32365 15.7541 3.44497L15.0911 2.78206ZM12.9698 3.84272C13.2627 3.54982 13.7376 3.54982 14.0305 3.84272L14.6934 4.50563C14.9863 4.79852 14.9863 5.2734 14.6934 5.56629L14.044 6.21573L12.3204 4.49215L12.9698 3.84272ZM11.2597 5.55281L5.6359 11.1766C5.53309 11.2794 5.46238 11.4099 5.43238 11.5522L5.01758 13.5185L6.98394 13.1037C7.1262 13.0737 7.25666 13.003 7.35947 12.9002L12.9833 7.27639L11.2597 5.55281Z"
              />
            </svg>
            <span>Editar perfil</span>
          </button>
          
          <div class="flex flex-col gap-1 mt-4">
            <button 
              v-for="role in roles" 
              :key="role.value"
              @click="currentRole = role.value"
              class="px-3 py-1.5 text-sm rounded-lg transition-colors"
              :class="currentRole === role.value ? 
                'bg-brand-500 text-white' : 
                'bg-gray-100 text-gray-700 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700'"
            >
              {{ role.label }}
            </button>
          </div>
        </div>
      </div>
    </div>
    <Modal v-if="isProfileInfoModal" @close="isProfileInfoModal = false">
      <template #body>
        <div
          class="no-scrollbar relative w-full max-w-[700px] overflow-y-auto rounded-3xl bg-white p-4 dark:bg-gray-900 lg:p-11"
        >
          <!-- close btn -->
          <button
            @click="isProfileInfoModal = false"
            class="transition-color absolute right-5 top-5 z-999 flex h-11 w-11 items-center justify-center rounded-full bg-gray-100 text-gray-400 hover:bg-gray-200 hover:text-gray-600 dark:bg-gray-700 dark:bg-white/[0.05] dark:text-gray-400 dark:hover:bg-white/[0.07] dark:hover:text-gray-300"
          >
            <svg
              class="fill-current"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M6.04289 16.5418C5.65237 16.9323 5.65237 17.5655 6.04289 17.956C6.43342 18.3465 7.06658 18.3465 7.45711 17.956L11.9987 13.4144L16.5408 17.9565C16.9313 18.347 17.5645 18.347 17.955 17.9565C18.3455 17.566 18.3455 16.9328 17.955 16.5423L13.4129 12.0002L17.955 7.45808C18.3455 7.06756 18.3455 6.43439 17.955 6.04387C17.5645 5.65335 16.9313 5.65335 16.5408 6.04387L11.9987 10.586L7.45711 6.04439C7.06658 5.65386 6.43342 5.65386 6.04289 6.04439C5.65237 6.43491 5.65237 7.06808 6.04289 7.4586L10.5845 12.0002L6.04289 16.5418Z"
                fill=""
              />
            </svg>
          </button>
          <div class="px-2 pr-14">
            <h4 class="mb-2 text-2xl font-semibold text-gray-800 dark:text-white/90">
              Editar Información Personal
            </h4>
            <p class="mb-6 text-sm text-gray-500 dark:text-gray-400 lg:mb-7">
              Actualice sus datos para mantener su perfil al día.
            </p>
          </div>
          <form class="flex flex-col">
            <div class="custom-scrollbar h-[458px] overflow-y-auto p-2">
              <div class="mt-7">
                <h5 class="mb-5 text-lg font-medium text-gray-800 dark:text-white/90 lg:mb-6">
                  Enlaces
                </h5>

                <div class="grid grid-cols-1 gap-x-6 gap-y-5 lg:grid-cols-2">
                  <div>
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Sitio Web
                    </label>
                    <input
                      type="text"
                      value="https://www.laboratoriopatologia.com"
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>

                  <div>
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Portal de Pacientes
                    </label>
                    <input
                      type="text"
                      value="https://pacientes.laboratoriopatologia.com"
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>
                </div>
              </div>
              
              <div class="mt-7">
                <h5 class="mb-5 text-lg font-medium text-gray-800 dark:text-white/90 lg:mb-6">
                  Información Personal
                </h5>

                <div class="grid grid-cols-1 gap-x-6 gap-y-5 lg:grid-cols-2">
                  <div class="col-span-2 lg:col-span-1">
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Nombre
                    </label>
                    <input
                      type="text"
                      :value="userData[currentRole].firstName"
                      class="dark:bg-dark-900 h-11 w-full rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>

                  <div class="col-span-2 lg:col-span-1">
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Apellido
                    </label>
                    <input
                      type="text"
                      :value="userData[currentRole].lastName"
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>

                  <div class="col-span-2 lg:col-span-1">
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Correo Electrónico
                    </label>
                    <input
                      type="text"
                      :value="userData[currentRole].email"
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>

                  <div class="col-span-2 lg:col-span-1">
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Teléfono
                    </label>
                    <input
                      type="text"
                      :value="userData[currentRole].phone"
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>

                  <div class="col-span-2">
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Rol
                    </label>
                    <input
                      type="text"
                      :value="userData[currentRole].role"
                      disabled
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>

                  <div v-if="currentRole === 'specialist'" class="col-span-2">
                    <label
                      class="mb-1.5 block text-sm font-medium text-gray-700 dark:text-gray-400"
                    >
                      Especialidad
                    </label>
                    <input
                      type="text"
                      value="Anatomía Patológica"
                      class="dark:bg-dark-900 h-11 w-full appearance-none rounded-lg border border-gray-300 bg-transparent bg-none px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 dark:border-gray-700 dark:bg-gray-900 dark:text-white/90 dark:placeholder:text-white/30 dark:focus:border-brand-800"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="flex items-center gap-3 px-2 mt-6 lg:justify-end">
              <button
                @click="isProfileInfoModal = false"
                type="button"
                class="flex w-full justify-center rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-white/[0.03] sm:w-auto"
              >
                Cancelar
              </button>
              <button
                @click="saveProfile"
                type="button"
                class="flex w-full justify-center rounded-lg bg-brand-500 px-4 py-2.5 text-sm font-medium text-white hover:bg-brand-600 sm:w-auto"
              >
                Guardar Cambios
              </button>
            </div>
          </form>
        </div>
      </template>
    </Modal>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Modal from './Modal.vue'

const isProfileInfoModal = ref(false)
const currentRole = ref<'admin' | 'dataentry' | 'transcriber' | 'specialist'>('admin')

const roles = [
  { value: 'admin', label: 'Administrador' },
  { value: 'dataentry', label: 'Ingreso de Informes' },
  { value: 'transcriber', label: 'Transcriptor' },
  { value: 'specialist', label: 'Especialista' },
] as const

type UserData = {
  admin: {
    firstName: string;
    lastName: string;
    email: string;
    phone: string;
    role: string;
  };
  dataentry: {
    firstName: string;
    lastName: string;
    email: string;
    phone: string;
    role: string;
  };
  transcriber: {
    firstName: string;
    lastName: string;
    email: string;
    phone: string;
    role: string;
  };
  specialist: {
    firstName: string;
    lastName: string;
    email: string;
    phone: string;
    role: string;
  };
}

const userData: UserData = {
  admin: {
    firstName: 'Carlos',
    lastName: 'Rodríguez',
    email: 'carlos.rodriguez@patolab.com',
    phone: '+51 987 654 321',
    role: 'Administrador del Sistema'
  },
  dataentry: {
    firstName: 'María',
    lastName: 'López',
    email: 'maria.lopez@patolab.com',
    phone: '+51 912 345 678',
    role: 'Ingreso de Informes'
  },
  transcriber: {
    firstName: 'Jorge',
    lastName: 'Gómez',
    email: 'jorge.gomez@patolab.com',
    phone: '+51 923 456 789',
    role: 'Transcriptor de Informes'
  },
  specialist: {
    firstName: 'Ana',
    lastName: 'Martínez',
    email: 'dra.martinez@patolab.com',
    phone: '+51 934 567 890',
    role: 'Patólogo Especialista'
  }
}

const saveProfile = () => {
  // Implement save profile logic here
  console.log('Perfil guardado')
  isProfileInfoModal.value = false
}
</script>

<style scoped>
.edit-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 9999px;
  border: 1px solid #e5e7eb;
  color: #6b7280;
  transition-property: color, background-color, border-color;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.edit-button:hover {
  border-color: transparent;
  background-color: #f3f4f6;
  color: #374151;
}

.dark .edit-button {
  border-color: #374151;
  color: #9ca3af;
}

.dark .edit-button:hover {
  border-color: transparent;
  background-color: #1f2937;
  color: #d1d5db;
}

.edit-button-modern {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  color: white;
  background-color: #3b82f6;
  border: none;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.edit-button-modern:hover {
  background-color: #2563eb;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
  transform: translateY(-1px);
}

.edit-button-modern:active {
  transform: translateY(1px);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.dark .edit-button-modern {
  background-color: #4f46e5;
}

.dark .edit-button-modern:hover {
  background-color: #4338ca;
}

.edit-icon {
  fill: currentColor;
}
</style>
