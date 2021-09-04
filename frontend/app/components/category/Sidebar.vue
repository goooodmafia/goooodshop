<template>
  <div class="sidebar">
    <div class="catalog-menu-toggle" @click="dropdown=!dropdown">
      <div class="catalog-menu-toggle__burger">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <span class="catalog-menu-toggle__text">Каталог</span>
    </div>
    <!-- BEGIN catalog-menu -->
    <ul class="catalog-menu" :style="{display: dropdown ? 'block':'none'}">
      <category-menu-item
        v-for="item in this.items"
        :item="item"
        :showchildren="true"
        :currentpath="currentpath"
        :level="0"
        :key="item.name"/>
      <li class="catalog-menu__item">
        <nuxt-link :to="localePath('/news')" class="catalog-menu__link">Новинки</nuxt-link>
      </li>
    </ul>

    <slot></slot>

  </div>
</template>
<script>

import CategoryMenuItem from './CategoryMenuItem.vue'


export default {

  components: {
    CategoryMenuItem
  },

  props: ['filters', 'currentpath', 'items'],

  data() {
    return {
      dropdown: false
    }
  },
}
</script>
