
<template>
  <audio :height="height" :width="width" :preload="preload" muted="muted">
  </audio>
</template>

<style>
@import '../..//node_modules/mediaelement/build/mediaelementplayer.min.css';
/* .mejs__container {
  min-width: auto !important;
}
.mejs__overlay-button {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.mejs__controls div{
  display: inline-block;
}
.mejs__time-rail {
  width: 50%;
}
.mejs__fullscreen > button {
  background-position: -80px 0 !important;
}

mediaelementwrapper,mediaelementwrapper > div {
  height: 100%;
  display: block;
}
mediaelementwrapper object{
  width: 100% !important;
  height: 100% !important;
} */

/* Player background */
.mejs__container .mejs__container,
.mejs__container .mejs__controls,
.mejs__container .mejs__embed,
.mejs__container .mejs__embed body {
  background-color: #efefef;
}

/* Player controls */
.mejs__container .mejs__button > button {
  /* background-image: url("images/mejs-controls-dark.svg"); */
}

.mejs__container .mejs__time {
  color: #888888;
}

/* Progress and audio bars */

/* Progress and audio bar background */
.mejs__container .mejs__controls .mejs__horizontal-volume-slider .mejs__horizontal-volume-total,
.mejs__container .mejs__controls .mejs__time-rail .mejs__time-total {
  background-color: #fff;
}

/* Track progress bar background (amount of track fully loaded)
  We prefer to style these with the main accent color of our theme */
.mejs__container .mejs__controls .mejs__time-rail .mejs__time-loaded {
  background-color: rgba(219, 78, 136, 0.075);
}

/* Current track progress and active audio volume level bar */
.mejs__container .mejs__controls .mejs__horizontal-volume-slider .mejs__horizontal-volume-current,
.mejs__container .mejs__controls .mejs__time-rail .mejs__time-current {
  background: #db4e88;
}

/* Reduce height of the progress and audio bars */
.mejs__container .mejs__time-buffering,
.mejs__container .mejs__time-current,
.mejs__container .mejs__time-float,
.mejs__container .mejs__time-float-corner,
.mejs__container .mejs__time-float-current,
.mejs__container .mejs__time-hovered,
.mejs__container .mejs__time-loaded,
.mejs__container .mejs__time-marker,
.mejs__container .mejs__time-total,
.mejs__container .mejs__horizontal-volume-total,
.mejs__container .mejs__time-handle-content {
  height: 3px;
}

.mejs__container .mejs__time-handle-content {
  /* top: -6px; */
}

.mejs__container .mejs__time-total {
  margin-top: 8px;
}

.mejs__container .mejs__horizontal-volume-total {
  top: 19px;
}
</style>

<script>
import 'mediaelement'
export default {
  name: 'mediaelement',
  props: {
    source: {
      type: String,
      required: true,
      default: ''
    },
    width: {
      type: String,
      required: false,
      default: 'auto'
    },
    height: {
      type: String,
      required: false,
      default: 'auto'
    },
    preload: {
      type: String,
      required: false,
      default: 'none'
    },
    autoplay: {
      type: Boolean,
      required: false,
      default: false
    },
    forceLive: {
      type: Boolean,
      required: false,
      default: true
    },
    success: {
      type: Function,
      default () {
        return false
      }
    },
    error: {
      type: Function,
      default () {
        return false
      }
    }
  },
  data: () => ({
    refresh: false,
    player: null
  }),
  mounted () {
    const {MediaElementPlayer} = global
    if (!MediaElementPlayer) {
      return
    }
    const componentObject = this
    this.player = new MediaElementPlayer(this.$el, {
      // renderers: [''],
    //   pluginPath: 'https://cdn.jsdelivr.net/npm/mediaelement@4.2.7/build/',
      shimScriptAccess: 'always',
      // forceLive: this.forceLive,
      // (by default, this is set as `sameDomain`)
      // shimScriptAccess: 'always',
      success: (mediaElement, originalNode, instance) => {
        instance.setSrc(componentObject.source)
        if (componentObject.autoplay) {
          mediaElement.addEventListener('canplay', function () {
            instance.play()
          })
        }
        this.success(mediaElement, originalNode, instance)
      },
      error: (e) => {
        this.error(e)
      }
    })
  },
  methods: {
    features (key) {
      const {mejs} = global
      return mejs.Features[key]
    },
    remove () {
      this.player.remove()
    }
  },
  beforeDestroy () {
    this.remove()
  },
  watch: {
    source: function (newSource) {
      this.player.setSrc(newSource)
      this.player.setPoster('')
      this.player.load()
    },
    forceLive: function (newForceLive, oldForceLive) {
      if (newForceLive === oldForceLive) {
        return
      }
      this.player.options.forceLive = newForceLive
    }
  }
}
</script>
