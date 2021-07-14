<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breadcrumbs"/>
      </div>
    </template>
    <template>
      <div class="container">
<!--        <div class="row">-->
<!--          <div class="col">-->
<!--            <div class="gd-btn" @click="onClick()">Купить</div>-->
<!--          </div>-->
<!--        </div>-->
        <div class="row">
          <div class="col">
            <div class="toggle-heading">
              <nuxt-link :to="localePath('cart')" class="toggle-heading__item toggle-heading__item--active">Корзина</nuxt-link>
              <nuxt-link :to="localePath('wishes')" class="toggle-heading__item">Избранное</nuxt-link>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <CartWidget :items="products"/>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>

import Wrapper from "../../components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";
import CatalogItem from "../../components/category/catalog-unit/CatalogItem";
import CartWidget from "../../components/cart/CartWidget";
import {mapState} from "vuex";


export default {

  name: 'cart',

  components: {CartWidget, CatalogItem, Wrapper, Breadcrumbs, Sidebar},

  data() {
    return {
      breadcrumbs: {
        title: this.$t('page.cart.title'),
        breadcrumbs: [],
      },
    }
  },

  computed:{
    ...mapState('cart', ['products', 'wishes']),
  },

  methods: {

    onClick() {
      this.$store.dispatch('cart/increaseSize', {sku:'14-1817', price:999, size:'XS', count:2})
      this.$store.dispatch('cart/increaseSize', {sku:'14-1817', price:999, size:'S', count:3})
      this.$store.dispatch('cart/increaseSize', {sku:'14-1817', price:999, size:'M', count:4})

      this.$store.dispatch('cart/increaseSize', {sku:'14-1773', price:999, size:'L', count:2})
      this.$store.dispatch('cart/increaseSize', {sku:'14-1773', price:999, size:'S', count:3})
      this.$store.dispatch('cart/increaseSize', {sku:'14-1773', price:999, size:'M', count:4})
    }
  }
}

</script>
