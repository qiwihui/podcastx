<template>
  <div class="container">
    <header>
      <nav-bar :displayitems="false"></nav-bar>
    </header>
    <div class="login-container">
      <div class="login-panel">
        <h2 class="title">欢迎来到 PodcastX</h2>
        <form @submit.prevent="submit">
          <div class="login-item">
            <label for="email" class="login-item-label mb-2">邮箱</label>
            <input
              type="email"
              name="email"
              v-model="form.email"
              placeholder="username@example.com"
              required="required"
              autofocus="autofocus"
            />
          </div>
          <div class="login-item">
            <label for="username" class="login-item-label mb-2">用户名</label>
            <input
              type="text"
              name="username"
              v-model="form.username"
              placeholder="username"
              required="required"
              autofocus="autofocus"
            />
          </div>
          <div class="login-item">
            <div class="login-password mb-2">
              <label for="password" class="login-item-label">密码</label>
            </div>
            <input
              name="password"
              type="password"
              v-model="form.password"
              placeholder="••••••••••"
              required="required"
            />
          </div>
          <div class="error mb-2" v-show="errorMessage!==''">{{ errorMessage }}</div>
          <div>
            <button type="submit">注册</button>
            <div class="no-account">
              <p>
                已经有帐号？
                <span class="register"
                  ><router-link :to="{ name: 'Login' }" exact
                    >登录</router-link
                  ></span
                >
              </p>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import { mapActions } from 'vuex'
export default {
  name: 'Register',
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      errorMessage: ''
    }
  },
  methods: {
    ...mapActions(['Register']),
    async submit () {
      this.errorMessage = ''
      const User = new FormData()
      User.append('email', this.form.email)
      User.append('username', this.form.username)
      User.append('password', this.form.password)
      let self = this
      try {
        await this.Register(User).then(data => {
          console.log(data)
          self.errorMessage = data.msg
        })
        // this.$router.push("/posts");
      } catch (error) {
        this.errorMessage = '请求错误'
      }
    }
  },
  components: {
    NavBar
  }
}
</script>

<style scoped>
.container {
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  padding: 0 15px;
}

input,
button {
  box-sizing: border-box;
  border-width: 0px;
  border-style: solid;
  border-color: rgb(226, 232, 240);
  border-image: initial;
}

.login-container {
  width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  background: white;
  border-radius: 0.25rem;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 4px 0px;
  max-width: 30rem;
}

.login-panel {
  width: 80%;
  /* padding: 0 2rem; */
}

.title {
  text-align: center;
  font-size: 1.5rem;
  /* padding: 1.5rem 0; */
}

.login-item {
  margin-bottom: 1rem;
}

.login-item-label {
  display: block;
  color: rgba(74, 85, 104, 1);
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.login-password {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

input {
  border-width: 1px;
  border-radius: 0.25rem;
  width: 100%;
  padding: 0.75rem;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

button[type="submit"] {
  background: linear-gradient(65deg, rgb(66, 185, 131), rgb(0, 185, 131));
  width: 100%;
  color: rgba(255, 255, 255, 1);
  position: relative;
  padding: 1rem 1.5rem;
  height: 3rem;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.25rem;
  line-height: 1.15;
  cursor: pointer;
}
button[type="submit"]:focus {
  outline: none;
}

.error {
  color: rgba(252,129,129, 1);
  text-align: center;
  font-size: .75rem;
}

.forget-password {
  color: rgba(113, 128, 150, 1);
  font-size: 0.875rem;
}

.forget-password:hover {
  text-decoration: underline;
}

.no-account {
  text-align: center;
  padding: 1rem 0;
  font-size: 0.875rem;
}

.no-account p {
  color: rgba(113, 128, 150, 1);
}

.register {
  font-weight: bold;
  text-decoration: none;
  cursor: pointer;
}
</style>
