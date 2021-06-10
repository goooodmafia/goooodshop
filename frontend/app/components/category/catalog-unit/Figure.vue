<template>
  <div class="catalog-unit__figure">
    <div v-if="item.new" class="catalog-unit__label">NEW</div>
    <div v-if="item.hit" class="catalog-unit__label">HIT</div>
    <nuxt-link :to="localePath(`/product/${item.sku}`)">
      <slot></slot>
    </nuxt-link>
  </div>
</template>
<script>

export default {
  props: {
    item: {},
  },
}
</script>
