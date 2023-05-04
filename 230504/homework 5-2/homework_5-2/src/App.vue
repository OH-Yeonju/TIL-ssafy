// App.vue

<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  // data: function() {
  //   return {
  //     counter : 0
  //   }
  // },
  // computed: {
    
  // },
  methods: {
    increase: function () {
      this.$store.dispatch('increaseCnt')
    },
    decrease: function () {
      this.$store.dispatch('decreaseCnt')
    },
  },
  computed: {
    counter : function() {
      return this.$store.state.counter
    },
    counterDouble: function () {
      return this.$store.getters.counterDouble
    },
  },
}
</script>

<style>
</style>