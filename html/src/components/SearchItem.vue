<template>
  <div>
    <div class="input">
      <input
        v-model="searchValue"
        type="text"
        :placeholder="searchPlaceholder"
        class="url-input"
      />
      <span class="search" @click="bottonClick">
        <span v-if="loading == false">{{ bottonText }}</span>
        <span v-else>
          <spinner size="15"></spinner>
        </span>
      </span>
    </div>
    <div class="input-message" v-if="errorMessage != ''">
      <span>{{ errorMessage }}</span>
    </div>
  </div>
</template>

<script>
import Spinner from 'vue-simple-spinner'
export default {
  name: 'Search',
  props: {
    searchPlaceholder: {
      type: String,
      default: '请输入搜索内容'
    },
    endpoint: {
      type: String,
      default: '/api/example_articles'
    },
    loading: {
      type: Boolean,
      default: false
    },
    errorMessage: {
      type: String,
      default: ''
    },
    bottonText: {
      type: String,
      default: '搜索'
    }
  },
  data () {
    return {
      searchValue: ''
    }
  },
  methods: {
    bottonClick () {
      this.$emit('bottonClicked', this.searchValue)
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
