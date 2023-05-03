<template>
  <div id="app">
    <div class="container">
      <nav>
        <SearchBar @fetch-videos="onFetch"/>
      </nav>
      <section class="row">
          <VideoDetail v-if="isSelected()" :video="selectedVideo" class="col"/>
          <VideoList :videos="videos" class="col"
          @select-video="onSelect"/>
      </section>
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoList from './components/VideoList.vue'
import VideoDetail from './components/VideoDetail.vue'




export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data : function () {
    return {
      videos: [],
      selectedVideo: {},
    }
  },
  methods : {
    onFetch: function(videos) {
      this.videos = videos
      // console.log(this.videos)
    },
    onSelect : function(video) {
      this.selectedVideo = video
      console.log(this.selectedVideo)
    },
    isSelected: function() {
      return !!Object.keys(this.selectedVideo).length
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
