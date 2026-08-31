<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
import logoA from '@/assets/images/logoA.jpg'
import qrImage from '@/assets/images/QR.png'
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

        <img
          :src="qrImage"
          alt="Código QR"
          class="qr-image"
        />

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