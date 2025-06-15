<template>
  <div class="flex gap-6">
    <!-- Selector de tipo de usuario -->
    <div class="w-64 p-5 border border-gray-200 rounded-2xl dark:border-gray-800">
      <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 mb-4">
        Tipo de Usuario
      </h4>
      <div class="space-y-2">
        <button
          v-for="type in tiposUsuario"
          :key="type.value"
          @click="tipoUsuarioSeleccionado = type.value"
          class="w-full text-left px-4 py-2 rounded-lg transition-colors"
          :class="tipoUsuarioSeleccionado === type.value ? 
            'bg-brand-500 text-white' : 
            'bg-gray-100 text-gray-700 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700'"
        >
          {{ type.label }}
        </button>
      </div>
    </div>

    <!-- Formulario de creación -->
    <div class="flex-1">
      <div class="p-5 mb-6 border border-gray-200 rounded-2xl dark:border-gray-800 lg:p-6">
        <div class="flex flex-col gap-6 lg:flex-row lg:items-start lg:justify-between">
          <div class="w-full">
            <!-- Sección de foto de perfil solo para administrativo y patólogo -->
            <div v-if="['administrativo', 'patologo'].includes(tipoUsuarioSeleccionado)" class="flex flex-col items-center w-full gap-6 mb-6 xl:flex-row">
              <div class="relative w-20 h-20 overflow-hidden border border-gray-200 rounded-full dark:border-gray-800 group">
                <img :src="previewImage || '/images/user/owner.jpg'" alt="user" class="w-full h-full object-cover" />
                <div class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer" @click="triggerFileInput">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <input
                  ref="fileInput"
                  type="file"
                  accept="image/*"
                  class="hidden"
                  @change="handleFileChange"
                />
              </div>
              <div>
                <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 lg:mb-3">
                  Crear Nuevo {{ tipoUsuarioSeleccionado ? tiposUsuario.find(t => t.value === tipoUsuarioSeleccionado)?.label : 'Usuario' }}
                </h4>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                  Haz clic en la imagen para cambiar la foto de perfil
                </p>
              </div>
            </div>

            <!-- Título sin foto para entidad y CUPS -->
            <div v-else class="mb-6">
              <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90">
                Crear Nuevo {{ tipoUsuarioSeleccionado ? tiposUsuario.find(t => t.value === tipoUsuarioSeleccionado)?.label : 'Usuario' }}
              </h4>
            </div>

            <!-- Formulario Administrativo -->
            <form v-if="tipoUsuarioSeleccionado === 'administrativo'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre Completo</label>
                <input v-model="nuevoUsuario.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Documento de Identidad</label>
                <input v-model="nuevoUsuario.documento" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 1234567890" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
                <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Celular</label>
                <input v-model="nuevoUsuario.phone" type="tel" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 3001234567" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Fecha de Ingreso</label>
                <input v-model="nuevoUsuario.startDate" type="date" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear Usuario Administrativo</button>
              </div>
            </form>

            <!-- Formulario Patólogo -->
            <form v-if="tipoUsuarioSeleccionado === 'patologo'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre Completo</label>
                <input v-model="nuevoUsuario.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Documento de Identidad</label>
                <input v-model="nuevoUsuario.documento" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 1234567890" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
                <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Celular</label>
                <input v-model="nuevoUsuario.phone" type="tel" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 3001234567" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Especialidad</label>
                <input v-model="nuevoUsuario.specialty" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: Anatomía Patológica" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Registro Médico</label>
                <input v-model="nuevoUsuario.medicalLicense" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" placeholder="Ej: 12345" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Estado</label>
                <div class="flex items-center space-x-4 mt-2">
                  <label class="inline-flex items-center">
                    <input
                      type="radio"
                      v-model="nuevoUsuario.isActive"
                      :value="true"
                      class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
                      required
                    />
                    <span class="ml-2 text-sm text-gray-700">Activo</span>
                  </label>
                  <label class="inline-flex items-center">
                    <input
                      type="radio"
                      v-model="nuevoUsuario.isActive"
                      :value="false"
                      class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
                      required
                    />
                    <span class="ml-2 text-sm text-gray-700">Inactivo</span>
                  </label>
                </div>
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Fecha de Ingreso</label>
                <input 
                  v-model="nuevoUsuario.startDate" 
                  type="date" 
                  required 
                  class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" 
                />
              </div>
              <div class="col-span-2">
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Firma del Patólogo</label>
                <Dropzone
                  :uploadUrl="'/api/upload-signature'"
                  @file-added="handleFirmaFile"
                  id="firmaDropzonePatologo" 
                />
                <div v-if="firmaPatologoFile" class="mt-2 text-sm text-gray-600">
                  Archivo seleccionado: {{ firmaPatologoFile.name }}
                </div>
              </div>
              <div class="col-span-2">
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Observaciones</label>
                <textarea
                  v-model="nuevoUsuario.observaciones"
                  placeholder="Observaciones adicionales sobre el patólogo"
                  rows="3"
                  class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs resize-none"
                ></textarea>
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear Patólogo</button>
              </div>
            </form>

            <!-- Formulario Entidad -->
            <form v-if="tipoUsuarioSeleccionado === 'entidad'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre de la Entidad</label>
                <input v-model="nuevoUsuario.entityName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">NIT</label>
                <input v-model="nuevoUsuario.nit" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Dirección</label>
                <input v-model="nuevoUsuario.address" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Teléfono</label>
                <input v-model="nuevoUsuario.phone" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
                <input v-model="nuevoUsuario.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Tipo de Entidad</label>
                <select v-model="nuevoUsuario.entityType" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                  <option value="">Seleccione un tipo</option>
                  <option value="hospital">Hospital</option>
                  <option value="clinica">Clínica</option>
                  <option value="laboratorio">Laboratorio</option>
                  <option value="ips">IPS</option>
                </select>
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear Entidad</button>
              </div>
            </form>

            <!-- Formulario CUPS -->
            <form v-if="tipoUsuarioSeleccionado === 'cups'" @submit.prevent="crearUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Código CUPS</label>
                <input v-model="nuevoUsuario.cupsCode" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre del Procedimiento</label>
                <input v-model="nuevoUsuario.cupsName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Categoría</label>
                <select v-model="nuevoUsuario.cupsCategory" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                  <option value="">Seleccione una categoría</option>
                  <option value="diagnostico">Diagnóstico</option>
                  <option value="terapeutico">Terapéutico</option>
                  <option value="quirurgico">Quirúrgico</option>
                  <option value="procedimiento">Procedimiento</option>
                </select>
              </div>
              <div>
                <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Descripción</label>
                <textarea v-model="nuevoUsuario.cupsDescription" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" rows="3"></textarea>
              </div>
              <div class="col-span-2 flex justify-end mt-4">
                <button type="submit" class="edit-button-modern">Crear CUPS</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div v-if="usuarioCreado" class="p-4 mt-4 rounded-lg bg-green-50 text-green-800 border border-green-200">
        {{ mensajeExito }}
      </div>
    </div>
  </div>

  <!-- Sección de Editar Usuario -->
  <div class="mt-8">
    <div class="p-5 border border-gray-200 rounded-2xl dark:border-gray-800">
      <h4 class="text-lg font-semibold text-gray-800 dark:text-white/90 mb-4">
        Editar Usuario
      </h4>
      
      <!-- Buscador -->
      <div class="mb-6">
        <div class="flex gap-4">
          <div class="flex-1">
            <input
              v-model="busquedaUsuario"
              type="text"
              placeholder="Buscar por nombre, documento o correo..."
              class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs"
              @keyup.enter="buscarUsuarios"
              :disabled="estaBuscando"
            />
          </div>
          <div class="w-48">
            <select
              v-model="tipoBusqueda"
              class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs"
              :disabled="estaBuscando"
            >
              <option value="todos">Todos los tipos</option>
              <option v-for="type in tiposUsuario" :key="type.value" :value="type.value">
                {{ type.label }}
              </option>
            </select>
          </div>
          <div class="flex gap-2">
            <button
              @click="buscarUsuarios"
              class="px-4 py-2.5 text-sm font-medium text-white bg-brand-500 rounded-lg hover:bg-brand-600 focus:outline-none focus:ring-2 focus:ring-brand-500 focus:ring-offset-2 dark:focus:ring-offset-gray-800 disabled:opacity-50 disabled:cursor-not-allowed"
              :disabled="estaBuscando || !busquedaUsuario.trim()"
            >
              <div class="flex items-center gap-2">
                <svg v-if="!estaBuscando" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                <svg v-else class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                {{ estaBuscando ? 'Buscando...' : 'Buscar' }}
              </div>
            </button>
            <button
              @click="limpiarBusqueda"
              class="px-4 py-2.5 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700 dark:focus:ring-offset-gray-800 disabled:opacity-50 disabled:cursor-not-allowed"
              :disabled="estaBuscando"
            >
              <div class="flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
                Limpiar
              </div>
            </button>
          </div>
        </div>
        
        <!-- Mensaje de error -->
        <div v-if="errorBusqueda" class="mt-2 text-sm text-red-600 dark:text-red-400">
          {{ errorBusqueda }}
        </div>
      </div>

      <!-- Resultados de búsqueda -->
      <div v-if="resultadosBusqueda.length > 0" class="space-y-4">
        <div
          v-for="usuario in resultadosBusqueda"
          :key="usuario.id"
          class="p-4 border border-gray-200 rounded-lg dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer transition-colors"
          @click="seleccionarUsuarioParaEditar(usuario)"
        >
          <div class="flex items-center gap-4">
            <div v-if="usuario.fotoPerfil" class="w-12 h-12 rounded-full overflow-hidden">
              <img :src="usuario.fotoPerfil" :alt="usuario.nombre" class="w-full h-full object-cover" />
            </div>
            <div class="flex-1">
              <h5 class="font-medium text-gray-800 dark:text-white/90">{{ usuario.nombre }}</h5>
              <p class="text-sm text-gray-500 dark:text-gray-400">{{ tiposUsuario.find(t => t.value === usuario.tipo)?.label }}</p>
            </div>
            <div class="text-sm text-gray-500 dark:text-gray-400">
              {{ usuario.documento || usuario.nit || usuario.cupsCode }}
            </div>
          </div>
        </div>
      </div>

      <!-- Mensaje cuando no hay resultados -->
      <div v-else-if="busquedaRealizada && !estaBuscando" class="text-center py-8 text-gray-500 dark:text-gray-400">
        No se encontraron resultados para tu búsqueda
      </div>

      <!-- Formulario de edición -->
      <div v-if="usuarioSeleccionado" class="mt-6">
        <h5 class="text-lg font-semibold text-gray-800 dark:text-white/90 mb-4">
          Editando: {{ usuarioSeleccionado.nombre }}
        </h5>
        
        <!-- Formulario de edición según el tipo de usuario -->
        <form @submit.prevent="actualizarUsuario" class="grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-7 2xl:gap-x-32">
          <!-- Los campos del formulario se cargarán dinámicamente según el tipo de usuario -->
          <template v-if="usuarioSeleccionado.tipo === 'administrativo'">
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre Completo</label>
              <input v-model="usuarioSeleccionado.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Documento de Identidad</label>
              <input v-model="usuarioSeleccionado.documento" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Correo Electrónico</label>
              <input v-model="usuarioSeleccionado.email" type="email" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Celular</label>
              <input v-model="usuarioSeleccionado.phone" type="tel" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
          </template>

          <template v-if="usuarioSeleccionado.tipo === 'patologo'">
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre Completo</label>
              <input v-model="usuarioSeleccionado.firstName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Especialidad</label>
              <input v-model="usuarioSeleccionado.specialty" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Registro Médico</label>
              <input v-model="usuarioSeleccionado.medicalLicense" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Estado</label>
              <div class="flex items-center space-x-4 mt-2">
                <label class="inline-flex items-center">
                  <input
                    type="radio"
                    v-model="usuarioSeleccionado.isActive"
                    :value="true"
                    class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
                  />
                  <span class="ml-2 text-sm text-gray-700">Activo</span>
                </label>
                <label class="inline-flex items-center">
                  <input
                    type="radio"
                    v-model="usuarioSeleccionado.isActive"
                    :value="false"
                    class="form-radio h-4 w-4 text-brand-600 border-gray-300 focus:ring-brand-500"
                  />
                  <span class="ml-2 text-sm text-gray-700">Inactivo</span>
                </label>
              </div>
            </div>
          </template>

          <template v-if="usuarioSeleccionado.tipo === 'entidad'">
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre de la Entidad</label>
              <input v-model="usuarioSeleccionado.entityName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">NIT</label>
              <input v-model="usuarioSeleccionado.nit" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Tipo de Entidad</label>
              <select v-model="usuarioSeleccionado.entityType" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                <option value="hospital">Hospital</option>
                <option value="clinica">Clínica</option>
                <option value="laboratorio">Laboratorio</option>
                <option value="ips">IPS</option>
              </select>
            </div>
          </template>

          <template v-if="usuarioSeleccionado.tipo === 'cups'">
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Código CUPS</label>
              <input v-model="usuarioSeleccionado.cupsCode" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Nombre del Procedimiento</label>
              <input v-model="usuarioSeleccionado.cupsName" type="text" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs" />
            </div>
            <div>
              <label class="mb-2 text-xs leading-normal text-gray-500 dark:text-gray-400">Categoría</label>
              <select v-model="usuarioSeleccionado.cupsCategory" required class="text-sm font-medium text-gray-800 dark:text-white/90 w-full rounded-lg border border-gray-300 dark:border-gray-700 px-4 py-2.5 bg-transparent shadow-theme-xs">
                <option value="diagnostico">Diagnóstico</option>
                <option value="terapeutico">Terapéutico</option>
                <option value="quirurgico">Quirúrgico</option>
                <option value="procedimiento">Procedimiento</option>
              </select>
            </div>
          </template>

          <div class="col-span-2 flex justify-end gap-4 mt-4">
            <button type="button" @click="cancelarEdicion" class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-300 dark:hover:bg-gray-700">
              Cancelar
            </button>
            <button type="submit" class="edit-button-modern">Guardar Cambios</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import Dropzone from '@/components/Muestras/NuevaMuestra/Dropzone.vue'

// Interfaces
interface Usuario {
  id: string
  nombre: string
  tipo: string
  fotoPerfil?: string
  documento?: string
  nit?: string
  codigo?: string
  firstName?: string
  lastName?: string
  email?: string
  phone: string
  specialty?: string
  medicalLicense?: string
  isActive?: boolean
  entityName?: string
  entityType?: string
  address?: string
  cupsCode?: string
  cupsName?: string
  cupsCategory?: string
  cupsDescription?: string
  role: string
  startDate?: string
  observaciones?: string
  firmaPatologoUrl?: string
}

interface NuevoUsuario {
  firstName: string
  lastName: string
  email: string
  phone: string
  role: string
  specialty?: string
  documento?: string
  startDate?: string
  entityName?: string
  nit?: string
  address?: string
  entityType?: string
  medicalLicense?: string
  observaciones?: string
  firmaPatologoUrl?: string
  isActive?: boolean
  cupsCode?: string
  cupsName?: string
  cupsCategory?: string
  cupsDescription?: string
}

const tiposUsuario = [
  { value: 'administrativo', label: 'Administrativo' },
  { value: 'patologo', label: 'Patólogo' },
  { value: 'entidad', label: 'Entidad' },
  { value: 'cups', label: 'CUPS' }
]

const tipoUsuarioSeleccionado = ref('')

const firmaPatologoFile = ref<File | null>(null)

const nuevoUsuario = ref({
  // Campos comunes
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  role: '',
  specialty: '',
  
  // Campos específicos para administrativo
  documento: '',
  startDate: '',
  
  // Campos específicos para entidad
  entityName: '',
  nit: '',
  address: '',
  entityType: '',
  
  // Campos específicos para patólogo
  medicalLicense: '',
  observaciones: '',
  firmaPatologoUrl: '',
  isActive: true,
  
  // Campos específicos para CUPS
  cupsCode: '',
  cupsName: '',
  cupsCategory: '',
  cupsDescription: ''
})

const usuarioCreado = ref(false)

const mensajeExito = ref('')
const mensajeActualizacion = ref('')

// Ejemplos de usuarios para cada tipo
const usuariosEjemplo: Usuario[] = [
  {
    id: '1',
    nombre: 'Juan Pérez',
    tipo: 'administrativo',
    fotoPerfil: '/images/user/owner.jpg',
    documento: '1234567890',
    firstName: 'Juan',
    lastName: 'Pérez',
    email: 'juan.perez@example.com',
    phone: '3001234567',
    startDate: '2024-01-01',
    role: 'administrativo'
  },
  {
    id: '2',
    nombre: 'Dra. María Rodríguez',
    tipo: 'patologo',
    fotoPerfil: '/images/user/owner.jpg',
    documento: '9876543210',
    firstName: 'María',
    lastName: 'Rodríguez',
    email: 'maria.rodriguez@example.com',
    phone: '3009876543',
    specialty: 'Anatomía Patológica',
    medicalLicense: 'MP12345',
    isActive: true,
    startDate: '2024-01-15',
    role: 'patologo',
    observaciones: 'Especialista en patología oncológica'
  },
  {
    id: '3',
    nombre: 'Clínica San José',
    tipo: 'entidad',
    nit: '900123456-7',
    entityName: 'Clínica San José',
    address: 'Calle 123 #45-67',
    phone: '6012345678',
    email: 'contacto@clinicasanjose.com',
    entityType: 'clinica',
    role: 'entidad'
  },
  {
    id: '4',
    nombre: 'Biopsia de Mama',
    tipo: 'cups',
    cupsCode: '88103',
    cupsName: 'Biopsia de Mama con Aguja Gruesa',
    cupsCategory: 'diagnostico',
    cupsDescription: 'Procedimiento diagnóstico para obtener muestras de tejido mamario',
    role: 'cups',
    phone: 'N/A'
  }
]

// Mock API Service
const api = {
  buscarUsuarios: async (params: { query: string; tipo?: string }) => {
    // Simular delay de red
    await new Promise(resolve => setTimeout(resolve, 300))
    
    const query = params.query.toLowerCase().trim()
    const tipo = params.tipo === 'todos' ? undefined : params.tipo
    
    return {
      success: true,
      data: usuariosEjemplo.filter(usuario => {
        // Si no hay query, no mostrar resultados
        if (!query) return false
        
        // Filtrar por tipo si está especificado
        if (tipo && usuario.tipo !== tipo) return false
        
        // Buscar en todos los campos relevantes
        const searchableFields = [
          usuario.nombre,
          usuario.documento,
          usuario.nit,
          usuario.cupsCode,
          usuario.email,
          usuario.entityName,
          usuario.cupsName,
          usuario.specialty,
          usuario.medicalLicense
        ].filter((field): field is string => field !== undefined && field !== null)
        
        return searchableFields.some(field => 
          field.toLowerCase().includes(query)
        )
      })
    }
  },
  
  actualizarUsuario: async (usuario: Usuario) => {
    // Simular delay de red
    await new Promise(resolve => setTimeout(resolve, 500))
    
    // Simular actualización exitosa
    return {
      success: true,
      data: usuario
    }
  },
  
  crearUsuario: async (usuario: NuevoUsuario) => {
    // Simular delay de red
    await new Promise(resolve => setTimeout(resolve, 500))
    
    // Simular creación exitosa
    return {
      success: true,
      data: {
        ...usuario,
        id: Math.random().toString(36).substr(2, 9) // Generar ID aleatorio
      }
    }
  }
}

// Variables para la búsqueda y edición
const busquedaUsuario = ref('')
const tipoBusqueda = ref('todos')
const resultadosBusqueda = ref<Usuario[]>([])
const usuarioSeleccionado = ref<Usuario | null>(null)
const estaBuscando = ref(false)
const errorBusqueda = ref('')
const busquedaRealizada = ref(false)

// Función de búsqueda mejorada
const buscarUsuarios = async () => {
  if (!busquedaUsuario.value.trim()) {
    resultadosBusqueda.value = []
    busquedaRealizada.value = false
    return
  }

  estaBuscando.value = true
  errorBusqueda.value = ''
  busquedaRealizada.value = true

  try {
    const response = await api.buscarUsuarios({
      query: busquedaUsuario.value,
      tipo: tipoBusqueda.value
    })

    if (response.success) {
      resultadosBusqueda.value = response.data
      if (response.data.length === 0) {
        errorBusqueda.value = 'No se encontraron resultados para tu búsqueda'
      }
    } else {
      errorBusqueda.value = 'Error al realizar la búsqueda'
      resultadosBusqueda.value = []
    }
  } catch (error) {
    console.error('Error en la búsqueda:', error)
    errorBusqueda.value = 'Error al realizar la búsqueda'
    resultadosBusqueda.value = []
  } finally {
    estaBuscando.value = false
  }
}

// Función para limpiar la búsqueda
const limpiarBusqueda = () => {
  busquedaUsuario.value = ''
  tipoBusqueda.value = 'todos'
  resultadosBusqueda.value = []
  usuarioSeleccionado.value = null
  errorBusqueda.value = ''
  busquedaRealizada.value = false
}

// Observar cambios en el tipo de búsqueda
watch(tipoBusqueda, () => {
  if (busquedaUsuario.value.trim()) {
    buscarUsuarios()
  }
})

// Seleccionar usuario para editar
const seleccionarUsuarioParaEditar = (usuario: Usuario) => {
  usuarioSeleccionado.value = { ...usuario }
}

// Cancelar edición
const cancelarEdicion = () => {
  usuarioSeleccionado.value = null
}

// Actualizar usuario
const actualizarUsuario = async () => {
  if (!usuarioSeleccionado.value) return

  try {
    const response = await api.actualizarUsuario(usuarioSeleccionado.value)
    if (response.success) {
      // Actualizar la lista de resultados
      const index = resultadosBusqueda.value.findIndex(u => u.id === usuarioSeleccionado.value?.id)
      if (index !== -1 && usuarioSeleccionado.value) {
        resultadosBusqueda.value[index] = { ...usuarioSeleccionado.value }
      }
      
      // Mostrar mensaje de éxito
      switch (tipoUsuarioSeleccionado.value) {
        case 'administrativo':
          mensajeActualizacion.value = 'Usuario administrativo actualizado exitosamente.'; break;
        case 'patologo':
          mensajeActualizacion.value = 'Patólogo actualizado exitosamente.'; break;
        case 'entidad':
          mensajeActualizacion.value = 'Entidad actualizada exitosamente.'; break;
        case 'cups':
          mensajeActualizacion.value = 'CUPS actualizado exitosamente.'; break;
        default:
          mensajeActualizacion.value = 'Registro actualizado exitosamente.';
      }
      usuarioCreado.value = true
      mensajeExito.value = mensajeActualizacion.value
      
      // Limpiar selección después de 3 segundos
      setTimeout(() => {
        usuarioCreado.value = false
        usuarioSeleccionado.value = null
      }, 3000)
    }
  } catch (error) {
    console.error('Error al actualizar usuario:', error)
    errorBusqueda.value = 'Error al actualizar usuario'
  }
}

// Crear usuario
const crearUsuario = async () => {
  try {
    const usuarioData = { ...nuevoUsuario.value } as NuevoUsuario
    const response = await api.crearUsuario(usuarioData)
    
    if (response.success) {
      // Limpiar el formulario
      nuevoUsuario.value = {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        role: '',
        specialty: '',
        documento: '',
        startDate: '',
        entityName: '',
        nit: '',
        address: '',
        entityType: '',
        medicalLicense: '',
        observaciones: '',
        firmaPatologoUrl: '',
        isActive: true,
        cupsCode: '',
        cupsName: '',
        cupsCategory: '',
        cupsDescription: ''
      }
      
      // Mostrar mensaje de éxito
      alert('Usuario creado exitosamente')
    }
  } catch (error) {
    console.error('Error al crear usuario:', error)
    alert('Error al crear usuario')
  }
}

const fileInput = ref<HTMLInputElement | null>(null)
const previewImage = ref<string | null>(null)

const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    // Validar tipo de archivo
    if (!file.type.startsWith('image/')) {
      alert('Por favor, selecciona un archivo de imagen válido')
      return
    }
    
    // Validar tamaño (máximo 2MB)
    if (file.size > 2 * 1024 * 1024) {
      alert('La imagen no debe superar los 2MB')
      return
    }
    
    // Crear preview
    const reader = new FileReader()
    reader.onload = (e) => {
      previewImage.value = e.target?.result as string
    }
    reader.readAsDataURL(file)
  }
}

// Manejar el archivo de la firma desde el evento del Dropzone
const handleFirmaFile = (file: File) => {
  firmaPatologoFile.value = file
  // Opcionalmente, podrías mostrar una vista previa o el nombre del archivo
  console.log('Firma recibida:', file.name)
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
