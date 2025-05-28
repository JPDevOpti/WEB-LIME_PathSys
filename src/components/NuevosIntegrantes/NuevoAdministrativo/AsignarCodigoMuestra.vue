<template>
  <div class="space-y-6">
    <!-- Verificación de Paciente por Cédula -->
    <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-lg p-6">
      <div class="mb-4">
        <h3 class="text-lg font-semibold text-blue-800 mb-2 flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
          Asignar Código a una Muestra
        </h3>
        <p class="text-sm text-blue-600">Ingrese la cédula para verificar si el paciente ya está registrado en el sistema</p>
      </div>

      <div>
        <label class="mb-2 block text-sm font-medium text-gray-700">
          Número de Cédula del Paciente *
        </label>
        <div class="relative">
          <span class="absolute left-0 top-1/2 -translate-y-1/2 border-r border-gray-200 px-3.5 py-3 text-blue-500">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.33333 14.1667C11.555 14.1667 14.1667 11.555 14.1667 8.33333C14.1667 5.11167 11.555 2.5 8.33333 2.5C5.11167 2.5 2.5 5.11167 2.5 8.33333C2.5 11.555 5.11167 14.1667 8.33333 14.1667Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M17.5 17.5L13.125 13.125" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
          <input
            v-model="cedula"
            type="text"
            placeholder="Ejemplo: 12345678"
            class="h-12 w-full rounded-lg border border-gray-300 bg-white px-4 py-3 pl-[62px] text-sm text-gray-800 shadow-sm placeholder:text-gray-400 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500/20"
            @keyup.enter="verificarPaciente"
            :disabled="isLoading"
            maxlength="12"
          />
          <div class="absolute right-2 top-1/2 -translate-y-1/2 flex items-center space-x-2">
            <button
              v-if="cedula.trim()"
              @click="cedula = ''"
              type="button"
              class="rounded-lg bg-gray-100 p-2 text-gray-500 hover:bg-gray-200 transition-colors"
              title="Limpiar campo"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
            <button
              @click="verificarPaciente"
              :disabled="!cedula.trim() || isLoading"
              class="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
              {{ isLoading ? 'Verificando...' : 'Verificar' }}
            </button>
          </div>
        </div>

        <!-- Resultado de la verificación -->
        <div v-if="searchPerformed" class="mt-4">
          <!-- Paciente encontrado -->
          <div v-if="pacienteEncontrado" class="rounded-lg bg-emerald-50 border border-emerald-200 p-4">
            <div class="flex items-start space-x-3">
              <div class="flex-shrink-0">
                <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div class="flex-1">
                <h4 class="text-sm font-semibold text-emerald-800 mb-2">¡Paciente encontrado!</h4>
                <div class="mt-3 flex items-center space-x-2">
                  <span class="inline-flex items-center px-3 py-1.5 bg-emerald-100 text-emerald-800 text-xs font-medium rounded-md">
                    <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                    Paciente Asignado Automáticamente
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Paciente no encontrado -->
          <div v-else class="rounded-lg bg-amber-50 border border-amber-200 p-4">
            <div class="flex items-start space-x-3">
              <div class="flex-shrink-0">
                <svg class="w-6 h-6 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                </svg>
              </div>
              <div class="flex-1">
                <h4 class="text-sm font-semibold text-amber-800 mb-1">Paciente no encontrado</h4>
                <div class="flex items-center justify-between">
                  <p class="text-xs text-amber-600">
                    No existe un paciente registrado con la cédula <strong>{{ cedula }}</strong>
                  </p>
                  <button
                    @click="copyCedula"
                    class="ml-2 inline-flex items-center px-2 py-1 bg-amber-100 text-amber-700 text-xs font-medium rounded-md hover:bg-amber-200 transition-colors"
                    title="Copiar número de cédula"
                  >
                    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                    Copiar
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Formulario de Nueva Muestra (se muestra automáticamente si el paciente es encontrado) -->
    <div v-if="pacienteAsignado" class="space-y-6">
      <!-- Información del Paciente Asignado (Solo lectura) -->
      <div class="bg-white border border-gray-200 rounded-lg p-6">
        <h3 class="text-lg font-semibold text-gray-800 mb-4 flex items-center">
          <svg class="w-5 h-5 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          Paciente Asignado - Nueva Muestra
        </h3>

        <!-- Datos del Paciente (Solo lectura) -->
        <div class="bg-gray-50 rounded-lg p-4 border border-gray-200 mb-6">
          <h4 class="text-sm font-semibold text-gray-700 mb-3">Información del Paciente</h4>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Número de Cédula</label>
              <input
                type="text"
                :value="pacienteInfo.cedula"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Nombre del Paciente</label>
              <input
                type="text"
                :value="pacienteInfo.nombre"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Sexo</label>
              <input
                type="text"
                :value="pacienteInfo.sexo"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Edad</label>
              <input
                type="text"
                :value="pacienteInfo.edad"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Entidad</label>
              <input
                type="text"
                :value="pacienteInfo.entidad"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Tipo de Atención</label>
              <input
                type="text"
                :value="pacienteInfo.tipoAtencion"
                class="h-10 w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed"
                readonly
              />
            </div>
            <div class="md:col-span-2">
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Observaciones</label>
              <textarea
                :value="pacienteInfo.observaciones"
                rows="2"
                class="w-full rounded-lg border border-gray-200 bg-gray-100 px-3 py-2 text-sm text-gray-500 cursor-not-allowed resize-none"
                readonly
              ></textarea>
            </div>
          </div>
        </div>

        <!-- Número de Caso -->
        <div class="mb-4">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">Número de Caso *</label>
          <input
            type="text"
            v-model="formData.numeroCaso"
            placeholder="Ingrese el número de caso"
            class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            required
            @input="formData.numeroCaso = formData.numeroCaso.replace(/[^0-9]/g, '')"
          />
        </div>

        <!-- Número de Muestras -->
        <div class="mb-4">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">Número de Muestras *</label>
          <input
            type="text"
            v-model="formData.numeroMuestras"
            @input="handleNumeroMuestrasInput"
            placeholder="Ingrese el número de muestras"
            class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            required
          />
        </div>

        <!-- CUPS por Muestra -->
        <div class="mb-6">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">
            CUPS por Muestra *
          </label>
          <div class="space-y-6">
            <div v-for="(muestra, muestraIndex) in formData.muestras" :key="muestraIndex" class="space-y-2">
              <h4 class="text-sm font-medium text-gray-700">Muestra {{ muestra.numero }}</h4>
              <div v-for="(cups, cupsIndex) in muestra.cups" :key="cupsIndex" class="flex items-center space-x-2">
                <input
                  type="text"
                  v-model="formData.muestras[muestraIndex].cups[cupsIndex]"
                  placeholder="Ingrese el CUPS"
                  class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                  required
                  @keydown.enter.prevent="agregarCupsSiNecesario(muestraIndex, cupsIndex)"
                  :ref="el => { if (el) cupsInputs[muestraIndex][cupsIndex] = el as HTMLInputElement }"
                />
                <button
                  v-if="muestra.cups.length > 1"
                  @click="eliminarCups(muestraIndex, cupsIndex)"
                  type="button"
                  class="p-2 text-red-600 hover:text-red-800"
                >
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                  </svg>
                </button>
              </div>
              <button
                @click="agregarCups(muestraIndex)"
                type="button"
                class="mt-2 inline-flex items-center px-3 py-1.5 border border-gray-300 rounded-md text-xs font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-1 transition-colors"
              >
                <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                Agregar CUPS
              </button>
            </div>
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="flex justify-end space-x-4 mt-6">
          <button
            @click="limpiarFormulario"
            type="button"
            class="inline-flex items-center px-6 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
            Limpiar
          </button>
          <button
            @click="guardarMuestra"
            type="button"
            class="inline-flex items-center px-6 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-3 focus:ring-brand-300 disabled:bg-gray-400 disabled:hover:bg-gray-400 disabled:cursor-not-allowed transition-colors"
            :disabled="!isFormValid"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            Guardar Muestra
          </button>
        </div>

        <!-- Código de Muestra Asignado -->
        <div v-if="registeredSampleId" class="mt-6">
          <div class="rounded-lg bg-emerald-50 border border-emerald-200 p-4">
            <div class="flex items-start space-x-3">
              <div class="flex-shrink-0">
                <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div class="flex-1">
                <h4 class="text-sm font-semibold text-emerald-800 mb-2">Código de Muestra Asignado</h4>
                <div class="flex items-center justify-between">
                  <span class="text-2xl font-bold text-emerald-600 font-mono">{{ registeredSampleId }}</span>
                  <button
                    @click="copyToClipboard"
                    class="inline-flex items-center px-3 py-1.5 bg-emerald-600 text-white text-xs font-medium rounded-md hover:bg-emerald-700 transition-colors"
                  >
                    <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                    Copiar Código
                  </button>
                </div>
                <p class="text-xs text-emerald-600 mt-2">
                  Este código ha sido asignado a la muestra del paciente {{ pacienteInfo.nombre }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Notificación Emergente Centrada -->
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="opacity-0 transform scale-95"
      enter-to-class="opacity-100 transform scale-100"
      leave-active-class="transition ease-in duration-200"
      leave-from-class="opacity-100 transform scale-100"
      leave-to-class="opacity-0 transform scale-95"
    >
      <div
        v-if="showNotification"
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
      >
        <!-- Overlay oscuro -->
        <div 
          class="absolute inset-0 bg-black bg-opacity-50"
          @click="showNotification = false"
        ></div>
        
        <!-- Modal de notificación -->
        <div
          class="relative bg-white rounded-2xl shadow-2xl border-l-4 border-green-500 p-8 max-w-md w-full"
        >
          <div class="text-center">
            <!-- Ícono de éxito -->
            <div class="mx-auto flex items-center justify-center w-16 h-16 rounded-full bg-green-100 mb-4">
              <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            
            <!-- Título -->
            <h3 class="text-2xl font-bold text-gray-900 mb-2">¡Muestra Registrada!</h3>
            
            <!-- Mensaje -->
            <p class="text-gray-600 mb-1">
              La muestra para el paciente
            </p>
            <p class="text-lg font-semibold text-brand-600 mb-1">
              {{ pacienteInfo.nombre }}
            </p>
            <p class="text-gray-600 mb-1">
              se ha registrado con el código
            </p>
            <p class="text-2xl font-bold text-green-600 font-mono mb-4">
              {{ registeredSampleId }}
            </p>
            <p class="text-gray-600 mb-6">
              correctamente en el sistema.
            </p>
            
            <!-- Timestamp -->
            <div class="flex items-center justify-center text-sm text-gray-500 mb-6">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {{ new Date().toLocaleTimeString() }}
            </div>
            
            <!-- Barra de progreso -->
            <div class="w-full bg-gray-200 rounded-full h-2 mb-6">
              <div 
                class="bg-green-500 h-2 rounded-full transition-all duration-75 ease-linear"
                :style="{ width: progressWidth + '%' }"
              ></div>
            </div>
            
            <!-- Botones de acción -->
            <div class="space-y-3">
              <!-- Botón principal para copiar código -->
              <button
                @click="copyFromNotificationAndClose"
                class="w-full inline-flex items-center justify-center px-6 py-3 border border-transparent rounded-lg text-base font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-3 focus:ring-green-500 focus:ring-offset-2 transition-colors"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                Copiar Código
              </button>
              
              <!-- Botón secundario -->
              <button
                @click="showNotification = false"
                class="w-full inline-flex items-center justify-center px-6 py-3 border border-green-300 rounded-lg text-base font-medium text-green-700 bg-green-50 hover:bg-green-100 focus:outline-none focus:ring-3 focus:ring-green-500 focus:ring-offset-2 transition-colors"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Entendido
              </button>
            </div>
          </div>
          
          <!-- Botón X en la esquina -->
          <button
            @click="showNotification = false"
            class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 transition-colors p-2 rounded-full hover:bg-gray-100"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, nextTick, onMounted } from 'vue'

interface PacienteData {
  nombre: string
  cedula: string
  edad?: string
  telefono?: string
  sexo?: string
  entidad?: string
  tipoAtencion?: string
  observaciones?: string
}

interface MuestraData {
  id: string
  paciente: PacienteData
  numeroCaso: string
  muestras: {
    numero: number
    cups: string[]
  }[]
}

// Estado del formulario
const pacienteAsignado = ref<PacienteData | null>(null)
const pacienteInfo = ref<PacienteData>({
  nombre: '',
  cedula: '',
  edad: '',
  telefono: '',
  sexo: '',
  entidad: '',
  tipoAtencion: '',
  observaciones: ''
})

// Estados para verificación de paciente
const cedula = ref('')
const isLoading = ref(false)
const searchPerformed = ref(false)
const pacienteEncontrado = ref(false)

// Estados para el formulario de muestra
const showNotification = ref(false)
const progressWidth = ref(100)
const registeredSampleId = ref('')

// Datos del formulario de muestra
const formData = reactive({
  numeroCaso: '',
  numeroMuestras: '1',
  muestras: [{
    numero: 1,
    cups: ['']
  }] as { numero: number; cups: string[] }[],
})

// Referencias a los inputs
const cupsInputs = ref<(HTMLInputElement | null)[][]>([[]])

// Base de datos simulada de pacientes
const pacientesDB: Record<string, PacienteData> = {
  '12345678': {
    nombre: 'Juan Pérez García',
    cedula: '12345678',
    edad: '45',
    telefono: '(555) 123-4567',
    sexo: 'Masculino',
    entidad: 'ESSALUD',
    tipoAtencion: 'hospitalizado',
    observaciones: 'Paciente con antecedentes de hipertensión arterial'
  },
  '87654321': {
    nombre: 'María López Silva',
    cedula: '87654321',
    edad: '32',
    telefono: '(555) 987-6543',
    sexo: 'Femenino',
    entidad: 'MINSA',
    tipoAtencion: 'ambulatorio',
    observaciones: 'Paciente con antecedentes de diabetes tipo 2'
  },
  '11223344': {
    nombre: 'Carlos Rodríguez Torres',
    cedula: '11223344',
    edad: '28',
    telefono: '(555) 111-2233',
    sexo: 'Masculino',
    entidad: 'FFAA',
    tipoAtencion: 'ambulatorio',
    observaciones: 'Paciente con antecedentes de hipercolesterolemia'
  },
  '55667788': {
    nombre: 'Ana Martínez Díaz',
    cedula: '55667788',
    edad: '56',
    telefono: '(555) 555-6677',
    sexo: 'Femenino',
    entidad: 'SIS',
    tipoAtencion: 'ambulatorio',
    observaciones: 'Paciente con antecedentes de obesidad'
  }
}

// Validación del formulario
const isFormValid = computed(() => {
  return !!(
    pacienteAsignado.value &&
    formData.numeroCaso &&
    formData.muestras.length > 0 &&
    formData.muestras.every(muestra => 
      muestra.cups.length > 0 && 
      muestra.cups.every(cups => cups.trim() !== '')
    )
  )
})

// Función para verificar paciente (modificada para asignar automáticamente)
const verificarPaciente = async () => {
  if (!cedula.value.trim()) return

  isLoading.value = true
  searchPerformed.value = true

  try {
    const paciente = pacientesDB[cedula.value]
    
    if (paciente) {
      pacienteEncontrado.value = true
      pacienteInfo.value = { ...paciente }
      // Asignar automáticamente el paciente
      pacienteAsignado.value = { ...paciente }
      emit('paciente-verificado', { 
        encontrado: true, 
        paciente: paciente, 
        cedula: cedula.value 
      })
      emit('asignar-paciente', paciente)
    } else {
      pacienteEncontrado.value = false
      pacienteAsignado.value = null
      pacienteInfo.value = {
        nombre: '',
        cedula: cedula.value,
        edad: '',
        telefono: '',
        sexo: '',
        entidad: '',
        tipoAtencion: '',
        observaciones: ''
      }
      emit('paciente-verificado', { 
        encontrado: false, 
        paciente: null, 
        cedula: cedula.value 
      })
    }
  } catch (error) {
    console.error('Error al verificar paciente:', error)
  } finally {
    isLoading.value = false
  }
}

// Función para limpiar todo el formulario
const limpiarFormulario = () => {
  // Limpiar datos del paciente
  cedula.value = ''
  searchPerformed.value = false
  pacienteEncontrado.value = false
  pacienteAsignado.value = null
  pacienteInfo.value = {
    nombre: '',
    cedula: '',
    edad: '',
    telefono: '',
    sexo: '',
    entidad: '',
    tipoAtencion: '',
    observaciones: ''
  }

  // Limpiar datos de la muestra
  formData.numeroCaso = ''
  formData.numeroMuestras = '1'
  formData.muestras = [{
    numero: 1,
    cups: ['']
  }]
  
  // Limpiar notificación
  showNotification.value = false
  progressWidth.value = 100
  registeredSampleId.value = ''
}

// Emits
const emit = defineEmits<{
  'paciente-verificado': [data: { encontrado: boolean; paciente: PacienteData | null; cedula: string }]
  'asignar-paciente': [paciente: PacienteData]
  'sample-registered': [data: MuestraData]
}>()

// Exponer funciones para uso externo
defineExpose({
  limpiarFormulario,
  verificarPaciente
})

// Función para manejar el input del número de muestras
const handleNumeroMuestrasInput = (event: Event) => {
  const input = event.target as HTMLInputElement
  let value = input.value.replace(/[^0-9]/g, '')
  
  if (value === '') {
    formData.numeroMuestras = ''
    return
  }

  const numValue = parseInt(value)
  if (numValue > 10) {
    value = '10'
  }
  
  formData.numeroMuestras = value
  actualizarNumeroMuestras()
}

// Función para actualizar el número de muestras
const actualizarNumeroMuestras = () => {
  const numeroMuestras = formData.numeroMuestras === '' ? 1 : Math.max(1, Math.min(10, parseInt(formData.numeroMuestras)))
  
  // Ajustar el array de muestras
  while (formData.muestras.length < numeroMuestras) {
    formData.muestras.push({
      numero: formData.muestras.length + 1,
      cups: ['']
    })
    cupsInputs.value.push([])
  }
  while (formData.muestras.length > numeroMuestras) {
    formData.muestras.pop()
    cupsInputs.value.pop()
  }
}

// Función para agregar CUPS a una muestra específica
const agregarCups = (muestraIndex: number) => {
  formData.muestras[muestraIndex].cups.push('')
  nextTick(() => {
    const lastIndex = formData.muestras[muestraIndex].cups.length - 1
    if (cupsInputs.value[muestraIndex]?.[lastIndex]) {
      cupsInputs.value[muestraIndex][lastIndex]?.focus()
    }
  })
}

// Función para eliminar CUPS de una muestra específica
const eliminarCups = (muestraIndex: number, cupsIndex: number) => {
  formData.muestras[muestraIndex].cups.splice(cupsIndex, 1)
  nextTick(() => {
    const newIndex = Math.min(cupsIndex, formData.muestras[muestraIndex].cups.length - 1)
    if (cupsInputs.value[muestraIndex]?.[newIndex]) {
      cupsInputs.value[muestraIndex][newIndex]?.focus()
    }
  })
}

// Función para manejar la adición de CUPS con Enter
const agregarCupsSiNecesario = (muestraIndex: number, cupsIndex: number) => {
  const currentCups = formData.muestras[muestraIndex].cups[cupsIndex]
  if (currentCups.trim() !== '') {
    agregarCups(muestraIndex)
  }
}

// Inicializar con un CUPS al montar el componente
onMounted(() => {
  if (formData.muestras[0].cups.length === 0) {
    agregarCups(0)
  }
})

// Función para copiar desde la notificación y cerrarla
const copyFromNotificationAndClose = async () => {
  await copyToClipboard()
  showNotification.value = false
}

// Función para copiar al portapapeles
const copyToClipboard = async () => {
  try {
    await navigator.clipboard.writeText(registeredSampleId.value)
  } catch (err) {
    console.error('Error al copiar:', err)
  }
}

// Función para guardar la muestra
const guardarMuestra = () => {
  if (!isFormValid.value || !pacienteAsignado.value) return

  const nuevaMuestra: MuestraData = {
    id: `M${Date.now()}`,
    paciente: pacienteAsignado.value,
    numeroCaso: formData.numeroCaso,
    muestras: formData.muestras.map(muestra => ({
      numero: muestra.numero,
      cups: muestra.cups.filter(cups => cups.trim() !== '')
    }))
  }

  // Guardar el ID de la muestra
  registeredSampleId.value = nuevaMuestra.id

  // Mostrar notificación
  showNotification.value = true
  progressWidth.value = 100

  // Crear barra de progreso para auto-cierre
  const duration = 5000 // 5 segundos
  const interval = 50 // Update every 50ms
  const decrement = (interval / duration) * 100

  const progressInterval = setInterval(() => {
    progressWidth.value -= decrement
    if (progressWidth.value <= 0) {
      clearInterval(progressInterval)
      showNotification.value = false
      progressWidth.value = 100
    }
  }, interval)

  // Emitir evento de éxito
  emit('sample-registered', nuevaMuestra)
}

// Función para copiar la cédula
const copyCedula = async () => {
  try {
    await navigator.clipboard.writeText(cedula.value)
  } catch (err) {
    console.error('Error al copiar:', err)
  }
}
</script>