<template>
  <div class="footer">
    <div class="container">
      <div>
        <a href="/help">Help</a> |
        <a href="/about">About</a>
      </div>
    </div>
  </div>
</template>
<style scoped>
.footer {
  position: absolute;
  /* bottom: 0px; */
  width: 100%;
  display: block;
  /* font-size: 1.25rem; */
  background: #42b983;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 0;
}

.container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.container > div {
  margin: 0 auto;
}

a {
  text-decoration: none;
  color: white;
}
</style>
