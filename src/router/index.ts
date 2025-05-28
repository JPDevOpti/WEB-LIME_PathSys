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
      component: () => import('../views/Auth/InicioSesion.vue'),
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
      path: '/nuevo-administrativo',
      name: 'Nuevo Administrativo',
      component: () => import('../views/NuevosIntegrantes/NuevoAdministrativo.vue'),
      meta: {
        title: 'Nuevo Administrativo',
      },
    },

    
    {
      path: '/calendar',
      name: 'Calendar',
      component: () => import('../views/Others/Calendar.vue'),
      meta: {
        title: 'Calendar',
      },
    },
    {
      path: '/form-elements',
      name: 'Form Elements',
      component: () => import('../views/Forms/FormElements.vue'),
      meta: {
        title: 'Form Elements',
      },
    },

    {
      path: '/basic-tables',
      name: 'Basic Tables',
      component: () => import('../views/Tables/BasicTables.vue'),
      meta: {
        title: 'Basic Tables',
      },
    },
    {
      path: '/line-chart',
      name: 'Line Chart',
      component: () => import('../views/Chart/LineChart/LineChart.vue'),
    },
    {
      path: '/bar-chart',
      name: 'Bar Chart',
      component: () => import('../views/Chart/BarChart/BarChart.vue'),
    },
    {
      path: '/alerts',
      name: 'Alerts',
      component: () => import('../views/UiElements/Alerts.vue'),
      meta: {
        title: 'Alerts',
      },
    },
    {
      path: '/avatars',
      name: 'Avatars',
      component: () => import('../views/UiElements/Avatars.vue'),
      meta: {
        title: 'Avatars',
      },
    },
    {
      path: '/badge',
      name: 'Badge',
      component: () => import('../views/UiElements/Badges.vue'),
      meta: {
        title: 'Badge',
      },
    },

    {
      path: '/buttons',
      name: 'Buttons',
      component: () => import('../views/UiElements/Buttons.vue'),
      meta: {
        title: 'Buttons',
      },
    },

    {
      path: '/images',
      name: 'Images',
      component: () => import('../views/UiElements/Images.vue'),
      meta: {
        title: 'Images',
      },
    },
    {
      path: '/videos',
      name: 'Videos',
      component: () => import('../views/UiElements/Videos.vue'),
      meta: {
        title: 'Videos',
      },
    },
    {
      path: '/blank',
      name: 'Blank',
      component: () => import('../views/Pages/BlankPage.vue'),
      meta: {
        title: 'Blank',
      },
    },

    {
      path: '/error-404',
      name: '404 Error',
      component: () => import('../views/Errors/FourZeroFour.vue'),
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
