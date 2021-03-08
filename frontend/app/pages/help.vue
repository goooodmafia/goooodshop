<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <div class="help">
              <HelpItem :item="item" v-for="(item,key) in help" :key="key"/>
            </div>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "../components/layout/Wrapper";
import Breadcrumbs from "../components/layout/Breadcrumbs";
import HelpItem from "../components/layout/HelpItem";

export default {

  name: 'Help',

  components: {Breadcrumbs, Wrapper, HelpItem},

  data() {
    return {
      help: null,

      breacrumbs: {
        title: this.$t('page.help.title'),
        breadcrumbs: [],
      },
    }
  },
  async asyncData({app}) {
    // const help_about = await import(`~/content/help/help_about_${app.i18n.locale}.md`)
    const help = await import(`~/content/help/help_${app.i18n.locale}.json`)
    return {
      // help_about: help_about.html,
      help: help.default,
    }
  }
}
</script>
