<template>
  <Wrapper>
    <!--<div v-if="error">{{ error }}</div>-->

    <div class="container">
      <div class="row">
        <div class="col-md-auto col-sm-12">
          <Sidebar>
            <Filters :filters="filters"/>
          </Sidebar>
        </div>

        <Breadcrumbs :data="breadcrumbs()">

          <Sorter/>
          <Products :products="fetchproducts"/>

          <div ref="scrollmonitor">
            <div v-if="this.$apollo.queries.fetchproducts.loading" class="text-center">
              <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>
            </div>
          </div>

        </Breadcrumbs>
      </div>
    </div>

  </Wrapper>
</template>
<script>

import CATEGORY from "~/api/query/category.graphql"
import FILTERS from "~/api/query/filters.graphql"
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"

import Wrapper from "../../components/layout/Wrapper";
import Breadcrumbs from "../../components/layout/Breadcrumbs";
import Sidebar from "../../components/category/Sidebar";
import Sorter from "../../components/category/Sorter";
import Products from "../../components/category/Products";
import Filters from "../../components/category/Filters";
import scrollMonitor from "scrollmonitor";

export default {
  name: 'category',

  components: {Breadcrumbs, Wrapper, Products, Sorter, Sidebar, Filters,},

  data() {
    return {
      category: {
        link: "index",
        breadcrumbs: []
      },
      error: null,
      filters: null,
      skipProducts: true,
      fetchproducts: [],
      totalCount: null,
      page: 0,
      pageSize: 12
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
      error(error) {
        this.error = JSON.stringify(error.message);
      }
    },
    filters: {
      query: FILTERS,
      variables() {
        return {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
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
      skip() {
        return this.skipProducts
      },
    }
  },

  watch: {
    filters: {
      handler(val) {

        console.log(this.$data.fetchproducts)
        this.$data.skipProducts = false
        this.setProducts([])
        this.$data.page = 0

        // console.log('update filters')

        this.fetchMore()

      },
      deep: true
    }
  },

  computed: {},

  methods: {
    getColorFilters() {
      console.log('get colors')
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
      console.log(colorFilter.join())
      return colorFilter.join()
    },
    getRoute() {
      return this.$route.path
        .replace('\/' + this.$i18n.locale, '/')
        .replace('\/\/', '/')
    },

    breadcrumbs() {
      return {
        title: this.category && this.category.name,
        breadcrumbs: this.category && this.category.breadcrumbs
      }
    },

    setProducts(products) {
      console.log(this.fetchproducts)
      this.fetchproducts = products
      console.log(this.fetchproducts)
    },

    fetchMore() {
      // console.log('fetch more page' + this.page)
      if (!this.skipProducts) {

        this.$apollo.queries.fetchproducts.fetchMore({
          variables: {
            route: this.getRoute(),
            languageCode: this.$i18n.locale.toUpperCase(),
            limit: this.pageSize,
            offset: (this.page * this.pageSize),
            colors: this.getColorFilters()
          },
          updateQuery: function(existing, incoming) {
            console.log('update Query')
            console.log(this.fetchproducts)
            return {
              fetchproducts: [...existing.fetchproducts, ...incoming.fetchMoreResult.fetchproducts]
            }
          },
        })
        this.page++;
      }
    },
  },

  mounted() {
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
