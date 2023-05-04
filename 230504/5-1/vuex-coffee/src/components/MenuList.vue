<template>
  <div class="menu-list">
    <h3 class="text-start">1. 음료를 고르세요.</h3>
      <MenuListItem v-for="menu in menuList" :key="menu.title"
      :menu="menu"/>
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem.vue'


export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
    totalOrderCount() {
      return this.$store.getters.totalOrderCount
    }
  },
  methods: {
    selectMenu: function (menu) {
      // this.$store.commit('updateMenuList', menu)
      this.$store.dispatch('updateMenuListAction', menu)
    },
  },
}
</script>

<style>

</style>