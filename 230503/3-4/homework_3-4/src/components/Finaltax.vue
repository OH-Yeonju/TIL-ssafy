<template>
  <div>
   <h2>결정세액 : {{ finalize }} 만원</h2>
  </div>
</template>

<script>
export default {
  name:'FinalTax',
  props : {
    finaltax : Number,
    reduction : Number,
  },
  computed : {
    finalize : function() {
      if (this.finaltax - this.reduction < 0) {
        return 0
      }
      return this.finaltax - this.reduction
    }
  }
}
</script>

<style>

</style>