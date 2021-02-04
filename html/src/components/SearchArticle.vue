<template>
  <div>
    <div class="input">
      <input
        v-model="searchUrl"
        type="text"
        placeholder="输入文章链接"
        class="url-input"
      />
      <span class="search" @click="extractUrl">
        <span v-if="loading == false">生成语音</span>
        <span v-else>
          <spinner size="15"></spinner>
        </span>
      </span>
    </div>
    <div class="input-message" v-if="error_message != ''">
      <span>{{ error_message }}</span>
    </div>
  </div>
</template>

<script>
import Spinner from 'vue-simple-spinner'
export default {
  props: {
    endpoint: {
      type: String,
      default: '/api/example_articles'
    }
  },
  data () {
    return {
      loading: false,
      error_message: '',
      articleId: '',
      searchUrl: ''
    }
  },
  methods: {
    async extractUrl () {
      this.loading = true
      this.error_message = ''
      this.articleId = ''
      let urlData = { url: this.searchUrl }
      await this.$http
        .post(this.endpoint, urlData)
        .then(response => response.data)
        .then(data => {
          if (data.status === 1) {
            this.articleId = data.data.id
            // articleId changed
            this.$emit('articleChanged', this.articleId)
          } else {
            this.error_message = '解析错误，请重试'
          }
          this.loading = false
        })
        .catch(error => {
          this.error_message = '请求错误，请稍后重试'
          this.loading = false
          console.error(error)
        })
        .finally(() => {
          this.loading = false
        })
    }
  },
  components: {
    Spinner
  }
}
</script>

<style scoped>
.input {
  width: 100%;
  max-width: 960px;
  text-align: center;
  display: flex;
  margin: 0 auto 10px auto;
}

input {
  flex: 5;
  padding-left: 8px;
  /* height: 40px; */
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

input[type="text"] {
  font-size: 18px;
}

.input-message {
  padding-left: 10px;
  color: red;
}

.search {
  flex: 1;
  min-width: 70px;
  background-color: #42b983;
  /* height: 40px; */
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
</style>
