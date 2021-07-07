<template>
  <div class="basket">
    <div class="basket__in">
      <table class="basket__table">
        <CartWidgetItem v-for="(item,index) in items" :item="item" :sku="index" :key="index"/>
      </table>
    </div>
  </div>
</template>
<script>

import CartWidgetItem from "./CartWidgetItem";
export default {
  components: {CartWidgetItem},
  props:['items']
}
</script>
