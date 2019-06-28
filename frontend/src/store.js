import Vue from 'vue'
import Vuex from 'vuex'
import users from './store/users.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users: users
  },
  state: {

  },
  mutations: {

  },
  actions: {

  }
})
