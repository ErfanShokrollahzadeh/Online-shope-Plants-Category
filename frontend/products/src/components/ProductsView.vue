<template>
  <div class="products-container">
    <!-- Filters Section -->
    <div class="filters" data-aos="fade-down">
      <div class="filter-controls">
        <div class="search-box">
          <i class="bi bi-search"></i>
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
        class="product-card"
        data-aos="fade-up"
      >
        <div class="product-image">
          <img :src="product?.image" :alt="product?.title" />
          <div class="product-overlay">
            <button @click="addToCart(product)" class="cart-btn">
              <i class="bi bi-cart-plus"></i>
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.filters {
  margin-bottom: 2rem;
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
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
  min-width: 200px;
}

.search-box i {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
}

.search-box input {
  width: 100%;
  padding: 0.8rem 1rem 0.8rem 2.5rem;
  border: 1px solid #eee;
  border-radius: 25px;
  transition: all 0.3s ease;
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
  border: 1px solid #eee;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.filter-select:focus,
.price-filter input:focus {
  border-color: #4caf50;
  outline: none;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
}

.product-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.product-image {
  position: relative;
  height: 250px;
  overflow: hidden;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
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
  background: rgba(0, 0, 0, 0.4);
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
  background: #4caf50;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  transform: translateY(20px);
  transition: all 0.3s ease;
}

.product-card:hover .cart-btn {
  transform: translateY(0);
}

.cart-btn:hover {
  background: #45a049;
}

.product-info {
  padding: 1.5rem;
}

.product-category {
  margin-bottom: 0.5rem;
}

.category-tag {
  display: inline-block;
  padding: 0.3rem 0.8rem;
  background: #e8f5e9;
  color: #4caf50;
  border-radius: 15px;
  font-size: 0.8rem;
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
