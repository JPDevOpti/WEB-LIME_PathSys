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
              placeholder="DD/MM/YYYY HH:MM"
              class="h-11 w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            />
            <span class="absolute inset-y-0 right-0 flex items-center px-3 text-gray-400">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
              </svg>
            </span>
          </div>
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
                          v-model="formData.muestras[muestraIndex].cups[cupsIndex]"
                          @focus="showCupsList[getCupsKey(muestraIndex, cupsIndex)] = true"
                          @blur="ocultarCupsList(muestraIndex, cupsIndex)"
                          placeholder="Seleccione o escriba el código CUPS"
                          class="h-11 w-full rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                          required
                          @keydown.enter.prevent="agregarCupsSiNecesario(muestraIndex, cupsIndex)"
                          :ref="el => { if (el) cupsInputs[muestraIndex][cupsIndex] = el as HTMLInputElement }"
                        />
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
                            v-for="cupsOption in getCupsFiltrados(formData.muestras[muestraIndex].cups[cupsIndex])"
                            :key="cupsOption.value"
                            @mousedown="seleccionarCups(muestraIndex, cupsIndex, cupsOption)"
                            class="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer transition-colors"
                          >
                            {{ cupsOption.label }}
                          </li>
                          <li
                            v-if="getCupsFiltrados(formData.muestras[muestraIndex].cups[cupsIndex]).length === 0"
                            class="px-4 py-2 text-sm text-gray-500"
                          >
                            No se encontraron códigos CUPS
                          </li>
                        </ul>
                      </div>
                    </div>
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
                    @click="copyToClipboardHandler"
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
import { ref, reactive, computed, nextTick, onMounted, watchEffect } from 'vue'

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
  { value: 'urgencias', label: 'Urgencias' },
  { value: 'cirugia', label: 'Cirugía' }
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
    cups: string[]
  }[]
}

interface Muestra {
  numero: number
  regionCuerpo: string
  cups: string[]
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
  cups: ['']
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

// Estados del formulario
const registeredSampleId = ref('')
const fechaIngreso = ref('')
const formData = reactive({
  numeroMuestras: '1',
  muestras: [createEmptyMuestra(1)]
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
    formData.muestras.length > 0 &&
    formData.muestras.every(muestra => 
      muestra.regionCuerpo.trim() &&
      muestra.cups.length > 0 && 
      muestra.cups.every(cups => cups.trim() !== '')
    )
  )
})

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

// ===== FUNCTIONS =====
const generarFechaIngreso = (): string => {
  const ahora = new Date()
  const dia = ahora.getDate().toString().padStart(2, '0')
  const mes = (ahora.getMonth() + 1).toString().padStart(2, '0')
  const año = ahora.getFullYear()
  const horas = ahora.getHours().toString().padStart(2, '0')
  const minutos = ahora.getMinutes().toString().padStart(2, '0')
  
  return `${dia}/${mes}/${año} ${horas}:${minutos}`
}

const verificarPaciente = async () => {
  if (!cedula.value.trim()) return

  isLoading.value = true
  searchPerformed.value = true

  try {
    const paciente = MOCK_PATIENTS[cedula.value]
    
    if (paciente) {
      pacienteEncontrado.value = true
      pacienteInfo.value = { ...paciente }
      pacienteAsignado.value = { ...paciente }
      
      // Generar fecha de ingreso automáticamente
      fechaIngreso.value = generarFechaIngreso()
      
      emit('paciente-verificado', { 
        encontrado: true, 
        paciente, 
        cedula: cedula.value 
      })
      emit('asignar-paciente', paciente)
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
  formData.muestras[muestraIndex].cups.push('')
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
  const currentCups = formData.muestras[muestraIndex].cups[cupsIndex]
  if (currentCups.trim() !== '') {
    agregarCups(muestraIndex)
  }
}

const generarCodigoMuestra = (): string => {
  const timestamp = Date.now()
  const suffix = Math.random().toString(36).substring(2, 6).toUpperCase()
  return `M${timestamp}${suffix}`
}

const guardarMuestra = () => {
  if (!isFormValid.value || !pacienteAsignado.value) return

  const nuevaMuestra: MuestraData = {
    id: generarCodigoMuestra(),
    paciente: pacienteAsignado.value,
    regionCuerpo: '', // Este campo se mantendrá por compatibilidad pero las regiones estarán en cada muestra
    muestras: formData.muestras
      .map(muestra => ({
        numero: muestra.numero,
        regionCuerpo: muestra.regionCuerpo,
        cups: muestra.cups.filter(cups => cups.trim() !== '')
      }))
      .filter(muestra => muestra.cups.length > 0 && muestra.regionCuerpo.trim() !== '')
  }

  registeredSampleId.value = nuevaMuestra.id
  showNotif()
  emit('sample-registered', nuevaMuestra)
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
  formData.muestras[muestraIndex].cups[cupsIndex] = cups.value
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
}>()

// ===== EXPOSE =====
defineExpose({
  limpiarFormulario,
  verificarPaciente
})
</script>