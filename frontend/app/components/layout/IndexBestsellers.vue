<template>
  <div class="bestseller">
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="heading heading--h2">
            <h2>Лидеры продаж</h2>
          </div>
          <hooper style="height: 100%" :settings="settings">
            <slide v-for="(item, index) in items" :key="index">
              <CatalogItem :item="item"/>
            </slide>
            <navigation slot="hooper-addons">
              <div slot="hooper-prev"
                   class="main-slider__button main-slider__button--prev slider-button slider-button--prev"></div>
              <div slot="hooper-next"
                   class="main-slider__button main-slider__button--next slider-button slider-button--next"></div>
            </navigation>
          </hooper>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {Hooper, Slide, Navigation, Pagination} from 'hooper';
import CatalogItem from "~/components/category/catalog-unit/CatalogItem";


export default {
  components: {Hooper, Slide, Navigation, Pagination, CatalogItem},

  props: ['items'],

  data() {
    return {
      settings: {
        itemsToShow: 1,
        mouseDrag: true,
        touchDrag: true,
        wheelControl: false,
        keysControl: false,
        infiniteScroll: true,

        breakpoints: {
          576: {
            itemsToShow: 2
          },
          768: {
            itemsToShow: 3
          },
          992: {
            itemsToShow: 4
          },
        }
      }
    }
  },


}
</script>

<style>
.bestseller .hooper-navigation {
  top: 100px;
  position: absolute;
  width: 100%;
}

.bestseller .hooper-navigation .hooper-prev, .bestseller .hooper-navigation .hooper-next {
  fill: white;
}

</style>
