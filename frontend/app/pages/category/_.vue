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

          <div class="sorting sorting--catalog">
            <div class="sorting__title">Сортировать по:</div>
            <div class="sorting__list">
              <div
                @click="sort(item)"
                v-for="item in sortingItems"
                :class="[
                  'sorting__item',
                  {'sorting__item--decrease':item.sortOrder},
                  {'sorting__item--increase':!item.sortOrder},
                  {'active':item.active}
                  ]"
              >{{ item.title }}
              </div>
            </div>
          </div>

          <div class="catalog">
            <div class="catalog__in">
              <div class="catalog__item" v-for="item in fetchproducts">
                <CatalogItemHover :item="item" :key="item.sku"/>
              </div>
            </div>
          </div>

          <div ref="scrollmonitor">
            <div v-if="this.$apollo.loading" class="text-center">
              <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>
            </div>
          </div>
        </template>

      </Breadcrumbs>

    </div>
    <!--    </div>-->
  </Wrapper>
</template>
<script>
import CATEGORY from "~/api/query/category.graphql"
import CATEGORIES from '~/api/query/categories.graphql'
import FILTERS from "~/api/query/filters.graphql"
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"
import FETCHPRODUCTSCOUNT from "~/api/query/fetchproductscount.graphql"

import Wrapper from "~/components/layout/Wrapper";
import Filters from "~/components/category/Filters";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";
import CatalogItemHover from "~/components/category/catalog-unit/CatalogItemHover"
import scrollMonitor from "scrollmonitor";


export default {
  name: 'category',

  components: {Wrapper, Filters, Breadcrumbs, Sidebar, CatalogItemHover},

  data() {
    return {
      fetchproducts: [],
      fetchproductscount: 0,
      page: 1,
      pageSize: 12,
      sortingItems: [
        {
          title: 'новизне',
          sortEnum: 'Order',
          active: true,
          sortOrder: true
        },
        {
          title: 'цене',
          sortEnum: 'Price',
          active: false,
          sortOrder: true
        },
        {
          title: 'скидкам',
          sortEnum: 'Sale',
          active: false,
          sortOrder: true
        }
      ],
      myorder: 'OrderInc'
    }
  },

  apollo: {
    filters: {
      query: FILTERS,
      variables() {
        return {
          route: this.getRoute(),
          sizes: '',
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
          languageCode: this.$i18n.locale.toUpperCase(),
          perPage: this.pageSize,
          page: 1,
          route: this.getRoute(),
          sizes: '',
          colors: '',
          effects: '',
          tags: '',
          query: '',
          order: "OrderInc"
        }
      },
    },
    fetchproductscount: {
      query: FETCHPRODUCTSCOUNT,
      variables() {
        return {
          route: this.getRoute(),
          sizes: '',
          colors: '',
          effects: ''
        }
      },
    },

    categories: {
      query: CATEGORIES,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
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
            page: this.page

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
      let sizes = this.getSizes()

      this.page = 1

      this.$apollo.queries.filters.refetch({
        route: route,
        sizes: sizes,
        colors: colors,
        effects: effects,
      })

      this.$apollo.queries.fetchproductscount.refetch({
        route: route,
        sizes: sizes,
        colors: colors,
        effects: effects,
      })

      this.$apollo.queries.fetchproducts.refetch({
        route: route,
        languageCode: this.$i18n.locale.toUpperCase(),
        perPage: this.pageSize,
        page: 1,
        sizes: sizes,
        colors: colors,
        effects: effects,
        query: '',
        order: this.myorder
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

    getSizes() {
      var sizeFilters = [];
      if (this.$data.filters) {
        for (let sfilter of this.$data.filters) {
          if (sfilter.name === 'size') {
            for (let s of sfilter.items) {
              if (s.value) {
                sizeFilters.push(s.lable)
              }
            }
          }
        }
      }
      return sizeFilters.join()
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
        breadcrumbs: this.category && this.category.breadcrumbs.slice(0, -1)
      }
    },

    sort(current) {
      if (current.active) {
        current.sortOrder = !current.sortOrder
      } else {
        current.sortOrder = true
      }

      this.sortingItems.forEach((element) => {
        element.active = false
      })

      current.active = true

      this.page = 1
      let s = current.sortOrder ? 'Inc' : 'Dec'

      // console.log(s)
      this.myorder = current.sortEnum + s
      // console.log(this.order)

      this.refetchProducts()


      // }else {
      //   current.active = true
      //   current.sortOrder = true
      // }
    }
  },
  mounted() {
    const elementWatcher = scrollMonitor.create(this.$refs.scrollmonitor);
    elementWatcher.enterViewport(() => {
      if (this.fetchproducts) {
        this.fetchMoreProducts();
      }
    });
  },

  computed: {
    currentpath() {
      const pathArray = this.$route.fullPath.split('/')
      return pathArray.slice(pathArray.indexOf('category') + 1)
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
