<template>
  <div class="catalog-unit__details">
      <div class="catalog-unit__price">{{ item.price }} руб.</div>
      <a href="#" class="catalog-unit__to-cart"></a>
<!--      <div class="catalog-unit__sale">-->
<!--        <div class="catalog-unit__old-price">2000 руб.</div>-->
<!--        <div class="catalog-unit__sale-perc">-30%</div>-->
<!--      </div>-->
      <div class="catalog-unit__title">{{ item.sku }}</div>
      <div class="catalog-unit__title">
        <nuxt-link :to="localePath(`/product/${item.sku}`)">{{ item.model }}</nuxt-link>
      </div>
      <!--    <div>{{ item.colors }}</div>-->
      <div class="catalog-unit__category">
        <nuxt-link :to="localePath(item.category.link)">{{ item.category.title }}</nuxt-link>
      </div>
    </div>
</template>

<script>
export default {
  props: ['item']
}
</script>
