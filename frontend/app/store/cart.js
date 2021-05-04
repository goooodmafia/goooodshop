import PRODUCT from "~/api/query/product.graphql"

export const state = () => ({
  cart: [],
  wishes: []
})

export const getters = {
  cartCount(state,) {
    return state.cart.length
  },
  wishesCount(state,) {
    return state.wishes.length
  }
}


export const mutations = {
  // ADD_TO_CART(state, product) {
  //   state.cart.push(product)
  // }

  INCREASE_SIZE(state, sku, size) {
    if (state.cart[sku]) {
      state.cart[sku].size[size] += 1
    } else {
      state.cart[sku] = {
        size: {
          'size_ns': 0,
          'size_xs': 0,
          'size_s': 0,
          'size_m': 0,
          'size_l': 0,
          'size_xl': 0,
          'size_2xl': 0,
          'size_3xl': 0,
          'size_4xl': 0,
        }
      }
      state.cart[sku].size[size] += 1
    }
  }
}

export const actions = {
  addToCart({commit}, sku) {
  },
  removeFromCart({commit}, sku) {
  },

  increaseSize({commit}, sku, size) {
    commit('INCREASE_SIZE', sku, size)
  },
  decreaseSize({commit}, sku, size) {
  }
}

