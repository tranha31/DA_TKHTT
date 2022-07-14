import Vue from "vue"
import Vuex from 'vuex'
import VuexPersistence from "vuex-persist"
import account from "@/js/store/account"

const vuexLocal = new VuexPersistence({
    storage: window.localStorage
})

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        account
    },
    plugins: [vuexLocal.plugin]
})