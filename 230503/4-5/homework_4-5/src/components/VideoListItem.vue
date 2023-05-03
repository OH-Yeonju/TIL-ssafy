<template>
  <div>
    <li @click="onSelect">
      <img :src="videoUrl" :alt="video.id.videoId">
      <p>{{ video.snippet.title }}</p>
    </li>
  </div>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: Object,
  },
  computed: {
    videoUrl : function() {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods : {
    onSelect : function() {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>

</style>