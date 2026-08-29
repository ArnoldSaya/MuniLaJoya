<script setup lang="ts">
import { onMounted, ref } from 'vue'

import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
import { obtenerInformacionArea } from '@/api/areas'
import type { AreaInformacion } from '@/api/types'

const props = defineProps<{
  slug: string
}>()

const cargando = ref(true)
const error = ref('')
const informacion = ref<AreaInformacion | null>(null)

onMounted(async () => {
  try {
    informacion.value = await obtenerInformacionArea(props.slug)
  } catch {
    error.value = 'No se pudo conectar con el servidor.'
  } finally {
    cargando.value = false
  }
})
</script>

<template>
  <div
    class="page-bg pronto-view"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >
    <template v-if="cargando">
      <h1>Cargando...</h1>
    </template>

    <template v-else-if="informacion">
      <h1>{{ informacion.titulo }}</h1>

      <p class="area-descripcion">
        {{ informacion.descripcion }}
      </p>

      <router-link to="/">
        Volver al inicio
      </router-link>
    </template>

    <template v-else>
      <h1>Error</h1>

      <p class="area-descripcion">
        {{ error }}
      </p>

      <router-link to="/">
        Volver al inicio
      </router-link>
    </template>
  </div>
</template>

<style scoped>
.area-descripcion {
  color: var(--blanco);

  max-width: 640px;

  font-size: 18px;

  margin: 0 0 24px;

  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
}
</style>