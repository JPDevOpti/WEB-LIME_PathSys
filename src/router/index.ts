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
      path: '/nuevo-patologo',
      name: 'Nueva Patologo',
      component: () => import('../views/NuevosIntegrantes/NuevoPatologo.vue'),
      meta: {
        title: 'Nueva Patologo',
      },
    },
    {
      path: '/nueva-entidad',
      name: 'Nueva Entidad',
      component: () => import('../views/NuevosIntegrantes/NuevaEntidad.vue'),
      meta: {
        title: 'Nueva Entidad',
      },
    },
        {
      path: '/nuevo-cups',
      name: 'Nuevo Cups',
      component: () => import('../views/NuevosIntegrantes/NuevoCups.vue'),
      meta: {
        title: 'Nuevo Cups',
      },
    },
    {
      path: '/line-chart',
      name: 'Line Chart',
      component: () => import('../views/Estadisticas/LineChart/LineChart.vue'),
    },
    {
      path: '/bar-chart',
      name: 'Bar Chart',
      component: () => import('../views/Estadisticas/BarChart/BarChart.vue'),
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
