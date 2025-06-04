<template>
  <div>
    <div class="p-5 mb-6 border border-gray-200 rounded-2xl dark:border-gray-800 lg:p-6">
      <div class="flex flex-col gap-6 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <div class="flex flex-col items-center w-full gap-6 mb-6 xl:flex-row">
            <div class="w-20 h-20 overflow-hidden border border-gray-200 rounded-full dark:border-gray-800">
              <img src="/images/user/owner.jpg" alt="user" />
            </div>
            <div>
              <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 lg:mb-3">
                Crear Nuevo Usuario
              </h4>
            </div>
          </div>
          <form @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre</label>
              <input v-model="nuevoUsuario.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Apellido</label>
              <input v-model="nuevoUsuario.lastName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
              <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</label>
              <input v-model="nuevoUsuario.phone" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Rol</label>
              <select v-model="nuevoUsuario.role" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                <option value="">Seleccione un rol</option>
                <option value="admin">Administrador</option>
                <option value="dataentry">Ingreso de Informes</option>
                <option value="transcriber">Secretaria</option>
                <option value="specialist">Patólogo</option>
              </select>
            </div>
            <div v-if="nuevoUsuario.role === 'specialist'">
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Especialidad</label>
              <input v-model="nuevoUsuario.specialty" type="text" class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: Anatomía Patológica" />
            </div>
            <div class="col-span-2 flex justify-end mt-4">
              <button type="submit" class="edit-button-modern">Crear Usuario</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div v-if="usuarioCreado" class="p-4 mt-4 rounded-lg bg-green-50 text-green-800 border border-green-200">
      Usuario creado exitosamente.
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const nuevoUsuario = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  role: '',
  specialty: ''
})
const usuarioCreado = ref(false)

const crearUsuario = () => {
  // Aquí iría la lógica para guardar el usuario (API, etc.)
  usuarioCreado.value = true
  setTimeout(() => usuarioCreado.value = false, 3000)
  // Limpiar formulario
  nuevoUsuario.value = { firstName: '', lastName: '', email: '', phone: '', role: '', specialty: '' }
}
</script>

<style scoped>
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
</style>
