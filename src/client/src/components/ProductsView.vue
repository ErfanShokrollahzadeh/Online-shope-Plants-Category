<template>
  <div class="products-container">
    <div v-if="loading" class="loading">
      Loading products...
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else>
      <div class="products-grid">
        <div v-for="product in products" :key="product.id" class="product-card">
          <img :src="product.image" :alt="product.title" class="product-image">
          <div class="product-info">
            <span class="category-badge">{{ product.category.title }}</span>
            <h3>{{ product.title }}</h3>
            <p>{{ product.short_description }}</p>
            <div class="product-details">
              <span class="detail-item">
                <i class="bi bi-brightness-high"></i>
                {{ formatLightRequirement(product.light_requirement) }}
              </span>
              <span class="detail-item">
                <i class="bi bi-arrows-angle-expand"></i>
                {{ formatPlantSize(product.plant_size) }}
              </span>
            </div>
            <p class="price">${{ product.price }}</p>
            <router-link 
              :to="`/product/${product.slug}`"
              class="view-details"
            >
              View Details
            </router-link>
          </div>
        </div>
      </div>
      
      <!-- Pagination -->
      <div v-if="pagination.count > 0" class="pagination">
        <button 
          :disabled="!pagination.previous" 
          @click="changePage(-1)"
          class="pagination-btn"
        >
          Previous
        </button>
        <span class="page-info">
          Page {{ currentPage }} of {{ totalPages }}
        </span>
        <button 
          :disabled="!pagination.next" 
          @click="changePage(1)"
          class="pagination-btn"
        >
          Next
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'ProductsView',
  data() {
    return {
      currentPage: 1
    }
  },
  computed: {
    ...mapState({
      products: state => state.products,
      loading: state => state.loading,
      error: state => state.error,
      pagination: state => state.pagination
    }),
    totalPages() {
      return Math.ceil(this.pagination.count / 12); // Assuming 12 items per page
    }
  },
  methods: {
    ...mapActions(['fetchProducts']),
    formatLightRequirement(requirement) {
      return requirement.charAt(0).toUpperCase() + requirement.slice(1) + ' Light';
    },
    formatPlantSize(size) {
      return size.charAt(0).toUpperCase() + size.slice(1) + ' Size';
    },
    async changePage(direction) {
      this.currentPage += direction;
      await this.fetchProducts(this.currentPage);
      window.scrollTo(0, 0);
    }
  },
  created() {
    this.fetchProducts(1);
  }
}
</script>

<style scoped>
.products-container {
  padding: 20px;
}

.loading, .error {
  text-align: center;
  padding: 20px;
}

.error {
  color: red;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.product-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-info {
  padding: 15px;
}

.product-info h3 {
  margin: 0;
  font-size: 1.2em;
}

.price {
  font-weight: bold;
  color: #2c3e50;
}

.view-details {
  display: inline-block;
  padding: 8px 16px;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  margin-top: 10px;
}

.view-details:hover {
  background-color: #3aa876;
}

.category-badge {
  background-color: #e9ecef;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8em;
  color: #495057;
  margin-bottom: 8px;
  display: inline-block;
}

.product-details {
  display: flex;
  gap: 12px;
  margin: 8px 0;
  font-size: 0.9em;
  color: #6c757d;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 4px;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 30px;
  padding: 20px 0;
}

.pagination-btn {
  padding: 8px 16px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.pagination-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.page-info {
  color: #666;
}
</style>
