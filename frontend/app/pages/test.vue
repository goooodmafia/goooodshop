<template>
  <Wrapper>
    <div class="container">
      <div class="row">
        <div class="col-md-auto col-sm-12">
          <Sidebar>
            <Filters :filters="filters"/>
          </Sidebar>
        </div>
        <Breadcrumbs :data="breadcrumbs()">
          <Products :products="fetchproducts"/>

          <div ref="scrollmonitor">
            <div v-if="this.$apollo.loading" class="text-center">
              <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>
            </div>
          </div>

          <div class="btn btn--orange" @click="fetchMoreProducts()">загрузить</div>
          <div class="btn btn--orange" @click="refetchProducts()">перезагрузить</div>
        </Breadcrumbs>
      </div>
    </div>
  </Wrapper>
</template>

<script>

import FILTERS from "~/api/query/filters.graphql"
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"
import FETCHPRODUCTSCOUNT from "~/api/query/fetchproductscount.graphql"

import Wrapper from "../components/layout/Wrapper";
import Products from "../components/category/Products";
import Filters from "../components/category/Filters";
import Breadcrumbs from "../components/layout/Breadcrumbs";
import Sidebar from "../components/category/Sidebar";
import scrollMonitor from "scrollmonitor";

export default {

  components: {Wrapper, Products, Filters, Breadcrumbs, Sidebar},

  data() {
    return {
      fetchproducts: [],
      fetchproductscount: 0,
      page: 1,
      pageSize: 12,
    }
  },

  apollo: {
    filters: {
      query: FILTERS,
      variables() {
        return {
          route: this.getRoute(),
        }
      },
      update: data => data.filters
    },

    fetchproducts: {
      query: FETCHPRODUCTS,
      variables() {
        return {
          route: this.getRoute(),
          languageCode: this.$i18n.locale.toUpperCase(),
          limit: this.pageSize,
          offset: 0,
          colors: '',
        }
      },
      // skip() {
      //   return this.skipProducts
      // },
    },
    fetchproductscount: {
      query: FETCHPRODUCTSCOUNT,
      variables() {
        return {
          route: this.getRoute(),
          colors: '',
        }
      },
    }
  },

  watch: {
    filters: {
      handler(val) {
        this.refetchProducts()
      },
      deep: true,
    }
  },

  methods: {
    fetchMoreProducts() {
      console.log('fetch check')
      console.log(this.fetchproductscount)
      console.log(this.fetchproducts.length)
      if (this.fetchproductscount > this.fetchproducts.length) {
        console.log('fetch')
        this.page++
        console.log(this.page)
        this.$apollo.queries.fetchproducts.fetchMore({
          variables: {
            offset: this.pageSize * this.page
          },
          updateQuery: function (existing, incoming) {
            console.log('update Query')
            console.log(this.fetchproducts)
            return {
              fetchproducts: [...existing.fetchproducts, ...incoming.fetchMoreResult.fetchproducts]
            }
          },
        })

      }
    },
    refetchProducts() {
      let route = this.getRoute()
      let colors = this.getColors()

      this.page = 0

      this.$apollo.queries.fetchproductscount.refetch({
        route: route,
        colors: colors,
      })

      this.$apollo.queries.fetchproducts.refetch({
        route: route,
        languageCode: this.$i18n.locale.toUpperCase(),
        limit: this.pageSize,
        offset: 0,
        colors: colors,
      })
    },

    getColors() {
      var colorFilter = [];
      for (let filter of this.$data.filters) {
        if (filter.name === 'color') {
          for (let color of filter.items) {
            if (color.value) {
              colorFilter.push(color.lable)
            }
          }
        }
      }
      return colorFilter.join()
    },

    getRoute() {
      return '/category/muzhskoe/futbolki-korotkii-rukav'
      // return this.$route.path
      //   .replace('\/' + this.$i18n.locale, '/')
      //   .replace('\/\/', '/')
    },
    breadcrumbs() {
      return {
        title: this.category && this.category.name,
        breadcrumbs: this.category && this.category.breadcrumbs
      }
    },
  },
  mounted() {
    const elementWatcher = scrollMonitor.create(this.$refs.scrollmonitor);
    elementWatcher.enterViewport(() => {
      if (this.fetchproducts) {
        this.fetchMoreProducts();
      }
    });
  }
}
</script>
