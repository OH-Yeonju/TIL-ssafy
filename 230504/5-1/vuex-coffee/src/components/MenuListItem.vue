<template>
  <div @click="selectMenu(menu)">
    <button type="button" :class="{'selected':menu.selected}" class="btn btn-outline-dark d-flex justify-content-between align-items-center">
      <img :src="menu.image" alt="">
      <span>{{ menu.title }}</span>
      <span>{{ menu.price }}원</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    selectMenu: function (menu) {
      // this.$store.commit('updateMenuList', menu)
      this.$store.dispatch('updateMenuListAction', menu)
    },
  }
}
</script>

<style scoped>
img {
  border-radius: 25%;
  width: 40px;
  height: 40px;
}

.btn {
  width: 400px;
  height: 55px;
  margin-bottom: 10px;

}

.btn:hover {
  background-color: #43936C;
  color: white;
}

.selected {
  background-color: #43936C;
  color: white;
}
</style>