<template>
  <li class="catalog-menu__item">
    <nuxt-link :to="localePath(item.path)" :class="['catalog-menu__link', {'current':show()}]">{{ item.name }}</nuxt-link>
    <ul class="catalog-menu__in" v-if="item.children.length > 0">
      <category-menu-item
        v-for="child in item.children"
        :item="child"
        :showchildren="showchildren"
        :currentpath="currentpath"
        :level="level+1"
        :key="child.name"/>
    </ul>
  </li>
</template>
<script>

export default {
  name: 'category-menu-item',
  props: [
    'item',
    'showchildren',
    'currentpath',
    'level'
  ],
  // data() {
  //   return {show: false}
  // },

  methods: {
    show() {
      return this.currentpath[this.level] === this.item.slug
    },
  },


}
</script>

<style>
.catalog-menu__in {
  padding: 0px 0px 0px 22px;
}
</style>
