import PRODUCT from "~/api/query/product.graphql"

export const state = () => ({
  products: {},
  productsSkuList: [],

  wishes: {}
})

export const getters = {
  cartCount(state,) {
    return state.productsSkuList.length
  },
  is_in_cart: (state) => (sku) => {
    return state.productsSkuList.includes(sku)
  }
}


export const mutations = {
  ADD_TO_CART(state, sku) {
    let obj = {}
    obj[sku] = {
      size: {
        'NoSizw': 0,
        'XS': 0,
        'S': 0,
        'M': 0,
        'size_l': 0,
        'size_xl': 0,
        'size_2xl': 0,
        'size_3xl': 0,
        'size_4xl': 0,
      },
      price: 0
    }
    state.products = {...state.products, ...obj}
    state.productsSkuList.push(sku)
  },

  INCREASE_SIZE(state, payload) {
    state.products[payload.sku].size[payload.size] += payload.count
  }
}

export const actions = {
  addToCart({commit, getters}, payload) {
    if (!getters.is_in_cart(payload.sku)) {
      commit('ADD_TO_CART', payload.sku)
    }
  },

  removeFromCart({commit}, payload) {
  },

  increaseSize({commit, getters, dispatch}, payload) {
    dispatch('addToCart', payload)
    commit('INCREASE_SIZE', payload)
  },

  decreaseSize({commit}, payload) {
  }
}

