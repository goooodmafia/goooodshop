<template>
  <div class="catalog-unit__figure">
    <div v-if="item.new" class="catalog-unit__label">new</div>
    <div v-if="item.hit" class="catalog-unit__label">hit</div>
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
