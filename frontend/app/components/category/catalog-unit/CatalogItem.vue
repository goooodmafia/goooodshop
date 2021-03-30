<template>


  <div
    class="catalog-unit catalog-unit--catalog"
    @mouseover="hover = true"
    @mouseleave="hover = false"
  >
    <!-- <Figure :item="item"/>-->

    <div :class="['catalog-unit__figure',{'my-catalog-z':hover}]">
      <div v-if="item.new" class="catalog-unit__label">new</div>
      <div v-if="item.hit" class="catalog-unit__label">hit</div>
      <nuxt-link :to="localePath(`/product/${item.sku}`)">
        <hooper
          ref="slider_main"
          :settings="options_main"
          :group="item.sku"
          style="width:160px;height: 200px;"
        >
          <slide>
            <img class="my-catalog-slider-main-img" :src="item.thumbnail"/>
          </slide>
          <slide v-for="(img, index) in item.mediaFiles" :key="index">
            <img class="my-catalog-slider-main-img" :src="img.src"/>
          </slide>
        </hooper>
      </nuxt-link>
    </div>

    <div :class="['catalog-unit__details', {'my-catalog-z':hover}]">
      <div class="catalog-unit__price">1530 руб.</div>
      <a href="#" class="catalog-unit__to-cart"></a>
      <div class="catalog-unit__sale">
        <div class="catalog-unit__old-price">2000 руб.</div>
        <div class="catalog-unit__sale-perc">-30%</div>
      </div>
      <span>{{ item.sku }}</span>
      <div class="catalog-unit__title">
        <nuxt-link :to="localePath(`/product/${item.sku}`)">{{ item.model }}</nuxt-link>
      </div>
      <!--    <div>{{ item.colors }}</div>-->
      <div class="catalog-unit__category">
        <nuxt-link :to="localePath(item.category.link)">{{ item.category.title }}</nuxt-link>
      </div>
    </div>

    <div v-if="hover" :class="['catalog-unit__hover', 'load', {show:hover}]">
      <div class="my-catalog-slider-nav">
        <hooper
          ref="slider_nav"
          :settings="options_nav"
          :group="item.sku"
          style="width:70px; height:321px; top:13px; left:17px;"
        >
          <slide>
            <div @click="$refs.slider_nav.slideTo(0)">
              <img class="my-catalog-slider-nav-img" :src="item.thumbnail"/>
            </div>
          </slide>
          <slide v-for="(img, index) in item.mediaFiles" :key="index">
            <div @click="$refs.slider_nav.slideTo(index+1)">
              <img class="my-catalog-slider-nav-img" :src="img.src"/>
            </div>
          </slide>
          <navigation slot="hooper-addons">
            <div slot="hooper-prev"></div>
          </navigation>
        </hooper>
      </div>
    </div>

  </div>

</template>

<script>
import Details from "./Details";
import {Hooper, Navigation, Slide} from "hooper";

export default {
  components: {Details, Hooper, Slide, Navigation},
  props: ["item"],

  data() {
    return {
      hover: false,
      options_main: {
        mouseDrag: false,
        touchDrag: false,
        wheelControl: false,
        keysControl: false,
        infiniteScroll: true,
      },
      options_nav: {
        vertical: true,
        itemsToShow: 3,
        infiniteScroll: true,
      },
    }
  }
}
</script>

<style lang="scss">
.catalog-unit__figure {
  min-width: 160px;
  min-height: 200px;
  background-color: rgba(255, 255, 255, 0.2);
}

.catalog-unit__hover {
  background-color: transparent;
}

.my-catalog-slider-nav {
  background-color: #1f4ea3;
  height: 100%;
  width: 87px;
  left: 0px;
}

.my-catalog-slider-nav-img {
  width: 70px;
  height: 94px;
  object-fit: cover;
}

.my-catalog-slider-main-img {
  width: 160px;
  height: 200px;
  object-fit: cover;
}

.my-catalog-z {
  z-index: 11;
}
</style>
