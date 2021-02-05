<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <div class="audio-player">
      <audio-player :articleId="articleId" ref="vPlay" :autoplay="true" :forceLive="true" preload="true" :source="selected"></audio-player>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import PodcastPlayer from '@/components/PodcastPlayer'
import AudioPlayer from '@/components/AudioPlayer'
export default {
  name: 'Podcast',
  data () {
    return {
      selected: 'https://podcastx.qiwihui.com/media/601226b5e83cd5e6edf3417e/full.mp3',
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
    PodcastPlayer,
    AudioPlayer
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
