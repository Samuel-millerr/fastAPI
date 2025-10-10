<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
    <header id="site-header">
        <RouterLink to="/" id="router-link"> CountryAPI </RouterLink>
    </header>
</template>

<style scoped>
#site-header {
  display: flex;
  justify-content: center;
  width: 100%;
  background-color: #2c3e50;
  color: white;
  padding: 2rem 2rem 2rem 3rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#router-link {
    font-size: 36px;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
    color: white;
}
</style>