<template>
  <div
    class="catalog-unit catalog-unit--catalog"
    @mouseover="hover = true"
    @mouseleave="hover = false"
  >

    <Figure :item="item" :class="{'my-catalog-z':show}">
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
    </Figure>

    <Details :item="item" :class="{'my-catalog-z':show}"/>

    <div v-if="hover" :class="['catalog-unit__hover', 'load', {show:show}]">
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
import Figure from "./Figure"
import {Hooper, Navigation, Slide} from "hooper";

export default {
  components: {Details, Figure, Hooper, Slide, Navigation},
  props: {
    item: {},
  },

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
  },
  computed: {
    show() {
      return this.hover
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
  position: relative;
}
</style>
