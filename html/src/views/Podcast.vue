<template>
  <div>
    <div>
      <nav-bar></nav-bar>
    </div>
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

h1,
h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}

.audio-player {
  width: 95%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

</style>
