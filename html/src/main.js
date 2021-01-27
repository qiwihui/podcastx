// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueGtag from 'vue-gtag'

Vue.config.productionTip = false
// google tag manager
Vue.use(VueGtag, {
  config: { id: 'G-S66VR7JQ5Y' }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
