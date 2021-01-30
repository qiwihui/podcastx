<template>
  <div class="feature">
    <div class="feature-image-container">
      <img :src="image" class="feature-image" />
    </div>
    <div class="feature-info">
      <div class="feature-title">
        <span>{{ title }}</span>
      </div>
      <div class="description">
        {{ description }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeatureCard',
  props: {
    image: {
      type: String
    },
    title: {
      type: String
    },
    description: {
      type: String
    }
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
.feature {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  padding: 8px 5px;
}

.feature-image {
  border-radius: 50%;
}

.feature-image-container {
  width: 73px;
  height: 73px;
  min-width: 73px;
  min-height: 73px;
  border-radius: 50%;
  margin-right: 12px;
  background-color: #ecf0f5;
}

.feature-info {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.feature-title {
  font-size: 24px;
}
</style>
