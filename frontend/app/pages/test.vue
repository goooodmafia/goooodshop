<template>
  <Wrapper>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>###test</h1>
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
