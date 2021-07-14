<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container" v-html="brand_about"/>
      <div class="container" v-html="brand_principles"/>
      <div class="container">
        <div class="row">
          <div class="col pb-4">
            <hooper :settings="settings" style="height: auto">
              <slide v-for="(item,key) in banners" :key="key">
                <b-img :src="item.img" fluid class="h-100 w-100"></b-img>
              </slide>

              <navigation slot="hooper-addons">
                <div slot="hooper-prev"
                     class="main-slider__button main-slider__button--prev slider-button slider-button--prev"></div>

                <div slot="hooper-next"
                     class="main-slider__button main-slider__button--next slider-button slider-button--next"></div>
              </navigation>
              <pagination slot="hooper-addons"></pagination>

            </hooper>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "../components/layout/Wrapper";
import Breadcrumbs from "../components/layout/Breadcrumbs";
import OptHelpItem from "../components/layout/OptHelpItem";
import {Hooper, Navigation, Pagination, Slide} from "hooper";

export default {

  name: 'Brand',

  components: {Breadcrumbs, Wrapper, Hooper, Slide, Navigation, Pagination},

  data() {
    return {
      brand_about: null,
      brand_principles: null,

      breacrumbs: {
        title: this.$t('page.brand.title'),
        breadcrumbs: [],
      },

      settings: {
        mouseDrag: true,
        touchDrag: true,
        wheelControl: false,
        keysControl: false,
        infiniteScroll: true
      }

    }
  },
  async asyncData({app}) {
    const brand_about = await import(`~/content/brand/brand_about_${app.i18n.locale}.md`)
    const brand_principles = await import(`~/content/brand/brand_principles_${app.i18n.locale}.md`)
    const banners = await import(`~/content/brand/banners.json`)
    return {
      brand_about: brand_about.html,
      brand_principles: brand_principles.html,
      banners: banners.default,
    }
  }
}
</script>
