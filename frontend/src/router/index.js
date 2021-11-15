import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Actors from '../views/Actors.vue'
import Directors from '../views/Directors.vue'
import Genres from '../views/Genres.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/actors',
    name: 'Actors',
    component: Actors
  },
  {
    path: '/directors',
    name: 'Directors',
    component: Directors
  },
  {
    path: '/genres',
    name: 'Genres',
    component: Genres
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
