<template>

  <div class="catalog">
    <div class="catalog__in">
      <ProductItem v-for="item in products" :item="item" :key="item.sku"/>
    </div>
  </div>

</template>
<script>
import ProductItem from "./ProductItem";
import PRODUCTS from "~/api/query/products.graphql"

export default {
  components: {ProductItem},

  data(){
    return{
      totalCount:null
    }
  },

  apollo: {
    products: {
      query: PRODUCTS,
      variables() {
        return {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
      update(data) {
        this.totalCount = data.products.totalCount
        return data.products.results
      }

    }
  }
}
</script>
