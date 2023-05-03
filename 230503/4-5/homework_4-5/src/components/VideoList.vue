<template>
  <div>
      <ul>
        <VideoListItem v-for="video in videos" :key="video.id.videoid"
        :video="video"
        @select-video="onSelect"/>
      </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name:"VideoList",
  components :{
    VideoListItem
  },
  props : {
    videos : Array,
  },
  methods : {
    onSelect : function(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>