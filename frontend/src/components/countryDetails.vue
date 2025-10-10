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
    console.log(country.value)
}

async function getStatistic(countryId) {
    const response = await fetch(`http://localhost:8000/api/v1/statistics/${countryId}`);
    const data = await response.json();
    statistic.value = data;
    console.log(statistic.value)
}

onMounted(() => {
    getCountry(id.value),
    getStatistic(id.value);
})


</script>

<template>
    <section id="country-conteiner">
        <section id="country-info-conteiner">
            <h1> {{country.official_name}}</h1>
            <!-- Ideal nessa parte é realizar a criação de um componente que recebe props, atualização futura -->
            <div class="info-conteiner">
                <img src="../assets/icons/coin.svg"/>
                <p> {{ country.coin_code }} </p>
            </div>
            <div class="info-conteiner">
                <img src="../assets/icons/capital.svg"/>
                <p> {{ country.capital }} </p>
            </div>
            <div class="info-conteiner">
                <img src="../assets/icons/continent.svg"/>
                <p> {{ country.continent }} </p>
            </div>
            <div class="info-conteiner">
                <img src="../assets/icons/demonym.svg"/>
                <p> {{ country.demonym }} </p>
            </div>
            <div class="info-conteiner">
                <img src="../assets/icons/language.svg"/>
                <p> {{ country.primary_language }} </p>
            </div>
        </section>
        <aside id="country-statistics-conteiner">
            <img :src="country.flag" alt="Bandeira do país" v-if="country.flag" id="country-flag"/>
            <div>
                <p> Área: {{ statistic.area }} km²</p>
                <p> GPD: $ {{ statistic.gdp_usd }} </p>
                <p> GPR Per Capita: {{ statistic.gdp_per_capita }}</p>
                <p> População: {{ statistic.population }}</p>
                <p> IDH: {{ statistic.hdi }}</p>
                <p> Expectativa de vida: {{ statistic.life_expectancy }} anos </p>
            </div>
        </aside>
    </section>
</template>

<style>
#country-conteiner {
    display: flex;
    justify-content: space-around;
    width: 100%;
    gap: 1rem;
    padding: 2rem 28rem 2rem 28rem;
}

#country-info-conteiner {
    display: flex;
    flex-direction: column;
    padding: 0.5rem;
    gap: 0.5rem;
}

#country-info-conteiner h1 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 500;
    font-size: 36px
}

.info-conteiner {
    display: flex;
    align-items: center;
    text-align: center;
    font-size: 22px;
    font-weight: 500;
    gap: 0.5rem;
}

.info-conteiner img {
    min-width: 2.1rem;
}

/* Estilização da lateral da página - bandeira e estatisticas do país*/
#country-statistics-conteiner {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
    align-items: center;
    border: 1px solid black;
    padding: 1rem;
    box-shadow: 0 0 3px 2px grey;
}

#country-statistics-conteiner div{
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    font-size: 18px;
    font-weight: 600;
}


#country-flag {
    width: 17rem;
    border: 1px solid black;
}
</style>