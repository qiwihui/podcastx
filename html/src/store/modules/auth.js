import axios from '@/lib/axios'

const state = {
  user: null,
  token: null
}
const getters = {
  isAuthenticated: state => !!state.user,
  StateUser: state => state.user,
  StateToken: state => state.token
}
const actions = {
  async Login ({ commit }, User) {
    return axios.post('/api/login', User).then((response) => {
      let data = response.data
      if (data.status === 1) {
        commit('setToken', data.token)
        commit('setUser', User.username)
      }
      return data
    })
  },
  async Register ({ dispatch }, userObject) {
    return axios.post('/api/register', userObject).then((response) => {
      let data = response.data
      if (data.status === 1) {
        return dispatch('Login', userObject)
      } else {
        return data
      }
    }).catch((error) => {
      console.error(error)
    })
  },
  async Logout ({commit}) {
    let user = null
    commit('logout', user)
  }
}
const mutations = {
  setUser (state, username) {
    state.user = username
  },
  setToken (state, token) {
    state.token = token
  },
  logout (state) {
    state.user = null
    state.token = null
  }
}
export default {
  state,
  getters,
  actions,
  mutations
}
