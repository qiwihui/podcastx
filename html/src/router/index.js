import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Podcast from '@/views/Podcast'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/podcasts/:podcastId',
      name: 'Podcast',
      component: Podcast
    }
  ]
})
