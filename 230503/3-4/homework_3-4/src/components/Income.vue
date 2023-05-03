<template>
  <div>
    <p>연봉 입력 (만원) : <input v-model.number="income" type="number"></p>
    <p>세액감면액 (만원) : <input v-model.number="reduction" type="number"></p>
    <hr>
    <h2>종합소득금액 : {{ income }} 만원</h2>
    <h2>종합소득공제 : (-) {{ deduction }} 만원</h2>
    <h2>과세표준 : {{ taxbase }} 만원</h2>
    <hr>
    <TexRate :taxbase="taxbase" :reduction="reduction"/>
  </div>
</template>

<script>
import TexRate from '@/components/Texrate.vue'


export default {
  name:'InCome',
  components: {
    TexRate,
  },
  data : function() {
    return {
      income : 0,
      deduction : 150,
      reduction : 0,
      // taxbase : 0
    }
  },
  computed : {
    taxbase : function() {
      if (this.income - this.deduction < 0) {
        return 0
      } else {
        return this.income - this.deduction
      }
    }
  },
}
</script>

<style>

</style>