<template>
  <div class="basket">
    <div class="basket__in" v-if="items.length > 0">
      <table class="basket__table">
        <CartWidgetItem v-for="(item,index) in items" :item="item" :key="index"/>
        <tr>
          <td colspan="3" class="basket__cell basket__cell--total"></td>
          <td class="basket__cell basket__cell--total basket__total-count">{{ getTotalCount }} шт.</td>
          <td class="basket__cell basket__cell--total basket__total-sum">{{ getTotalPrice }} руб.</td>
          <td colspan="2" class="basket__cell basket__cell--total basket__actions">
            <a href="#" class="gd-btn btn--orange-bg btn--to-order">Оформить</a>
          </td>
        </tr>
      </table>
    </div>
    <h4 class="my-5" v-else>Корзина пуста</h4>
  </div>
</template>
<script>

import CartWidgetItem from "./CartWidgetItem";
import {mapGetters, mapState} from "vuex";

export default {
  components: {CartWidgetItem},
  props: ['items'],

  computed: {
    ...mapGetters("cart", ['getTotalCount', 'getTotalPrice'])
  }
}
</script>
