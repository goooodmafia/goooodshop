<template>
  <div class="lang-toggle">
<!--    <nuxt-link-->
<!--      v-for="locale in availableLocales"-->
<!--      :class="['lang-toggle__item',{'lang-toggle__item&#45;&#45;active':isCurrentLocale(locale)}]"-->
<!--      :key="locale.code"-->
<!--      :to="switchLocalePath(locale.code)">{{ locale.name }}-->
<!--    </nuxt-link> -->
    <a
      v-for="locale in availableLocales"
      :class="['lang-toggle__item',{'lang-toggle__item--active':isCurrentLocale(locale)}]"
      :key="locale.code"
      :href="switchLocalePath(locale.code)">
      {{ locale.name }}
    </a>
  </div>
</template>

<script>

export default {
  computed: {
    availableLocales() {
      return this.$i18n.locales
    },
  },
  methods:{
    isCurrentLocale(locale){
      return locale.code === this.$i18n.locale
    }
  }
}
</script>
