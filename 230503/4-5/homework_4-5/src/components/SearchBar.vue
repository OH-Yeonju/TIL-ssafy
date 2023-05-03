<template>
  <div>
    <h2 class="title">SSAFY TUBE</h2>
    <div class="d-flex justify-content-center align-items-center">
      <input type="text" v-model="query">
      <button @click="onClick">검색</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name:"SearchBar",
  data: function() {
    return {
      query: "SSAFY",
    }
  },
  methods : {
    onClick : function() {
      axios({
        method:'get',
        url:'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: 'AIzaSyDVgcN3N07tev6y76x2Pzi8tKrz9XPdwYM',
          type: 'video',
          part:'snippet',
          q: this.query,
        }
      })
      .then((res)=>{
        // console.log(res.data.items)
        this.$emit('fetch-videos', res.data.items)
      })
      .catch((error)=>{
        console.log(error)
      })
    }
  }
}
</script>

<style>
.title {
  color: rgb(96, 176, 250);
  font-weight: bold;
}

</style>