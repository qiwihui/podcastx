import axios from 'axios'
const state = {
  user: null
}
const getters = {
  isAuthenticated: state => !!state.user,
  StateUser: state => state.user
}
const actions = {
  async Login ({ commit }, User) {
    await axios.post('Login', User)
    await commit('setUser', User.get('username'))
  },
  async Register ({ dispatch }, form) {
    await axios.post('register', form)
    let UserForm = new FormData()
    UserForm.append('username', form.username)
    UserForm.append('password', form.password)
    await dispatch('Login', UserForm)
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
  logout (state) {
    state.user = null
  }
}
export default {
  state,
  getters,
  actions,
  mutations
}
