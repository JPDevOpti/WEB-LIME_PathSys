<template>
  <div class="space-y-4">
    <!-- Barra de búsqueda y filtros -->
    <div class="bg-white rounded-xl border border-gray-200 p-4">
      <div class="flex flex-col gap-4">
        <!-- Fila de búsqueda -->
        <div class="flex flex-col sm:flex-row sm:items-center gap-3">
          <div class="relative flex-1">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Buscar por nombre, cedula o ID de muestra..."
              class="h-11 w-full pl-10 pr-4 rounded-lg border border-gray-300 bg-transparent py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
            />
          </div>
          <div class="relative flex-1">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </div>
            <input
              ref="medicoInput"
              v-model="searchMedico"
              type="text"
              placeholder="Buscar por medico solicitante..."
              class="h-11 w-full pl-10 pr-10 rounded-lg border border-gray-300 bg-transparent py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
              @input="filterMedicos"
              @focus="showMedicosList = true"
              @keydown.down.prevent="highlightNextMedico"
              @keydown.up.prevent="highlightPrevMedico"
              @keydown.enter.prevent="selectHighlightedMedico"
              autocomplete="off"
            />
            <button type="button" class="absolute inset-y-0 right-0 flex items-center pr-3" @mousedown.prevent="toggleMedicosList">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            <div
              v-if="showMedicosList && filteredMedicos.length > 0"
              class="absolute z-50 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto"
            >
              <div
                v-for="(medico, idx) in filteredMedicos"
                :key="medico"
                @mousedown.prevent="selectMedico(medico)"
                class="px-4 py-2 hover:bg-gray-100 cursor-pointer text-sm"
                :class="{ 'bg-gray-100': highlightedMedicoIndex === idx }"
              >
                {{ medico }}
              </div>
            </div>
          </div>
        </div>

        <!-- Fila de filtros -->
        <div class="flex flex-col sm:flex-row sm:items-center gap-3">
          <div class="flex flex-col sm:flex-row gap-3 flex-1">
            <!-- Filtro por rango de fechas -->
            <div class="w-full sm:w-auto flex flex-col sm:flex-row gap-3 items-end">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1.5">
                  Desde
                </label>
                <input
                  type="date"
                  v-model="fechaDesde"
                  class="h-11 w-full sm:w-32 rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                  :max="fechaHasta || undefined"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1.5">
                  Hasta
                </label>
                <input
                  type="date"
                  v-model="fechaHasta"
                  class="h-11 w-full sm:w-32 rounded-lg border border-gray-300 bg-transparent px-4 py-2.5 text-sm text-gray-800 shadow-theme-xs focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                  :min="fechaDesde || undefined"
                />
              </div>
            </div>

            <!-- Filtro por entidad -->
            <div class="w-full sm:w-auto relative">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Entidad
              </label>
              <input
                ref="entidadInput"
                v-model="selectedAnalisis"
                type="text"
                placeholder="Buscar entidad..."
                class="h-11 w-full sm:w-48 pl-4 pr-10 rounded-lg border border-gray-300 bg-transparent py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                @input="filterEntidades"
                @focus="showEntidadesList = true"
                @keydown.down.prevent="highlightNextEntidad"
                @keydown.up.prevent="highlightPrevEntidad"
                @keydown.enter.prevent="selectHighlightedEntidad"
                autocomplete="off"
              />
              <button type="button" class="absolute inset-y-0 right-0 flex items-center pr-3 top-[2.2rem] sm:top-[2.2rem]" @mousedown.prevent="toggleEntidadesList">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div
                v-if="showEntidadesList && filteredEntidades.length > 0"
                class="absolute z-50 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto"
                style="min-width:12rem"
              >
                <div
                  v-for="(entidad, idx) in filteredEntidades"
                  :key="entidad"
                  @mousedown.prevent="selectEntidad(entidad)"
                  class="px-4 py-2 hover:bg-gray-100 cursor-pointer text-sm"
                  :class="{ 'bg-gray-100': highlightedEntidadIndex === idx }"
                >
                  {{ entidad }}
                </div>
              </div>
            </div>

            <!-- Filtro por estado -->
            <div class="w-full sm:w-auto relative">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                Estado
              </label>
              <input
                ref="estadoInput"
                v-model="selectedEstado"
                type="text"
                placeholder="Buscar estado..."
                class="h-11 w-full sm:w-40 pl-4 pr-10 rounded-lg border border-gray-300 bg-transparent py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                @input="filterEstados"
                @focus="showEstadosList = true"
                @keydown.down.prevent="highlightNextEstado"
                @keydown.up.prevent="highlightPrevEstado"
                @keydown.enter.prevent="selectHighlightedEstado"
                autocomplete="off"
              />
              <button type="button" class="absolute inset-y-0 right-0 flex items-center pr-3 top-[2.2rem] sm:top-[2.2rem]" @mousedown.prevent="toggleEstadosList">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div
                v-if="showEstadosList && filteredEstados.length > 0"
                class="absolute z-50 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto"
                style="min-width:10rem"
              >
                <div
                  v-for="(estado, idx) in filteredEstados"
                  :key="estado"
                  @mousedown.prevent="selectEstado(estado)"
                  class="px-4 py-2 hover:bg-gray-100 cursor-pointer text-sm"
                  :class="{ 'bg-gray-100': highlightedEstadoIndex === idx }"
                >
                  {{ estado }}
                </div>
              </div>
            </div>

            <!-- Filtro por CUPS -->
            <div class="w-16 sm:w-auto relative">
              <label class="block text-sm font-medium text-gray-700 mb-1.5">
                CUPS
              </label>
              <input
                ref="cupsInput"
                v-model="selectedCups"
                type="text"
                placeholder="Buscar CUPS..."
                class="h-11 w-full sm:w-40 pl-4 pr-10 rounded-lg border border-gray-300 bg-transparent py-2.5 text-sm text-gray-800 shadow-theme-xs placeholder:text-gray-400 focus:border-brand-300 focus:outline-hidden focus:ring-3 focus:ring-brand-500/10"
                @input="filterCups"
                @focus="showCupsList = true"
                @keydown.down.prevent="highlightNextCups"
                @keydown.up.prevent="highlightPrevCups"
                @keydown.enter.prevent="selectHighlightedCups"
                autocomplete="off"
              />
              <button type="button" class="absolute inset-y-0 right-0 flex items-center pr-3 top-[2.2rem] sm:top-[2.2rem]" @mousedown.prevent="toggleCupsList">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              <div
                v-if="showCupsList && filteredCups.length > 0"
                class="absolute z-50 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-lg max-h-60 overflow-y-auto"
                style="min-width:8rem"
              >
                <div
                  v-for="(cups, idx) in filteredCups"
                  :key="cups"
                  @mousedown.prevent="selectCups(cups)"
                  class="px-4 py-2 hover:bg-gray-100 cursor-pointer text-sm font-mono"
                  :class="{ 'bg-gray-100': highlightedCupsIndex === idx }"
                >
                  {{ cups }}
                </div>
              </div>
            </div>
          </div>

          <!-- Contador y botón limpiar -->
          <div class="flex items-center gap-3">
            <span class="text-sm text-gray-500">
              {{ filteredMuestras.length }} de {{ muestras.length }} muestras
            </span>
            <button
              v-if="hasActiveFilters"
              @click="clearAllFilters"
              class="inline-flex items-center px-3 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-3 focus:ring-gray-300/30 transition-colors"
            >
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
              Limpiar filtros
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tabla -->
    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white">
      <!-- Acciones en lote -->
      <div v-if="selectedMuestras.length > 0" class="p-4 border-b border-gray-200 bg-gray-50">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="text-sm text-gray-600">
              {{ selectedMuestras.length }} muestras seleccionadas
            </span>
            <select
              v-model="accionEnLote"
              class="h-9 rounded-lg border border-gray-300 bg-white px-3 py-1.5 text-sm text-gray-700 focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-500/10"
            >
              <option value="">Acciones en lote</option>
              <option value="urgente">Marcar como Urgente</option>
              <option value="en-proceso">Marcar como En Proceso</option>
              <option value="por validar">Marcar como Por Validar</option>
              <option value="completado">Marcar como Completado</option>
            </select>
            <button
              v-if="accionEnLote"
              @click="aplicarAccionEnLote"
              class="inline-flex items-center px-3 py-1.5 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20 transition-colors"
            >
              Aplicar
            </button>
          </div>
          <button
            @click="selectedMuestras = []"
            class="text-gray-500 hover:text-gray-700"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>

      <div class="max-w-full overflow-x-auto custom-scrollbar">
        <table class="min-w-full">
          <thead>
            <tr class="border-b border-gray-200">
              <th class="px-5 py-3 text-left w-1/24 sm:px-6">
                <div class="flex items-center">
                  <input
                    type="checkbox"
                    :checked="isAllSelected"
                    @change="toggleSelectAll"
                    class="h-4 w-4 rounded border-gray-300 text-brand-500 focus:ring-brand-500"
                  />
                </div>
              </th>
              <th 
                v-for="column in columns" 
                :key="column.key"
                class="px-5 py-3 text-left sm:px-6"
                :class="column.class"
              >
                <button
                  class="flex items-center gap-1 font-medium text-gray-500 text-theme-xs hover:text-gray-700"
                  @click="sortBy(column.key)"
                >
                  {{ column.label }}
                  <svg
                    v-if="sortKey === column.key"
                    class="w-4 h-4"
                    :class="{ 'transform rotate-180': sortOrder === 'desc' }"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                  </svg>
                </button>
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="(muestra, index) in paginatedMuestras"
              :key="index"
              class="border-t border-gray-100 hover:bg-gray-50 transition-colors"
            >
              <td class="px-5 py-4 sm:px-6">
                <input
                  type="checkbox"
                  :checked="selectedMuestras.includes(muestra.id)"
                  @change="toggleSelect(muestra.id)"
                  class="h-4 w-4 rounded border-gray-300 text-brand-500 focus:ring-brand-500"
                />
              </td>
              <td class="px-5 py-4 sm:px-6">
                <div class="flex items-center gap-3">
                  <div class="h-[32px] w-[32px] flex items-center justify-center bg-blue-50 rounded-md">
                    <svg
                      class="w-6 h-6 text-brand-700"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      viewBox="0 0 24 24"
                    >
                      <rect x="6" y="4" width="12" height="2" rx="1" stroke="currentColor" />
                      <rect x="6" y="6" width="12" height="14" rx="3" stroke="currentColor" />
                      <rect x="9" y="12" width="6" height="4" rx="0" stroke="currentColor" />
                    </svg>
                  </div>
                  <div>
                    <span class="block font-medium text-gray-800 text-theme-sm">
                      <span v-html="highlightText(muestra.id, searchQuery)"></span>
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
                  <p class="text-gray-500 text-theme-xs">
                    <span v-html="highlightText(muestra.dni, searchQuery)"></span>
                  </p>
                </div>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <p class="text-gray-800 text-theme-sm">{{ muestra.analisis }}</p>
                <p class="text-gray-500 text-theme-xs">{{ muestra.medico }}</p>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <div class="grid grid-cols-3 gap-1 max-h-12 overflow-hidden">
                  <span 
                    v-for="(cup, index) in muestra.cups" 
                    :key="index"
                    class="flex items-center justify-center bg-gray-100 text-gray-700 font-mono text-[10px] px-1.5 py-0.5 rounded border text-nowrap min-h-[20px]"
                  >
                    {{ cup }}
                  </span>
                </div>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <span
                  :class="[
                    'rounded-full px-2 py-0.5 text-theme-xs font-medium',
                    {
                      'bg-error-50 text-error-700': muestra.estado === 'Urgente',
                      'bg-warning-50 text-warning-700': muestra.estado === 'En Proceso',
                      'bg-info-50 text-info-700': muestra.estado === 'Por Validar',
                      'bg-success-50 text-success-700': muestra.estado === 'Completado',
                    },
                  ]"
                >
                  {{ muestra.estado }}
                </span>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <p class="text-gray-800 text-theme-sm">{{ formatDate(muestra.fechaRecepcion) }}</p>
                <p class="text-gray-500 text-theme-xs">{{ muestra.horaRecepcion }}</p>
              </td>
              <td class="px-5 py-4 sm:px-6">
                <div class="flex gap-2">
                  <button 
                    @click="mostrarDetallesMuestra(muestra)"
                    class="text-brand-500 hover:text-brand-700 p-1 rounded-md hover:bg-brand-50 transition-colors"
                    title="Ver detalles"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                    </svg>
                  </button>
                  <button 
                    @click="editarMuestra(muestra)"
                    class="text-brand-500 hover:text-brand-700 p-1 rounded-md hover:bg-brand-50 transition-colors"
                    title="Editar muestra"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </button>
                  <button 
                    @click="validarMuestra(muestra)"
                    class="text-green-600 hover:text-green-800 p-1 rounded-md hover:bg-green-50 transition-colors"
                    :disabled="muestra.estado === 'Validado'"
                    :class="{ 'opacity-50 cursor-not-allowed': muestra.estado === 'Validado' }"
                    title="Validar muestra"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </button>
                  <!-- Botón para cambiar de 'Por Validar' a 'Completado' -->
                  <button 
                    v-if="muestra.estado === 'Por Validar'"
                    @click="marcarComoCompletado(muestra)"
                    class="text-green-600 hover:text-green-800 p-1 rounded-md hover:bg-green-50 transition-colors"
                    title="Marcar como Completado"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
            <!-- Mensaje cuando no hay resultados -->
            <tr v-if="filteredMuestras.length === 0">
              <td colspan="8" class="px-5 py-8 text-center">
                <div class="flex flex-col items-center">
                  <svg class="w-12 h-12 text-gray-400 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>
                  </svg>
                  <p class="text-gray-500 text-theme-sm font-medium">
                    {{ hasActiveFilters ? 'No se encontraron muestras con los filtros aplicados' : 'No hay muestras disponibles' }}
                  </p>
                  <p v-if="hasActiveFilters" class="text-gray-400 text-theme-xs mt-1">
                    Intente con otros criterios de búsqueda
                  </p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal de Detalles -->
      <transition
        enter-active-class="transition ease-out duration-300"
        enter-from-class="opacity-0 transform scale-95"
        enter-to-class="opacity-100 transform scale-100"
        leave-active-class="transition ease-in duration-200"
        leave-from-class="opacity-100 transform scale-100"
        leave-to-class="opacity-0 transform scale-95"
      >
        <div
          v-if="muestraSeleccionada"
          class="fixed inset-0 z-50 flex items-center justify-center p-4"
        >
          <!-- Overlay oscuro -->
          <div 
            class="absolute inset-0 bg-black bg-opacity-50"
            @click="muestraSeleccionada = null"
          ></div>
          
          <!-- Modal -->
          <div
            class="relative bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto"
          >
            <!-- Encabezado -->
            <div class="sticky top-0 z-10 bg-white border-b border-gray-200 px-6 py-4 rounded-t-2xl">
              <div class="flex items-center justify-between">
                <h3 class="text-xl font-semibold text-gray-900">
                  Detalles de la Muestra
                </h3>
                <button
                  @click="muestraSeleccionada = null"
                  class="text-gray-400 hover:text-gray-600 transition-colors"
                >
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                  </svg>
                </button>
              </div>
            </div>

            <!-- Contenido -->
            <div class="p-6 space-y-6">
              <!-- ID y Estado -->
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="text-lg font-medium text-gray-900">{{ muestraSeleccionada.id }}</h4>
                  <p class="text-sm text-gray-500">{{ muestraSeleccionada.tipoMuestra }}</p>
                </div>
                <span
                  :class="[
                    'rounded-full px-3 py-1 text-sm font-medium',
                    {
                      'bg-success-50 text-success-700': muestraSeleccionada.estado === 'Completado',
                      'bg-warning-50 text-warning-700': muestraSeleccionada.estado === 'En Proceso',
                      'bg-error-50 text-error-700': muestraSeleccionada.estado === 'Urgente',
                      'bg-info-50 text-info-700': muestraSeleccionada.estado === 'Por Validar',
                    },
                  ]"
                >
                  {{ muestraSeleccionada.estado }}
                </span>
              </div>

              <!-- Información del Paciente -->
              <div class="bg-gray-50 rounded-xl p-4">
                <h5 class="text-sm font-medium text-gray-700 mb-3">Información del Paciente</h5>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <p class="text-sm text-gray-500">Nombre</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.paciente }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">DNI/Cédula</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.dni }}</p>
                  </div>
                </div>
              </div>

              <!-- Información del Análisis -->
              <div class="bg-gray-50 rounded-xl p-4">
                <h5 class="text-sm font-medium text-gray-700 mb-3">Información de la Entidad</h5>
                <div class="grid grid-cols-3 gap-4">
                  <div>
                    <p class="text-sm text-gray-500">Entidad</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.analisis }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">Médico Solicitante</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.medico }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">CUPS</p>
                    <div class="flex flex-wrap gap-1 mt-1">
                      <span 
                        v-for="(cup, index) in muestraSeleccionada.cups" 
                        :key="index"
                        class="inline-block bg-white text-gray-800 font-mono text-[10px] px-1.5 py-0.5 rounded border border-gray-200 text-nowrap"
                      >
                        {{ cup }}
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Información de Recepción -->
              <div class="bg-gray-50 rounded-xl p-4">
                <h5 class="text-sm font-medium text-gray-700 mb-3">Información de Recepción</h5>
                <div class="grid grid-cols-2 gap-4">
                  <div>
                    <p class="text-sm text-gray-500">Fecha de Recepción</p>
                    <p class="text-base font-medium text-gray-900">{{ formatDate(muestraSeleccionada.fechaRecepcion) }}</p>
                  </div>
                  <div>
                    <p class="text-sm text-gray-500">Hora de Recepción</p>
                    <p class="text-base font-medium text-gray-900">{{ muestraSeleccionada.horaRecepcion }}</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Pie del Modal -->
            <div class="sticky bottom-0 bg-white border-t border-gray-200 px-6 py-4 rounded-b-2xl">
              <div class="flex justify-end gap-3">
                <button
                  @click="muestraSeleccionada = null"
                  class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-brand-500/10"
                >
                  Cerrar
                </button>
                <button
                  @click="editarMuestra(muestraSeleccionada)"
                  class="inline-flex items-center px-4 py-2 border border-transparent rounded-lg text-sm font-medium text-white bg-brand-500 hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500/20"
                >
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                  Editar Muestra
                </button>
              </div>
            </div>
          </div>
        </div>
      </transition>

      <!-- Paginación -->
      <div class="px-5 py-4 border-t border-gray-200">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500">Mostrando</span>
            <select
              v-model="itemsPerPage"
              class="h-9 rounded-lg border border-gray-300 bg-white px-3 py-1.5 text-sm text-gray-700 focus:border-brand-300 focus:outline-none focus:ring-2 focus:ring-brand-500/10"
            >
              <option :value="5">5</option>
              <option :value="10">10</option>
              <option :value="20">20</option>
              <option :value="50">50</option>
            </select>
            <span class="text-sm text-gray-500">de {{ filteredMuestras.length }} resultados</span>
          </div>
          <div class="flex items-center gap-2">
            <button
              @click="currentPage--"
              :disabled="currentPage === 1"
              class="inline-flex items-center px-3 py-1.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-brand-500/10 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Anterior
            </button>
            <span class="text-sm text-gray-500">
              Página {{ currentPage }} de {{ totalPages }}
            </span>
            <button
              @click="currentPage++"
              :disabled="currentPage === totalPages"
              class="inline-flex items-center px-3 py-1.5 border border-gray-300 rounded-lg text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-brand-500/10 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

// Estados para búsqueda y filtros
const searchQuery = ref('')
const searchMedico = ref('')
const fechaDesde = ref('')
const fechaHasta = ref('')
const selectedAnalisis = ref('')
const selectedEstado = ref('')
const selectedCups = ref('')

// Estados para ordenamiento
const sortKey = ref('id')
const sortOrder = ref('asc')

// Estados para paginación
const currentPage = ref(1)
const itemsPerPage = ref(10)

// Estados para selección en lote
const selectedMuestras = ref<string[]>([])
const accionEnLote = ref('')

// Estado para el modal de detalles
const muestraSeleccionada = ref<Muestra | null>(null)

// Definición de columnas
const columns = [
  { key: 'id', label: 'ID Muestra', class: 'w-2/10  ' },
  { key: 'paciente', label: 'Paciente', class: 'w-2/12' },
  { key: 'analisis', label: 'Entidad', class: 'w-2/12' },
  { key: 'cups', label: 'CUPS', class: 'w-2/12' },
  { key: 'estado', label: 'Estado', class: 'w-1/12' },
  { key: 'fechaRecepcion', label: 'Fecha Recepción', class: 'w-2/12' },
  { key: 'acciones', label: 'Acciones', class: 'w-1/12' }
]

// Estados disponibles
const estados = [
  'Urgente',
  'En Proceso',
  'Por Validar',
  'Completado'
]

// CUPS únicos disponibles (obtenidos de todas las muestras)
const cupsList = computed(() => {
  const allCups = new Set<string>()
  muestras.value.forEach(muestra => {
    muestra.cups.forEach(cup => allCups.add(cup))
  })
  return Array.from(allCups).sort()
})

// Tipos de análisis disponibles
const tiposAnalisis = [
  'ESSALUD',
  'MINSA',
  'PRIVADO',
  'OTRO'
]

// Tipado para muestra
interface Muestra {
  id: string;
  tipoMuestra: string;
  paciente: string;
  dni: string;
  analisis: string;
  medico: string;
  estado: string;
  fechaRecepcion: string;
  horaRecepcion: string;
  cups: string[];
}

const muestras = ref<Muestra[]>([
  {
    id: 'M-2024-001',
    tipoMuestra: 'Sangre',
    paciente: 'Juan Pérez',
    dni: '12345678',
    analisis: 'ESSALUD',
    medico: 'Dr. García',
    estado: 'Completado',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '09:30',
    cups: ['90001', '90101', '90201']
  },
  {
    id: 'M-2024-002',
    tipoMuestra: 'Orina',
    paciente: 'María López',
    dni: '87654321',
    analisis: 'MINSA',
    medico: 'Dra. Martínez',
    estado: 'En Proceso',
    fechaRecepcion: '2024-03-20',
    horaRecepcion: '10:15',
    cups: ['90002', '90102']
  },
  {
    id: 'M-2024-003',
    tipoMuestra: 'Heces',
    paciente: 'Carlos Ruiz',
    dni: '23456789',
    analisis: 'PRIVADO',
    medico: 'Dr. Sánchez',
    estado: 'Urgente',
    fechaRecepcion: '2024-02-15',
    horaRecepcion: '11:00',
    cups: ['90003', '90103', '90203', '90303']
  },
  {
    id: 'M-2024-004',
    tipoMuestra: 'Sangre',
    paciente: 'Ana Torres',
    dni: '34567890',
    analisis: 'ESSALUD',
    medico: 'Dra. Rodríguez',
    estado: 'Completado',
    fechaRecepcion: '2024-01-10',
    horaRecepcion: '11:45',
    cups: ['90004']
  },
  {
    id: 'M-2023-005',
    tipoMuestra: 'Sangre',
    paciente: 'Roberto Díaz',
    dni: '45678901',
    analisis: 'OTRO',
    medico: 'Dr. Fernández',
    estado: 'En Proceso',
    fechaRecepcion: '2023-12-05',
    horaRecepcion: '12:30',
    cups: ['90005', '90105', '90205']
  },
  {
    id: 'M-2023-006',
    tipoMuestra: 'Orina',
    paciente: 'Lucía Ramírez',
    dni: '56789012',
    analisis: 'ESSALUD',
    medico: 'Dra. Morales',
    estado: 'Urgente',
    fechaRecepcion: '2023-11-22',
    horaRecepcion: '08:45',
    cups: ['90006', '90106']
  },
  {
    id: 'M-2023-007',
    tipoMuestra: 'Heces',
    paciente: 'Miguel Castro',
    dni: '67890123',
    analisis: 'MINSA',
    medico: 'Dr. Herrera',
    estado: 'Completado',
    fechaRecepcion: '2023-10-18',
    horaRecepcion: '10:10',
    cups: ['90007', '90107', '90207']
  },
  {
    id: 'M-2023-008',
    tipoMuestra: 'Sangre',
    paciente: 'Patricia Gómez',
    dni: '78901234',
    analisis: 'PRIVADO',
    medico: 'Dra. Vargas',
    estado: 'Completado',
    fechaRecepcion: '2023-09-30',
    horaRecepcion: '09:00',
    cups: ['90008']
  },
  {
    id: 'M-2023-009',
    tipoMuestra: 'Orina',
    paciente: 'Jorge Salazar',
    dni: '89012345',
    analisis: 'ESSALUD',
    medico: 'Dr. Paredes',
    estado: 'Urgente',
    fechaRecepcion: '2023-08-15',
    horaRecepcion: '11:20',
    cups: ['90009', '90109']
  },
  {
    id: 'M-2023-010',
    tipoMuestra: 'Heces',
    paciente: 'Carmen Ríos',
    dni: '90123456',
    analisis: 'MINSA',
    medico: 'Dra. Mendoza',
    estado: 'En Proceso',
    fechaRecepcion: '2023-07-12',
    horaRecepcion: '13:05',
    cups: ['90010', '90110', '90210']
  },
  {
    id: 'M-2023-011',
    tipoMuestra: 'Sangre',
    paciente: 'Luis Torres',
    dni: '11223344',
    analisis: 'OTRO',
    medico: 'Dr. Castillo',
    estado: 'Completado',
    fechaRecepcion: '2023-06-25',
    horaRecepcion: '10:30',
    cups: ['90011', '90111']
  },
  {
    id: 'M-2023-012',
    tipoMuestra: 'Orina',
    paciente: 'Elena Bravo',
    dni: '22334455',
    analisis: 'ESSALUD',
    medico: 'Dra. Peña',
    estado: 'Completado',
    fechaRecepcion: '2023-05-19',
    horaRecepcion: '09:50',
    cups: ['90012']
  },
  {
    id: 'M-2023-013',
    tipoMuestra: 'Heces',
    paciente: 'Ricardo Medina',
    dni: '33445566',
    analisis: 'PRIVADO',
    medico: 'Dr. Aguirre',
    estado: 'Urgente',
    fechaRecepcion: '2023-04-10',
    horaRecepcion: '12:15',
    cups: ['90013', '90113']
  },
  {
    id: 'M-2023-014',
    tipoMuestra: 'Sangre',
    paciente: 'Gabriela Soto',
    dni: '44556677',
    analisis: 'MINSA',
    medico: 'Dra. Cárdenas',
    estado: 'En Proceso',
    fechaRecepcion: '2023-03-03',
    horaRecepcion: '08:20',
    cups: ['90014', '90114', '90214']
  },
  {
    id: 'M-2023-015',
    tipoMuestra: 'Orina',
    paciente: 'Fernando León',
    dni: '55667788',
    analisis: 'ESSALUD',
    medico: 'Dr. Rojas',
    estado: 'Completado',
    fechaRecepcion: '2023-02-14',
    horaRecepcion: '10:40',
    cups: ['90015']
  }
])

// Computed property para filtrar y ordenar las muestras
const filteredMuestras = computed(() => {
  let filtered = muestras.value
  // Filtrar por búsqueda de texto
  if (searchQuery.value) {
    const normalize = (str: string) => str.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLowerCase().trim();
    const query = normalize(searchQuery.value)
    filtered = filtered.filter(muestra => {
      return (
        normalize(muestra.id).includes(query) ||
        normalize(muestra.dni).includes(query) ||
        normalize(muestra.paciente).includes(query)
      )
    })
  }
  // Filtrar por búsqueda de médico
  if (searchMedico.value) {
    const medicoQuery = searchMedico.value.toLowerCase().trim()
    filtered = filtered.filter(muestra => muestra.medico.toLowerCase().includes(medicoQuery))
  }
  // Filtrar por rango de fechas
  if (fechaDesde.value) {
    filtered = filtered.filter(muestra => muestra.fechaRecepcion >= fechaDesde.value)
  }
  if (fechaHasta.value) {
    filtered = filtered.filter(muestra => muestra.fechaRecepcion <= fechaHasta.value)
  }
  // Filtrar por entidad
  if (selectedAnalisis.value) {
    filtered = filtered.filter(muestra => muestra.analisis === selectedAnalisis.value)
  }
  // Filtrar por estado
  if (selectedEstado.value) {
    filtered = filtered.filter(muestra => muestra.estado === selectedEstado.value)
  }
  // Filtrar por CUPS
  if (selectedCups.value) {
    filtered = filtered.filter(muestra => muestra.cups.includes(selectedCups.value))
  }
  // Ordenar
  filtered.sort((a, b) => {
    let aValue: string | Date = a[sortKey.value as keyof Muestra] as string
    let bValue: string | Date = b[sortKey.value as keyof Muestra] as string
    if (sortKey.value === 'fechaRecepcion') {
      aValue = new Date(a.fechaRecepcion)
      bValue = new Date(b.fechaRecepcion)
    }
    if (aValue < bValue) return sortOrder.value === 'asc' ? -1 : 1
    if (aValue > bValue) return sortOrder.value === 'asc' ? 1 : -1
    return 0
  })
  return filtered
})

// Computed property para verificar si hay filtros activos
const hasActiveFilters = computed(() => {
  return searchQuery.value || searchMedico.value || fechaDesde.value || fechaHasta.value || selectedAnalisis.value || selectedEstado.value || selectedCups.value
})

// Computed properties para paginación
const totalPages = computed(() => {
  return Math.ceil(filteredMuestras.value.length / itemsPerPage.value)
})

const paginatedMuestras = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  const end = start + itemsPerPage.value
  return filteredMuestras.value.slice(start, end)
})

// Computed property para selección en lote
const isAllSelected = computed(() => {
  return paginatedMuestras.value.length > 0 && 
         paginatedMuestras.value.every(m => selectedMuestras.value.includes(m.id))
})

// Funciones para selección en lote
const toggleSelectAll = () => {
  if (isAllSelected.value) {
    selectedMuestras.value = selectedMuestras.value.filter(
      id => !paginatedMuestras.value.some(m => m.id === id)
    )
  } else {
    const newSelected = paginatedMuestras.value.map(m => m.id)
    selectedMuestras.value = [...new Set([...selectedMuestras.value, ...newSelected])]
  }
}

const toggleSelect = (id: string) => {
  const index = selectedMuestras.value.indexOf(id)
  if (index === -1) {
    selectedMuestras.value.push(id)
  } else {
    selectedMuestras.value.splice(index, 1)
  }
}

// Función para aplicar acción en lote
const aplicarAccionEnLote = () => {
  if (!accionEnLote.value) return
  muestras.value = muestras.value.map(muestra => {
    if (selectedMuestras.value.includes(muestra.id)) {
      let nuevoEstado = accionEnLote.value
      if (accionEnLote.value === 'por validar') nuevoEstado = 'Por Validar'
      if (accionEnLote.value === 'en-proceso') nuevoEstado = 'En Proceso'
      if (accionEnLote.value === 'urgente') nuevoEstado = 'Urgente'
      if (accionEnLote.value === 'completado') nuevoEstado = 'Completado'
      return { ...muestra, estado: nuevoEstado }
    }
    return muestra
  })
  selectedMuestras.value = []
  accionEnLote.value = ''
}

// Función para ordenar
const sortBy = (key: string) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

// Watch para resetear la página cuando cambian los filtros
watch([searchQuery, searchMedico, fechaDesde, fechaHasta, selectedAnalisis, selectedEstado, selectedCups], () => {
  currentPage.value = 1
})

// Watch para resetear la página cuando cambia el número de items por página
watch(itemsPerPage, () => {
  currentPage.value = 1
})

// Función para limpiar todos los filtros
const clearAllFilters = () => {
  searchQuery.value = ''
  searchMedico.value = ''
  fechaDesde.value = ''
  fechaHasta.value = ''
  selectedAnalisis.value = ''
  selectedEstado.value = ''
  selectedCups.value = ''
  currentPage.value = 1
}

// Función para resaltar texto coincidente
const highlightText = (text: string, query: string) => {
  if (!query) return text
  const regex = new RegExp(`(${query})`, 'gi')
  return text.replace(regex, '<mark class="bg-yellow-200 px-1 rounded">$1</mark>')
}

// Función para formatear fecha
const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
  })
}

// Función para mostrar los detalles de la muestra
const mostrarDetallesMuestra = (muestra: Muestra) => {
  muestraSeleccionada.value = muestra
}

const router = useRouter()

// Función para editar la muestra
const editarMuestra = (muestra: Muestra) => {
  router.push(`/editar-muestra/${muestra.id}`)
  muestraSeleccionada.value = null
}

// Función para validar la muestra
const validarMuestra = (muestra: Muestra) => {
  if (muestra.estado === 'Validado') {
    return // No hacer nada si ya está validado
  }
  
  // Cambiar el estado de la muestra a "Validado"
  const index = muestras.value.findIndex(m => m.id === muestra.id)
  if (index !== -1) {
    muestras.value[index].estado = 'Validado'
  }
  
  // También actualizar la muestra seleccionada si coincide
  if (muestraSeleccionada.value && muestraSeleccionada.value.id === muestra.id) {
    muestraSeleccionada.value.estado = 'Validado'
  }
  
  // Aquí podrías agregar una llamada a la API para actualizar el estado en el backend
  console.log(`Muestra ${muestra.id} validada correctamente`)
}

// Nueva función para marcar como completado
const marcarComoCompletado = (muestra: Muestra) => {
  if (muestra.estado === 'Por Validar') {
    const index = muestras.value.findIndex(m => m.id === muestra.id)
    if (index !== -1) {
      muestras.value[index].estado = 'Completado'
    }
    if (muestraSeleccionada.value && muestraSeleccionada.value.id === muestra.id) {
      muestraSeleccionada.value.estado = 'Completado'
    }
  }
}

// Computed property para obtener médicos únicos disponibles
const availableMedicos = computed(() => {
  const medicos = muestras.value.map(m => m.medico)
  return [...new Set(medicos)]
})

// --- Combobox de médicos (como en AsignarPatologoMuestra.vue) ---
const medicoInput = ref<HTMLInputElement | null>(null)
const showMedicosList = ref(false)
const filteredMedicos = ref<string[]>([])
const highlightedMedicoIndex = ref(-1)

const filterMedicos = () => {
  const search = searchMedico.value.toLowerCase()
  filteredMedicos.value = availableMedicos.value.filter(medico =>
    medico.toLowerCase().includes(search)
  )
  highlightedMedicoIndex.value = -1
}

const selectMedico = (medico: string) => {
  searchMedico.value = medico
  showMedicosList.value = false
  filterMedicos()
}

const toggleMedicosList = () => {
  if (!showMedicosList.value) {
    filterMedicos()
    showMedicosList.value = true
    medicoInput.value?.focus()
  } else {
    showMedicosList.value = false
  }
}

const highlightNextMedico = () => {
  if (!showMedicosList.value) {
    showMedicosList.value = true
    filterMedicos()
    return
  }
  if (filteredMedicos.value.length === 0) return
  highlightedMedicoIndex.value = (highlightedMedicoIndex.value + 1) % filteredMedicos.value.length
}

const highlightPrevMedico = () => {
  if (!showMedicosList.value) {
    showMedicosList.value = true
    filterMedicos()
    return
  }
  if (filteredMedicos.value.length === 0) return
  highlightedMedicoIndex.value = (highlightedMedicoIndex.value - 1 + filteredMedicos.value.length) % filteredMedicos.value.length
}

const selectHighlightedMedico = () => {
  if (showMedicosList.value && highlightedMedicoIndex.value >= 0) {
    selectMedico(filteredMedicos.value[highlightedMedicoIndex.value])
  }
}

// Cerrar lista al hacer clic fuera
const onClickOutsideMedico = (e: MouseEvent) => {
  const target = e.target as HTMLElement
  if (!medicoInput.value?.parentElement?.contains(target)) {
    showMedicosList.value = false
  }
}
onMounted(() => {
  document.addEventListener('mousedown', onClickOutsideMedico)
})
onBeforeUnmount(() => {
  document.removeEventListener('mousedown', onClickOutsideMedico)
})

// Inicializar lista filtrada
onMounted(() => {
  filteredMedicos.value = availableMedicos.value
})
watch(searchMedico, filterMedicos)

// --- Combobox de entidades (como el de médicos) ---
const entidadInput = ref<HTMLInputElement | null>(null)
const showEntidadesList = ref(false)
const filteredEntidades = ref<string[]>([])
const highlightedEntidadIndex = ref(-1)

const filterEntidades = () => {
  const search = selectedAnalisis.value.toLowerCase()
  filteredEntidades.value = tiposAnalisis.filter(entidad =>
    entidad.toLowerCase().includes(search)
  )
  highlightedEntidadIndex.value = -1
}

const selectEntidad = (entidad: string) => {
  selectedAnalisis.value = entidad
  showEntidadesList.value = false
  filterEntidades()
}

const toggleEntidadesList = () => {
  if (!showEntidadesList.value) {
    filterEntidades()
    showEntidadesList.value = true
    entidadInput.value?.focus()
  } else {
    showEntidadesList.value = false
  }
}

const highlightNextEntidad = () => {
  if (!showEntidadesList.value) {
    showEntidadesList.value = true
    filterEntidades()
    return
  }
  if (filteredEntidades.value.length === 0) return
  highlightedEntidadIndex.value = (highlightedEntidadIndex.value + 1) % filteredEntidades.value.length
}

const highlightPrevEntidad = () => {
  if (!showEntidadesList.value) {
    showEntidadesList.value = true
    filterEntidades()
    return
  }
  if (filteredEntidades.value.length === 0) return
  highlightedEntidadIndex.value = (highlightedEntidadIndex.value - 1 + filteredEntidades.value.length) % filteredEntidades.value.length
}

const selectHighlightedEntidad = () => {
  if (showEntidadesList.value && highlightedEntidadIndex.value >= 0) {
    selectEntidad(filteredEntidades.value[highlightedEntidadIndex.value])
  }
}

// Cerrar lista al hacer clic fuera
const onClickOutsideEntidad = (e: MouseEvent) => {
  const target = e.target as HTMLElement
  if (!entidadInput.value?.parentElement?.contains(target)) {
    showEntidadesList.value = false
  }
}
onMounted(() => {
  document.addEventListener('mousedown', onClickOutsideEntidad)
})
onBeforeUnmount(() => {
  document.removeEventListener('mousedown', onClickOutsideEntidad)
})

// Inicializar lista filtrada
onMounted(() => {
  filteredEntidades.value = tiposAnalisis
})
watch(selectedAnalisis, filterEntidades)

// --- Combobox de estados (como el de médicos y entidad) ---
const estadoInput = ref<HTMLInputElement | null>(null)
const showEstadosList = ref(false)
const filteredEstados = ref<string[]>([])
const highlightedEstadoIndex = ref(-1)

const filterEstados = () => {
  const search = selectedEstado.value.toLowerCase()
  filteredEstados.value = estados.filter(estado =>
    estado.toLowerCase().includes(search)
  )
  highlightedEstadoIndex.value = -1
}

const selectEstado = (estado: string) => {
  selectedEstado.value = estado
  showEstadosList.value = false
  filterEstados()
}

const toggleEstadosList = () => {
  if (!showEstadosList.value) {
    filterEstados()
    showEstadosList.value = true
    estadoInput.value?.focus()
  } else {
    showEstadosList.value = false
  }
}

const highlightNextEstado = () => {
  if (!showEstadosList.value) {
    showEstadosList.value = true
    filterEstados()
    return
  }
  if (filteredEstados.value.length === 0) return
  highlightedEstadoIndex.value = (highlightedEstadoIndex.value + 1) % filteredEstados.value.length
}

const highlightPrevEstado = () => {
  if (!showEstadosList.value) {
    showEstadosList.value = true
    filterEstados()
    return
  }
  if (filteredEstados.value.length === 0) return
  highlightedEstadoIndex.value = (highlightedEstadoIndex.value - 1 + filteredEstados.value.length) % filteredEstados.value.length
}

const selectHighlightedEstado = () => {
  if (showEstadosList.value && highlightedEstadoIndex.value >= 0) {
    selectEstado(filteredEstados.value[highlightedEstadoIndex.value])
  }
}

// Cerrar lista al hacer clic fuera
const onClickOutsideEstado = (e: MouseEvent) => {
  const target = e.target as HTMLElement
  if (!estadoInput.value?.parentElement?.contains(target)) {
    showEstadosList.value = false
  }
}
onMounted(() => {
  document.addEventListener('mousedown', onClickOutsideEstado)
})
onBeforeUnmount(() => {
  document.removeEventListener('mousedown', onClickOutsideEstado)
})

// Inicializar lista filtrada
onMounted(() => {
  filteredEstados.value = estados
})
watch(selectedEstado, filterEstados)

// --- Combobox de CUPS ---
const cupsInput = ref<HTMLInputElement | null>(null)
const showCupsList = ref(false)
const filteredCups = ref<string[]>([])
const highlightedCupsIndex = ref(-1)

const filterCups = () => {
  const search = selectedCups.value.toLowerCase()
  filteredCups.value = cupsList.value.filter(cup =>
    cup.toLowerCase().includes(search)
  )
  highlightedCupsIndex.value = -1
}

const selectCups = (cups: string) => {
  selectedCups.value = cups
  showCupsList.value = false
  filterCups()
}

const toggleCupsList = () => {
  if (!showCupsList.value) {
    filterCups()
    showCupsList.value = true
    cupsInput.value?.focus()
  } else {
    showCupsList.value = false
  }
}

const highlightNextCups = () => {
  if (!showCupsList.value) {
    showCupsList.value = true
    filterCups()
    return
  }
  if (filteredCups.value.length === 0) return
  highlightedCupsIndex.value = (highlightedCupsIndex.value + 1) % filteredCups.value.length
}

const highlightPrevCups = () => {
  if (!showCupsList.value) {
    showCupsList.value = true
    filterCups()
    return
  }
  if (filteredCups.value.length === 0) return
  highlightedCupsIndex.value = (highlightedCupsIndex.value - 1 + filteredCups.value.length) % filteredCups.value.length
}

const selectHighlightedCups = () => {
  if (showCupsList.value && highlightedCupsIndex.value >= 0) {
    selectCups(filteredCups.value[highlightedCupsIndex.value])
  }
}

// Cerrar lista al hacer clic fuera
const onClickOutsideCups = (e: MouseEvent) => {
  const target = e.target as HTMLElement
  if (!cupsInput.value?.parentElement?.contains(target)) {
    showCupsList.value = false
  }
}

onMounted(() => {
  document.addEventListener('mousedown', onClickOutsideCups)
})

onBeforeUnmount(() => {
  document.removeEventListener('mousedown', onClickOutsideCups)
})

// Inicializar lista filtrada
onMounted(() => {
  filteredCups.value = cupsList.value
})
watch(selectedCups, filterCups)
</script>

<style scoped>
/* Estilos para el highlight */
:deep(mark) {
  background-color: rgb(254 240 138);
  padding: 0.125rem 0.25rem;
  border-radius: 0.25rem;
}

/* Custom scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  height: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

/* Estilos para el ordenamiento */
.sort-icon {
  transition: transform 0.2s ease-in-out;
}

.sort-icon.rotate {
  transform: rotate(180deg);
}

/* Estilos para el scroll del modal */
.modal-content {
  scrollbar-width: thin;
  scrollbar-color: #cbd5e1 #f1f5f9;
}

.modal-content::-webkit-scrollbar {
  width: 8px;
}

.modal-content::-webkit-scrollbar-track {
  background: #f1f5f9;
}

.modal-content::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}

.modal-content::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}
</style>