<template>
  <nuxt-link :to="localePath('cart')" class="cart cart--header">
    <div class="cart__in">
      <div class="cart__item">{{ getCartTitle }}</div>
      <div v-if="cartCount>0" class="cart__item cart__item--sum">1500 руб.</div>
    </div>
  </nuxt-link>
</template>

<script>

import {mapGetters} from "vuex";

export default {

  computed: {
    ...mapGetters('cart', ['cartCount',]),

    getCartTitle() {
      if (this.cartCount < 1) {
        return this.$t('layout.header.cart.title0')
      } else if (this.cartCount === 1) {
        return this.$t('layout.header.cart.title1', {count: this.cartCount})
      } else if (this.cartCount < 5) {
        return this.$t('layout.header.cart.title2', {count: this.cartCount})
      } else if (this.cartCount >= 5) {
        return this.$t('layout.header.cart.title5', {count: this.cartCount})
      }


    }
  }
}
</script>
