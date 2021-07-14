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


    <td class="basket__cell">
      <div class="basket__headline">Размеры</div>
      <template v-for="s in item.size">
        <div class="basket__value" v-if="s.count > 0">{{ s.size }}</div>
      </template>
    </td>

    <td class="basket__cell">
      <div class="basket__headline">Количество</div>
      <template v-for="s in item.size">
        <div class="basket__value" v-if="s.count > 0">
          <SizeCountSpinbuttonWidget :size="s.size" :sku="item.sku" :price="product.price"/>
        </div>
      </template>
    </td>

    <td class="basket__cell">
      <div class="basket__headline">Сумма</div>
      <template v-for="s in item.size">
        <div class="basket__value" v-if="s.count > 0">{{ s.count * product.price }}</div>
      </template>
    </td>

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
import SizeCountSpinbuttonWidget from "./SizeCountSpinbuttonWidget";


export default {

  components: {SizeCountSpinbuttonWidget},

  props: ['item'],

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
          sku: this.item.sku,
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
