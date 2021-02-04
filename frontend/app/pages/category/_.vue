<template>
  <Wrapper>

    <Breadcrumbs :data="breadcrumbs()"/>

  </Wrapper>
</template>
<script>
import Wrapper from "../../components/layout/Wrapper";
import CATEGORY from "~/api/query/category.graphql"
import Breadcrumbs from "../../components/layout/Breadcrumbs";

export default {
  name: 'category',

  components: {Breadcrumbs, Wrapper},

  data(){
    return{
      category: {
        link:"index",
        breadcrumbs:[]
      }
    }
  },

  apollo: {
    category: {
      query: CATEGORY,
      variables() {
        return {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
      // update(data) {
      //   return data
      // }
    }
  },

  methods: {
    breadcrumbs() {
      return {
        title: this.category && this.category.name,
        breadcrumbs: this.category && this.category.breadcrumbs
      }
    }
  }
}
</script>
