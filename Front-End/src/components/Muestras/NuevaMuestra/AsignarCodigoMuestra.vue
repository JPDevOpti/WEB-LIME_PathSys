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
          Cédula del Paciente *
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
            class="h-12 w-full rounded-lg border bg-white px-4 py-3 pl-[62px] pr-[140px] text-sm text-gray-800 shadow-sm placeholder:text-gray-400 focus:outline-none focus:ring-2 transition-colors"
            :class="{
              'border-gray-300 focus:border-blue-500 focus:ring-blue-500/20': !cedula || isValidCedulaFormat(cedula),
              'border-red-300 focus:border-red-500 focus:ring-red-500/20': cedula && !isValidCedulaFormat(cedula)
            }"
            @keyup.enter="verificarPaciente"
            :disabled="isLoading"
            maxlength="12"
            @input="handleCedulaInput"
          />
          <div class="absolute right-2 top-1/2 -translate-y-1/2 flex items-center space-x-2">
            <!-- Contador de caracteres -->
            <span class="text-xs text-gray-400">
              {{ cedula.length }}/12
            </span>
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
              :disabled="!cedula.trim() || isLoading || !isValidCedulaFormat(cedula)"
              class="rounded-lg px-4 py-2 text-sm font-medium text-white transition-colors"
              :class="{
                'bg-blue-600 hover:bg-blue-700': cedula.trim() && !isLoading && isValidCedulaFormat(cedula),
                'bg-gray-400 cursor-not-allowed': !cedula.trim() || isLoading || !isValidCedulaFormat(cedula)
              }"
            >
              {{ isLoading ? 'Verificando...' : 'Verificar' }}
            </button>
          </div>
        </div>
        
        <!-- Mensaje de validación de cédula -->
        <div v-if="cedula && !isValidCedulaFormat(cedula)" class="mt-1 text-xs text-red-600">
          La cédula debe contener solo números y tener entre 6 y 12 dígitos
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
                <h4 class="text-sm font-semibold text-emerald-800 mb-2">
                  {{ pacienteAsignadoAutomaticamente ? '¡Paciente asignado automáticamente!' : '¡Paciente encontrado!' }}
                </h4>
                <div class="mt-3 flex items-center space-x-2">
                  <span class="inline-flex items-center px-3 py-1.5 bg-emerald-100 text-emerald-800 text-xs font-medium rounded-md">
                    <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                    </svg>
                    {{ pacienteAsignadoAutomaticamente ? 'Paciente Recién Registrado' : 'Paciente Asignado Automáticamente' }}
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
                    title="Copiar cédula"
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
      <!-- Mensaje de Error Global -->
      <div v-if="errorMessage" class="rounded-lg bg-red-50 border border-red-200 p-4 mb-4">
        <div class="flex items-start space-x-3">
          <div class="flex-shrink-0">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
            </svg>
          </div>
          <div class="flex-1">
            <h4 class="text-sm font-semibold text-red-800 mb-1">Error</h4>
            <p class="text-sm text-red-600">{{ errorMessage }}</p>
            <button
              @click="errorMessage = ''"
              class="mt-2 text-xs text-red-600 hover:text-red-800 underline"
            >
              Cerrar
            </button>
          </div>
        </div>
      </div>

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
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Cédula</label>
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
              <div class="relative">
                <div class="relative">
                  <input
                    type="text"
                    :value="getEntidadLabel(pacienteInfo.entidad || '')"
                    @focus="showEntidades = true"
                    @blur="ocultarEntidades"
                    placeholder="Seleccione la entidad"
                    class="h-11 w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                    readonly
                  />
                  <button
                    type="button"
                    @click="showEntidades = !showEntidades"
                    class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-500"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </button>
                </div>
                
                <!-- Lista desplegable de entidades -->
                <transition
                  enter-active-class="transition ease-out duration-200"
                  enter-from-class="opacity-0 transform scale-95"
                  enter-to-class="opacity-100 transform scale-100"
                  leave-active-class="transition ease-in duration-150"
                  leave-from-class="opacity-100 transform scale-100"
                  leave-to-class="opacity-0 transform scale-95"
                >
                  <div
                    v-if="showEntidades"
                    class="absolute z-50 w-full mt-1 bg-white rounded-lg shadow-lg border border-gray-200 max-h-60 overflow-auto"
                  >
                    <ul class="py-1">
                      <li
                        v-for="entidad in ENTIDADES"
                        :key="entidad.value"
                        @mousedown="seleccionarEntidad(entidad)"
                        class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer transition-colors"
                        :class="{ 'bg-brand-50 text-brand-700': pacienteInfo.entidad === entidad.value }"
                      >
                        {{ entidad.label }}
                      </li>
                    </ul>
                  </div>
                </transition>
              </div>
            </div>
            <div>
              <label class="mb-1.5 block text-sm font-medium text-gray-600">Tipo de Atención</label>
              <div class="relative">
                <div class="relative">
                  <input
                    type="text"
                    :value="getTipoAtencionLabel(pacienteInfo.tipoAtencion || '')"
                    @focus="showTiposAtencion = true"
                    @blur="ocultarTiposAtencion"
                    placeholder="Seleccione el tipo de atención"
                    class="h-11 w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                    readonly
                  />
                  <button
                    type="button"
                    @click="showTiposAtencion = !showTiposAtencion"
                    class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-500"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </button>
                </div>
                
                <!-- Lista desplegable de tipos de atención -->
                <transition
                  enter-active-class="transition ease-out duration-200"
                  enter-from-class="opacity-0 transform scale-95"
                  enter-to-class="opacity-100 transform scale-100"
                  leave-active-class="transition ease-in duration-150"
                  leave-from-class="opacity-100 transform scale-100"
                  leave-to-class="opacity-0 transform scale-95"
                >
                  <div
                    v-if="showTiposAtencion"
                    class="absolute z-50 w-full mt-1 bg-white rounded-lg shadow-lg border border-gray-200 max-h-60 overflow-auto"
                  >
                    <ul class="py-1">
                      <li
                        v-for="tipo in TIPOS_ATENCION"
                        :key="tipo.value"
                        @mousedown="seleccionarTipoAtencion(tipo)"
                        class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer transition-colors"
                        :class="{ 'bg-brand-50 text-brand-700': pacienteInfo.tipoAtencion === tipo.value }"
                      >
                        {{ tipo.label }}
                      </li>
                    </ul>
                  </div>
                </transition>
              </div>
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

        <!-- Fecha de Ingreso -->
        <div class="mb-4">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">Fecha de Ingreso*</label>
          <div class="relative">
            <input
              type="text"
              v-model="fechaIngreso"
              @input="handleFechaIngresoInput"
              placeholder="DD/MM/AAAA HH:MM (ej: 15/06/2025 14:30)"
              class="h-11 w-full rounded-lg border px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3 transition-colors"
              :class="{
                'border-gray-300 bg-white focus:border-brand-300 focus:ring-brand-500/10': !fechaIngreso || isValidDateFormat(fechaIngreso),
                'border-red-300 bg-red-50 focus:border-red-500 focus:ring-red-500/10': fechaIngreso && !isValidDateFormat(fechaIngreso)
              }"
              @blur="validateFechaIngreso"
              maxlength="16"
            />
            <span class="absolute inset-y-0 right-0 flex items-center px-3 text-gray-400">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </span>
            <button
              type="button"
              @click="fechaIngreso = generarFechaIngreso()"
              class="absolute inset-y-0 right-8 flex items-center px-2 text-blue-500 hover:text-blue-700 transition-colors"
              title="Usar fecha y hora actual"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </button>
          </div>
          <div v-if="fechaIngreso && !isValidDateFormat(fechaIngreso)" class="mt-1 text-xs text-red-600">
            Formato inválido. Use DD/MM/AAAA HH:MM (ejemplo: 15/06/2025 14:30)
          </div>
        </div>
        <!-- Médico Solicitante -->
        <div class="mb-4">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">Médico Solicitante</label>
          <input
            type="text"
            v-model="formData.medicoSolicitante"
            placeholder="Nombre del médico solicitante (opcional)"
            class="h-11 w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
          />
        </div>

        <!-- Número de Muestras -->
        <div class="mb-4">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">
            Número de Muestras * 
            <span class="text-xs text-gray-500">(máximo {{ MAX_MUESTRAS }})</span>
          </label>
          <div class="relative">
            <input
              type="text"
              v-model="formData.numeroMuestras"
              @input="handleNumeroMuestrasInput"
              placeholder="Ingrese el número de muestras"
              class="h-11 w-full rounded-lg border px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3 transition-colors"
              :class="{
                'border-gray-300 bg-transparent focus:border-brand-300 focus:ring-brand-500/10': isValidNumeroMuestras(formData.numeroMuestras),
                'border-red-300 bg-red-50 focus:border-red-500 focus:ring-red-500/10': !isValidNumeroMuestras(formData.numeroMuestras)
              }"
              required
              maxlength="2"
            />
            <div class="absolute inset-y-0 right-0 flex items-center pr-3">
              <div class="flex items-center space-x-1">
                <!-- Botones de incremento/decremento -->
                <button
                  type="button"
                  @click="decrementarMuestras"
                  :disabled="parseInt(formData.numeroMuestras) <= 1"
                  class="p-1 rounded text-gray-500 hover:text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                  </svg>
                </button>
                <button
                  type="button"
                  @click="incrementarMuestras"
                  :disabled="parseInt(formData.numeroMuestras) >= MAX_MUESTRAS"
                  class="p-1 rounded text-gray-500 hover:text-gray-700 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div v-if="!isValidNumeroMuestras(formData.numeroMuestras)" class="mt-1 text-xs text-red-600">
            Ingrese un número válido entre 1 y {{ MAX_MUESTRAS }}
          </div>
        </div>

        <!-- CUPS por Muestra -->
        <div class="mb-6">
          <label class="mb-1.5 block text-sm font-medium text-gray-700">
            Información por Muestra *
          </label>
          <div class="space-y-6">
            <div v-for="(muestra, muestraIndex) in formData.muestras" :key="muestraIndex" class="space-y-4 p-4 border border-gray-200 rounded-lg bg-gray-50">
              <h4 class="text-sm font-medium text-gray-700">Muestra {{ muestra.numero }}</h4>
              
              <!-- Región del Cuerpo para esta muestra -->
              <div>
                <label class="mb-1.5 block text-sm font-medium text-gray-700">Región del Cuerpo *</label>
                <div class="relative">
                  <div class="relative">
                    <input
                      type="text"
                      v-model="formData.muestras[muestraIndex].regionCuerpo"
                      @focus="showRegiones[getRegionKey(muestraIndex)] = true"
                      @blur="ocultarRegiones(muestraIndex)"
                      placeholder="Seleccione o escriba la región del cuerpo"
                      class="h-11 w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                      required
                    />
                    <button
                      type="button"
                      @click="showRegiones[getRegionKey(muestraIndex)] = !showRegiones[getRegionKey(muestraIndex)]"
                      class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-500"
                    >
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                      </svg>
                    </button>
                  </div>
                  
                  <!-- Lista desplegable de regiones -->
                  <transition
                    enter-active-class="transition ease-out duration-200"
                    enter-from-class="opacity-0 transform scale-95"
                    enter-to-class="opacity-100 transform scale-100"
                    leave-active-class="transition ease-in duration-150"
                    leave-from-class="opacity-100 transform scale-100"
                    leave-to-class="opacity-0 transform scale-95"
                  >
                    <div
                      v-if="showRegiones[getRegionKey(muestraIndex)]"
                      class="absolute z-50 w-full mt-1 bg-white rounded-lg shadow-lg border border-gray-200 max-h-60 overflow-auto"
                    >
                      <ul class="py-1">
                        <li
                          v-for="region in getRegionesFiltradas(formData.muestras[muestraIndex].regionCuerpo)"
                          :key="region.value"
                          @mousedown="seleccionarRegion(muestraIndex, region)"
                          class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer transition-colors"
                        >
                          {{ region.label }}
                        </li>
                        <li
                          v-if="getRegionesFiltradas(formData.muestras[muestraIndex].regionCuerpo).length === 0"
                          class="px-4 py-2 text-sm text-gray-500"
                        >
                          No se encontraron resultados
                        </li>
                      </ul>
                    </div>
                  </transition>
                </div>
              </div>

              <!-- CUPS para esta muestra -->
              <div>
                <label class="mb-1.5 block text-sm font-medium text-gray-700">Códigos CUPS *</label>
                <div class="space-y-2">
                  <div v-for="(cups, cupsIndex) in muestra.cups" :key="cupsIndex" class="flex items-center space-x-2">
                    <div class="relative flex-1">
                      <div class="relative">
                        <input
                          type="text"
                          v-model="formData.muestras[muestraIndex].cups[cupsIndex].code"
                          @focus="showCupsList[getCupsKey(muestraIndex, cupsIndex)] = true"
                          @blur="ocultarCupsList(muestraIndex, cupsIndex)"
                          placeholder="Seleccione o escriba el código CUPS"
                          class="h-11 w-full rounded-lg border px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:outline-hidden focus:ring-3 transition-colors"
                          :class="{
                            'border-gray-300 bg-transparent focus:border-brand-300 focus:ring-brand-500/10': !cups.code || isValidCupsCode(cups.code),
                            'border-red-300 bg-red-50 focus:border-red-500 focus:ring-red-500/10': cups.code && !isValidCupsCode(cups.code)
                          }"
                          required
                          @keydown.enter.prevent="agregarCupsSiNecesario(muestraIndex, cupsIndex)"
                          :ref="el => { if (el) cupsInputs[muestraIndex][cupsIndex] = el as HTMLInputElement }"
                        />
                        <div class="absolute inset-y-0 right-8 flex items-center">
                          <!-- Indicador de validación -->
                          <div v-if="cups.code" class="mr-2">
                            <svg v-if="isValidCupsCode(cups.code)" class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                            </svg>
                            <svg v-else class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                          </div>
                        </div>
                        <button
                          type="button"
                          @click="showCupsList[getCupsKey(muestraIndex, cupsIndex)] = !showCupsList[getCupsKey(muestraIndex, cupsIndex)]"
                          class="absolute inset-y-0 right-0 flex items-center px-2 text-gray-500"
                        >
                          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                          </svg>
                        </button>
                      </div>
                      
                      <!-- Lista desplegable de códigos CUPS -->
                      <div
                        v-if="showCupsList[getCupsKey(muestraIndex, cupsIndex)]"
                        class="absolute z-50 w-full mt-1 bg-white rounded-lg shadow-lg border border-gray-200 max-h-60 overflow-auto"
                      >
                        <ul class="py-1">
                          <li
                            v-for="cupsOption in getCupsFiltrados(formData.muestras[muestraIndex].cups[cupsIndex].code)"
                            :key="cupsOption.value"
                            @mousedown="seleccionarCups(muestraIndex, cupsIndex, cupsOption)"
                            class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer transition-colors"
                          >
                            {{ cupsOption.label }}
                          </li>
                          <li
                            v-if="getCupsFiltrados(formData.muestras[muestraIndex].cups[cupsIndex].code).length === 0"
                            class="px-4 py-2 text-sm text-gray-500"
                          >
                            No se encontraron códigos CUPS
                          </li>
                        </ul>
                      </div>
                    </div>
                    <!-- Input para el multiplicador -->
                    <input
                      type="number"
                      min="1"
                      v-model.number="formData.muestras[muestraIndex].cups[cupsIndex].cantidad"
                      class="w-11 h-11 rounded-lg border border-gray-300 bg-white px-1 py-1 text-sm text-gray-800 text-center focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10 appearance-none hide-number-spin"
                      placeholder="#"
                      title="Cantidad de veces"
                      inputmode="numeric"
                      @wheel="(e) => { const t = e.target as HTMLInputElement; if (t) t.blur(); }"
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
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="flex justify-end space-x-4 mt-6">
          <button
            @click="limpiarFormulario"
            type="button"
            class="inline-flex items-center px-6 py-2.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            :disabled="isSaving"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
            Limpiar
          </button>
          
          <button
            @click="guardarMuestra"
            type="button"
            class="inline-flex items-center px-6 py-2.5 border border-transparent rounded-lg text-sm font-medium text-white transition-colors"
            :class="{
              'bg-brand-500 hover:bg-brand-600 focus:ring-brand-300': isFormValid && !isSaving,
              'bg-gray-400 hover:bg-gray-400 cursor-not-allowed': !isFormValid || isSaving
            }"
            :disabled="!isFormValid || isSaving"
            :title="!isFormValid ? (primerErrorValidacion || 'Complete todos los campos requeridos') : 'Guardar la solicitud de muestra'"
          >
            <svg
              v-if="isSaving"
              class="animate-spin -ml-1 mr-2 h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <svg
              v-else
              class="w-5 h-5 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            {{ isSaving ? 'Guardando...' : 'Guardar Muestra' }}
          </button>
        </div>

        <!-- Información de Validación -->
        <div v-if="!isFormValid && primerErrorValidacion" class="mt-4">
          <div class="rounded-lg bg-amber-50 border border-amber-200 p-3">
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-amber-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
              </svg>
              <p class="text-sm text-amber-700">
                <strong>Para continuar:</strong> {{ primerErrorValidacion }}
              </p>
            </div>
          </div>
        </div>

        <!-- Progreso del Formulario -->
        <div class="mt-6 bg-gray-50 rounded-lg p-4">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-medium text-gray-700">Progreso del Formulario</span>
            <span class="text-sm text-gray-600">{{ progresoFormulario }}%</span>
          </div>
          <div class="w-full bg-gray-200 rounded-full h-2">
            <div 
              class="h-2 rounded-full transition-all duration-300"
              :class="{
                'bg-red-500': progresoFormulario < 40,
                'bg-yellow-500': progresoFormulario >= 40 && progresoFormulario < 80,
                'bg-green-500': progresoFormulario >= 80
              }"
              :style="{ width: progresoFormulario + '%' }"
            ></div>
          </div>
          <div class="mt-2 text-xs text-gray-500">
            {{ getProgresoDescripcion() }}
          </div>
        </div>

        <!-- Código de Muestra Asignado -->
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
          class="relative bg-white rounded-xl shadow-2xl border-l-4 border-green-500 p-6 max-w-sm w-full"
        >
          <div class="text-center">
            <!-- Ícono de éxito -->
            <div class="mx-auto flex items-center justify-center w-12 h-12 rounded-full bg-green-100 mb-3">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            
            <!-- Título -->
            <h3 class="text-lg font-bold text-gray-900 mb-2">¡Muestra Registrada!</h3>
            
            <!-- Mensaje -->
            <p class="text-sm text-gray-600 mb-1">
              Paciente: <span class="font-semibold text-brand-600">{{ pacienteInfo.nombre }}</span>
            </p>
            <p class="text-xs text-gray-500 mb-3">
              Código asignado:
            </p>
            <p class="text-xl font-bold text-green-600 font-mono mb-4">
              {{ registeredSampleId }}
            </p>
            
            <!-- Timestamp compacto -->
            <div class="flex items-center justify-center text-xs text-gray-400 mb-4">
              <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {{ new Date().toLocaleTimeString() }}
            </div>
            
            <!-- Barra de progreso -->
            <div class="w-full bg-gray-200 rounded-full h-1.5 mb-4">
              <div 
                class="bg-green-500 h-1.5 rounded-full transition-all duration-75 ease-linear"
                :style="{ width: progressWidth + '%' }"
              ></div>
            </div>
            
            <!-- Botones de acción compactos -->
            <div class="space-y-2">
              <!-- Botón principal para copiar código -->
              <button
                @click="copyFromNotificationAndClose"
                class="w-full inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-lg text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-1 transition-colors"
              >
                <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                Copiar Código
              </button>
              
              <!-- Botón secundario -->
              <button
                @click="showNotification = false"
                class="w-full inline-flex items-center justify-center px-4 py-2 border border-green-300 rounded-lg text-sm font-medium text-green-700 bg-green-50 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-1 transition-colors"
              >
                <svg class="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
import { ref, reactive, computed, nextTick, onMounted, watchEffect, watch } from 'vue'
import { buscarPacientePorCedula } from '@/api/pacientes'
import { crearSolicitudMuestras } from '@/api/muestras'

// ===== PROPS =====
interface PacienteGuardado {
  numeroCedula: string
  nombrePaciente: string
  sexo: string
  edad: string | number
  entidad: string
  tipoAtencion: string
  observaciones: string
}

const props = defineProps<{
  nuevoPacienteGuardado?: PacienteGuardado | null
}>()

// ===== CONSTANTS =====
const MAX_MUESTRAS = 10
const NOTIFICATION_DURATION = 5000
const PROGRESS_INTERVAL = 50

const REGIONES_CUERPO = [
  { value: 'cabeza-cuello', label: 'Cabeza y Cuello' },
  { value: 'torax', label: 'Tórax' },
  { value: 'abdomen', label: 'Abdomen' },
  { value: 'pelvis', label: 'Pelvis' },
  { value: 'extremidades-superiores', label: 'Extremidades Superiores' },
  { value: 'extremidades-inferiores', label: 'Extremidades Inferiores' },
  { value: 'espalda', label: 'Espalda' },
  { value: 'piel-tejido-subcutaneo', label: 'Piel y Tejido Subcutáneo' },
  { value: 'sistema-nervioso', label: 'Sistema Nervioso' },
  { value: 'organos-internos', label: 'Órganos Internos' },
  { value: 'sangre', label: 'Sangre' },
  { value: 'orina', label: 'Orina' },
  { value: 'otros-fluidos', label: 'Otros Fluidos Corporales' },
  { value: 'otro', label: 'Otro' }
] as const

const CODIGOS_CUPS = [
  { value: '880102', label: '880102 - Biopsia de piel' },
  { value: '880103', label: '880103 - Biopsia de tejido subcutáneo' },
  { value: '880201', label: '880201 - Biopsia de músculo' },
  { value: '880301', label: '880301 - Biopsia de hueso' },
  { value: '880401', label: '880401 - Biopsia de cartílago' },
  { value: '881001', label: '881001 - Biopsia de hígado' },
  { value: '881002', label: '881002 - Biopsia de riñón' },
  { value: '881003', label: '881003 - Biopsia de pulmón' },
  { value: '881004', label: '881004 - Biopsia de corazón' },
  { value: '881101', label: '881101 - Biopsia de mama' },
  { value: '881102', label: '881102 - Biopsia de tiroides' },
  { value: '881103', label: '881103 - Biopsia de próstata' },
  { value: '881201', label: '881201 - Biopsia de ganglios linfáticos' },
  { value: '881301', label: '881301 - Biopsia de médula ósea' },
  { value: '882001', label: '882001 - Citología cervicovaginal' },
  { value: '882002', label: '882002 - Citología de líquido pleural' },
  { value: '882003', label: '882003 - Citología de líquido ascítico' },
  { value: '882004', label: '882004 - Citología de LCR' },
  { value: '883001', label: '883001 - Estudio histopatológico básico' },
  { value: '883002', label: '883002 - Estudio histopatológico complejo' },
  { value: '883003', label: '883003 - Inmunohistoquímica básica' },
  { value: '883004', label: '883004 - Inmunohistoquímica compleja' },
  { value: '884001', label: '884001 - Microscopia electrónica' },
  { value: '885001', label: '885001 - Estudio molecular PCR' },
  { value: '885002', label: '885002 - Secuenciación genética' },
  { value: '886001', label: '886001 - Consulta anatomopatológica' },
  { value: '887001', label: '887001 - Segunda opinión patológica' }
] as const

const TIPOS_ATENCION = [
  { value: 'ambulatorio', label: 'Ambulatorio' },
  { value: 'hospitalizado', label: 'Hospitalizado' },
] as const

const ENTIDADES = [
  { value: 'ESSALUD', label: 'ESSALUD' },
  { value: 'MINSA', label: 'MINSA' },
  { value: 'SIS', label: 'SIS' },
  { value: 'FFAA', label: 'FFAA' },
  { value: 'FFPP', label: 'FFPP' },
  { value: 'PARTICULAR', label: 'PARTICULAR' },
  { value: 'OTRO', label: 'OTRO' }
] as const

const MOCK_PATIENTS: Record<string, PacienteData> = {
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

// ===== INTERFACES =====
interface PacienteData {
  id?: string
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
  regionCuerpo: string
  muestras: {
    numero: number
    regionCuerpo?: string
    cups: { code: string, cantidad: number }[]
  }[]
  medicoSolicitante?: string
}

interface Muestra {
  numero: number
  regionCuerpo: string
  cups: { code: string, cantidad: number }[]
}

// ===== COMPOSABLES =====
const useClipboard = () => {
  const copyToClipboard = async (text: string): Promise<boolean> => {
    try {
      await navigator.clipboard.writeText(text)
      return true
    } catch (err) {
      console.error('Error al copiar:', err)
      return false
    }
  }
  return { copyToClipboard }
}

const useNotification = () => {
  const showNotification = ref(false)
  const progressWidth = ref(100)
  
  const startAutoClose = () => {
    progressWidth.value = 100
    const decrement = (PROGRESS_INTERVAL / NOTIFICATION_DURATION) * 100
    
    const progressInterval = setInterval(() => {
      progressWidth.value -= decrement
      if (progressWidth.value <= 0) {
        clearInterval(progressInterval)
        showNotification.value = false
        progressWidth.value = 100
      }
    }, PROGRESS_INTERVAL)
  }
  
  const show = () => {
    showNotification.value = true
    startAutoClose()
  }
  
  const hide = () => {
    showNotification.value = false
    progressWidth.value = 100
  }
  
  return { showNotification, progressWidth, show, hide }
}

// ===== BASE DE DATOS SIMULADA =====
// Utilizamos MOCK_PATIENTS definida arriba

// ===== UTILITY FUNCTIONS =====
const createEmptyPaciente = (cedula = ''): PacienteData => ({
  nombre: '',
  cedula,
  edad: '',
  telefono: '',
  sexo: '',
  entidad: '',
  tipoAtencion: '',
  observaciones: ''
})

const createEmptyMuestra = (numero: number): Muestra => ({
  numero,
  regionCuerpo: '',
  cups: [{ code: '', cantidad: 1 }]
})

const sanitizeNumericInput = (value: string, max: number): string => {
  const cleaned = value.replace(/[^0-9]/g, '')
  if (cleaned === '') return ''
  const numValue = parseInt(cleaned)
  return numValue > max ? max.toString() : cleaned
}

// ===== STATE =====
// Estados del paciente
const pacienteAsignado = ref<PacienteData | null>(null)
const pacienteInfo = ref<PacienteData>(createEmptyPaciente())
const cedula = ref('')
const isLoading = ref(false)
const searchPerformed = ref(false)
const pacienteEncontrado = ref(false)
const pacienteAsignadoAutomaticamente = ref(false) // Para distinguir asignación automática

// Estados del formulario
const registeredSampleId = ref('')
const fechaIngreso = ref('')
const isSaving = ref(false)  // Estado de carga para guardar
const errorMessage = ref('')  // Mensaje de error
const formData = reactive({
  numeroMuestras: '1',
  muestras: [createEmptyMuestra(1)],
  medicoSolicitante: ''
})

// Referencias y utilidades
const cupsInputs = ref<(HTMLInputElement | null)[][]>([[]])
const { copyToClipboard } = useClipboard()
const { showNotification, progressWidth, show: showNotif, hide: hideNotif } = useNotification()

// Estados para el combobox de región del cuerpo
const showRegiones = ref<Record<string, boolean>>({})

// Estados para el combobox de tipo de atención
const showTiposAtencion = ref(false)

// Estados para el combobox de entidad
const showEntidades = ref(false)

// Estados para el combobox de CUPS
const showCupsList = ref<Record<string, boolean>>({})

// ===== COMPUTED =====
const isFormValid = computed(() => {
  return !!(
    pacienteAsignado.value &&
    fechaIngreso.value.trim() &&
    formData.muestras.length > 0 &&
    formData.muestras.every(muestra => 
      muestra.regionCuerpo.trim() &&
      muestra.cups.length > 0 && 
      muestra.cups.every(cups => cups.code.trim() !== '' && cups.cantidad > 0)
    )
  )
})

// Validaciones individuales para retroalimentación en tiempo real
const validacionCampos = computed(() => ({
  fechaIngreso: {
    valido: fechaIngreso.value.trim() !== '',
    mensaje: 'La fecha de ingreso es obligatoria'
  },
  numeroMuestras: {
    valido: formData.numeroMuestras !== '' && parseInt(formData.numeroMuestras) > 0,
    mensaje: 'Debe especificar al menos 1 muestra'
  },
  muestras: formData.muestras.map(muestra => ({
    regionCuerpo: {
      valido: muestra.regionCuerpo.trim() !== '',
      mensaje: 'La región del cuerpo es obligatoria'
    },
    cups: muestra.cups.map(cups => ({
      codigo: {
        valido: cups.code.trim() !== '',
        mensaje: 'El código CUPS es obligatorio'
      },
      cantidad: {
        valido: cups.cantidad > 0,
        mensaje: 'La cantidad debe ser mayor a 0'
      }
    }))
  }))
}))

// Función para obtener el primer error de validación
const primerErrorValidacion = computed(() => {
  const validacion = validacionCampos.value
  
  if (!validacion.fechaIngreso.valido) {
    return validacion.fechaIngreso.mensaje
  }
  
  if (!validacion.numeroMuestras.valido) {
    return validacion.numeroMuestras.mensaje
  }
  
  for (let i = 0; i < validacion.muestras.length; i++) {
    const muestra = validacion.muestras[i]
    if (!muestra.regionCuerpo.valido) {
      return `Muestra ${i + 1}: ${muestra.regionCuerpo.mensaje}`
    }
    
    for (let j = 0; j < muestra.cups.length; j++) {
      const cups = muestra.cups[j]
      if (!cups.codigo.valido) {
        return `Muestra ${i + 1}, CUPS ${j + 1}: ${cups.codigo.mensaje}`
      }
      if (!cups.cantidad.valido) {
        return `Muestra ${i + 1}, CUPS ${j + 1}: ${cups.cantidad.mensaje}`
      }
    }
  }
  
  return null
})

// Progreso del formulario en porcentaje
const progresoFormulario = computed(() => {
  let totalCampos = 0
  let camposCompletos = 0
  
  // Campos básicos
  totalCampos += 2 // fechaIngreso, numeroMuestras
  if (fechaIngreso.value.trim() && isValidDateFormat(fechaIngreso.value)) camposCompletos++
  if (formData.numeroMuestras && isValidNumeroMuestras(formData.numeroMuestras)) camposCompletos++
  
  // Muestras
  formData.muestras.forEach((muestra) => {
    totalCampos += 1 // regionCuerpo
    if (muestra.regionCuerpo.trim()) camposCompletos++
    
    // CUPS por muestra
    muestra.cups.forEach((cups) => {
      totalCampos += 1 // código CUPS
      if (cups.code.trim() && isValidCupsCode(cups.code) && cups.cantidad > 0) camposCompletos++
    })
  })
  
  return totalCampos > 0 ? Math.round((camposCompletos / totalCampos) * 100) : 0
})

// Descripción del progreso
const getProgresoDescripcion = () => {
  const progreso = progresoFormulario.value
  if (progreso < 40) return 'Comenzando... Complete la información básica'
  if (progreso < 80) return 'En progreso... Agregue los códigos CUPS necesarios'
  if (progreso < 100) return 'Casi listo... Revise los datos antes de guardar'
  return '¡Formulario completo! Listo para guardar'
}

// Computed para filtrar códigos CUPS
const getCupsFiltrados = (searchTerm: string) => {
  if (!searchTerm) return CODIGOS_CUPS
  const term = searchTerm.toLowerCase()
  return CODIGOS_CUPS.filter(cups => 
    cups.label.toLowerCase().includes(term) ||
    cups.value.includes(term)
  )
}

// Función para filtrar regiones del cuerpo por muestra
const getRegionesFiltradas = (searchTerm: string) => {
  if (!searchTerm) return REGIONES_CUERPO
  const term = searchTerm.toLowerCase()
  return REGIONES_CUERPO.filter(region => 
    region.label.toLowerCase().includes(term)
  )
}

// ===== WATCHERS =====
watchEffect(() => {
  // Actualizar muestras cuando cambia el número
  const numeroMuestras = formData.numeroMuestras === '' ? 1 : Math.max(1, Math.min(MAX_MUESTRAS, parseInt(formData.numeroMuestras)))
  
  // Ajustar el array de muestras
  while (formData.muestras.length < numeroMuestras) {
    formData.muestras.push(createEmptyMuestra(formData.muestras.length + 1))
    cupsInputs.value.push([])
  }
  while (formData.muestras.length > numeroMuestras) {
    formData.muestras.pop()
    cupsInputs.value.pop()
  }
})

// ===== WATCHERS =====
// Watcher para manejar cuando se guarda un nuevo paciente
watch(
  () => props.nuevoPacienteGuardado,
  (nuevosPaciente) => {
    if (nuevosPaciente) {
      console.log('Nuevo paciente recibido:', nuevosPaciente)
      
      // Actualizar el campo de cédula
      cedula.value = nuevosPaciente.numeroCedula
      
      // Simular la asignación automática del paciente
      pacienteEncontrado.value = true
      searchPerformed.value = true
      pacienteAsignadoAutomaticamente.value = true // Marcar como asignación automática
      
      // Mapear los datos del nuevo paciente a la estructura esperada
      pacienteInfo.value = {
        id: nuevosPaciente.numeroCedula,
        cedula: nuevosPaciente.numeroCedula,
        nombre: nuevosPaciente.nombrePaciente,
        sexo: nuevosPaciente.sexo,
        edad: nuevosPaciente.edad.toString(),
        entidad: nuevosPaciente.entidad,
        tipoAtencion: nuevosPaciente.tipoAtencion,
        observaciones: nuevosPaciente.observaciones || ''
      }
      
      // Asignar el paciente
      pacienteAsignado.value = { ...pacienteInfo.value }
      
      // Generar fecha de ingreso automáticamente
      fechaIngreso.value = generarFechaIngreso()
      
      // Emitir eventos
      emit('paciente-verificado', { 
        encontrado: true, 
        paciente: pacienteInfo.value, 
        cedula: cedula.value 
      })
      emit('asignar-paciente', pacienteInfo.value)
      
      // Resetear el estado en el componente padre
      emit('reset-nuevo-paciente')
    }
  },
  { immediate: true }
)

// ===== FUNCTIONS =====
const generarFechaIngreso = (): string => {
  const ahora = new Date()
  
  // Asegurar que estamos trabajando con una fecha válida
  if (isNaN(ahora.getTime())) {
    console.error('Error: fecha actual inválida')
    return ''
  }
  
  const dia = ahora.getDate().toString().padStart(2, '0')
  const mes = (ahora.getMonth() + 1).toString().padStart(2, '0')
  const año = ahora.getFullYear()
  const horas = ahora.getHours().toString().padStart(2, '0')
  const minutos = ahora.getMinutes().toString().padStart(2, '0')
  
  const fechaFormateada = `${dia}/${mes}/${año} ${horas}:${minutos}`
  
  // Validar que la fecha generada es correcta
  if (!isValidDateFormat(fechaFormateada)) {
    console.error('Error: fecha generada inválida:', fechaFormateada)
    return ''
  }
  
  return fechaFormateada
}

const verificarPaciente = async () => {
  if (!cedula.value.trim()) return

  isLoading.value = true
  searchPerformed.value = true
  pacienteAsignadoAutomaticamente.value = false // Resetear para búsqueda manual

  try {
    // Buscar paciente en la base de datos real
    const paciente = await buscarPacientePorCedula(cedula.value.trim())
    
    if (paciente) {
      pacienteEncontrado.value = true
      // Mapear los campos del paciente a la estructura esperada
      // Nota: Con los cambios en el backend, el 'id' ahora es la cédula directamente
      pacienteInfo.value = {
        id: paciente.id, // ID del paciente (que es la cédula)
        cedula: paciente.id, // Usar id como cédula (ya que _id = numeroCedula)
        nombre: paciente.nombrePaciente,
        sexo: paciente.sexo,
        edad: paciente.edad,
        entidad: paciente.entidad,
        tipoAtencion: paciente.tipoAtencion,
        observaciones: paciente.observaciones || ''
      }
      pacienteAsignado.value = { ...pacienteInfo.value }
      
      // Generar fecha de ingreso automáticamente
      fechaIngreso.value = generarFechaIngreso()
      
      emit('paciente-verificado', { 
        encontrado: true, 
        paciente: pacienteInfo.value, 
        cedula: cedula.value 
      })
      emit('asignar-paciente', pacienteInfo.value)
    } else {
      pacienteEncontrado.value = false
      pacienteAsignado.value = null
      pacienteInfo.value = createEmptyPaciente(cedula.value)
      
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

const limpiarFormulario = () => {
  // Limpiar datos del paciente
  cedula.value = ''
  searchPerformed.value = false
  pacienteEncontrado.value = false
  pacienteAsignado.value = null
  pacienteInfo.value = createEmptyPaciente()

  // Limpiar datos de la muestra
  formData.numeroMuestras = '1'
  formData.muestras = [createEmptyMuestra(1)]
  formData.medicoSolicitante = ''
  fechaIngreso.value = ''
  
  // Limpiar notificación
  hideNotif()
  registeredSampleId.value = ''
}

const handleNumeroMuestrasInput = (event: Event) => {
  const input = event.target as HTMLInputElement
  const sanitized = sanitizeNumericInput(input.value, MAX_MUESTRAS)
  formData.numeroMuestras = sanitized
}

const agregarCups = (muestraIndex: number) => {
  formData.muestras[muestraIndex].cups.push({ code: '', cantidad: 1 })
  nextTick(() => {
    const lastIndex = formData.muestras[muestraIndex].cups.length - 1
    cupsInputs.value[muestraIndex]?.[lastIndex]?.focus()
  })
}

const eliminarCups = (muestraIndex: number, cupsIndex: number) => {
  formData.muestras[muestraIndex].cups.splice(cupsIndex, 1)
  nextTick(() => {
    const newIndex = Math.min(cupsIndex, formData.muestras[muestraIndex].cups.length - 1)
    cupsInputs.value[muestraIndex]?.[newIndex]?.focus()
  })
}

const agregarCupsSiNecesario = (muestraIndex: number, cupsIndex: number) => {
  const currentCups = formData.muestras[muestraIndex].cups[cupsIndex].code
  if (currentCups.trim() !== '') {
    agregarCups(muestraIndex)
  }
}

const generarCodigoMuestra = (): string => {
  const timestamp = Date.now()
  const suffix = Math.random().toString(36).substring(2, 6).toUpperCase()
  return `M${timestamp}${suffix}`
}

const guardarMuestra = async () => {
  // Validación previa detallada
  if (!pacienteAsignado.value || !pacienteInfo.value.id) {
    errorMessage.value = 'Error: No hay un paciente asignado válido'
    return
  }

  const errorValidacion = primerErrorValidacion.value
  if (errorValidacion) {
    errorMessage.value = `Error de validación: ${errorValidacion}`
    return
  }

  try {
    isSaving.value = true
    errorMessage.value = ''

    // Validar fecha de ingreso con formato
    if (!isValidDateFormat(fechaIngreso.value)) {
      throw new Error('El formato de fecha de ingreso no es válido. Use DD/MM/YYYY HH:MM (ejemplo: 15/06/2025 14:30)')
    }

    // Validar que la fecha no sea muy antigua o muy futura
    try {
      const [datePart, timePart] = fechaIngreso.value.split(' ')
      const [day, month, year] = datePart.split('/').map(Number)
      const [hours, minutes] = timePart.split(':').map(Number)
      const fechaIngreso_parsed = new Date(year, month - 1, day, hours, minutes)
      
      const ahora = new Date()
      const diferenciaDias = Math.abs((fechaIngreso_parsed.getTime() - ahora.getTime()) / (1000 * 60 * 60 * 24))
      
      if (diferenciaDias > 365) {
        throw new Error('La fecha de ingreso no puede ser mayor a un año en el pasado o futuro')
      }
    } catch (error) {
      if (error instanceof Error && error.message.includes('año')) {
        throw error
      }
      throw new Error('Error al procesar la fecha de ingreso. Verifique el formato DD/MM/YYYY HH:MM')
    }

    // Preparar los datos para enviar a la API
    const solicitudData = {
      numeroMuestras: formData.numeroMuestras,
      muestras: formData.muestras.map(muestra => ({
        numero: muestra.numero,
        regionCuerpo: muestra.regionCuerpo,
        cups: muestra.cups.filter(cups => cups.code.trim() !== '' && cups.cantidad > 0)
      })).filter(muestra => muestra.cups.length > 0 && muestra.regionCuerpo.trim() !== ''),
      medicoSolicitante: formData.medicoSolicitante.trim() || '',
      fechaIngreso: fechaIngreso.value,
      pacienteId: pacienteInfo.value.id,
      // Agregar nombre del paciente y entidad
      nombrePaciente: pacienteInfo.value.nombre,
      entidad: pacienteInfo.value.entidad || '',
      observaciones: ''
    }

    // Validación final antes del envío
    if (solicitudData.muestras.length === 0) {
      throw new Error('Debe configurar al menos una muestra válida con sus códigos CUPS')
    }

    // Verificar conectividad (opcional)
    if (!navigator.onLine) {
      throw new Error('No hay conexión a internet. Verifique su conexión e inténtelo nuevamente.')
    }

    // Llamar a la API para crear la solicitud de muestras
    const resultado = await crearSolicitudMuestras(solicitudData)
    
    if (!resultado || !resultado.codigo_solicitud) {
      throw new Error('La respuesta del servidor no contiene el código de solicitud')
    }
    
    // Mostrar el código de solicitud generado
    registeredSampleId.value = resultado.codigo_solicitud
    showNotif()
    
    // Emitir eventos para compatibilidad
    emit('sample-registered', {
      id: resultado.codigo_solicitud,
      paciente: pacienteAsignado.value,
      regionCuerpo: '',
      muestras: solicitudData.muestras.map(muestra => ({
        numero: muestra.numero,
        regionCuerpo: muestra.regionCuerpo,
        cups: muestra.cups
      })),
      medicoSolicitante: formData.medicoSolicitante
    })

    // Limpiar el formulario después del éxito, conservando el código asignado
    limpiarFormularioPostGuardado()

  } catch (error) {
    console.error('Error al guardar la solicitud de muestras:', error)
    
    // Manejo específico de diferentes tipos de errores
    let mensajeError = 'Error desconocido al guardar la muestra'
    
    if (error instanceof Error) {
      // Errores de validación o de red
      if (error.message.includes('fecha') || error.message.includes('Invalid time')) {
        mensajeError = `Error de fecha: ${error.message}`
      } else if (error.message.includes('fetch')) {
        mensajeError = 'Error de conexión. Verifique su conexión a internet e inténtelo nuevamente.'
      } else if (error.message.includes('400')) {
        mensajeError = 'Datos inválidos. Por favor, revise la información ingresada.'
      } else if (error.message.includes('401')) {
        mensajeError = 'No autorizado. Por favor, inicie sesión nuevamente.'
      } else if (error.message.includes('404')) {
        mensajeError = 'Paciente no encontrado en el sistema.'
      } else if (error.message.includes('500')) {
        mensajeError = 'Error interno del servidor. Contacte al administrador del sistema.'
      } else {
        mensajeError = error.message
      }
    }
    
    errorMessage.value = mensajeError
    
    // Scroll hacia arriba para mostrar el error
    scrollToTop()
  } finally {
    isSaving.value = false
  }
}

// Función auxiliar para validar formato de fecha
const isValidDateFormat = (dateString: string): boolean => {
  const regex = /^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}$/
  if (!regex.test(dateString)) return false
  
  try {
    const [datePart, timePart] = dateString.split(' ')
    const [day, month, year] = datePart.split('/').map(Number)
    const [hours, minutes] = timePart.split(':').map(Number)
    
    // Validar rangos básicos
    if (day < 1 || day > 31) return false
    if (month < 1 || month > 12) return false
    if (year < 1900 || year > 2100) return false
    if (hours < 0 || hours > 23) return false
    if (minutes < 0 || minutes > 59) return false
    
    // Verificar que la fecha sea válida usando el constructor Date
    const fecha = new Date(year, month - 1, day, hours, minutes)
    
    // Verificar que la fecha construida coincide con los valores ingresados
    // (esto detecta fechas como 31/02/2025 que son inválidas)
    const fechaValida = fecha.getFullYear() === year &&
                       fecha.getMonth() === month - 1 &&
                       fecha.getDate() === day &&
                       fecha.getHours() === hours &&
                       fecha.getMinutes() === minutes
    
    return fechaValida
  } catch {
    return false
  }
}

// Función auxiliar para scroll hacia arriba
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Función para validar fecha de ingreso al perder el foco
const validateFechaIngreso = () => {
  if (fechaIngreso.value && !isValidDateFormat(fechaIngreso.value)) {
    // Opcionalmente agregar un pequeño delay para mejor UX
    setTimeout(() => {
      if (fechaIngreso.value && !isValidDateFormat(fechaIngreso.value)) {
        // Podrías agregar feedback visual adicional aquí
      }
    }, 100)
  }
}

// Función para formatear automáticamente la fecha mientras se escribe
const handleFechaIngresoInput = (event: Event) => {
  const input = event.target as HTMLInputElement
  let value = input.value.replace(/[^0-9]/g, '') // Solo números
  
  // Formatear automáticamente: DDMMYYYYHHMM -> DD/MM/YYYY HH:MM
  if (value.length >= 2) {
    value = value.substring(0, 2) + '/' + value.substring(2)
  }
  if (value.length >= 5) {
    value = value.substring(0, 5) + '/' + value.substring(5)
  }
  if (value.length >= 10) {
    value = value.substring(0, 10) + ' ' + value.substring(10)
  }
  if (value.length >= 13) {
    value = value.substring(0, 13) + ':' + value.substring(13)
  }
  
  // Limitar a 16 caracteres máximo (DD/MM/YYYY HH:MM)
  if (value.length > 16) {
    value = value.substring(0, 16)
  }
  
  fechaIngreso.value = value
}

// Función para validar código CUPS
const isValidCupsCode = (code: string): boolean => {
  if (!code || code.trim() === '') return false
  
  // Verificar si el código existe en la lista predefinida
  const exists = CODIGOS_CUPS.some(cups => cups.value === code.trim())
  if (exists) return true
  
  // Si no existe en la lista, verificar formato básico (6 dígitos)
  const basicFormat = /^\d{6}$/.test(code.trim())
  return basicFormat
}

// Función para validar formato de cédula
const isValidCedulaFormat = (cedula: string): boolean => {
  if (!cedula || cedula.trim() === '') return false
  
  // Solo números, entre 6 y 12 dígitos
  const regex = /^\d{6,12}$/
  return regex.test(cedula.trim())
}

// Función para manejar input de cédula (solo números)
const handleCedulaInput = (event: Event) => {
  const input = event.target as HTMLInputElement
  const value = input.value.replace(/[^0-9]/g, '') // Solo números
  cedula.value = value.slice(0, 12) // Máximo 12 caracteres
}

// Función para validar número de muestras
const isValidNumeroMuestras = (numero: string): boolean => {
  if (!numero || numero.trim() === '') return false
  const num = parseInt(numero)
  return !isNaN(num) && num >= 1 && num <= MAX_MUESTRAS
}

// Función para incrementar número de muestras
const incrementarMuestras = () => {
  const current = parseInt(formData.numeroMuestras) || 0
  if (current < MAX_MUESTRAS) {
    formData.numeroMuestras = (current + 1).toString()
  }
}

// Función para decrementar número de muestras
const decrementarMuestras = () => {
  const current = parseInt(formData.numeroMuestras) || 0
  if (current > 1) {
    formData.numeroMuestras = (current - 1).toString()
  }
}

// Función para limpiar solo el formulario de muestras
const limpiarFormularioMuestras = () => {
  formData.numeroMuestras = '1'
  formData.muestras = [createEmptyMuestra(1)]
  formData.medicoSolicitante = ''
  fechaIngreso.value = generarFechaIngreso()
  errorMessage.value = ''
}

const limpiarFormularioPostGuardado = () => {
  // Limpiar los datos del paciente
  cedula.value = ''
  pacienteAsignado.value = null
  pacienteInfo.value = createEmptyPaciente()
  
  // Limpiar el formulario de muestras
  formData.numeroMuestras = '1'
  formData.muestras = [createEmptyMuestra(1)]
  formData.medicoSolicitante = ''
  fechaIngreso.value = generarFechaIngreso()
  errorMessage.value = ''
  
  // NO limpiar registeredSampleId ni cerrar la notificación para conservar el código asignado
  // registeredSampleId.value = ''
  // showSuccessNotif.value = false
}

const copyFromNotificationAndClose = async () => {
  await copyToClipboard(registeredSampleId.value)
  hideNotif()
}

const copyCedula = async () => {
  await copyToClipboard(cedula.value)
}

const copyToClipboardHandler = async () => {
  await copyToClipboard(registeredSampleId.value)
}

// Funciones para el combobox de región del cuerpo
const getRegionKey = (muestraIndex: number) => {
  return `region-${muestraIndex}`
}

const seleccionarRegion = (muestraIndex: number, region: { value: string, label: string }) => {
  formData.muestras[muestraIndex].regionCuerpo = region.label
  const key = getRegionKey(muestraIndex)
  showRegiones.value[key] = false
}

const ocultarRegiones = (muestraIndex: number) => {
  window.setTimeout(() => {
    const key = getRegionKey(muestraIndex)
    showRegiones.value[key] = false
  }, 200)
}

// Funciones para el combobox de tipo de atención
const seleccionarTipoAtencion = (tipo: { value: string, label: string }) => {
  pacienteInfo.value.tipoAtencion = tipo.value
  showTiposAtencion.value = false
}

const ocultarTiposAtencion = () => {
  window.setTimeout(() => {
    showTiposAtencion.value = false
  }, 200)
}

const getTipoAtencionLabel = (value: string) => {
  const tipo = TIPOS_ATENCION.find(t => t.value === value)
  return tipo ? tipo.label : value
}

// Funciones para el combobox de entidad
const seleccionarEntidad = (entidad: { value: string, label: string }) => {
  pacienteInfo.value.entidad = entidad.value
  showEntidades.value = false
}

const ocultarEntidades = () => {
  window.setTimeout(() => {
    showEntidades.value = false
  }, 200)
}

const getEntidadLabel = (value: string) => {
  const entidad = ENTIDADES.find(e => e.value === value)
  return entidad ? entidad.label : value
}

// Funciones para el combobox de CUPS
const getCupsKey = (muestraIndex: number, cupsIndex: number) => {
  return `${muestraIndex}-${cupsIndex}`
}

const seleccionarCups = (muestraIndex: number, cupsIndex: number, cups: { value: string, label: string }) => {
  formData.muestras[muestraIndex].cups[cupsIndex].code = cups.value
  const key = getCupsKey(muestraIndex, cupsIndex)
  showCupsList.value[key] = false
}

const ocultarCupsList = (muestraIndex: number, cupsIndex: number) => {
  window.setTimeout(() => {
    const key = getCupsKey(muestraIndex, cupsIndex)
    showCupsList.value[key] = false
  }, 200)
}

// ===== LIFECYCLE =====
onMounted(() => {
  if (formData.muestras[0]?.cups.length === 0) {
    agregarCups(0)
  }
})

// ===== EMITS =====
const emit = defineEmits<{
  'paciente-verificado': [data: { encontrado: boolean; paciente: PacienteData | null; cedula: string }]
  'asignar-paciente': [paciente: PacienteData]
  'sample-registered': [data: MuestraData]
  'reset-nuevo-paciente': []
}>()

// ===== EXPOSE =====
defineExpose({
  limpiarFormulario,
  verificarPaciente
})
</script>

<style scoped>
/* Oculta los spinners de los inputs type=number en la mayoría de navegadores */
.hide-number-spin::-webkit-inner-spin-button,
.hide-number-spin::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.hide-number-spin {
  appearance: textfield;
  -moz-appearance: textfield;
}
</style>