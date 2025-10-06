<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';

const country = ref([])
const statistic = ref([]);
const route = useRoute()
const id = computed(() => route.params.id)

async function getCountry(countryId) {
    const response = await fetch(`http://localhost:8000/api/v1/countries/${countryId}`);
    const data = await response.json();
    country.value = data;
}

async function getStatistic(countryId) {
    const response = await fetch(`http://localhost:8000/api/v1/statistics/${countryId}`);
    const data = await response.json();
    statistic.value = data;
}

onMounted(() => {
    getCountry(id.value),
    getStatistic(id.value);
})

defineExpose({
    country,
    statistic,
})
</script>

<template>
    <h1> {{country.common_name}} - {{statistic.area}}</h1>
</template>
