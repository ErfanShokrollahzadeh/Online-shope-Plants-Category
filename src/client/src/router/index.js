import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'
import ProductsView from '@/components/ProductsView.vue'
import ProductDetail from '@/components/ProductDetail.vue'
import AboutView from '@/views/AboutView.vue'
import ContactView from '@/views/ContactView.vue'
import CategoriesView from '@/views/CategoriesView.vue'

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
      },
      {
        path: 'about',
        name: 'about',
        component: AboutView
      },
      {
        path: 'contact',
        name: 'contact',
        component: ContactView
      },
      {
        path: 'categories',
        name: 'categories',
        component: CategoriesView
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
