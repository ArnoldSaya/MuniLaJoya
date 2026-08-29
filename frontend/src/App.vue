<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import '@/assets/styles/main.css'

import footerImage from '@/assets/images/foot.jpg'
import logoA from '@/assets/images/logoA.jpg'
import logoFacebook from '@/assets/images/logoFce.jpg'
import logoTiktok from '@/assets/images/logoTiktok.jpg'

const menuOpen = ref(false)
const router = useRouter()

function closeMenu() {
  menuOpen.value = false
}

// Cierra el menú automáticamente al navegar a otra página
router.afterEach(() => {
  menuOpen.value = false
})
</script>

<template>
  <div id="app-wrapper">

    <!-- =========================
         HEADER / NAVBAR
         ========================= -->

    <header class="navbar">

      <!-- Marca -->
      <div class="brand">

        <img
          :src="logoA"
          alt="Alianza para el Progreso"
          class="brand-letter"
        />

        <div class="brand-text">
          ALIANZA PARA<br />
          EL PROGRESO
        </div>

      </div>


      <!-- Botón hamburguesa (solo visible en móvil/tablet) -->
      <button
        class="menu-toggle"
        :class="{ 'is-active': menuOpen }"
        aria-label="Abrir menú"
        :aria-expanded="menuOpen"
        @click="menuOpen = !menuOpen"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>


      <!-- Navegación -->
      <nav class="nav-links" :class="{ 'is-open': menuOpen }">

        <router-link to="/" @click="closeMenu">
          INICIO
        </router-link>

        <router-link to="/propuestas" @click="closeMenu">
          PROPUESTAS
        </router-link>

        <router-link to="/conocenos" @click="closeMenu">
          CONÓCENOS
        </router-link>

        <router-link to="/multimedia" @click="closeMenu">
          MULTIMEDIA
        </router-link>

        <router-link to="/contacto" @click="closeMenu">
          CONTACTO
        </router-link>

        <!-- Acciones dentro del menú móvil -->
        <div class="nav-actions nav-actions--mobile">

          <router-link
            to="/contacto"
            class="btn-unete"
            @click="closeMenu"
          >
            ÚNETE
          </router-link>

          <div class="socials">

            <a
              href="https://www.facebook.com/camilo.carpio.concha.2025"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Facebook"
            >
              <img :src="logoFacebook" alt="Facebook" />
            </a>

            <a
              href="https://www.tiktok.com/@camilocarpio.lajoya"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="TikTok"
            >
              <img :src="logoTiktok" alt="TikTok" />
            </a>

          </div>

        </div>

      </nav>


      <!-- Acciones (solo visibles en desktop, se ocultan en móvil
           porque ya están duplicadas dentro de .nav-links arriba) -->
      <div class="nav-actions nav-actions--desktop">

        <router-link
          to="/contacto"
          class="btn-unete"
        >
          ÚNETE
        </router-link>

        <div class="socials">

          <a
            href="https://www.facebook.com/camilo.carpio.concha.2025"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Facebook"
          >
            <img :src="logoFacebook" alt="Facebook" />
          </a>

          <a
            href="https://www.tiktok.com/@camilocarpio.lajoya"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="TikTok"
          >
            <img :src="logoTiktok" alt="TikTok" />
          </a>

        </div>

      </div>

    </header>


    <!-- Fondo oscuro al abrir el menú (opcional, mejora UX) -->
    <div
      v-if="menuOpen"
      class="menu-backdrop"
      @click="closeMenu"
    ></div>


    <!-- =========================
         CONTENIDO DE LAS VISTAS
         ========================= -->

    <main>
      <router-view />
    </main>


    <!-- =========================
         FOOTER
         ========================= -->

    <footer class="footer">

      <img
        :src="footerImage"
        alt="Pie de página"
        class="footer-image"
      />

      <div class="footer-overlay">

        <div class="footer-brand">
          <img
            :src="logoA"
            alt="Alianza para el Progreso"
            class="brand-letter"
          />
          <span>Municipalidad de La Joya</span>
        </div>

        <div class="footer-slogan">
          <strong>Atrévete al cambio.</strong>
          <span>La Joya avanza.</span>
        </div>

        <div class="footer-contact">
          <p>📍 La Joya, Arequipa</p>
          <p>📞 +51 987 654 321</p>
          <p>✉️ contacto@alianzaparaelprogreso.pe</p>
        </div>

        <div class="footer-socials">

          <a
            href="https://www.facebook.com/camilo.carpio.concha.2025"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Facebook"
          >
            <img :src="logoFacebook" alt="Facebook" />
          </a>

          <a
            href="https://www.tiktok.com/@camilocarpio.lajoya"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="TikTok"
          >
            <img :src="logoTiktok" alt="TikTok" />
          </a>

        </div>

      </div>

    </footer>

  </div>
</template>