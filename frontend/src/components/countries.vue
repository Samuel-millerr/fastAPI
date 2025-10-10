<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const countries = ref([]);
const router = useRouter()

async function getCountries() {
    const response = await fetch("http://localhost:8000/api/v1/countries/");
    const data = await response.json();
    countries.value = data;
}

onMounted(() => {
    getCountries()
})

function goToStatistics(countryId) {
  router.push({ name: 'CountryDetails', params: { id: countryId } });
}
</script>

<template>
    <section>
        <h1>Lista de Países</h1>
        <table>
            <thead>
                <th> ID </th>
                <th> País </th>
                <th> Capital </th>
                <th> Língua </th>
                <th> Gentílico </th>
            </thead>
            <tr v-for="country in countries" :key="country.id_country" @click="goToStatistics(country.id_country)">
                <td> {{ country.id_country }} </td>
                <td> {{ country.common_name }} </td>
                <td> {{ country.capital }} </td>
                <td> {{ country.primary_language }} </td>
                <td> {{ country.demonym }} </td>
            </tr>
        </table>
      </section>
</template>

<style scoped>
article {
  padding: 2rem;
}

section {padding: 2rem;}

section h1 {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 30px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 0.5rem;
  font-family: Arial, sans-serif;
  font-size: 0.85rem; 
  cursor: pointer;
}

table th,
table td {
  border: 1px solid #ccc;
  padding: 6px 8px;
  font-size: 20px;
  text-align: left;
  vertical-align: top;
}

table th {
  background-color: #2c3e50;
  color: white;
  font-weight: 600;
  font-size: 18px;
  padding: 0.5rem;
}

table tr:hover {
  background-color: #f1f1f1;
}

table td {
  color: #333;
  line-height: 1.3;
}

h1 {
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>