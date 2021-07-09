<template>
  <tr class="basket__row">

    <td class="basket__wrap basket__cell">
      <div class="basket__figure">
        <a href="#">
          <b-img :src="product.thumbnail" alt="" width="110" height="145"/>
        </a>
      </div>
      <div class="basket__details">
        <div class="basket__headline">Наименование</div>
        <div class="basket__title">
          <nuxt-link :to="localePath(`/product/${product.sku}`)">{{ product.model }}</nuxt-link>
        </div>
        <div class="basket__article">Артикул: {{ product.sku }}</div>
        <div class="basket__color">Цвет: Черный</div>
      </div>
    </td>
    <td class="basket__price basket__cell">
      <div class="basket__headline">Цена за единицу</div>
      <div class="basket__value">{{ product.price }} руб.</div>
    </td>

    <SizeCountWidget :item="item" :price="product.price"/>

    <td class="basket__to-fav basket__cell">
      <a href="#" class="to-favourites">В избранное</a>
    </td>
    <td class="basket__del basket__cell">
      <b-button @click="removeFromCart(product.sku)" class="gd-btn gd-btn--delete" title="Удалить"></b-button>
    </td>

  </tr>
</template>
<script>
import PRODUCT from "~/api/query/product.graphql"
import SizeCountWidget from "./SizeCountWidget";


export default {
  components: {SizeCountWidget},

  props: ['item', 'sku'],

  data() {
    return {
      product: {
        thumbnail: null
      }
    }
  },

  apollo: {
    product: {
      query: PRODUCT,
      variables() {
        return {
          sku: this.sku,
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
    }
  },
  methods:{
    removeFromCart(sku){
      console.log(sku)
      this.$store.dispatch(
          'cart/removeFromCart',
        {sku:sku}
      )
    }
  },
}
</script>
