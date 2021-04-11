<template>
  <div class="sidebar">
    <div class="catalog-menu-toggle">
      <div class="catalog-menu-toggle__burger">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <span class="catalog-menu-toggle__text">Каталог</span>
    </div>
    <!-- BEGIN catalog-menu -->
    <ul class="catalog-menu">
      <category-menu-item
        v-for="item in this.items"
        :item="item"
        :showchildren="true"
        :currentpath="currentpath"
        :level="0"
        :key="item.name"/>
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



  props: ['filters', 'currentpath' , 'items'],
}
</script>
