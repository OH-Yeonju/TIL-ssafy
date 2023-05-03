<template>
  <div>
    <h1>Appchild</h1>
    <input @input="ChildToParent" type="text" v-model="info3">
    <p>appData: {{ datain1 }}</p>
    <p>parentData:{{ datain2 }}</p>
    <p >childData:{{ info3 }}</p>
  </div>
</template>

<script>

export default {
  name:"AppChild",
  components: {
  },
  data: function() {
    return {
      info3:'',
    }
  },
  props: {
    info2:String,
    info1:String,
  },
  computed : {
    datain2 : function() {
      return this.info2
    },
    datain1 : function() {
      return this.info1
    }
  },
  methods: {
    ChildToParent : function() {
      this.$emit('c-to-p', this.info3)
    }
  }
}
</script>

<style>

</style>