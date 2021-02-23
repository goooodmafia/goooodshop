<template>

  <div class="catalog">
    <div class="catalog__in">
      <ProductItem v-for="item in products" :item="item" :key="item.sku"/>
    </div>
  </div>

</template>
<script>
import ProductItem from "./ProductItem";
export default {
  components: {ProductItem},
  props:['products']
}
</script>
