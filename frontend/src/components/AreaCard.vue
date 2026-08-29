<template>
  <router-link :to="link" class="option-card">
    <img
      :src="image"
      :alt="title"
      class="option-image"
    />

    <div class="option-title">
      {{ title }}
    </div>
  </router-link>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  image: string
  link: string
}>()
</script>