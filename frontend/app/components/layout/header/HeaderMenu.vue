<template>
  <div class="container">
    <portal to="mobile-portal" :disabled="!mobileShow" :order="1">
      <div class="menu">

        <HeaderMenuItem :item="item" v-for="(item,index) in this.categories.concat(this.menu)" :key="index"/>


<!--        <div class="menu__item" v-for="item in this.categories.concat(this.menu)">-->
<!--          <nuxt-link :to="localePath(item.path)" class="menu__link">{{ item.name }}</nuxt-link>-->

<!--            <div v-if="dropdown" class="menu-dropdown" style="display: block">-->
<!--              <div class="menu-dropdown__item" v-for="child in item.children">-->
<!--                <nuxt-link-->
<!--                  :to="localePath({path:child.path, hash:child.hash})"-->
<!--                  class="menu-dropdown__link"-->
<!--                >{{ child.name }}-->
<!--                </nuxt-link>-->
<!--              </div>-->
<!--            </div>-->

<!--          <div class="dropdown-toggle" @click="dropdown=!dropdown"></div>-->
<!--        </div>-->
      </div>
    </portal>
  </div>
</template>
<script>
import CATEGORIES from '~/api/query/categories.graphql'
import HeaderMenuItem from "./HeaderMenuItem";

export default {
  components: {HeaderMenuItem},
  data() {
    return {
      menu: [
        {name: 'Купить оптом', path: 'wholesale', slug: '', children: []},
        {
          name: 'Бренд GOOD', path: 'brand', slug: '', children: [
            {name: 'Оптовый прайс-лист', path: 'wholesale', slug: '', hash: ''},
            {name: 'Помощь оптовикут', path: 'wholesale', slug: '', hash: 'wholesale-help'},
            {name: 'Список транспортных', path: 'wholesale', slug: '', hash: 'wholesale-delivery'},
          ]
        },
        {name: 'Новинки', path: 'news', slug: '', children: []},
      ],
      categories: [],

      mobileShow: false,
      dropdown: false
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
      // update:function(categories){
      //   const
      //   return categories.concat(menu)
      // },
    }
  },

  mounted() {
    this.$bus.$on('MOBILEMENU_SHOW', () => {
      this.mobileShow = true
    })
    this.$bus.$on('MOBILEMENU_HIDE', () => {
      this.mobileShow = false
    })
  }

}
</script>

<style>
  .slide-enter-active, .slide-leave-active { transition: height .5s; }
  .slide-enter, .slide-leave-active { height: 0; }
</style>
