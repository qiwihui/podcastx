// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueGtag from 'vue-gtag'
import VueAPlayer from 'vue-aplayer'

VueAPlayer.disableVersionBadge = true

Vue.config.productionTip = false
// google tag manager
Vue.use(VueGtag, {
  config: { id: 'G-T9V2FSEG0Q' }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
