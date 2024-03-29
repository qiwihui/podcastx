<template>
  <div class="podcast">
    <div class="podcast-art">
      <div
        class="podcast-art-image"
        :style="'background-image: url(' + podcast.image + ')'"
      ></div>
    </div>
    <div class="podcast-title">
      <div class="podcast-title-title">
        <a :href="podcast.url" target="_blank">{{ podcast.title }}</a>
      </div>
      <div class="podcast-title-subtitle" v-if="podcast.author!=''">{{ podcast.author }}</div>
      <div class="podcast-title-subtitle">&nbsp;</div>
    </div>
    <div class="podcast-description">
      {{ podcastDescription }}
    </div>
    <div class="podcast-actions">
      <div class="podcast-toolbox">
        <div class="podcast-player">
          <div
            class="podcast-player-button"
            @click="showPlay"
            title="播放"
          >
            <img src="../assets/player.svg" />
          </div>
          <div class="podcast-player-information">
            <span>{{ podcast.created_at | formatDate }}</span>
          </div>
        </div>
        <div class="podcast-community">
          <div class="action-button like">
            <div class="action-button-content">
              <heart :fill='"#fd6752"' :stroke='"#fd6752"' @click.native="doUnlike" v-if="podcast.like==1"></heart>
              <heart :fill='"none"' :stroke='"#000"' @click.native="doLike" v-else></heart>
              <div class="action-button-text">
                <span class="like-count-unliked">{{ podcast.likes_count }}</span>
              </div>
            </div>
          </div>
          <!-- <a
            native="true"
            :href="'/podcasts/' + podcast.id + '/comments'"
            target="_blank"
          >
            <div class="action-button action-button-comment none">
              <div class="action-button-content">
                <img src="../assets/comment.svg" />
                <div class="action-button-text">评论</div>
              </div>
            </div>
          </a>
          <div class="action-button share">
            <div class="action-button-content">
              <img src="../assets/share.svg" />
              <div class="action-button-text"></div>
            </div>
          </div> -->
          <div class="action-button share" v-if="podcast.added">
            <div class="action-button-content">
              <img src="../assets/trash.svg" @click="doDelete" v-if="deleteLoading==false"/>
              <span v-else><spinner size="14"></spinner></span>
            </div>
          </div>
          <div class="action-button share" v-else>
            <div class="action-button-content">
              <img src="../assets/plus.svg" @click="doAdd" v-if="deleteLoading==false" title="加入播放列表"/>
              <span v-else><spinner size="14"></spinner></span>
            </div>
          </div>
        </div>
      </div>
      <div class="podcast-mini-player" v-show="showSelect || isSelected">
        <audio-player
          :height="'40px'"
          ref="vPlay"
          :autoplay="false"
          :forceLive="false"
          :preload="'none'"
          :source="podcast.audios[0]"
        ></audio-player>
      </div>
    </div>
  </div>
</template>

<script>
import AudioPlayer from '@/components/AudioPlayer'
import Spinner from 'vue-simple-spinner'
import Heart from '@/components/icons/Heart'
export default {
  name: 'PodcastItem',
  props: {
    podcast: Object,
    showDelete: {
      type: Boolean,
      default: true
    },
    showSelect: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      deleteLoading: false,
      isSelected: false
    }
  },
  methods: {
    showPlay () {
      this.isSelected = !this.isSelected
      if (this.isSelected) {
        this.$refs.vPlay.play()
      } else {
        this.$refs.vPlay.stop()
      }
    },
    async doAdd () {
      this.deleteLoading = true
      if (!this.isLoggedIn) {
        this.$router.push({name: 'Login'})
        return
      }
      await this.$http
        .post('/api/articles/' + this.podcast.id, { action: 'add' })
        .then(response => {
          let data = response.data
          if (data.status === 1) {
            this.podcast.added = 1
          }
        }).finally(() => {
          this.deleteLoading = false
        })
    },
    async doLike () {
      if (!this.isLoggedIn) {
        this.$router.push({name: 'Login'})
        return
      }
      await this.$http
        .post('/api/articles/' + this.podcast.id, { action: 'like' })
        .then(response => {
          let data = response.data
          if (data.status === 1) {
            this.podcast.likes_count = data.data.likes_count
            this.podcast.like = 1
          }
        })
    },
    async doUnlike () {
      if (!this.isLoggedIn) {
        this.$router.push({name: 'Login'})
        return
      }
      await this.$http
        .post('/api/articles/' + this.podcast.id, { action: 'unlike' })
        .then(response => {
          let data = response.data
          if (data.status === 1) {
            this.podcast.likes_count = data.data.likes_count
            this.podcast.like = 0
          }
        })
    },
    async doDelete () {
      this.deleteLoading = true
      await this.$http
        .delete('/api/articles/' + this.podcast.id)
        .then(response => {
          let data = response.data
          if (data.status === 1) {
            if (!this.showDelete) {
              this.podcast.added = 0
            } else {
              this.$destroy()
              this.$el.parentNode.removeChild(this.$el)
            }
          }
        }).finally(() => {
          this.deleteLoading = false
        })
    }
  },
  computed: {
    podcastDescription: function () {
      return this.podcast.content
    },
    isLoggedIn: function () { return this.$store.getters.isAuthenticated }
  },
  components: {
    Heart,
    Spinner,
    AudioPlayer
  }
}
</script>

<style scoped>
.podcast {
  padding: 1.75rem 1.25rem 0;
  line-height: 130%;
  /* cursor: pointer; */
  text-decoration: none;
  display: grid;
  grid-template-columns: 7rem auto;
  grid-template-rows: 1fr auto auto auto;
  gap: 0 1.5rem;
  grid-template-areas:
    "art title"
    "art description"
    "art player"
    "art player";
  border: 1px solid transparent;
  border-left: 0;
  border-right: 0;
}

@media screen and (max-width: 900px) {
  .podcast {
      grid-template-columns: 5.5rem auto;
  }
}

@media screen and (max-width: 540px) {
  .podcast {
      padding: 1.25rem;
      border-bottom: 1px solid #e5e5e5;
      display: grid;
      grid-template-columns: 4.5rem auto;
      grid-template-rows: 1fr auto auto auto;
      gap: 0 1rem;
      grid-template-areas:
          'art title'
          'description description'
          'player player'
          'player player';
  }
}

.podcast:hover {
  background-color: #f7f5f3;
  transition: background-color 0.4s;
  border: 1px solid #e5e5e5;
  border-left: 0;
  border-right: 0;
  margin: -1px 0 0;
}

.podcast-art {
  grid-area: art;
  grid-row-start: 1;
  grid-row-end: 4;
}

.podcast-art-image,
.podcast-art-placeholder {
  flex-shrink: 0;
  width: 7rem;
  height: 7rem;
  background-position: center;
  background-repeat: no-repeat;
  -webkit-background-size: cover;
  background-size: cover;
}

@media screen and (max-width: 900px) {
  .podcast-art-image, .podcast-art-placeholder {
      width: 5.5rem;
      height: 5.5rem;
  }
}

@media screen and (max-width: 540px) {
  .podcast-art-image, .podcast-art-placeholder {
      width: 3.5rem;
      height: 3.5rem;
  }
}

.podcast-title {
  grid-area: title;
}

.podcast-title-title {
  font-size: 1.125rem;
  font-weight: bold;
  overflow: hidden;
}

@media screen and (max-width: 540px) {
  .podcast-title-title {
    min-height: 2rem;
  }
}

.podcast-title-subtitle {
  font-size: 0.875rem;
  font-weight: 500;
  overflow: inline-block;
}

.podcast-description {
  grid-area: description;
  font-size: 1rem;
  color: #78706c;
  margin: 0.5rem 0 0 0;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.podcast-actions {
  position: relative;
  top: 1px;
  grid-area: player;
  border-bottom: 1px solid #e5e5e5;
  margin-top: 0.75rem;
  padding-bottom: 1.25rem;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
}

@media screen and (max-width: 540px) {
  .podcast-actions {
      border-bottom: none;
      padding-bottom: 0.25rem;
  }
}

.podcast-toolbox {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.podcast-player {
  display: flex;
  align-items: center;
  line-height: 1rem;
}

.podcast-player .podcast-player-button {
  cursor: pointer;
  margin-right: 0.75rem;
}

a {
  color: #1a1a1a;
  text-decoration: none;
}

.podcast-player-information {
  color: #78706c;
  font-weight: 500;
  font-size: 0.875rem;
  display: flex;
  align-items: flex-end;
}

.podcast-community {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.podcast-mini-player {
  padding-top: 0.75rem;
  width: 100%;
  display: inline-block;
}

.action-button {
  color: #1c110b;
  cursor: pointer;
  display: inline-block;
  margin-right: 0.875rem;
}

.action-button .action-button-content {
  display: flex;
  align-items: center;
  padding: 0.3125rem 0;
}

.action-button .action-button-text {
  position: relative;
  color: #78706c;
  line-height: 1rem;
  margin-left: 0.25rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.action-button.share svg {
  height: 16px;
  width: 16px;
  padding: 2px;
}
</style>
