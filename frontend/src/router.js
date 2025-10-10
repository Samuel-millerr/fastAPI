import { createMemoryHistory, createRouter } from "vue-router";

import Countries from "./components/countries.vue";
import CountryDetails from "./components/countryDetails.vue";

const routes = [
    {path:'/', component: Countries},
    {path:'/countryDetails/:id', name: 'CountryDetails', component: CountryDetails}
]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
})

export default router