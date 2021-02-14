<template>
  <Wrapper>
<!--    <div v-if="error">{{ error }}</div>-->
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

  data() {
    return {
      category: {
        link: "index",
        breadcrumbs: []
      },
      error: null,
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
      error(error) {
        this.error = JSON.stringify(error.message);
      }
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
