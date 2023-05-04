import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title : '아메리카노',
        price : 3000,
        selected : true,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title : '라떼',
        price : 4000,
        selected : false,
        image : 'https://source.unsplash.com/featured/?latte'
      },
      {
        title : '바닐라라떼',
        price : 5000,
        selected : false,
        image : 'https://source.unsplash.com/featured/?vanilla-latte'
      },
    ],
    sizeList: [
      {
        name : 'small',
        price : 0,
        selected : true,
      },
      {
        name : 'medium',
        price : 500,
        selected : false,
      },
      {
        name : 'medium',
        price : 1000,
        selected : false,
      },
    ],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      let totalPrice = 0
      for (let order of state.orderList) {
        totalPrice += order.menu.price
        totalPrice += order.size.price
      }
      return totalPrice
    }
  },
  mutations: {
    addOrder: function (state) {
      const menu = state.menuList.find((menu)=> {
        return menu.selected
      })

      const size = state.sizeList.find((size)=> {
        return size.selected
      })

      const order = {menu:menu, size:size}
      state.orderList.push(order)
      
    },
    updateMenuList: function (state, selectedMenu) {
      state.menuList = state.menuList.map((menu)=>{
        if (menu.title === selectedMenu.title) {
          menu.selected = true
        } else {
          menu.selected = false
        }
        return menu
      })
    },
    updateSizeList: function (state, selectedSize) {
      state.sizeList = state.sizeList.map((size)=>{
        if (size.name === selectedSize.name) {
          size.selected = true
        } else {
          size.selected = false
        }
        return size
      })
    },
  },
  actions: {
    updateMenuListAction: function(context, selectedMenu) {
      context.commit("updateMenuList", selectedMenu)
    },
    addMenuOrder : function(context) {
      context.commit("addOrder")
    }
  },
  modules: {
  }
})