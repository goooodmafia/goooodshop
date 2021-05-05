<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breadcrumbs"/>
      </div>
    </template>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <div class="btn" @click="onClick">Купить</div>
          </div>
        </div>
        <div class="row">
          <div class="col">
            <div class="toggle-heading">
              <nuxt-link :to="localePath('/cart')" class="toggle-heading__item">Корзина</nuxt-link>
              <nuxt-link :to="localePath('/cart/wishes')" class="toggle-heading__item toggle-heading__item--active">Избранное</nuxt-link>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <CartWidget :items="cart"/>
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
        title: this.$t('page.wishes.title'),
        breadcrumbs: [],
      },
    }
  },

  computed:{
    ...mapState('cart', ['cart', 'wishes']),
  },
  methods: {
    onClick(sku) {
      this.$store.dispatch('cart/addToCart', {sku:'14-1817', size:'XS'})
      // this.$store.dispatch('cart/increaseSize', {sku:'14-1817', size:'XS'})
    }
  }
}

</script>
