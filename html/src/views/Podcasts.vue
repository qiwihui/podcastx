<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <!-- <h2 class="podcast-list">添加</h2> -->
    <search class="search-container mb-4" :endpoint='"/api/articles"' @articleChanged="updateArticle"></search>
    <section class="audio-player mb-4">
      <podcast-player
        autoplay
        theme="pic"
        show-lrc
        :articleId="articleId"
        v-if="articleId != ''"
      ></podcast-player>
    </section>
    <h2 class="podcast-list">播客列表</h2>
    <div class="podcast-cat">
      <div class="audio-list">
        <div class="audio-item">
          <podcast-item
            v-for="article in articles"
            :key="article._id"
            :podcast="article"
          ></podcast-item>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import PodcastItem from '@/components/PodcastItem'
import PodcastPlayer from '@/components/PodcastPlayer'
import Search from '@/components/Search'
export default {
  name: 'Podcasts',
  data () {
    return {
      error_message: '',
      loading: false,
      articles: [],
      articleId: ''
    }
  },
  mounted () {
    this.getArticles()
  },
  methods: {
    getArticles () {
      let self = this
      this.$http
        .get('/api/articles')
        .then(response => {
          let data = response.data
          self.articles = data.data.articles
          console.log(self.articles)
        })
        .catch(() => {})
    },
    updateArticle (e) {
      this.articleId = e
    }
  },
  components: {
    NavBar,
    PodcastItem,
    Search,
    PodcastPlayer
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

.mb-4 {
  margin-bottom: 40px;
}

.podcast-cat {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.podcast-list {
  text-align: left;
  margin-bottom: 20px;
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
