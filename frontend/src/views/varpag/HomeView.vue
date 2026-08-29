<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
import logoA from '@/assets/images/logoA.jpg'
</script>

<template>
  <div
    class="home"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >

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


      <!-- =========================
           LOGO / ALIANZA
      ========================== -->

      <div class="hero-badge">

        <img
          :src="logoA"
          alt="Alianza para el Progreso"
          class="badge-circle"
        />

        <div class="badge-text">
          ALIANZA PARA<br />
          EL PROGRESO
        </div>

      </div>


      <!-- =========================
           TARJETA DEL PLAN
      ========================== -->

      <div class="hero-card">

        <h3>
          CONOCE NUESTRO<br />
          PLAN DE GOBIERNO
        </h3>

        <p>
          Escanea el código QR y conoce
          todas nuestras propuestas
          para La Joya.
        </p>

        <div class="qr-placeholder"></div>

        <router-link
          to="/propuestas"
          class="btn-plan-card"
        >
          VER PLAN COMPLETO
        </router-link>

      </div>

    </section>

  </div>
</template>