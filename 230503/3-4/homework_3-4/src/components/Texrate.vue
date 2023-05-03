<template>
  <div>
    <h2>산출세액 : {{ finaltax }} 만원</h2>
    <h2>세액감면 : (-) {{ reduction }} 만원</h2>
    <hr>
    <FinalTax :finaltax="finaltax" :reduction="reduction"/>
  </div>
</template>

<script>
import FinalTax from '@/components/Finaltax.vue'

export default {
  name:'TexRate',
  components : {
    FinalTax,
  },
  props : {
    taxbase : Number,
    reduction : Number,
  },
  
  data : function() {
    return {
      
    }
  },
  // methods : {
  //   standard : function() {
  //     if (this.texbase2 <= 1200) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.06)
  //     }
  //     else if (1200 < this.texbase2 <= 4600) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.15)-108
  //     }
  //     else if (4600 < this.texbase2 <= 8800) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.24)-522
  //     }
  //     else if (8800 < this.texbase2 <= 15000) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.35)-1490
  //     }
  //     else if (15000 < this.texbase2 <= 30000) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.38)-1940
  //     }
  //     else if (30000 < this.texbase2 <= 50000) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.40)-2540
  //     }
  //     else if (50000 < this.texbase2 <= 100000) {
  //       this.finaltax = Math.ceil(this.taxbase2 * 0.42)-3540
  //     }
  //     else {
  //       this.finaltax = Math.ceil(this.texbase2 * 0.45)-6540
  //     }
  //   }
  // },
  computed : {
    finaltax : function() {
      console.log(this.taxbase)
      if (this.taxbase <= 1200) {
        return Math.round(this.taxbase * 0.06)
      }
      else if (this.taxbase <= 4600) {
        return Math.round(this.taxbase * 0.15)-108
      }
      else if (this.taxbase <= 8800) {
        return Math.round(this.taxbase * 0.24)-522
      }
      else if (this.taxbase <= 15000) {
        return Math.round(this.taxbase * 0.35)-1490
      }
      else if (this.taxbase <= 30000) {
        return Math.round(this.taxbase * 0.38)-1940
      }
      else if (this.taxbase <= 50000) {
        return Math.round(this.taxbase * 0.40)-2540
      }
      else if (this.taxbase <= 100000) {
        return Math.round(this.taxbase * 0.42)-3540
      }
      else {
        return Math.round(this.taxbase * 0.45)-6540
      }
    }
  },
}
</script>

<style>

</style>