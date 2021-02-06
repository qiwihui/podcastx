<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <div class="audio-player">
      <podcast-item
        :podcast="article"
        :show-delete="false"
        :show-select="true"
      ></podcast-item>
    </div>
  </div>
</template>

<script>
import PodcastItem from '@/components/PodcastItem'
import NavBar from '@/components/NavBar'
import PodcastPlayer from '@/components/PodcastPlayer'
import AudioPlayer from '@/components/AudioPlayer'
export default {
  name: 'Podcast',
  data () {
    return {
      error_message: '',
      loading: false,
      article: {}
    }
  },
  mounted () {
    this.getArticle()
  },
  methods: {
    async getArticle () {
      let self = this
      this.loading = true
      await this.$http
        .get('/api/articles/' + this.$route.params.podcastId)
        .then(response => {
          self.article = response.data.data.article
        })
        .catch(() => {
        }).finally(() => {
          self.loading = false
        })
    }
  },
  components: {
    NavBar,
    PodcastPlayer,
    AudioPlayer,
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

.audio-player {
  width: 100%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

</style>
