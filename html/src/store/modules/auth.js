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
    await axios.post('/api/login', User)
    await commit('setUser', User.get('username'))
  },
  async Register ({ dispatch }, form) {
    let object = {}
    form.forEach((value, key) => { object[key] = value })

    return axios.post('/api/register', object).then((response) => {
      let data = response.data
      if (data.status === 1) {
        let UserForm = new FormData()
        UserForm.append('username', form.username)
        UserForm.append('password', form.password)
        return dispatch('Login', UserForm)
      } else {
        return data
      }
    }).catch((error) => {
      console.error(error)
    })

    // let UserForm = new FormData()
    // UserForm.append('email', form.email)
    // UserForm.append('username', form.username)
    // UserForm.append('password', form.password)
    // await dispatch('Login', UserForm)
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
