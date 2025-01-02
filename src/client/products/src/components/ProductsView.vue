<template>
  <div class="products-container">
    <!-- Filters Section -->
    <div class="filters hvr-shadow-radial" data-aos="fade-down">
      <div class="filter-controls">
        <div class="search-box">
          <i class="fas fa-leaf"></i>
          <input
            v-model="filters.search"
            type="text"
            placeholder="Search plants..."
          />
        </div>
        <div class="filter-groups">
          <select v-model="filters.category" class="filter-select">
            <option value="">All Categories</option>
            <option
              v-for="category in categories"
              :key="category.id"
              :value="category.id"
            >
              {{ category.title }}
            </option>
          </select>
          <div class="price-filter">
            <input
              v-model.number="filters.minPrice"
              type="number"
              placeholder="Min price"
            />
            <input
              v-model.number="filters.maxPrice"
              type="number"
              placeholder="Max price"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Products Grid -->
    <div class="products-grid">
      <div
        v-for="product in products"
        :key="product?.id"
        class="product-card hvr-grow-shadow"
        data-aos="fade-up"
        data-aos-delay="100"
        data-aos-anchor-placement="top-bottom"
      >
        <div class="product-image">
          <img :src="product?.image" :alt="product?.title" />
          <div class="product-overlay">
            <button @click="addToCart(product)" class="cart-btn">
              <i class="fas fa-cart-plus"></i>
              Add to Cart
            </button>
          </div>
        </div>
        <div class="product-info">
          <div class="product-category">
            <span
              v-for="cat in product?.category"
              :key="cat.id"
              class="category-tag"
            >
              {{ cat.title }}
            </span>
          </div>
          <h3>{{ product?.title }}</h3>
          <p class="price">${{ product?.price }}</p>
          <p class="description">{{ product?.short_description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import anime from "animejs";
import { gsap } from "gsap";
import AOS from "aos";
import "aos/dist/aos.css";

export default {
  name: "ProductsView",
  data() {
    return {
      products: [],
      categories: [],
      filters: {
        search: "",
        category: "",
        minPrice: "",
        maxPrice: "",
      },
    };
  },
  methods: {
    async fetchProducts() {
      try {
        const params = {
          category: this.filters.category,
          min_price: this.filters.minPrice,
          max_price: this.filters.maxPrice,
          search: this.filters.search,
        };
        const response = await axios.get(
          "http://127.0.0.1:8000/api/products/",
          { params }
        );
        this.products = response.data;
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    },
    addToCart(product) {
      // Implement cart functionality
      console.log("Adding to cart:", product);
    },
  },
  mounted() {
    this.fetchProducts();
    AOS.init({
      duration: 800,
      offset: 100,
      once: true,
    });

    // Anime.js animation for grid items
    anime({
      targets: ".product-card",
      scale: [0.9, 1],
      opacity: [0, 1],
      delay: anime.stagger(100),
      easing: "easeOutElastic(1, .8)",
    });

    // GSAP animations
    gsap.from(".filters", {
      duration: 1,
      y: -50,
      opacity: 0,
      ease: "power3.out",
    });
  },
  watch: {
    filters: {
      deep: true,
      handler() {
        this.fetchProducts();
      },
    },
  },
};
</script>

<style scoped>
.products-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
  background: linear-gradient(135deg, #f8faf8 0%, #ffffff 100%);
  min-height: 100vh;
}

.filters {
  margin-bottom: 2.5rem;
  background: linear-gradient(145deg, #ffffff, #f0f7f0);
  padding: 1.5rem;
  border-radius: 25px;
  box-shadow: 0 10px 30px rgba(76, 175, 80, 0.1);
}

.filter-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
}

.search-box {
  position: relative;
  flex: 1;
  min-width: 250px;
}

.search-box i {
  position: absolute;
  left: 1.2rem;
  top: 50%;
  transform: translateY(-50%);
  color: #4CAF50;
  font-size: 1.1rem;
}

.search-box input {
  width: 100%;
  padding: 1rem 1rem 1rem 3rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border: 2px solid #e8f5e9;
  border-radius: 30px;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.search-box input:focus {
  border-color: #4caf50;
  box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.1);
}

.filter-groups {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.filter-select,
.price-filter input {
  padding: 0.8rem 1rem;
  border: 2px solid #eee;
  border-radius: 15px;
  transition: all 0.3s ease;
}

.filter-select:focus,
.price-filter input:focus {
  border-color: #4caf50;
  outline: none;
}

.filter-select {
  padding: 0.8rem 2rem;
  border: 2px solid #eee;
  border-radius: 15px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%234CAF50' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E") no-repeat right 1rem center;
  appearance: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.price-filter input {
  padding: 0.8rem 1rem;
  border: 2px solid #eee;
  border-radius: 15px;
  width: 120px;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}

.product-card {
  background: linear-gradient(145deg, #ffffff, #f0f7f0);
  border-radius: 25px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transform-origin: center;
  will-change: transform;
}

.product-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.product-image {
  position: relative;
  height: 280px;
  overflow: hidden;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.product-image::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(76,175,80,0.1) 100%);
}

.product-card:hover .product-image img {
  transform: scale(1.1);
}

.product-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(rgba(76, 175, 80, 0.2), rgba(69, 160, 73, 0.4));
  backdrop-filter: blur(3px);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.product-card:hover .product-overlay {
  opacity: 1;
}

.cart-btn {
  background: linear-gradient(135deg, #66bb6a, #43a047);
  color: white;
  border: none;
  padding: 1.2rem 2.5rem;
  border-radius: 30px;
  font-weight: 600;
  letter-spacing: 1px;
  transform: translateY(20px);
  transform-origin: center;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  animation: pulseGlow 2s infinite;
}

.product-card:hover .cart-btn {
  transform: translateY(0);
}

.cart-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 25px rgba(76, 175, 80, 0.3);
  background: linear-gradient(135deg, #45a049, #3e8e41);
}

.product-info {
  padding: 1.5rem;
}

.product-category {
  margin-bottom: 0.5rem;
}

.category-tag {
  display: inline-block;
  padding: 0.4rem 1rem;
  background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
  color: #4caf50;
  border: 1px solid rgba(76, 175, 80, 0.2);
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 500;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
}

.product-info h3 {
  margin: 0.5rem 0;
  font-size: 1.2rem;
  color: #333;
}

.price {
  color: #4caf50;
  font-weight: bold;
  font-size: 1.2rem;
  margin: 0.5rem 0;
}

.description {
  color: #666;
  font-size: 0.9rem;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

@keyframes leafFall {
  0% { transform: rotate(0deg) translateY(-20px); opacity: 0; }
  100% { transform: rotate(360deg) translateY(0); opacity: 1; }
}

.product-card:hover::before {
  content: '🌿';
  position: absolute;
  top: -20px;
  left: 50%;
  font-size: 24px;
  animation: leafFall 1s ease forwards;
}

@keyframes pulseGlow {
  0% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
  100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }
}

@media (max-width: 768px) {
  .products-container {
    padding: 1rem;
  }

  .filter-controls {
    flex-direction: column;
  }

  .search-box,
  .filter-groups {
    width: 100%;
  }

  .price-filter {
    display: flex;
    gap: 0.5rem;
  }

  .price-filter input {
    flex: 1;
  }
}
</style>
