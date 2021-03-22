<template>
  <Wrapper class="main-content--index">

    <template v-slot:header>
      <IndexBanner :items="banners"/>
      <NewsIndex/>
    </template>

    <template>
      <section class="section section--gradi section--negative-indent">
        <IndexBestsellers :items="fetchproducts"/>
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
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"

export default {
  footerBorder: true,
  components: {
    IndexBestsellers,
    NewsIndex,
    IndexBanner,
    Wrapper,
  },

  data() {
    return {
      fetchproducts: [],
    }
  },

  async asyncData({app}) {
    const banners = await import(`~/content/index/index_banner_${app.i18n.locale}.json`)
    const wholesale = await import(`~/content/index/wholesale_${app.i18n.locale}.md`)
    const about = await import(`~/content/index/about_${app.i18n.locale}.md`)

    return {
      banners: banners.default,
      wholesale: wholesale.html,
      about: about.html,
    }
  },

  apollo: {
    fetchproducts: {
      query: FETCHPRODUCTS,
      variables() {
        return {
          route: "",
          languageCode: this.$i18n.locale.toUpperCase(),
          limit: 12,
          offset: 0,
          colors: '',
          effects: '',
          tags: ''
        }
      },
    },
  }

}
</script>
<style>

.hooper-navigation button {
  background: url(/img/arrow.svg) 0 0 no-repeat;
  background-size: cover;
  position: absolute;
  top: 50%;
  z-index: 5;
  width: 33px;
  height: 61px;
  cursor: pointer;
}

.hooper-navigation button.hooper-prev {
  /*left: -60px;*/
  -webkit-transform: scaleX(-1);
  -ms-transform: scaleX(-1);
  transform: scaleX(-1);
}
.hooper-navigation button.hooper-next {
  /*right: -60px;*/
  background-position: 100% 0;
}
.bestseller .hooper-navigation button.hooper-prev {
    top: 55px;
}
.bestseller .hooper-navigation button.hooper-next {
    top: 86px;
}

.bestseller .hooper-navigation button svg {
  display: none;
}
</style>

