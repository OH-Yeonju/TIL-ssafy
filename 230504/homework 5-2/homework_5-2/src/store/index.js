import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter : 0
  },
  getters: {
    counterDouble(state) {
      return state.counter * 2
    }
  },
  mutations: {
    COUNTER_INCREASE(state) {
      const inCnt = state.counter + 1
      state.counter = inCnt
    },
    COUNTER_DECREASE(state) {
      const deCnt = state.counter - 1
      state.counter = deCnt
    }
    
  },
  actions: {
    increaseCnt(context) {
      context.commit('COUNTER_INCREASE')
    },
    decreaseCnt(context) {
      context.commit('COUNTER_DECREASE')
    },
  },
  modules: {
  }
})
