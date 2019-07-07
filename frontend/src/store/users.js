export default{
  state: {
    user: localStorage.getItem('user')
  },
  mutations: {
    ['LOGIN'] (state,payload){
      state.user = payload
    }
  },
  actions: {
    login({commit},token){
      commit('LOGIN',token)
    }
  }
}