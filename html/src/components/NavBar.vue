<template>
  <nav>
    <div class="container">
      <h1 class="nav-title"><a href="/">PodcastX</a></h1>
    </div>
  </nav>
</template>

<style scoped>

h1 {
  font-size: 48px;
}

.nav {
  margin-bottom: 40px;
  color: #fff;
  position: relative;
  display: flex;
  align-items: center;
}

.nav .container {
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-title {
  margin: 20px 0 10px;
}

.nav-title a {
  cursor: pointer;
}

.nav-title a:link {
  text-decoration: none;
}

.nav-title a:visited {
  text-decoration: none;
  color: #000;
}

.nav-item {
  list-style: none;
  margin-left: 10px;
}
</style>
