<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap/dist/css/bootstrap.min.css'

export default {
  name: 'App'
}
</script>

<style>
@import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css';

#app {
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

/* Global styles */
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #4CAF50;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #45a049;
}

/* Animation Classes */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Hover Effects */
.hover-grow {
  transition: transform 0.3s ease;
}

.hover-grow:hover {
  transform: scale(1.05);
}

.hover-shadow {
  transition: box-shadow 0.3s ease;
}

.hover-shadow:hover {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

/* Custom Animation Keyframes */
@keyframes floatAnimation {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.float-element {
  animation: floatAnimation 3s ease-in-out infinite;
}

/* GSAP Classes */
.gsap-reveal {
  opacity: 0;
  visibility: hidden;
}

/* Smooth Transitions */
.page-enter-active,
.page-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Global Animation Settings */
* {
  transition: all 0.3s ease-in-out;
}
</style>
