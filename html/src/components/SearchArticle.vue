<template>
  <div>
    <search
      :search-placeholder='"输入文章链接"'
      :botton-text='"生成语音"'
      :error-message="error_message"
      :loading="loading"
      @bottonClicked="extractUrl"
    ></search>
  </div>
</template>

<script>
import Spinner from 'vue-simple-spinner'
import Search from '@/components/Search'
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
      articleId: ''
    }
  },
  methods: {
    async extractUrl (e) {
      this.loading = true
      this.error_message = ''
      this.articleId = ''
      let urlData = { url: e }
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
    Spinner,
    Search
  }
}
</script>

<style scoped>
</style>
