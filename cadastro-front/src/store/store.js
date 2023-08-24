const store = createStore({
    state:{
        view: "Home",
        user: JSON.parse(localStorage.getItem('user'))
    },
    mutations: {
        changeView (state, view) {
            state.view = view
        },
        login (state, user) {
            state.user = user
        },
        logout(state) {
            localStorage.removeItem('user')
            state.user = null
        }
    }
})

export default store