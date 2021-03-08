<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container" v-html="delivery_about"/>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "../components/layout/Wrapper";
import Breadcrumbs from "../components/layout/Breadcrumbs";

export default {

  name: 'Delivery',

  components: {Breadcrumbs, Wrapper,},

  data() {
    return {
      delivery_about: null,

      breacrumbs: {
        title: this.$t('page.delivery.title'),
        breadcrumbs: [],
      },
    }
  },
  async asyncData({app}) {
    const delivery_about = await import(`~/content/delivery/delivery_about_${app.i18n.locale}.md`)
    return {
      delivery_about: delivery_about.html,
    }
  }
}
</script>
