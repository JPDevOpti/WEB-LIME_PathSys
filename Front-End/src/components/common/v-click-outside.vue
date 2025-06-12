<!--
  Componente v-click-outside
  Detecta clics fuera de un elemento y ejecuta una función de callback.
  Utilizado para cerrar menús, modales, etc.
  Incluye soporte para accesibilidad y eventos de clic.
-->
<script>
import { onMounted, onUnmounted } from 'vue'

export default {
  created(el, binding) {
    el.clickOutsideEvent = (event) => {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event)
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent)
  },
}
</script>
