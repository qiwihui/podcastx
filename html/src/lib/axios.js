import router from '../router'
import store from '../store'
import axios from 'axios'

axios.defaults.withCredentials = true
// axios.defaults.baseURL = 'https://podcastx.qiwihui.com/'

axios.interceptors.request.use(config => {
  config.headers = {
    ...config.headers,
    Authorization: `Bearer ${store.getters.StateToken}`
  }
  return config
})

axios.interceptors.response.use(
  response => {
    if (
      response.status &&
      !(response.status >= 200 && response.status < 300)
    ) {
      throw new Error()
    }
    return response
  },
  error => {
    if (error) {
      const originalRequest = error.config

      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true
        store.dispatch('Logout')
        return router.push('/login')
      }
    }
  }
)

export default axios
