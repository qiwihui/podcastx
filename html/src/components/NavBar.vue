<template>
  <nav>
    <div class="container">
      <span class="nav-title">
        <a class="brand" href="/">PodcastX</a>
        <span class="nav-explore"><router-link :to="{name: 'Explore'}" exact>探索</router-link></span>
      </span>
      <div class="nav-items" v-show="displayitems">
        <span v-if="isLoggedIn">
          <span><a href="/podcasts">{{ username }}</a></span>
        </span>
        <span v-if="isLoggedIn">
          <a @click="logout">登出</a>
        </span>
        <span v-if="!isLoggedIn"><router-link :to="{name: 'Login'}" exact>登录</router-link></span>
        <span v-if="!isLoggedIn"><router-link :to="{name: 'Register'}" exact>注册</router-link></span>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  props: {
    displayitems: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('Logout')
      this.$router.push({name: 'Login'})
    }
  },
  computed: {
    isLoggedIn: function () { return this.$store.getters.isAuthenticated },
    username: function () { return this.$store.getters.stateUser }
  }
}
</script>
<style scoped>

h1 {
  font-size: 30px;
}

nav {
  margin: 10px 0 40px;
  /* color: #fff; */
  position: relative;
  display: flex;
  align-items: center;
}

nav .container {
  width: 100%;
  max-width: 960px;
  height: 3rem;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-title .brand {
  font-size: 30px;
  margin-right: 30px;
}

a {
  cursor: pointer;
  color: #000;
}

a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
  color: #000;
}

.nav-items {
  list-style: none;
  margin: 0 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-items span {
  padding-left: 1.5rem;
}

</style>
