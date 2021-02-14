<template>
  <div class="container">
    <div class="menu">

      <div class="menu__item" v-for="item in this.categories">
        <nuxt-link :to="localePath(item.path)" class="menu__link">{{ item.name }}</nuxt-link>
        <div class="menu-dropdown">
          <div class="menu-dropdown__item" v-for="child in item.children">
            <nuxt-link :to="localePath(child.path)" class="menu-dropdown__link">{{ child.name }}</nuxt-link>
          </div>
        </div>
        <div class="dropdown-toggle"></div>
      </div>

    </div>
  </div>
</template>
<script>
import CATEGORIES from '~/api/query/categories.graphql'

export default {

  data() {
    return {
      categories: []
    }
  },

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

}
</script>
