<template>
  <div class="text-start">
    <p>총 {{ totalOrderCount }}건 : {{ totalOrderPrice }}원</p>
    <OrderListItem v-for="(order, index) in orderList" :key="index"
    :order="order"/>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem.vue'

export default {
  name: 'OrderList',
  components: {
    OrderListItem
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style>
</style>