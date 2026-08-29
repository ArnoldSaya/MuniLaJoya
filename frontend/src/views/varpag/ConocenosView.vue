<script setup lang="ts">
import fondoCamilo from '@/assets/images/FondoCamilo.jpg'
</script>

<template>
  <div
    class="page-bg"
    :style="{ backgroundImage: `url(${fondoCamilo})` }"
  >
    <img
      :src="fondoCamilo"
      alt=""
      class="view-bg"
    />
    <div class="head-title">
      <h2>Conócenos</h2>
      <p>Quiénes somos y por qué trabajamos por La Joya.</p>
    </div>
  </div>
</template>
