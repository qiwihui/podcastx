<template>
  <div>
    <div>
      <nav-bar></nav-bar>
    </div>
    <div class="search-container">
      <h1>{{ msg }}</h1>
      <div class="input">
        <input
          v-model="searchUrl"
          type="text"
          placeholder="Article URL"
          class="url-input"
        />
        <span class="search" @click="extractUrl">
          <span>Analyse</span>
        </span>
      </div>
      <div class="input-message" v-if="error_message != ''">
        <span>{{ error_message }}</span>
      </div>
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
import FooterNote from '@/components/FooterNote'
import Aplayer from 'vue-aplayer'
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Podcast X',
      error_message: '',
      loading: false,
      searchUrl: '',
      articleId: '',
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
    extractUrl () {
      this.resetArticle()
      this.loading = true
      this.error_message = ''
      let data = {url: this.searchUrl}
      fetch('/api/articles', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(res => res.json())
        .then(data => {
          if (data.status === 1) {
            this.articleId = data.data.id
            this.fetchArticle()
            // this.fetchArticleAudios()
          } else {
            this.error_message = '解析错误，请重试'
          }
          this.loading = false
        })
        .catch(() => {
          this.error_message = '请求错误，请稍后重试'
          this.loading = false
        //   console.error(error)
        })
        .finally(() => { this.loading = false })
    },
    fetchArticle () {
      fetch('/api/articles/' + this.articleId)
        .then(res => res.json())
        .then(data => {
          if (data.status === 1) {
            this.article_info = data.data
            if (this.article_info.status === 1) {
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
        .finally(() => {})
    },
    fetchArticleAudios () {
      fetch('/api/articles/' + this.articleId + '/audios')
        .then(res => res.json())
        .then(data => {
          if (data.status === 1) {
            this.article_info.audios = data.data.audios
            for (let p in this.article_info.audios) {
              this.podcasts.push({
                title: this.article_info.title,
                artist: this.article_info.author,
                src: this.article_info.audios[p]
              })
            }
            this.podcast = this.podcasts[0]
          }
        })
        .catch(() => {
        })
        .finally(() => {})
    }
  },
  components: {
    NavBar,
    FooterNote,
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

.search-container {
  text-align: center;
  margin-bottom: 40px;
}

.search-container h1 {
  margin-bottom: 30px;
}

.input {
  width: 95%;
  max-width: 740px;
  text-align: center;
  display: flex;
  margin: 0 auto 10px auto;
}

input {
  flex: 4;
  padding-left: 10px;
  height: 40px;
  line-height: 40px;
  outline: 0;
  color: #000;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-radius: 8px 0 0 8px;
  box-shadow: none;
  border: 2px solid #42b983;
}

.input-message {
  padding-left: 10px;
  color: red;
}

.search {
  flex: 1;
  background-color: #42b983;
  height: 40px;
  line-height: 40px;
  color: #fff;
  cursor: pointer;
  font-weight: 500;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-radius: 0 8px 8px 0;
  box-shadow: none;
  border: 2px solid #42b983;
  display: flex;
  align-items: center;
  justify-content: center;
}

.audio-player {
  width: 95%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

</style>
