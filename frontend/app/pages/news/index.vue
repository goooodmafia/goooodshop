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
            <h1>### News</h1>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";

export default {

  name: 'review',

  components: {Breadcrumbs, Wrapper},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.news.title'),
        breadcrumbs: [],
      },
    }
  },
}
</script>
