import Vue from 'vue'
import Vuex from 'vuex'
import users from './store/users.js'
import routes from './store/backroutes.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    route: routes,
    users: users
  },
  state: {
    snackbar:{
      value: false,
      type: '',
      text: ''
    }
  },
  mutations: {
    ['SET_MSG'] (state,payload){
      state.snackbar = payload
    }
  },
  actions: {
    setMessage({commit},obj){
      commit('SET_MSG',obj)
    }
  }
})
