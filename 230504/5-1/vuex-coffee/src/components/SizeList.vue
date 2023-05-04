<template>
  <div>
    <h3 class="text-start">2. 사이즈를 고르세요.</h3>
    <SizeListItem v-for="size in sizeList" :key="size.title"
    :size="size"
    @click="selectSize(size)"/>
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem.vue'


export default {
  name: 'SizeList',
  components: {
    SizeListItem
  },
  methods: {
    selectSize: function (size) {
      this.$store.commit('updateSizeList', size)
    },
    onSelectMenu: function () {},
  },
  computed: {

    sizeList: function () {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>
</style>