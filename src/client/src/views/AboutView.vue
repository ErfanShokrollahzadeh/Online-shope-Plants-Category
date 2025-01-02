<template>
  <div class="about-view">
    <div class="container py-5">
      <h1 class="mb-4" data-aos="fade-up">About GreenOasis</h1>
      <div class="row">
        <div class="col-lg-6" data-aos="fade-right">
          <p class="lead">Welcome to GreenOasis, your premier destination for quality plants and gardening supplies.</p>
          <p>We are passionate about bringing nature into your living spaces and helping you create your own green paradise.</p>
          <div class="features mt-4">
            <div class="feature-item" data-aos="fade-up" data-aos-delay="100">
              <i class="fas fa-leaf"></i>
              <h4>Quality Plants</h4>
              <p>Carefully selected and nurtured plants for your home.</p>
            </div>
            <div class="feature-item" data-aos="fade-up" data-aos-delay="200">
              <i class="fas fa-truck"></i>
              <h4>Fast Delivery</h4>
              <p>Safe and quick delivery to your doorstep.</p>
            </div>
          </div>
        </div>
        <div class="col-lg-6" data-aos="fade-left">
          <div class="about-image">
            <img src="https://images.unsplash.com/photo-1416879595882-3373a0480b5b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" 
                 alt="About GreenOasis" 
                 class="img-fluid rounded shadow-lg">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>

<style scoped>
.about-view {
  padding: 2rem 0;
}

.feature-item {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

.feature-item i {
  color: #4CAF50;
  font-size: 2rem;
  margin-bottom: 1rem;
}
</style>
