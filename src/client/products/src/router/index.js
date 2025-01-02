import { createRouter, createWebHistory } from 'vue-router'
import ProductsView from '@/components/ProductsView.vue'

const routes = [
  {
    path: '/',
    name: 'products',
    component: ProductsView
  }
  // ...existing code...
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
