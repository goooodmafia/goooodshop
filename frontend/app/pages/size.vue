<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container" v-html="size_about"/>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "../components/layout/Wrapper";
import Breadcrumbs from "../components/layout/Breadcrumbs";

export default {

  name: 'Size',

  components: {Breadcrumbs, Wrapper,},

  data() {
    return {
      size_about: null,

      breacrumbs: {
        title: this.$t('page.size.title'),
        breadcrumbs: [],
      },
    }
  },
  async asyncData({app}) {
    const size_about = await import(`~/content/size/size_about_${app.i18n.locale}.md`)
    return {
      size_about: size_about.html,
    }
  }
}
</script>


