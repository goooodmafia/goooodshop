import PRODUCT from "~/api/query/product.graphql"

export const state = () => ({
  products: [],
  // productsSkuList: [],
  //
  // wishes: {}
})

export const getters = {

  // getProductBySku: (state) => (sku) => {
  //   return state.products[sku]
  // },
  //
  getCountBySize: (state) => (sku, size) => {
    console.log('getCountBySize')
    const pindex = state.products.findIndex(p => p.sku === sku)
    var c = 0
    if (pindex !== -1) {
      const sindex = state.products[pindex].size.findIndex(s => s.size === size)
      c = state.products[pindex].size[sindex].count
    }
    return c
  },
  //
  // cartCount(state,) {
  //   return state.productsSkuList.length
  // },
  is_in_cart: (state) => (sku) => {
    console.log('is_in_cart')
    const index = state.products.findIndex(p => p.sku === sku)
    return index !== -1;
  }
}


export const mutations = {
  ADD_TO_CART(state, sku) {
    state.products.push(
      {
        sku: sku,
        size: [
          {size: '4XS', count: 0},
          {size: '3XS', count: 0},
          {size: '2XS', count: 0},
          {size: 'XS', count: 0},
          {size: 'S', count: 0},
          {size: 'M', count: 0},
          {size: 'L', count: 0},
          {size: 'XL', count: 0},
          {size: '2XL', count: 0},
          {size: '3XL', count: 0},
          {size: '4XL', count: 0},
        ],
      })
  },

  REMOVE_FROM_CART(state, sku) {

    // const index = state.products.indexOf(sku);
    // if (index !== -1) {
    //   state.products.splice(index, 1)
    // }

    const index = state.products.findIndex(p => p.sku === sku)
    if (index !== -1) {
      state.products.splice(index, 1)
    }
  },

  SET_SIZE(state, payload) {

    const pindex = state.products.findIndex(p => p.sku === payload.sku)
    if (pindex !== -1) {
      const sindex = state.products[pindex].size.findIndex(s => s.size === payload.size)
      state.products[pindex].size[sindex].count = payload.count
    }
    // let getSizeIndex = state.products[payload.sku]
    //   .size.findIndex(x => x.size === payload.size);
    // state.products[payload.sku].size[getSizeIndex].count = payload.count
  },


}

export const actions = {
  addToCart({commit, getters}, payload) {
    console.log('addToCart')
    if (!getters.is_in_cart(payload.sku)) {
      commit('ADD_TO_CART', payload.sku)
    }
  },

  removeFromCart({commit}, payload) {
    console.log('removeFromCart')
    commit('REMOVE_FROM_CART', payload.sku)
  },

  increaseSize({commit, getters, dispatch}, payload) {
    console.log('increaseSize')
    dispatch('addToCart', payload)

    const c = getters.getCountBySize(payload.sku, payload.size)

    commit('SET_SIZE', {sku: payload.sku, size: payload.size, count: c + payload.count})
  },

  decreaseSize({commit, dispatch}, payload) {
    console.log('decreaseSize')
    const c = getters.getCountBySize(payload.sku, payload.size)
    if (c - payload.count < 1) {
      dispatch('removeFromCart', payload)
    } else {
      commit('SET_SIZE', {sku: payload.sku, size: payload.size, count: c - payload.count})
    }
  }
}

