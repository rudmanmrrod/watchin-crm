export default{
  state: {
    user: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')):null
  },
  mutations: {
    ['LOGIN'] (state,payload){
      localStorage.setItem('user',JSON.stringify(payload))
      state.user = JSON.stringify(payload)
    }
  },
  actions: {
    login({commit},token){
      commit('LOGIN',token)
    }
  }
}