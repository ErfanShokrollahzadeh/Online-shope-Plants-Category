<template>
  <footer class="site-footer">
    <div class="footer-leaves">
      <i class="fas fa-leaf leaf" v-for="n in 20" :key="n"></i>
    </div>
    
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4" data-aos="fade-right">
          <div class="footer-brand">
            <i class="fas fa-leaf brand-leaf"></i>
            <h3>GreenOasis</h3>
          </div>
          <p class="footer-description">
            Bringing nature's beauty to your doorstep. Discover our curated collection
            of plants and flowers to transform your space into a green paradise.
          </p>
          <div class="social-links">
            <a href="#" class="social-link hvr-float" v-for="(social, index) in socials" :key="index">
              <i :class="social.icon"></i>
            </a>
          </div>
        </div>

        <div class="col-lg-4" data-aos="fade-up">
          <h4 class="footer-title">Quick Links</h4>
          <ul class="footer-links">
            <li v-for="(link, index) in quickLinks" :key="index">
              <router-link :to="link.path" class="hvr-forward">
                <i :class="link.icon"></i>
                {{ link.title }}
              </router-link>
            </li>
          </ul>
        </div>

        <div class="col-lg-4" data-aos="fade-left">
          <h4 class="footer-title">Newsletter</h4>
          <p>Subscribe to receive updates, access to exclusive deals, and more.</p>
          <form @submit.prevent="subscribeNewsletter" class="newsletter-form">
            <div class="input-group">
              <input 
                type="email" 
                class="form-control" 
                placeholder="Enter your email"
                v-model="email"
              >
              <button class="btn btn-success hvr-grow" type="submit">
                <i class="fas fa-paper-plane"></i>
              </button>
            </div>
          </form>
        </div>
      </div>

      <div class="footer-bottom" data-aos="fade-up">
        <p>&copy; {{ new Date().getFullYear() }} GreenOasis. All rights reserved.</p>
        <div class="payment-methods">
          <i class="fab fa-cc-visa"></i>
          <i class="fab fa-cc-mastercard"></i>
          <i class="fab fa-cc-paypal"></i>
          <i class="fab fa-cc-apple-pay"></i>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import { ref } from 'vue'
import { gsap } from 'gsap'

export default {
  name: 'TheFooter',
  setup() {
    const email = ref('')

    const socials = [
      { icon: 'fab fa-facebook', url: '#' },
      { icon: 'fab fa-instagram', url: '#' },
      { icon: 'fab fa-twitter', url: '#' },
      { icon: 'fab fa-pinterest', url: '#' }
    ]

    const quickLinks = [
      { title: 'About Us', path: '/about', icon: 'fas fa-info-circle' },
      { title: 'Plant Care Guide', path: '/care-guide', icon: 'fas fa-book-open' },
      { title: 'Shipping Policy', path: '/shipping', icon: 'fas fa-truck' },
      { title: 'FAQs', path: '/faqs', icon: 'fas fa-question-circle' },
      { title: 'Contact Us', path: '/contact', icon: 'fas fa-envelope' }
    ]

    const subscribeNewsletter = () => {
      // Handle newsletter subscription
      console.log('Subscribed:', email.value)
      email.value = ''
    }

    // Animate floating leaves
    gsap.to('.leaf', {
      y: -20,
      rotation: 360,
      duration: 2,
      ease: 'power1.inOut',
      stagger: {
        each: 0.3,
        repeat: -1,
        yoyo: true
      }
    })

    return {
      email,
      socials,
      quickLinks,
      subscribeNewsletter
    }
  }
}
</script>

<style scoped>
.site-footer {
  background: linear-gradient(135deg, #1a1a1a, #2c3e50);
  color: white;
  padding: 4rem 0 2rem;
  position: relative;
  overflow: hidden;
}

.footer-leaves {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  pointer-events: none;
}

.leaf {
  position: absolute;
  color: rgba(255, 255, 255, 0.1);
  font-size: 1.5rem;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.brand-leaf {
  color: #4CAF50;
  font-size: 2rem;
}

.footer-description {
  color: #aaa;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.footer-title {
  font-size: 1.25rem;
  margin-bottom: 1rem;
}

.footer-links {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 0.5rem;
}

.footer-links a {
  color: white;
  text-decoration: none;
}

.footer-links a:hover {
  text-decoration: underline;
}

.newsletter-form {
  display: flex;
  gap: 0.5rem;
}

.input-group {
  display: flex;
  width: 100%;
}

.input-group input {
  flex: 1;
}

.input-group button {
  flex-shrink: 0;
}

.footer-bottom {
  text-align: center;
  margin-top: 2rem;
}

.payment-methods {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-top: 1rem;
}

.payment-methods i {
  font-size: 1.5rem;
  color: white;
}
</style>
