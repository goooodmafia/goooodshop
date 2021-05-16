<template>
  <Wrapper>
    <div class="container">
      <Breadcrumbs :data="breadcrumbs()">
        <template v-slot:sidebar>
          <div class="col-md-auto col-sm-12">
            <Sidebar :currentpath="currentpath" :items="categories">
              <Filters :filters="products.filters"/>

              <!--              <div class="filters">-->
              <!--                <div class="filters__headline">-->
              <!--                  <span>Фильтры</span>-->
              <!--                </div>-->
              <!--                <div class="filters__content">-->
              <!--                  <FilterComponent v-for="filter in filters" :filter="filter" :key="filter.title"/>-->
              <!--                  <template v-for="filter in filters" :filter="filter">-->
              <!--                    <div class="filters__item accordion__item is-active" v-if="filter.items && filter.items.length>1">-->
              <!--                      <div class="filters__title accordion__title">{{ filter.title }}</div>-->
              <!--                      <div class="filters__options accordion__content" style="display: block;">-->
              <!--                        <div class="f-options">-->
              <!--                          <div class="f-options__item" v-for="item in filter.items">-->
              <!--                            <input :id="filter.title+'_'+item.lable" type="checkbox" class="f-options__checkbox"-->
              <!--                                   :value="item.lable" v-model="item.value">-->
              <!--                            &lt;!&ndash;          <label :for="filter.title+'_'+item.lable" class="f-options__label">{{ item.lable }}<template v-if="item.count"><span class="f-options__count">&NonBreakingSpace;({{item.count}})</span></template></label>&ndash;&gt;-->
              <!--                            <label-->
              <!--                              :for="filter.title+'_'+item.lable"-->
              <!--                              class="f-options__label">{{ item.lable }}<span-->
              <!--                              class="f-options__count">&NonBreakingSpace;({{ item.count }})</span></label>-->
              <!--                          </div>-->
              <!--                        </div>-->
              <!--                      </div>-->
              <!--                    </div>-->
              <!--                  </template>-->
              <!--                </div>-->
              <!--              </div>-->
            </Sidebar>
          </div>
        </template>


        <template>
          <!--          <Sorter :order="order"/>-->
          <Sorter/>

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
import CATEGORY from "~/api/query/category.graphql"
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
      filters: {},
      products: {
        items: [],
        filters: []
      },
      productscount: 0,
      page: 1,
      pageSize: 12,


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
    // filters: {
    //   query: FILTERS,
    //   variables() {
    //     return {
    //       route: this.getRoute(),
    //       sizes: this.getFilter('size'),
    //       colors: this.getFilter('color'),
    //       effects: this.getFilter('effects'),
    //       query: this.getQuery(),
    //     }
    //   },
    //   update: data => data.filters
    // },

    category: {
      query: CATEGORY,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          route: this.getRoute(),
        }
      }
    },

    products: {
      query: PRODUCTS,
      fetchPolicy: 'network-only',
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
        }
      },
      // update(data) {
      //   console.log(data)
      //   this.filters = data.products.filters
      //   return data.products
      // },
      // skip: true,
      // manual: true,
      // result({data,loading}){
      //   if (!loading) {
      //     this.filters = data.products.filters
      //     this.products = data.products
      //   }
      // }
    },

  },

  // watch: {
  // filters: {
  //   handler(val) {
  //     console.log('filters change')
  //     this.refetchProducts()
  //   },
  //   deep: true,
  // },
  // size:{
  //   handler(val) {
  //     console.log('size change')
  //     console.log(val)
  //   },
  //   deep: true,
  // }
  // },

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
                filters: fetchMoreResult.products.filters,
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

      console.log('refetch')

      // let route = this.getRoute()
      // let colors = this.getFilter('color')
      // let effects = this.getFilter('effects')
      // let sizes = this.getFilter('size')
      // let query = this.getQuery()
      // let order = this.getOrder()

      // this.$apollo.queries.products.skip = false
      // await this.$apollo.queries.products.refetch({
      //
      //   languageCode: this.$i18n.locale.toUpperCase(),
      //   perPage: this.pageSize,
      //   page: 1,
      //   route: route,
      //   sizes: sizes,
      //   colors: colors,
      //   effects: effects,
      //   tags: '',
      //   query: query,
      //   order: order,


      // languageCode: this.$i18n.locale.toUpperCase(),
      // pageSize: this.pageSize,
      // page: 1,
      // route: this.getRoute(),
      // sizes: this.getFilter('size'),
      // colors: this.getFilter('color'),
      // effects: this.getFilter('effects'),
      // tags: '',
      // query: this.getQuery(),
      // order: this.getOrder(),
      // })
      // this.$apollo.queries.products.skip = true

      //
      // this.$apollo.queries.filters.refetch({
      //   route: this.getRoute(),
      //   sizes: this.getFilter('size'),
      //   colors: this.getFilter('color'),
      //   effects: this.getFilter('effects'),
      //   query: this.getQuery(),
      // })
    },

    getFilter(filter_name) {
      if (this.filters[filter_name]) {
        // for (let filter of this.filters) {
        //   if (filter.name === filter_name) {
        //     for (let item of filter.items) {
        //       if (item.value) {
        //         result_filter.push(item.lable)
        //       }
        //     }
        //   }
        // }
        return this.filters[filter_name].join()
      } else {
        return ''
      }
    },

    getQuery() {
      if (this.$route.query.search === undefined || this.$route.query.search === null) {
        this.filters['query'] = ''
      } else {
        this.filters['query'] = this.$route.query.search
      }
      return this.filters['query']
    },

    getRoute() {
      return this.$route.path
        .replace('\/' + this.$i18n.locale, '/')
        .replace('\/\/', '/')
    },

    getOrder() {
      if (this.filters['order']) {
        return this.filters['order']
      } else {
        return 'OrderInc'
      }
    },

    breadcrumbs() {

      let title = ''
      let breadcrumbs = []
      let query = this.getQuery()
      let route = this.currentpath

      if (query !== '') {
        if (route.join() !== '') {
          title = `Результат поиска "${query}" в категории "${this.category && this.category.name}":`
        } else {
          title = `Результат поиска "${query}":`
        }
        breadcrumbs = []
      } else {
        if (route.join() !== '') {
          title = this.category && this.category.name
          breadcrumbs = this.category && this.category.breadcrumbs.slice(0, -1)
        } else {
          title = `Каталог`
          breadcrumbs = []
        }
      }

      // title = `Каталог`
      // breadcrumbs = []


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
      this.refetchProducts()
    })

    this.$bus.$on('NEXT_PAGE', () => {
      this.page += 1
      this.refetchProducts()
    })
    this.$bus.$on('SET_ORDER', (order) => {
      this.filters['order'] = order
      // this.refetchProducts()
      this.$apollo.queries.products.refetch(
        {
          sizes: this.getFilter('size'),
          colors: this.getFilter('color'),
          effects: this.getFilter('effects'),
          order: this.getOrder()
        }
      )
    })

    this.$bus.$on('CLEAR_FILTERS', () => {
      console.log('filters cleared')
      this.filters = {}
    })

    this.$bus.$on('REFETCH', () => {
      this.refetchProducts()
    })
    this.$bus.$on('FETCH_MORE', () => {
      this.fetchMoreProducts();
    })

    this.$bus.$on('SET_FILTER', (filter, lable, value) => {
      console.log('set filter ' + filter + ' ' + lable + ' ' + value)


      if (!this.filters[filter]) {
        this.filters[filter] = []
      }
      if (value) {
        this.filters[filter].push(lable)
      } else {
        this.filters[filter].indexOf(lable) !== -1 && this.filters[filter].splice(this.filters[filter].indexOf(lable), 1)
      }

      this.$apollo.queries.products.refetch(
        {
          sizes: this.getFilter('size'),
          colors: this.getFilter('color'),
          effects: this.getFilter('effects'),
          order: this.getOrder()
        }
      )
    })

  },

  computed: {
    currentpath() {
      const pathArray = this.$route.path.split('/')
      return pathArray.slice(pathArray.indexOf('category') + 1)
    },
    categories() {
      return this.$store.state.categories.list
    },
    size() {
      // console.log(this.filters)
      // console.log(this.$data)
      return this.$data.filters['size']
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
