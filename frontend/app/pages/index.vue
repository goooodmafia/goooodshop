<template>
  <Wrapper class="main-content--index">

    <template v-slot:header>
      <IndexBanner :items="banners"/>
      <NewsIndex :items="news.items"/>
    </template>

    <template>
      <section class="section section--gradi section--negative-indent">
        <IndexBestsellers :items="products.items"/>
        <div class="wholesale" v-html="wholesale"/>
      </section>
    </template>

    <template v-slot:footer>
      <div class="about about--footer about--footer-index" v-html="about"/>
    </template>

  </Wrapper>
</template>


<script>

import Wrapper from "../components/layout/Wrapper";
import IndexBanner from "../components/layout/IndexBanner";
import NewsIndex from "../components/news/NewsIndex";
import IndexBestsellers from "../components/layout/IndexBestsellers";
// import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"
import PRODUCTS from "~/api/query/products.graphql"
import NEWS from "~/api/query/news.graphql"

export default {
  name: 'index',
  footerBorder: true,
  components: {
    IndexBestsellers,
    NewsIndex,
    IndexBanner,
    Wrapper,
  },

  data() {
    return {
      products: {items: []},
      news: [],
    }
  },

  async asyncData({app}) {
    let banners = await import(`~/content/index/index_banner_${app.i18n.locale}.json`)
    let wholesale = await import(`~/content/index/wholesale_${app.i18n.locale}.md`)
    let about = await import(`~/content/index/about_${app.i18n.locale}.md`)

    return {
      banners: banners.default,
      wholesale: wholesale.html,
      about: about.html,
    }
  },

  apollo: {
    news: {
      query: NEWS,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          pageSize: 4,
          page: 1,
        }
      },
    },
    products: {
      query: PRODUCTS,
      fetchPolicy: 'network-only',
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          pageSize: 12,
          page: 1,
          route: '',
          sizes: '',
          colors: '',
          effects: '',
          tags: '',
          hit: true,
          new: false,
          query: '',
          order: 'Random',
        }
      },
    },
    //
    // fetchproducts: {
    //   query: FETCHPRODUCTS,
    //   variables() {
    //     return {
    //       languageCode: this.$i18n.locale.toUpperCase(),
    //       perPage: 12,
    //       page: 1,
    //       route: '',
    //       sizes:'',
    //       colors: '',
    //       effects: '',
    //       tags: '',
    //       query: '',
    //       order: 'Random'
    //     }
    //   },
    // },

  }

}
</script>
<style>

/*.main-slider .hooper-navigation button {*/
/*  background: url(/static/img/arrow.svg) 0 0 no-repeat;*/
/*  background-size: cover;*/
/*  position: absolute;*/
/*  top: 50%;*/
/*  z-index: 5;*/
/*  width: 33px;*/
/*  height: 61px;*/
/*  cursor: pointer;*/
/*}*/

/*.main-slider .hooper-navigation button.hooper-prev {*/
/*  !*left: -60px;*!*/
/*  -webkit-transform: scaleX(-1);*/
/*  -ms-transform: scaleX(-1);*/
/*  transform: scaleX(-1);*/
/*}*/
/*.main-slider .hooper-navigation button.hooper-next {*/
/*  !*right: -60px;*!*/
/*  background-position: 100% 0;*/
/*}*/


/*.bestseller .hooper-navigation button svg {*/
/*  display: none;*/
/*}*/

</style>
