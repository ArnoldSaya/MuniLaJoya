<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'

import agriculturaImage from '@/assets/images/Agricultura.png'
import desarrolloImage from '@/assets/images/Desarrollo.png'
import eficienteImage from '@/assets/images/Eficiente.png'
import obrasImage from '@/assets/images/Obras.png'
import saneamientoImage from '@/assets/images/Saneamiento.png'
import seguridadImage from '@/assets/images/Seguridad.png'

const areas = [
  {
    title: 'Municipalidad eficiente',
    image: eficienteImage,
    to: '/municipalidad-eficiente'
  },
  {
    title: 'Saneamiento y ordenamiento territorial',
    image: saneamientoImage,
    to: '/saneamiento'
  },
  {
    title: 'Seguridad',
    image: seguridadImage,
    to: '/seguridad'
  },
  {
    title: 'Desarrollo e inclusión social',
    image: desarrolloImage,
    to: '/desarrollo'
  },
  {
    title: 'Obras e infraestructura',
    image: obrasImage,
    to: '/infraestructura'
  },
  {
    title: 'Agricultura',
    image: agriculturaImage,
    to: '/agricultura'
  }
]
</script>

<template>
  <div
    class="proposals-page"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >

    <div class="proposals-page__overlay"></div>

    <!-- =========================
         ENCABEZADO
    ========================== -->

    <section class="proposals-header">

      <div class="head-title">

        <h2>
          Propuestas
        </h2>

        <p>
          Conoce nuestras áreas de trabajo para La Joya.
        </p>

      </div>

    </section>


    <!-- =========================
         ÁREAS
    ========================== -->

    <main class="content proposals-content">

      <h2>
        Conoce nuestras áreas
      </h2>

      <div class="options">

        <router-link
          v-for="area in areas"
          :key="area.title"
          :to="area.to"
          class="option-card"
        >

          <!-- Imagen -->
          <img
            :src="area.image"
            :alt="area.title"
            class="option-image"
          />

        </router-link>

      </div>

    </main>

  </div>
</template>