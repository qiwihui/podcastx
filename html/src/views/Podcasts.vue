<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <div class="audio-list">
      <div class="audio-item">
        <podcast-item v-for='article in articles' :key='article._id' :podcast='article'></podcast-item>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import PodcastPlayer from '@/components/PodcastPlayer'
import PodcastItem from '@/components/PodcastItem'
export default {
  name: 'Podcasts',
  data () {
    return {
      error_message: '',
      loading: false,
      articles: []
    }
  },
  mounted () {
    this.getArticles()
  },
  methods: {
    getArticles () {
      let self = this
      this.$http.get('/api/articles').then(response => {
        let data = response.data
        self.articles = data.data.articles
        console.log(self.articles)
      }).catch(() => {})
    }
  },
  components: {
    NavBar,
    PodcastPlayer,
    PodcastItem
  }
}
</script>

<style scoped>
.container {
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50px;
  padding: 0 15px;
}

header {
  margin-bottom: 3rem;
}

a {
  color: #42b983;
}

.audio-list {
  width: 100%;
  max-width: 960px;
  margin: 0 auto 30px auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.audio-item {
  width: 100%;
}
</style>
