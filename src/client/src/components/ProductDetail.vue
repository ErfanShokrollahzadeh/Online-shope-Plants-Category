<template>
  <div class="product-detail">
    <div v-if="loading" class="loading">
      Loading...
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else-if="product" class="product-content">
      <div class="row g-4">
        <div class="col-md-6">
          <div class="product-image-container" data-aos="fade-right">
            <img :src="product.image" :alt="product.title" class="product-image">
            <div class="image-overlay">
              <i class="fas fa-search-plus"></i>
            </div>
          </div>
        </div>
        <div class="col-md-6" data-aos="fade-left">
          <div class="product-info">
            <span class="category-badge">
              <i class="fas fa-leaf me-2"></i>
              {{ product.category?.title }}
            </span>
            <h1 class="product-title">{{ product.title }}</h1>
            <div class="price-tag">
              <i class="fas fa-tag me-2"></i>
              ${{ product.price }}
            </div>
            <p class="description">{{ product.description }}</p>
            
            <div class="plant-details">
              <div class="detail-item">
                <i class="fas fa-sun"></i>
                <span>{{ formatLightRequirement(product.light_requirement) }}</span>
              </div>
              <div class="detail-item">
                <i class="fas fa-tint"></i>
                <span>{{ product.watering_frequency }}</span>
              </div>
              <div class="detail-item">
                <i class="fas fa-ruler-vertical"></i>
                <span>{{ formatPlantSize(product.plant_size) }}</span>
              </div>
            </div>

            <div class="care-instructions">
              <h3><i class="fas fa-hand-holding-heart me-2"></i>Care Instructions</h3>
              <p>{{ product.care_instructions }}</p>
            </div>

            <button class="add-to-cart-btn">
              <i class="fas fa-shopping-cart me-2"></i>
              Add to Cart
            </button>
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

.product-content {
  padding: 2rem;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.product-image-container {
  position: relative;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.product-image {
  width: 100%;
  height: auto;
  transition: transform 0.5s ease;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-overlay i {
  color: white;
  font-size: 2rem;
}

.product-image-container:hover .product-image {
  transform: scale(1.05);
}

.product-image-container:hover .image-overlay {
  opacity: 1;
}

.product-info {
  padding: 1rem;
}

.category-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #4CAF50, #45a049);
  color: white;
  border-radius: 25px;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  box-shadow: 0 2px 4px rgba(76, 175, 80, 0.2);
}

.product-title {
  font-size: 2.5rem;
  font-weight: 600;
  margin: 1rem 0;
  color: #2c3e50;
}

.price-tag {
  font-size: 1.8rem;
  color: #4CAF50;
  font-weight: 600;
  margin: 1rem 0;
}

.description {
  color: #666;
  line-height: 1.6;
  margin: 1.5rem 0;
}

.plant-details {
  background: linear-gradient(to right, #f8f9fa, #ffffff);
  padding: 1.5rem;
  border-radius: 12px;
  margin: 1.5rem 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.detail-item {
  display: flex;
  align-items: center;
  margin: 1rem 0;
  transition: transform 0.2s ease;
}

.detail-item:hover {
  transform: translateX(10px);
}

.detail-item i {
  font-size: 1.2rem;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #4CAF50;
  color: white;
  border-radius: 50%;
  margin-right: 1rem;
}

.care-instructions {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
  margin: 1.5rem 0;
}

.care-instructions h3 {
  color: #2c3e50;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.add-to-cart-btn {
  width: 100%;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #4CAF50, #45a049);
  color: white;
  border: none;
  border-radius: 30px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2);
}

.add-to-cart-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
}

.loading {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.error {
  color: #dc3545;
  padding: 1rem;
  border-radius: 8px;
  background: #fff;
  border: 1px solid #dc3545;
}
</style>
