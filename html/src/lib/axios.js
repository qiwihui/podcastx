import router from '../router'
import store from '../store'
import axios from 'axios'

axios.defaults.withCredentials = true
// axios.defaults.baseURL = 'https://podcastx.qiwihui.com/'

axios.interceptors.request.use(config => {
  let accessToken = store.getters.stateAccessToken
  if (accessToken) {
    config.headers = {
      ...config.headers,
      Authorization: `Bearer ${accessToken}`
    }
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
  async function (error) {
    if (error) {
      console.error('error occurred.')
      const originalRequest = error.config

      if (error.response.status in [401, 422]) {
        // originalRequest._retry = true
        await store.dispatch('Logout')
        return router.push('/login')
      }

      if (error.response.status in [403] && !originalRequest._retry) {
        originalRequest._retry = true
        const accessToken = await store.dispatch('RefreshAccessToken')
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken
        return axios(originalRequest)
      }
    }
  }
)

export default axios
