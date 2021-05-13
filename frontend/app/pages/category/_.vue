<template>
  <Wrapper>
    <div class="container">
      <Breadcrumbs :data="breadcrumbs()">
        <template v-slot:sidebar>
          <div class="col-md-auto col-sm-12">
            <Sidebar :currentpath="currentpath" :items="categories">
              <Filters :filters="filters"/>
            </Sidebar>
          </div>
        </template>


        <template>
          <Sorter :order="order"/>

          <div class="catalog">
            <div class="catalog__in">
              <div class="catalog__item" v-for="item in products.items">
                <CatalogItemHover :item="item" :key="item.sku"/>
              </div>
            </div>
          </div>

          <Scrollmonitor :products_has_more="products.hasNext"/>

        </template>
      </Breadcrumbs>
    </div>
  </Wrapper>
</template>
<script>
// import CATEGORY from "~/api/query/category.graphql"
// import CATEGORIES from '~/api/query/categories.graphql'
import FILTERS from "~/api/query/filters.graphql"
import PRODUCTS from "~/api/query/products.graphql"
// import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"
// import FETCHPRODUCTSCOUNT from "~/api/query/fetchproductscount.graphql"

import Wrapper from "~/components/layout/Wrapper";
import Filters from "~/components/category/Filters";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";
import CatalogItemHover from "~/components/category/catalog-unit/CatalogItemHover"
import Sorter from "../../components/category/Sorter";
import Scrollmonitor from "../../components/category/Scrollmonitor";


export default {
  name: 'category',

  components: {Scrollmonitor, Sorter, Wrapper, Filters, Breadcrumbs, Sidebar, CatalogItemHover},

  // watchQuery: ['search'],

  data() {
    return {
      products: {
        items: []
      },
      productscount: 0,
      page: 1,
      pageSize: 12,
      order: 'OrderInc'

      // myvariables: {
      //   route: this.getRoute(),
      //   sizes: '',
      //   colors: '',
      //   effects: '',
      //   query: '',
      //
      // },
    }
  },

  apollo: {
    filters: {
      query: FILTERS,
      variables() {
        return {
          route: this.getRoute(),
          sizes: this.getFilter('size'),
          colors: this.getFilter('color'),
          effects: this.getFilter('effects'),
          query: this.getQuery(),
        }
      },
      update: data => data.filters
    },

    products: {
      query: PRODUCTS,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          pageSize: this.pageSize,
          page: 1,
          route: this.getRoute(),
          sizes: this.getFilter('size'),
          colors: this.getFilter('color'),
          effects: this.getFilter('effects'),
          tags: '',
          query: this.getQuery(),
          order: this.getOrder(),
          // languageCode: this.$i18n.locale.toUpperCase(),
          //   pageSize: this.pageSize,
          //   page: 1,
          //   route: this.getRoute(),
          //   sizes: '',
          //   colors: '',
          //   effects: '',
          //   tags: '',
          //   query: '',
          //   order: "OrderInc"
        }
      },
    },

    // fetchproducts: {
    //   query: FETCHPRODUCTS,
    //   variables() {
    //     return {
    //       languageCode: this.$i18n.locale.toUpperCase(),
    //       perPage: this.pageSize,
    //       page: 1,
    //       route: this.getRoute(),
    //       sizes: '',
    //       colors: '',
    //       effects: '',
    //       tags: '',
    //       query: '',
    //       order: "OrderInc"
    //     }
    //   },
    // },

    // fetchproductscount: {
    //   query: FETCHPRODUCTSCOUNT,
    //   variables() {
    //     return {
    //       route: this.getRoute(),
    //       sizes: '',
    //       colors: '',
    //       effects: '',
    //       query: '',
    //     }
    //   },
    // },

    // categories: {
    //   query: CATEGORIES,
    //   variables() {
    //     return {
    //       languageCode: this.$i18n.locale.toUpperCase(),
    //     }
    //   },
    // },

    // category: {
    //   query: CATEGORY,
    //   variables() {
    //     return {
    //       route: this.getRoute(),
    //       languageCode: this.$i18n.locale.toUpperCase(),
    //     }
    //   },
    // }
  },

  watch: {
    // filters: {
    //   handler(val) {
    //     this.refetchProducts()
    //   },
    //   deep: true,
    // }
  },

  methods: {
    fetchMoreProducts() {
      // console.log('fetchMore')
      if (this.products.hasNext) {
        this.page++
        this.$apollo.queries.products.fetchMore({
          variables: {
            page: this.page
          },
          updateQuery: function (previousResult, {fetchMoreResult}) {
            return {
              products: {
                pages: fetchMoreResult.products.pages,
                hasNext: fetchMoreResult.products.hasNext,
                hasPrev: fetchMoreResult.products.hasPrev,
                total: fetchMoreResult.products.total,
                items: [...previousResult.products.items, ...fetchMoreResult.products.items],
                __typename: "ProductCountableType"
              }
            }
          }
        })
      }
      //   if (this.fetchproductscount > this.fetchproducts.length) {
      //     this.page++
      //     this.$apollo.queries.fetchproducts.fetchMore({
      //       variables: {
      //         page: this.page
      //       },
      //       updateQuery: function (existing, incoming) {
      //         return {
      //           fetchproducts: [...existing.fetchproducts, ...incoming.fetchMoreResult.fetchproducts]
      //         }
      //       },
      //     })
      //   }
    },

    refetchProducts() {

      // console.log('refetch')

      let route = this.getRoute()
      let colors = this.getFilter('color')
      let effects = this.getFilter('effects')
      let sizes = this.getFilter('size')
      let query = this.getQuery()
      let order = this.getOrder()

      this.$apollo.queries.products.refetch({
        route: route,
        languageCode: this.$i18n.locale.toUpperCase(),
        perPage: this.pageSize,
        page: 1,
        sizes: sizes,
        colors: colors,
        effects: effects,
        query: query,
        order: order
      })

      this.$apollo.queries.filters.refetch({
        route: this.getRoute(),
        sizes: this.getFilter('size'),
        colors: this.getFilter('color'),
        effects: this.getFilter('effects'),
        query: this.getQuery(),
      })

      // console.log('refetch')
      //
      // let route = this.getRoute()
      // let colors = this.getFilter('color')
      // let effects = this.getFilter('effects')
      // let sizes = this.getFilter('size')
      // let query = this.getQuery()
      // let route = this.myvariables.route
      // let colors = this.myvariables.colors
      // let effects = this.myvariables.effects
      // let sizes = this.myvariables.sizes
      // let query = this.myvariables.query

      // console.log(route)
      // console.log(colors)
      // console.log(effects)
      // console.log(sizes)
      // console.log(query)
      //
      // this.page = 1
      //
      // this.$apollo.queries.filters.refetch(
      //   {
      //     route: route,
      //     sizes: sizes,
      //     colors: colors,
      //     effects: effects,
      //     query: query
      //   })
      //
      // this.$apollo.queries.fetchproductscount.refetch({
      //   route: route,
      //   sizes: sizes,
      //   colors: colors,
      //   effects: effects,
      //   query: query,
      // })
      //
      // this.$apollo.queries.fetchproducts.refetch({
      //   route: route,
      //   languageCode: this.$i18n.locale.toUpperCase(),
      //   perPage: this.pageSize,
      //   page: 1,
      //   sizes: sizes,
      //   colors: colors,
      //   effects: effects,
      //   query: query,
      //   order: this.myvariables.myorder
      // })
    },

    getFilter(filter_name) {
      // console.log('getfilter')
      var result_filter = [];
      if (this.$data.filters) {
        for (let filter of this.$data.filters) {
          if (filter.name === filter_name) {
            for (let item of filter.items) {
              if (item.value) {
                result_filter.push(item.lable)
              }
            }
          }
        }
      }
      return result_filter.join()
    },

    getQuery() {
      if (this.$route.query.search === undefined || this.$route.query.search === null) {
        return ''
      } else {
        return this.$route.query.search
      }
    },

    getRoute() {
      return this.$route.path
        .replace('\/' + this.$i18n.locale, '/')
        .replace('\/\/', '/')
    },

    getOrder() {
      return this.order
    },

    breadcrumbs() {

      let title = ''
      let breadcrumbs = []
      let query = this.getQuery()
      let route = this.currentpath

      // if (query !== '') {
      //   if (route.join() !== '') {
      //     title = `Результат поиска "${query}" в категории "${this.category && this.category.name}":`
      //   } else {
      //     title = `Результат поиска "${query}":`
      //   }
      //   breadcrumbs = []
      // } else {
      //   if (route.join() !== '') {
      //     title = this.category && this.category.name
      //     breadcrumbs = this.category && this.category.breadcrumbs.slice(0, -1)
      //   } else {
      //     title = `Каталог`
      //     breadcrumbs = []
      //   }
      // }

      title = `Каталог`
      breadcrumbs = []


      return {
        title: title,
        breadcrumbs: breadcrumbs
      }
    },
  },

  mounted() {

    // console.log('mounted')

    this.$bus.$on('SET_PAGE', (page) => {
      this.page = page
    })

    this.$bus.$on('NEXT_PAGE', () => {
      this.page += 1
    })
    this.$bus.$on('SET_ORDER', (order) => {
      this.order = order
    })
    this.$bus.$on('REFETCH', () => {
      this.refetchProducts()
    })
    this.$bus.$on('FETCH_MORE', () => {
      this.fetchMoreProducts();
    })

  },

  computed: {
    currentpath() {
      const pathArray = this.$route.path.split('/')
      return pathArray.slice(pathArray.indexOf('category') + 1)
    },
    categories() {
      return this.$store.state.categories.list
    }
  }
}
</script>

<style>
.fa-spin {
  -webkit-animation: fa-spin 0.5s infinite linear;
  animation: fa-spin 0.5s infinite linear;
}
</style>
