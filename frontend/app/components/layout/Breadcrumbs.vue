<template>
  <div class="container">
    <div class="row">
      <div class="col-md-auto col-sm-12">
        <Sidebar/>
      </div>

      <div class="col">
        <div class="heading heading--h2 heading--breadcrumb">
          <h1>{{ data.title }}</h1>
        </div>
        <nav aria-label="breadcrumb">
          <ol class="mybreadcrumb">
            <li class="mybreadcrumb__item" v-for="(item, index) in breadcrumbs">
              <nuxt-link :to="localePath(item.link)" :class="['mybreadcrumb__link']">{{ item.title }}</nuxt-link>
            </li>
            <li class="mybreadcrumb__item active">{{ data.title }}</li>
          </ol>
        </nav>

        <Sorter/>

        <Products/>

      </div>
    </div>
  </div>
</template>

<script>

import Sidebar from "../category/Sidebar";
import Sorter from "../category/Sorter";
import Products from "../category/Products";

export default {

  components: {Products, Sorter, Sidebar},

  props: [
    'data'
  ],
  computed: {
    breadcrumbs() {
      var b = [{title: 'Главная', link: this.localePath('index')}]
      if (this.data.breadcrumbs) {
        return b.concat(this.data.breadcrumbs)
      } else {
        return b
      }
    },
  }
}
</script>
