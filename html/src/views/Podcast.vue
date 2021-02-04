<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <div class="audio-player">
      <podcast-player :articleId="articleId"></podcast-player>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import PodcastPlayer from '@/components/PodcastPlayer'
export default {
  name: 'Podcast',
  data () {
    return {
      error_message: '',
      loading: false,
      articleId: this.$route.params.podcastId
    }
  },
  mounted () {
  },
  methods: {
  },
  components: {
    NavBar,
    PodcastPlayer
  }
}
</script>

<style scoped>

.container {
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50px;
  padding: 0 15px;
}

header {
  margin-bottom: 3rem;
}

a {
  color: #42b983;
}

.audio-player {
  width: 100%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

</style>
