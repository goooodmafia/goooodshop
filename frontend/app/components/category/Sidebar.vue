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
        v-for="item in this.categories"
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
import CATEGORIES from '~/api/query/categories.graphql'


export default {

  components: {
    CategoryMenuItem
  },

  data() {
    return {
      categories: []
    }
  },

  props: ['filters'],

  apollo: {
    categories: {
      query: CATEGORIES,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
    }
  },

  computed: {
    currentpath() {
      const pathArray = this.$route.fullPath.split('/')
      return pathArray.slice(pathArray.indexOf('category') + 1)
    }
  }
}
</script>
