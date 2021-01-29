<template>
  <div class="container">
    <div class="audio-player">
      <podcast-player :articleId="articleId"></podcast-player>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import PodcastPlayer from '@/components/PodcastPlayer'
export default {
  name: 'EmbedPodcast',
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

body {
  background: none;
}

.container {
  /* max-width: 40rem; */
  margin-left: auto;
  margin-right: auto;
  /* margin-bottom: 50px; */
  padding: 10px;
}

a {
  color: #42b983;
}

.audio-player {
  width: 100%;
  max-width: 40rem;
  /* margin: 0 auto 30px auto; */
}

</style>
