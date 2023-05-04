<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <img id="menuimg" :src="order.menu.image" alt="">
        <div>
          <p>{{ order.menu.title }}</p>
          <p>사이즈 : {{ order.size.name }}</p>
        </div>
      </div>
      <div>
        <p id="price">{{ order.menu.price + order.size.price }}원</p>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style scoped>
img {
  width: 45px;
  height: 45px;
}

p {
  margin-bottom: 0px;
}

hr {
  width: 95%;
}

#menuimg {
  border-radius: 25%;
  margin-right: 10px;
}

#price {
  margin-right: 40px;
}
</style>