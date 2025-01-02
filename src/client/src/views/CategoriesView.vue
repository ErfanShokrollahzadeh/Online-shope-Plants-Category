<template>
  <div class="categories-view">
    <div class="container py-5">
      <h1 class="mb-4" data-aos="fade-up">Plant Categories</h1>
      <div class="row g-4">
        <div class="col-md-4" v-for="category in categories" :key="category.id" data-aos="fade-up">
          <div class="category-card">
            <img :src="category.image" :alt="category.name" class="category-image">
            <div class="category-content">
              <h3>{{ category.name }}</h3>
              <p>{{ category.description }}</p>
              <router-link :to="{ name: 'products', query: { category: category.id }}" 
                         class="btn btn-outline-success">
                View Plants
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CategoriesView',
  data() {
    return {
      categories: [
        {
          id: 1,
          name: 'Indoor Plants',
          description: 'Perfect for home decoration',
          image: 'https://images.unsplash.com/photo-1545241047-6083a3684587'
        },
        {
          id: 2,
          name: 'Outdoor Plants',
          description: 'Beautify your garden',
          image: 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b'
        },
        {
          id: 3,
          name: 'Succulents',
          description: 'Low maintenance plants',
          image: 'https://images.unsplash.com/photo-1446071103084-c257b5f70672'
        }
      ]
    }
  }
}
</script>

<style scoped>
.category-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0,0,0,0.2);
}

.category-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.category-content {
  padding: 1.5rem;
}
</style>
