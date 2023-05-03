<template>
  <div>
    <h1>AppParent</h1>
    <input @input="ChildToParent" type="text" v-model="info2">
    <p>appData : {{ datain }}</p>
    <p>childData :{{ childdatain }}</p>
    <AppChild @c-to-p="parentGetEvent" :info2="info2" :info1="info1"/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue'

export default {
  name:'AppParent',
  components : {
    AppChild,
  },
  props: {
    info1:String,
  },
  data: function() {
    return {
      info2:'',
      info3:'',
    }
  },
  methods: {
    parentGetEvent: function(info3) {
      this.info3 = info3
    },
    ChildToParent : function() {
      this.$emit('child-to-parent', {1:this.info2, 2:this.info3})
    },

  },
  computed : {
    datain : function() {
      return this.info1
    },
    childdatain : function() {
      return this.info3
    }
  },
}
</script>

<style>

</style>