<template>
  <div class="products-container">
    <div class="products-grid"></div>
      <div v-for="product in products" 
           :key="product.id" 
           class="product-card">
        <div class="product-image">
          <img :src="product.image" :alt="product.title"/>
        </div>
        <div class="product-info">
          <h3>{{ product.title }}</h3>
          <p class="price">${{ product.price }}</p>
          <button @click="addToCart(product)" class="add-to-cart">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'ProductsView',
  setup() {
    const products = ref([])

    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/products/')
        products.value = response.data
      } catch (error) {
        console.error('Error fetching products:', error)
      }
    }

    const addToCart = (product) => {
      console.log('Adding to cart:', product)
    }

    onMounted(() => {
      fetchProducts()
    })

    return {
      products,
      addToCart
    }
  }
}
</script>

<style scoped>
.products-container {
  padding: 20px;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.product-card {
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-info {
  padding: 15px;
}

.add-to-cart {
  background: #4CAF50;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.add-to-cart:hover {
  background: #45a049;
}
</style>
