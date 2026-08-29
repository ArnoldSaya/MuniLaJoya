<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
</script>

<template>
  <div
    class="page-bg pronto-view"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >
    <h1>Próximamente</h1>

    <p class="area-descripcion">
      Esta área está en preparación. Estamos trabajando
      para darte toda la información.
    </p>

    <router-link to="/propuestas">
      Regresar
    </router-link>
  </div>
</template>

<style scoped>
.area-descripcion {
  color: var(--blanco);

  max-width: 640px;

  font-size: 20px;

  margin: 0 0 24px;

  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
}
</style>