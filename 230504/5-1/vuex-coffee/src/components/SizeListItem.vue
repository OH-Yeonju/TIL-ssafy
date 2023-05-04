<template>
  <div>
    <div @click="selectSize(size)">
      <button type="button" :class="{'selected':size.selected}" class="btn btn-outline-dark d-flex justify-content-between align-items-center">
      <span>{{ size.name }}</span>
      <span>{{ size.price }}원</span>
    </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    selectSize: function (size) {
      this.$store.commit('updateSizeList', size)
    },
  }
}
</script>

<style scoped>
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