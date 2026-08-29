<script setup lang="ts">
import headImage from '@/assets/images/FondoCamilo.jpg'
</script>

<template>
  <section
    class="site-hero"
    :style="{ backgroundImage: `url(${headImage})` }"
  >

    <!-- Capa oscura para mejorar la lectura -->
    <div class="site-hero__overlay"></div>

    <!-- Contenido de la página -->
    <div class="site-hero__body">
      <slot />
    </div>

  </section>
</template>