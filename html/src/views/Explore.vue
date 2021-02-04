<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <h2 class="podcast-list">播客列表</h2>
    <div class="podcast-cat">
      <div class="audio-list">
        <div class="audio-item">
          <podcast-item
            v-for="article in articles"
            :key="article.id"
            :podcast="article"
            :show-delete="false"
          ></podcast-item>
        </div>
      </div>
    </div>
    <div class="more-podcasts">
      <span v-if="loading==true"><spinner size="35"></spinner></span>
      <span v-else @click="getArticles">加载更多</span>
    </div>
  </div>
</template>

<script>
import Spinner from 'vue-simple-spinner'
import NavBar from '@/components/NavBar'
import PodcastItem from '@/components/PodcastItem'
export default {
  name: 'Explore',
  data () {
    return {
      loading: false,
      articles: [],
      endpoint: '/api/explore/articles',
      page: -1,
      per_page: 10
    }
  },
  mounted () {
    this.getArticles()
    this.scroll()
  },
  methods: {
    async getArticles () {
      let self = this
      this.loading = true
      this.page = this.page + 1
      await this.$http
        .get(this.endpoint, {params: {page: this.page, per_page: this.per_page}})
        .then(response => {
          let data = response.data
          self.articles = self.articles.concat(data.data.articles)
        })
        .catch(() => {
        }).finally(() => {
          self.loading = false
        })
    },
    scroll () {
      let self = this
      window.onscroll = () => {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight ===
          document.documentElement.offsetHeight
        if (bottomOfWindow) {
          self.getArticles()
        }
      }
    }
  },
  components: {
    NavBar,
    Spinner,
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

.podcast-list {
  text-align: center;
  margin-bottom: 20px;
}

.audio-list {
  width: 100%;
  max-width: 960px;
  margin: 0 auto 30px auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.audio-item {
  width: 100%;
}

.more-podcasts {
  width: 100%;
  max-width: 960px;
  margin: 0 auto 30px auto;
  display: flex;
  align-content: flex-start;
}

.more-podcasts span {
  margin: 0 auto;
}
</style>
