<template>
  <Wrapper>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>###test</h1>
            <p>xs: {{ mediaQueries.xs }}</p>
            <p>sm: {{ mediaQueries.sm }}</p>
            <p>md: {{ mediaQueries.md }}</p>
            <p>lg: {{ mediaQueries.lg }}</p>
            <p>xl: {{ mediaQueries.xl }}</p>
            <p>xxl: {{ mediaQueries.xxl }}</p>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>


</template>

<script>

import Wrapper from "~/components/layout/Wrapper";
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"

export default {
  // middleware: 'auth',

  inject: ['mediaQueries'],

  components: {Wrapper},

  apollo:{
    fetchproducts: {
      query: FETCHPRODUCTS,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          perPage: 12,
          page: 1,
          route: '/category',
          colors: '',
          effects: '',
          tags: '',
          query:'',
          order:'Random'
        }
      },
    },
  }
}
</script>
