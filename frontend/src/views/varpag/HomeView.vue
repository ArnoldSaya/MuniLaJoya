<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
import logoA from '@/assets/images/logoA.jpg'
</script>

<template>
  <div
    class="home"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >

    <img
      :src="fondoCamilo"
      alt=""
      class="view-bg"
    />

    <div class="home__overlay"></div>

    <!-- =========================
         CONTENIDO PRINCIPAL
    ========================== -->

    <section class="hero">

      <div class="hero-content">

        <p class="hero-eyebrow">
          ATRÉVETE AL CAMBIO CON
        </p>

        <h1 class="hero-title">
          CAMILO
        </h1>

        <div class="hero-line"></div>

        <p class="hero-subtitle">
          Trabajamos por un distrito más seguro, moderno
          y con oportunidades para todos.
        </p>

        <router-link
          to="/propuestas"
          class="btn-plan"
        >
          CONOCE NUESTRO PLAN →
        </router-link>

      </div>

    </section>

  </div>
</template>