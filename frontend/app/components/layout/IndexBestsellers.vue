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
              <navigation slot="hooper-addons"></navigation>
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

  data(){
    return{
      settings:{
        itemsToShow:4,
        mouseDrag: true,
        touchDrag: true,
        wheelControl: false,
        keysControl: false,
        infiniteScroll: true
      }
    }
  },


}
</script>
