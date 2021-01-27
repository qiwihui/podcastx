<template>
  <div class="navbar">
    <div class="container">
      <h1 class="navbar-title"><a href="/">PodcastX</a></h1>
    </div>
  </div>
</template>

<style scoped>
* {
  padding: 0;
  margin: 0;
}
.navbar {
  margin-bottom: 40px;
  color: #fff;
  background: #42b983;
  height: 58px;
  position: relative;
  display: flex;
  align-items: center;
}

.navbar .container {
  width: 90%;
  max-width: 960px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
}

.navbar-nav {
  display: flex;
  flex-direction: row;
  list-style: none;
  align-items: center;
}

.navbar-title a {
  cursor: pointer;
}

.navbar-title a:link {
  text-decoration: none;
}

.navbar-title a:visited {
  text-decoration: none;
  color: #fff;
}

.nav-item {
  list-style: none;
  margin-left: 10px;
}
</style>
