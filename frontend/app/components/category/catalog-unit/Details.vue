<template>
  <div class="catalog-unit__details">
    <div class="catalog-unit__price">1530 руб.</div>
    <a href="#" class="catalog-unit__to-cart"></a>
    <div class="catalog-unit__sale">
      <div class="catalog-unit__old-price">2000 руб.</div>
      <div class="catalog-unit__sale-perc">-30%</div>
    </div>
    <div class="catalog-unit__title">
      <nuxt-link :to="localePath(`/product/${item.sku}`)">{{ item.model }}</nuxt-link>
    </div>
    <div>{{ item.colors }}</div>
    <div class="catalog-unit__category"><a href="#">Мужское / Футболки короткий рукав</a></div>
  </div>
</template>

<script>
export default {
  props:['item']
}
</script>
