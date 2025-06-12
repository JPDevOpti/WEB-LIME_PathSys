import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { left: 0, top: 0 }
  },
  routes: [
    //Paginas de inicio
    {
      path: '/',
      name: 'Inicio',
      component: () => import('../views/Inicio.vue'),
      meta: {
        title: 'Inicio',
      },
    },
    //Paginas para crear y editar las muesttras
    {
      path: '/nueva-muestra',
      name: 'Nueva Muestra',
      component: () => import('../views/Muestras/NuevaMuestra.vue'),
      meta: {
        title: 'Nueva Muestra',
      },
    },
    {
      path: '/editar-muestra',
      name: 'Editar Muestra',
      component: () => import('../views/Muestras/EditarMuestra.vue'),
      meta: {
        title: 'Editar Muestra',
      },
    },
    //Paginas para en listar y buscar muestras actuales y anteriores
    {
      path: '/Listado-muestras-actuales',
      name: 'Listado Muestras Actuales',
      component: () => import('../views/Muestras/ListadoMuestrasActuales.vue'),
      meta: {
        title: 'Listado Muestras Actuales',
      },
    },
    {
      path: '/Listado-muestras-anteriores',
      name: 'Listado Muestras Anteriores',
      component: () => import('../views/Muestras/ListadoMuestrasAnteriores.vue'),
      meta: {
        title: 'Listado Muestras Anteriores',
      },
    },

    //Paginas para crear y validar informes
    {
      path: '/Realizar-informe',
      name: 'Realizar Informe',
      component: () => import('../views/Informes/RealizarInforme.vue'),
      meta: {
        title: 'Realizar Informe',
      },
    },
    {
      path: '/Validar-informe',
      name: 'Validar Informe',
      component: () => import('../views/Informes/ValidarInforme.vue'),
      meta: {
        title: 'Validar Informe',
      },
    },
    //Paginas para listar informes
    {
      path: '/Listado-informes',
      name: 'Listado Informes',
      component: () => import('../views/Informes/ListadoInformes.vue'),
      meta: {
        title: 'Listado Informes',
      },
    },

    //Paginas para autenticación
    {
      path: '/inicio-sesion',
      name: 'Inicio Sesión',
      component: () => import('../views/Autentificacion/InicioSesion.vue'),
      meta: {
        title: 'Inicio Sesión',
      },
    },
    // Paginas para registro de nuevos integrantes
    {
      path: '/perfil',
      name: 'perfil',
      component: () => import('../views/NuevosIntegrantes/Perfil.vue'),
      meta: {
        title: 'perfil',
      },
    },
    {
      path: '/crear-usuario',
      name: 'Nuevo Usuario',
      component: () => import('../views/NuevosIntegrantes/NuevoUsuario.vue'),
      meta: {
        title: 'Nuevo Usuario',
      },
    },

    {
      path: '/informe-mensual',
      name: 'Informe Mensual',
      component: () => import('../views/Estadisticas/InformesMensuales.vue'),
      meta: {
        title: 'Informe Mensual',
      },
    },
    {
      path: '/informe-oportunidad',
      name: 'Informe Oportunidad',
      component: () => import('../views/Estadisticas/Oportunidad.vue'),
      meta: {
        title: 'Informe Oportunidad',
      },
    },

    {
      path: '/error-404',
      name: '404 Error',
      component: () => import('../views/Errores/FourZeroFour.vue'),
      meta: {
        title: '404 Error',
      },
    },
  ],
})

export default router

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title} | LIME - Alma Mater`
  next()
})
