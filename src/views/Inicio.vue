<template>
  <admin-layout>
    <div class="grid grid-cols-12 gap-4 md:gap-6">
      <div class="col-span-12 space-y-6 xl:col-span-7">
        <BloquesMetricas />
        <PruebasMes />
      </div>
      <div class="col-span-12 xl:col-span-5">
        <PorcentajeAvance />
      </div>

      <div class="col-span-12">
        <MuestrasUrgentes />
      </div>
    </div>
  </admin-layout>
</template>

<script>
import AdminLayout from '../components/layout/AdminLayout.vue'
import BloquesMetricas from '../components/Inicio/BloquesMetricas.vue'
import PruebasMes from '../components/Inicio/PruebasMes.vue'
import PorcentajeAvance from '../components/Inicio/PorcentajeAvance.vue'
import MuestrasUrgentes from '../components/Inicio/MuestrasUrgentes.vue'

export default {
  components: {
    AdminLayout,
    BloquesMetricas,
    PruebasMes,
    PorcentajeAvance,
    MuestrasUrgentes,
  },
  name: 'Inicio',
}
</script>