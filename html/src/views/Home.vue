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
          <span v-if="loading == false">Analyse</span>
          <span v-else>
            <spinner size="15"></spinner>
          </span>
        </span>
      </div>
      <div class="input-message" v-if="error_message != ''">
        <span>{{ error_message }}</span>
      </div>
    </div>
    <div class="audio-player">
      <podcast-player :articleId="articleId" v-if="articleId!=''"></podcast-player>
    </div>
  </div>
</template>

<script>
import Spinner from 'vue-simple-spinner'
import NavBar from '@/components/NavBar'
import FooterNote from '@/components/FooterNote'
import PodcastPlayer from '@/components/PodcastPlayer'
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Podcast X',
      error_message: '',
      loading: false,
      searchUrl: '',
      articleId: ''
    }
  },
  mounted () {
  },
  methods: {
    extractUrl () {
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
    }
  },
  components: {
    NavBar,
    FooterNote,
    Spinner,
    PodcastPlayer
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
