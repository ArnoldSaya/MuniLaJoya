<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
import agriculturaVideo from '@/assets/videos/agricultura.mp4'
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
      <h1 class="area-title">Agricultura</h1>
      <p class="area-descripcion">Apoyaremos a nuestros agricultores y productores, promoviendo capacitación, tecnología, gestión de recursos y mejores oportunidades de comercialización.</p>
      <div class="area-video-wrapper">
        <video
          :src="agriculturaVideo"
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
  color: #FFF8E6;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8);
  font-size: 30px;
  margin: 0 0 14px;
}

.area-descripcion {
  color: #FFF8E6;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8);
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
