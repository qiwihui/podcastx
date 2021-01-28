<template>
  <div>
    <div>
      <nav-bar></nav-bar>
    </div>
    <div class="audio-player">
      <aplayer autoplay :music=podcast :list=podcasts v-if="article_info.status==1" />
      <span v-if="loading==true"><spinner size="40"></spinner></span>
    </div>
  </div>
</template>

<script>
import Spinner from 'vue-simple-spinner'
import NavBar from '@/components/NavBar'
import Aplayer from 'vue-aplayer'
export default {
  name: 'Podcast',
  data () {
    return {
      msg: 'Podcast X',
      error_message: '',
      loading: false,
      searchUrl: '',
      articleId: this.$route.params.podcastId,
      article_info: {
        title: '',
        author: '',
        url: '',
        audios: [],
        status: 0
      },
      podcast: {
        title: '',
        artist: '',
        src: '',
        list: []
      },
      podcasts: []
    }
  },
  mounted () {
    this.fetchArticle()
  },
  methods: {
    resetArticle () {
      this.article_info = {
        title: '',
        author: '',
        url: '',
        audios: [],
        status: 0
      }
      this.podcasts = []
      this.podcast = {
        title: '',
        artist: '',
        src: '',
        list: []
      }
    },
    fetchArticle () {
      this.loading = true
      fetch('/api/articles/' + this.articleId)
        .then(res => res.json())
        .then(data => {
          if (data.status === 1) {
            this.article_info = data.data
            if (this.article_info.status === 1) {
              this.loading = false
              for (let p in this.article_info.audios) {
                this.podcasts.push({
                  title: this.article_info.title,
                  artist: this.article_info.author,
                  src: this.article_info.audios[p]
                })
              }
              this.podcast = this.podcasts[0]
            } else {
              setTimeout(this.fetchArticle, 3000)
            }
          }
        })
        .catch(() => {
        })
        .finally(() => {
          this.loading = false
        })
    }
  },
  components: {
    NavBar,
    Aplayer,
    Spinner
  }
}
</script>

<style scoped>

h1,
h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}

.audio-player {
  width: 95%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

</style>
