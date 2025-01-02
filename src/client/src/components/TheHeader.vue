<template>
  <header class="site-header" :class="{ 'header-scrolled': isScrolled }">
    <nav class="navbar navbar-expand-lg">
      <div class="container">
        <router-link class="navbar-brand" to="/" data-aos="fade-right">
          <i class="fas fa-leaf brand-leaf"></i>
          GreenOasis
        </router-link>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto" data-aos="fade-left">
            <li class="nav-item" v-for="(item, index) in menuItems" :key="index">
              <router-link :to="item.path" class="nav-link hvr-underline-from-center">
                <i :class="item.icon"></i>
                {{ item.title }}
              </router-link>
            </li>
          </ul>

          <div class="header-actions" data-aos="fade-left" data-aos-delay="100">
            <button class="btn search-btn hvr-grow">
              <i class="fas fa-search"></i>
            </button>
            <button class="btn cart-btn hvr-grow" @mouseenter="animateCart">
              <i class="fas fa-shopping-cart"></i>
              <span class="cart-count" v-if="cartCount">{{ cartCount }}</span>
            </button>
            <router-link to="/account" class="btn account-btn hvr-grow">
              <i class="fas fa-user"></i>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { gsap } from 'gsap'
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'TheHeader',
  setup() {
    const isScrolled = ref(false)
    const cartCount = ref(0) // Replace with your cart state management

    const menuItems = [
      { title: 'Home', path: '/', icon: 'fas fa-home' },
      { title: 'Plants', path: '/plants', icon: 'fas fa-seedling' },
      { title: 'Categories', path: '/categories', icon: 'fas fa-th-large' },
      { title: 'About', path: '/about', icon: 'fas fa-leaf' },
      { title: 'Contact', path: '/contact', icon: 'fas fa-envelope' }
    ]

    const handleScroll = () => {
      isScrolled.value = window.scrollY > 50
    }

    const animateCart = () => {
      gsap.to('.cart-btn', {
        scale: 1.2,
        duration: 0.3,
        yoyo: true,
        repeat: 1
      })
    }

    onMounted(() => {
      window.addEventListener('scroll', handleScroll)
      gsap.from('.brand-leaf', {
        rotate: 360,
        duration: 2,
        ease: 'power2.out'
      })
    })

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    return {
      isScrolled,
      menuItems,
      cartCount,
      animateCart
    }
  }
}
</script>

<style scoped>
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}

.header-scrolled {
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
}

.navbar {
  padding: 1rem 0;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2c3e50;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.brand-leaf {
  color: #4CAF50;
}

.nav-link {
  color: #2c3e50;
  font-weight: 500;
  padding: 0.5rem 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.header-actions {
  display: flex;
  gap: 1rem;
  margin-left: 2rem;
}

.btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  border: none;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
}

.cart-count {
  position: absolute;
  top: -5px;
  right: -5px;
  background: #4CAF50;
  color: white;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  font-size: 0.8rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 991px) {
  .header-actions {
    margin: 1rem 0;
    justify-content: center;
  }
}
</style>
