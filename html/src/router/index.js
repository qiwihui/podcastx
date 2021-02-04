import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Podcast from '@/views/Podcast'
import Podcasts from '@/views/Podcasts'
import EmbedPodcast from '@/views/EmbedPodcast'
import Login from '@/views/Login'
import Register from '@/views/Register'
import Explore from '@/views/Explore'

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
      path: '/explore',
      name: 'Explore',
      component: Explore
    },
    {
      path: '/podcasts/:podcastId',
      name: 'Podcast',
      component: Podcast
    },
    {
      path: '/podcasts',
      name: 'Podcasts',
      component: Podcasts,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/embed/:podcastId',
      name: 'EmbedPodcast',
      component: EmbedPodcast
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
