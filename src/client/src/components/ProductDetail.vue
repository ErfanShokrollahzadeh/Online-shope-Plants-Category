<template>
  <div class="product-detail">
    <div v-if="loading" class="loading">
      Loading...
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else-if="product" class="product-content">
      <div class="row">
        <div class="col-md-6">
          <img :src="product.image" :alt="product.title" class="img-fluid rounded">
        </div>
        <div class="col-md-6">
          <h1>{{ product.title }}</h1>
          <div class="category-badge mb-3">{{ product.category?.title }}</div>
          <p class="price h3 mb-4">${{ product.price }}</p>
          <p>{{ product.description }}</p>
          
          <div class="plant-details mt-4">
            <div class="detail-item">
              <i class="bi bi-brightness-high"></i>
              <span>Light Requirement: {{ formatLightRequirement(product.light_requirement) }}</span>
            </div>
            <div class="detail-item">
              <i class="bi bi-droplet"></i>
              <span>Watering Frequency: {{ product.watering_frequency }}</span>
            </div>
            <div class="detail-item">
              <i class="bi bi-arrows-angle-expand"></i>
              <span>Plant Size: {{ formatPlantSize(product.plant_size) }}</span>
            </div>
          </div>

          <div class="care-instructions mt-4">
            <h3>Care Instructions</h3>
            <p>{{ product.care_instructions }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProductDetail',
  data() {
    return {
      product: null,
      loading: true,
      error: null
    }
  },
  methods: {
    formatLightRequirement(requirement) {
      return requirement?.charAt(0).toUpperCase() + requirement?.slice(1) + ' Light';
    },
    formatPlantSize(size) {
      return size?.charAt(0).toUpperCase() + size?.slice(1) + ' Size';
    },
    async fetchProduct() {
      try {
        const response = await axios.get(`/api/products/${this.$route.params.slug}/`);
        this.product = response.data;
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    }
  },
  created() {
    this.fetchProduct();
  }
}
</script>

<style scoped>
.product-detail {
  padding: 20px;
}

.detail-item {
  margin: 10px 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.category-badge {
  background-color: #e9ecef;
  padding: 4px 8px;
  border-radius: 4px;
  display: inline-block;
}

.price {
  color: #2c3e50;
}

.plant-details {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
}
</style>
