import axios from '@/lib/axios'

const state = {
  user: null,
  access_token: null,
  refresh_token: null
}
const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
  stateAccessToken: state => state.access_token,
  stateRefreshToken: state => state.refresh_token
}
const actions = {
  async Login ({ commit }, User) {
    return axios.post('/api/login', User).then((response) => {
      let data = response.data
      if (data.status === 1) {
        commit('setAccessToken', data.data.access_token)
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
  },
  async RefreshAccessToken ({commit}) {
    let refreshToken = getters.stateRefreshToken
    let accessToken = await axios.post('/api/register', {'refresh_token': refreshToken}).then(response => {
      let data = response.data
      if (data.status === 1) {
        return data.access_token
      } else {
        return ''
      }
    })
    commit('setRefreshToken', accessToken)
  }
}
const mutations = {
  setUser (state, username) {
    state.user = username
  },
  setAccessToken (state, token) {
    state.access_token = token
  },
  setRefreshToken (state, token) {
    state.refresh_token = token
  },
  logout (state) {
    state.user = null
    state.access_token = null
    state.refresh_token = null
  }
}
export default {
  state,
  getters,
  actions,
  mutations
}
