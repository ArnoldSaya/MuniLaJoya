<script setup lang="ts">
import { computed } from 'vue'
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'

import eficienteVideo from '@/assets/videos/eficiente.mp4'
import saneamientoVideo from '@/assets/videos/saneamiento.mp4'
import seguridadVideo from '@/assets/videos/seguridad.mp4'
import inclusionVideo from '@/assets/videos/inclusion.mp4'
import obrasVideo from '@/assets/videos/obras.mp4'

const props = defineProps<{
  slug: string
}>()

const videoMap: Record<string, string> = {
  municipalidad: eficienteVideo,
  saneamiento: saneamientoVideo,
  seguridad: seguridadVideo,
  desarrollo: inclusionVideo,
  infraestructura: obrasVideo
}

const descripcionMap: Record<string, string> = {
  municipalidad: 'Una municipalidad moderna, transparente y cercana, que atienda con rapidez y administre responsablemente los recursos de La Joya.',
  saneamiento: 'Trabajaremos por ampliar los servicios básicos, avanzar con el saneamiento físico-legal y promover un crecimiento ordenado de nuestro distrito.',
  seguridad: 'Fortaleceremos la seguridad ciudadana con mayor prevención, vigilancia, recuperación de espacios públicos y coordinación permanente con la población.',
  desarrollo: 'Impulsaremos oportunidades y programas para mejorar la calidad de vida de niños, jóvenes, mujeres, adultos mayores y familias de La Joya.',
  infraestructura: 'Priorizaremos obras que respondan a las necesidades reales de cada sector, mejorando vías, espacios públicos y servicios para el desarrollo del distrito.'
}

const tituloMap: Record<string, string> = {
  municipalidad: 'Municipalidad eficiente',
  saneamiento: 'Saneamiento y ordenamiento territorial',
  seguridad: 'Seguridad',
  desarrollo: 'Desarrollo e inclusión social',
  infraestructura: 'Obras e infraestructura'
}

const videoSrc = computed(() => videoMap[props.slug] || null)
const descripcion = computed(() => descripcionMap[props.slug] || null)
const titulo = computed(() => tituloMap[props.slug] || null)
</script>

<template>
  <div
    class="page-bg pronto-view"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >
    <img
      :src="fondoCamilo"
      alt=""
      class="view-bg"
    />
    <div class="area-content">
      <h1 class="area-title" v-if="titulo">{{ titulo }}</h1>
      <p class="area-descripcion" v-if="descripcion">{{ descripcion }}</p>
      <div class="area-video-wrapper">
        <video
          v-if="videoSrc"
          :src="videoSrc"
          class="area-video"
          autoplay
          loop
          muted
          playsinline
        ></video>
      </div>
    </div>

    <router-link to="/propuestas" class="area-back">
      ← Regresar
    </router-link>
  </div>
</template>

<style scoped>
.area-content {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.area-title {
  color: var(--blanco);
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
  font-size: 30px;
  margin: 0 0 14px;
}

.area-descripcion {
  color: var(--blanco);
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
  font-size: 18px;
  line-height: 1.6;
  max-width: 720px;
  margin: 0 0 20px;
}

.area-video-wrapper {
  position: relative;
  width: 100%;
}

.area-video {
  width: 100%;
  height: auto;
  max-height: 60vh;
  object-fit: contain;
  border-radius: 8px;
  display: block;
}

.area-back {
  position: relative;
  z-index: 1;
  display: none;
  color: var(--blanco);
  font-size: 16px;
  font-weight: 600;
  text-decoration: underline;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
}

.area-back:hover {
  opacity: 0.8;
}

@media (max-width: 600px) {
  .area-content {
    padding: 20px 15px 15px;
    max-width: 100%;
  }

  .area-title {
    font-size: 24px;
    margin: 0 0 12px;
  }

  .area-descripcion {
    font-size: 15px;
    line-height: 1.5;
    margin: 0 0 16px;
  }

  .area-video {
    max-height: 50vh;
    border-radius: 4px;
  }

  .area-back {
    display: inline-block;
    font-size: 14px;
    margin-top: 16px;
    margin-bottom: 40px;
  }
}
</style>
