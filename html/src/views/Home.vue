<template>
  <div class="container">
    <header>
      <nav-bar></nav-bar>
    </header>
    <main>
      <article>
        <h2>AI 语音生成</h2>
        <p>使用最新文本转语音技术为您喜欢的新闻、博客生成逼真的语音朗读。</p>
        <p>您可以随时随地收听，无论是下班路上，还是工作间隙。</p>
      </article>
      <section class="search-container">
        <search-article @articleChanged="updateArticle"></search-article>
      </section>
      <section class="audio-player">
        <podcast-player
          autoplay
          theme="pic"
          show-lrc
          :articleId="articleId"
          v-if="articleId != ''"
        ></podcast-player>
      </section>
      <section class="feature-container">
        <h2>功能</h2>
        <section class="feature-items">
          <feature-card
            v-for="feature in features"
            :key="feature.title"
            :image="feature.image"
            :title="feature.title"
            :description="feature.description"
          ></feature-card>
        </section>
      </section>
    </main>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
import FooterNote from '@/components/FooterNote'
import PodcastPlayer from '@/components/PodcastPlayer'
import FeatureCard from '@/components/FeatureCard'
import SearchArticle from '@/components/SearchArticle'
export default {
  name: 'Home',
  data () {
    return {
      articleId: '',
      features: [
        {
          image: '',
          title: 'AI 语音',
          description:
            '使用 AI 驱动的文本到语音技术将喜欢的新闻、博客转换为清晰自然的语音。'
        },
        {
          image: '',
          title: '语言',
          description: '支持中文和英文，支持男生和女生发音。'
        },
        {
          image: '',
          title: '音频播放器',
          description: '支持使用播放器将音频嵌入到您的博客或网站中。'
        },
        {
          image: '',
          title: '文章导入',
          description: '支持从 URL 和 RSS 导入文章列表。'
        }
      ]
    }
  },
  mounted () {},
  methods: {
    updateArticle (e) {
      this.articleId = e
    }
  },
  components: {
    NavBar,
    FooterNote,
    PodcastPlayer,
    FeatureCard,
    SearchArticle
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

h1 {
  font-size: 48px;
}

h2 {
  font-size: 36px;
}

h3 {
  font-size: 24px;
}

p {
  margin: 0.5rem;
}

a {
  color: #42b983;
}

header {
  margin-bottom: 3rem;
}

article {
  text-align: center;
  font-size: 24px;
  margin-bottom: 50px;
}

.search-container {
  text-align: center;
  margin-bottom: 40px;
}

.search-container h1 {
  margin-bottom: 30px;
}

.audio-player {
  width: 100%;
  max-width: 960px;
  margin: 0 auto 30px auto;
}

.feature-container h2 {
  text-align: center;
}

.feature-items {
  display: flex;
  flex-wrap: wrap;
}

.feature-items div {
  width: 48%;
}

@media (max-width: 700px) {
  .feature-items div {
    width: 100%;
  }
}
</style>
