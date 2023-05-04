<template>
  <div id="app">
      <h2 id="title">Coffee Order App</h2>
        <div id="coffeeapp">
          <div id="menulist">

            <MenuList/>
          </div>
          <div id="sizelist">
            <SizeList/>
          </div>
        </div>
        <div class="d-grid gap-2">
        <button @click="menuOrder" type="button" class="btn">장바구니 담기</button>
        </div>
        <div class="orderlist">
          <h2 class="text-start">주문 내역</h2>
          <OrderList/>
        </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList.vue'
import SizeList from '@/components/SizeList.vue'
import OrderList from '@/components/OrderList.vue'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
  },
  methods :{
    menuOrder: function () {
      this.$store.dispatch('addMenuOrder')
    },
  }
}
</script>

<style scoped>


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#title {
  width: 1000px;
  
}

#coffeeapp {
  display: flex;
  width: 1000px;
  background-color: rgb(240, 240, 240);
  border-radius: 1%;
  padding: 20px;

}

#menulist{
  border-radius: 2%;
  display: flex;
  justify-content: center;
  width: 450px;
  background-color: white;
  margin-right: 30px;
  padding-top: 20px;
}

#sizelist {
  border-radius: 2%;
  display: flex;
  justify-content: center;
  width: 500px;
  background-color: white;
  padding-top: 20px;
}

.btn{
  background-color: #43936C;
  color: white;
  width: 900px;
  margin: 30px;
}

.orderlist {
  width: 1000px;
  background-color: rgb(240, 240, 240);
  padding-top: 30px;
  border-radius: 2%;
  padding-left: 20px;
  padding-bottom: 20px;

}
</style>
