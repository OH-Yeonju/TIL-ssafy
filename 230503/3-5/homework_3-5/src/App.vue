<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="info1">
    <p>parentData : {{ padatain }}</p>
    <p>childData: {{ cdatain }}</p>
    <AppParent @child-to-parent="parentGetEvent" :info1="info1"/>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent.vue'


export default {
  name: 'App',
  components: {
    AppParent,
  },
  data: function() {
    return {
      info1:'',
      childdata: '',
      parentdata: ''
    }
  },
  methods: {
  parentGetEvent: function(full) {
      this.childdata = full[2]
      this.parentdata = full[1]
      console.log(full)
    },
  },
  computed : {
    padatain : function() {
      return this.parentdata
    },
    cdatain : function() {
      return this.childdata
    }
  },
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
