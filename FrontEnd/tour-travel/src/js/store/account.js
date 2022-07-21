export default {
    namespaced: true,
    state: {
        currentUser: null
    },
    getters: {
        currentUser: state => state.currentUser
    },
    mutations: {
        setAccounts(state, user) {
            state.currentUser = user
        }
    }
}