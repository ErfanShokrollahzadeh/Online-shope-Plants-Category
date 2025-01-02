<template>
  <div class="main-layout">
    <!-- Add header component -->
    <TheHeader />

    <!-- Main content with fade transition -->
    <main class="main-content">
      <transition name="fade" mode="out-in">
        <router-view></router-view>
      </transition>
    </main>

    <!-- Add footer component -->
    <TheFooter />
  </div>
</template>

<script>
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'

export default {
  name: 'MainLayout',
  components: {
    TheHeader,
    TheFooter
  }
}
</script>

<style scoped>
.main-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding-top: 80px; /* Adjust based on header height */
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
}

/* Fade transition animations */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
