import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/varpag/HomeView.vue'
import MunicipalidadView from '../views/MunicipalidadView.vue'
import SaneamientoView from '../views/SaneamientoView.vue'
import InfraestructuraView from '../views/InfraestructuraView.vue'
import DesarrolloView from '../views/DesarrolloView.vue'
import AgriculturaView from '../views/AgriculturaView.vue'
import SeguridadView from '../views/SeguridadView.vue'
import PropuestasView from '../views/varpag/PropuestasView.vue'
import ConocenosView from '../views/varpag/ConocenosView.vue'
import MultimediaView from '../views/varpag/Multimedia.vue'
import ContactoView from '../views/varpag/Contacto.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/municipalidad-eficiente',
    name: 'municipalidad',
    component: MunicipalidadView
  },
  {
    path: '/saneamiento',
    name: 'saneamiento',
    component: SaneamientoView
  },
  {
    path: '/infraestructura',
    name: 'infraestructura',
    component: InfraestructuraView
  },
  {
    path: '/desarrollo',
    name: 'desarrollo',
    component: DesarrolloView
  },
  {
    path: '/agricultura',
    name: 'agricultura',
    component: AgriculturaView
  },
  {
    path: '/seguridad',
    name: 'seguridad',
    component: SeguridadView
  },
  {
    path: '/propuestas',
    name: 'propuestas',
    component: PropuestasView,
  },
  {
    path: '/conocenos',
    name: 'conocenos',
    component: ConocenosView,
  },
  {
    path: '/multimedia',
    name: 'multimedia',
    component: MultimediaView,
  },
  {
    path: '/contacto',
    name: 'contacto',
    component: ContactoView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router