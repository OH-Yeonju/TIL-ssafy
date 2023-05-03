<template>
  <div>
    <h1>VideoDetail</h1>
    
    <iframe id="player" width="640" height="360"
  :src="videoSrc"
  frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name:"VideoDetail",
  props : {
    video: Object
  },
  computed: {
    videoSrc : function() {
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    }
  }
}
</script>

<style>

</style>