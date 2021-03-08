<template>
  <Wrapper>
    <div class="container">
      <div class="row">
        <Breadcrumbs :data="breadcrumbs()">
          <template v-slot:sidebar>
            <div class="col-md-auto col-sm-12">
              <Sidebar>
                <Filters :filters="filters"/>
              </Sidebar>
            </div>
          </template>

          <template>
            <Products :products="fetchproducts"/>
            <div ref="scrollmonitor">
              <div v-if="this.$apollo.loading" class="text-center">
                <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>
              </div>
            </div>
          </template>

        </Breadcrumbs>

      </div>
    </div>
  </Wrapper>
</template>
<script>
import CATEGORY from "~/api/query/category.graphql"
import FILTERS from "~/api/query/filters.graphql"
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"
import FETCHPRODUCTSCOUNT from "~/api/query/fetchproductscount.graphql"

import Wrapper from "~/components/layout/Wrapper";
import Products from "~/components/category/Products";
import Filters from "~/components/category/Filters";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";
import scrollMonitor from "scrollmonitor";


export default {
  name: 'category',

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
          colors: '',
          effects: ''
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
          effects: ''
        }
      },
    },
    fetchproductscount: {
      query: FETCHPRODUCTSCOUNT,
      variables() {
        return {
          route: this.getRoute(),
          colors: '',
          effects: ''
        }
      },
    },

    category: {
      query: CATEGORY,
      variables() {
        return {
          route: this.getRoute(),
          languageCode: this.$i18n.locale.toUpperCase(),
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
      if (this.fetchproductscount > this.fetchproducts.length) {
        this.page++
        this.$apollo.queries.fetchproducts.fetchMore({
          variables: {
            offset: this.pageSize * this.page
          },
          updateQuery: function (existing, incoming) {
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
      let effects = this.getEffects()

      this.page = 0

      this.$apollo.queries.filters.refetch({
        route: route,
        colors: colors,
        effects: effects,
      })

      this.$apollo.queries.fetchproductscount.refetch({
        route: route,
        colors: colors,
        effects: effects,
      })

      this.$apollo.queries.fetchproducts.refetch({
        route: route,
        languageCode: this.$i18n.locale.toUpperCase(),
        limit: this.pageSize,
        offset: 0,
        colors: colors,
        effects: effects,
      })
    },

    getColors() {
      var colorFilter = [];
      if (this.$data.filters) {
        for (let filter of this.$data.filters) {
          if (filter.name === 'color') {
            for (let color of filter.items) {
              if (color.value) {
                colorFilter.push(color.lable)
              }
            }
          }
        }
      }
      return colorFilter.join()
    },

    getRoute() {
      return this.$route.path
        .replace('\/' + this.$i18n.locale, '/')
        .replace('\/\/', '/')
    },

    getEffects() {
      var effectFilter = [];
      if (this.$data.filters) {
        for (let filter of this.$data.filters) {
          if (filter.name === 'effects') {
            for (let effect of filter.items) {
              if (effect.value) {
                effectFilter.push(effect.lable)
              }
            }
          }
        }
      }
      return effectFilter.join()
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

<style>
.fa-spin {
  -webkit-animation: fa-spin 0.5s infinite linear;
  animation: fa-spin 0.5s infinite linear;
}
</style>
