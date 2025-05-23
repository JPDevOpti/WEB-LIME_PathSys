<template>
  <div
    class="overflow-hidden rounded-xl border border-gray-200 bg-white"
  >
    <div class="max-w-full overflow-x-auto custom-scrollbar">
      <table class="min-w-full">
        <thead>
          <tr class="border-b border-gray-200">
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs">ID Muestra</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs">Paciente</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs">Tipo de Análisis</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs">Estado</p>
            </th>
            <th class="px-5 py-3 text-left w-2/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs">Fecha Recepción</p>
            </th>
            <th class="px-5 py-3 text-left w-1/11 sm:px-6">
              <p class="font-medium text-gray-500 text-theme-xs">Acciones</p>
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="(muestra, index) in muestras"
            :key="index"
            class="border-t border-gray-100"
          >
            <td class="px-5 py-4 sm:px-6">
              <div class="flex items-center gap-3">
                <div>
                  <span class="block font-medium text-gray-800 text-theme-sm">
                    {{ muestra.id }}
                  </span>
                  <span class="block text-gray-500 text-theme-xs">
                    {{ muestra.tipoMuestra }}
                  </span>
                </div>
              </div>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <div>
                <p class="text-gray-800 text-theme-sm">{{ muestra.paciente }}</p>
                <p class="text-gray-500 text-theme-xs">{{ muestra.dni }}</p>
              </div>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <p class="text-gray-800 text-theme-sm">{{ muestra.analisis }}</p>
              <p class="text-gray-500 text-theme-xs">{{ muestra.medico }}</p>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <span
                :class="[
                  'rounded-full px-2 py-0.5 text-theme-xs font-medium',
                  {
                    'bg-success-50 text-success-700': muestra.estado === 'Completado',
                    'bg-warning-50 text-warning-700': muestra.estado === 'En Proceso',
                    'bg-error-50 text-error-700': muestra.estado === 'Pendiente',
                    'bg-info-50 text-info-700': muestra.estado === 'Validado',
                  },
                ]"
              >
                {{ muestra.estado }}
              </span>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <p class="text-gray-800 text-theme-sm">{{ muestra.fechaRecepcion }}</p>
              <p class="text-gray-500 text-theme-xs">{{ muestra.horaRecepcion }}</p>
            </td>
            <td class="px-5 py-4 sm:px-6">
              <div class="flex gap-2">
                <button class="text-brand-500 hover:text-brand-700">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                </button>
                <button class="text-brand-500 hover:text-brand-700">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const muestras = ref([
  {
    id: 'M-2024-001',
    tipoMuestra: 'Sangre',
    paciente: 'Juan Pérez',
    dni: '12345678',
    analisis: 'Hemograma Completo',
    medico: 'Dr. García',
    estado: 'Completado',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '09:30'
  },
  {
    id: 'M-2024-002',
    tipoMuestra: 'Orina',
    paciente: 'María López',
    dni: '87654321',
    analisis: 'Uroanálisis',
    medico: 'Dra. Martínez',
    estado: 'En Proceso',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '10:15'
  },
  {
    id: 'M-2024-003',
    tipoMuestra: 'Heces',
    paciente: 'Carlos Ruiz',
    dni: '23456789',
    analisis: 'Coprológico',
    medico: 'Dr. Sánchez',
    estado: 'Pendiente',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '11:00'
  },
  {
    id: 'M-2024-004',
    tipoMuestra: 'Sangre',
    paciente: 'Ana Torres',
    dni: '34567890',
    analisis: 'Perfil Lipídico',
    medico: 'Dra. Rodríguez',
    estado: 'Validado',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '11:45'
  },
  {
    id: 'M-2024-005',
    tipoMuestra: 'Sangre',
    paciente: 'Roberto Díaz',
    dni: '45678901',
    analisis: 'Glucosa',
    medico: 'Dr. Fernández',
    estado: 'En Proceso',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '12:30'
  }
])
</script>

<style scoped>
/* Add any additional styles here if needed */
</style>
