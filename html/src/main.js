// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueGtag from 'vue-gtag'
import VueAPlayer from 'vue-aplayer'
import axios from 'axios'

axios.defaults.withCredentials = true
// axios.defaults.baseURL = "https://podcastx.qiwihui.com/"

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      store.dispatch('Logout')
      return router.push('/login')
    }
  }
})

VueAPlayer.disableVersionBadge = true

Vue.config.productionTip = false
// google tag manager
Vue.use(VueGtag, {
  config: { id: 'G-T9V2FSEG0Q' }
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next()
      return
    }
    next('/login')
  }
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
