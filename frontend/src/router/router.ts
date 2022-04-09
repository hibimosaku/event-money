import top from "../top.vue"
import top1 from "../top1.vue"

// import { createRouter, createWebHashHistory } from "vue-router";

import { createRouter, createWebHistory } from 'vue-router'

const Home = { template: '<div>Home</div>' }

const routes = [
  { path: '/', component: top },
  { path: '/abb', component: top1 },

  { path: '/home', component: Home },
]

const router = createRouter({
  history: createWebHistory(),
  // history:createWebHashHistory(),
  routes,
})

export default router;