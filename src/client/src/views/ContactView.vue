<template>
  <div class="contact-view">
    <div class="container py-5">
      <h1 class="mb-4" data-aos="fade-up">Contact Us</h1>
      <div class="row g-4">
        <div class="col-lg-6" data-aos="fade-right">
          <form @submit.prevent="handleSubmit" class="contact-form p-4 bg-white rounded shadow-lg">
            <div class="mb-3">
              <label class="form-label">Name</label>
              <input type="text" class="form-control" v-model="form.name" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input type="email" class="form-control" v-model="form.email" required>
            </div>
            <div class="mb-3">
              <label class="form-label">Message</label>
              <textarea class="form-control" rows="5" v-model="form.message" required></textarea>
            </div>
            <button type="submit" class="btn btn-success w-100">Send Message</button>
          </form>
        </div>
        <div class="col-lg-6" data-aos="fade-left">
          <div class="contact-info p-4 bg-white rounded shadow-lg">
            <h3>Get in Touch</h3>
            <p>Have questions? We'd love to hear from you.</p>
            <div class="info-item">
              <i class="fas fa-map-marker-alt"></i>
              <p>123 Green Street, Plant City, PC 12345</p>
            </div>
            <div class="info-item">
              <i class="fas fa-phone"></i>
              <p>+1 (234) 567-8900</p>
            </div>
            <div class="info-item">
              <i class="fas fa-envelope"></i>
              <p>contact@greenoasis.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactView',
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: ''
      }
    }
  },
  methods: {
    handleSubmit() {
      // Handle form submission
      console.log('Form submitted:', this.form)
    }
  }
}
</script>

<style scoped>
.info-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.info-item i {
  color: #4CAF50;
  font-size: 1.2rem;
}
</style>
