import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'
import ProductsView from '@/components/ProductsView.vue'
import ProductDetail from '@/components/ProductDetail.vue'

const routes = [
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: '',
        name: 'products',
        component: ProductsView
      },
      {
        path: 'product/:slug',
        name: 'product-detail',
        component: ProductDetail
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
