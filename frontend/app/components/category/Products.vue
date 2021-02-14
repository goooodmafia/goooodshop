<template>

  <div class="catalog">
    <div class="catalog__in">
      <ProductItem v-for="item in fetchproducts" :item="item" :key="item.sku"/>
    </div>
<!--    <b-btn @click="fetchMore">Загрузить</b-btn>-->
    <div ref="scrollmonitor">
      <div v-if="this.$apollo.queries.fetchproducts.loading" class="text-center">
        <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>
      </div>
    </div>
  </div>


</template>
<script>
import ProductItem from "./ProductItem";
import PRODUCTS from "~/api/query/products.graphql"
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"

import scrollMonitor from 'scrollmonitor';

export default {
  components: {ProductItem},

  data() {
    return {
      fetchproducts: [],
      totalCount: null,
      page: 0,
      pageSize: 12
    }
  },

  apollo: {
    // products: {
    //   query: PRODUCTS,
    //   variables() {
    //     return {
    //       route: this.$route.path
    //         .replace('\/' + this.$i18n.locale, '/')
    //         .replace('\/\/', '/'),
    //       languageCode: this.$i18n.locale.toUpperCase(),
    //       limit: this.pageSize,
    //       offset: 0,
    //     }
    //   },
    //   update(data) {
    //     this.totalCount = data.products.totalCount
    //     return data.products.results
    //   }
    //
    // }

    fetchproducts: {
      query: FETCHPRODUCTS,
      variables() {
        return {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
          languageCode: this.$i18n.locale.toUpperCase(),
          limit: this.pageSize,
          offset: 0,
        }
      },
    }
  },

  methods: {
    fetchMore() {
      console.log('fetch page' + this.page)
      this.page++;
      this.$apollo.queries.fetchproducts.fetchMore({
        variables: {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
          languageCode: this.$i18n.locale.toUpperCase(),
          limit: this.pageSize,
          offset: (this.page * this.pageSize),
        },
        updateQuery: (existing, incoming) => ({
          fetchproducts: [...existing.fetchproducts, ...incoming.fetchMoreResult.fetchproducts]
        }),
      })
    },
  },
  mounted() {
    // const el = document.getElementById('sensor');
    const elementWatcher = scrollMonitor.create(this.$refs.scrollmonitor);
    elementWatcher.enterViewport(() => {
      if (this.fetchproducts) {
        this.fetchMore();
      }
    });
  }
}
</script>

<style>
.fa-spin {
  -webkit-animation: fa-spin 0.5s infinite linear;
  animation: fa-spin 0.5s infinite linear;
}
</style>
