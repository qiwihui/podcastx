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
    <!-- <footer-note></footer-note> -->
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import FooterNote from '@/components/FooterNote'
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Podcast X',
      error_message: '',
      loading: false,
      searchUrl: '',
      articleId: '',
      article_info: {}
    }
  },
  mounted () {
  },
  methods: {
    extractUrl () {
      this.loading = true
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
          if (data.status === 'ok') {
            this.article_info = data.data
          }
        })
        .catch(() => {
        })
        .finally(() => {})
    }
  },
  components: {
    NavBar,
    FooterNote
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

.thread-usage {
  width: 40%;
  margin: 0 auto;
}

.thread-usage ul {
  list-style-position: inside;
  /* display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  list-style-type: none; */
}

.thread-usage ul li {
  position: relative;
  margin: 0;
  padding-bottom: 1em;
  padding-left: 20px;
}

li:before {
  background-color: #c00;
  width: 2px;
  content: "";
  position: absolute;
  top: 0px;
  bottom: 0px;
  left: 5px;
}

li::after {
  content: "";
  position: absolute;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' viewBox='0 0 32 32' focusable='false'%3E%3Ccircle stroke='none' fill='%23c00' cx='16' cy='16' r='10'%3E%3C/circle%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-size: contain;
  left: 0;
  top: 2px;
  width: 12px;
  height: 12px;
}

.thread-container {
  width: 95%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

.more-recent-thread {
  width: 95%;
  max-width: 960px;
  margin: 0 auto 30px auto;
  display: flex;
  align-content: flex-start;
}

.btn {
  display: inline-block;
  font-weight: 400;
  color: #212529;
  text-align: center;
  vertical-align: middle;
  user-select: none;
  background-color: transparent;
  border: 1px solid transparent;
  padding: .375rem .375rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: .25rem;
  transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
  color: #6c757d;
  border-color: #6c757d;
}

</style>
