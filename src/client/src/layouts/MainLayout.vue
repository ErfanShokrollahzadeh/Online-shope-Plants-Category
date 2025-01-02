<template>
  <div class="main-layout">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <router-link class="navbar-brand" to="/">Plant Shop</router-link>
      </div>
    </nav>
    
    <main class="container py-4">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'MainLayout'
}
</script>
