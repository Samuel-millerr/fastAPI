<script setup>
import Header from './components/Header.vue'
</script>

<template>
  <Header/>
  <main>
    <RouterView/>
  </main>
</template>

<style scoped>
main {
  display: grid;
  grid-template-rows: 2f 20px;
  gap: 0.25rem;
  width: 100%;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
</style>
