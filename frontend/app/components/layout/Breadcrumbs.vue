<template>
  <div class="row">
    <slot name="sidebar"/>
    <div class="col">

      <template v-if="showBack">
        <div class="product-head">
          <div class="gd-btn gd-btn--back" @click="$router.back()" v-if="showBack">Назад</div>
          <div class="heading heading--h2 heading--breadcrumb" v-if="showTitle"><h1>{{ data.title }}</h1></div>
          <nav aria-label="breadcrumb breadcrumb--product">
            <ol class="mybreadcrumb">
              <li class="mybreadcrumb__item" v-for="(item, index) in breadcrumbs">
                <nuxt-link :to="localePath(item.link)" :class="['mybreadcrumb__link']">{{ item.title }}</nuxt-link>
              </li>
              <li class="mybreadcrumb__item active">{{ data.title }}</li>
            </ol>
          </nav>
        </div>
      </template>

      <template v-else>
        <div class="heading heading--h2 heading--breadcrumb" v-if="showTitle"><h1>{{ data.title }}</h1></div>
        <nav aria-label="breadcrumb">
            <ol class="mybreadcrumb">
              <li class="mybreadcrumb__item" v-for="(item, index) in breadcrumbs">
                <nuxt-link :to="localePath(item.link)" :class="['mybreadcrumb__link']">{{ item.title }}</nuxt-link>
              </li>
              <li class="mybreadcrumb__item active">{{ data.title }}</li>
            </ol>
          </nav>
      </template>

      <slot name="left"/>

      <slot name="default"/>
    </div>
    <slot name="right"/>
  </div>
</template>

<script>


export default {


  props: {
    data: {},
    showTitle: {
      type: Boolean,
      default: true,
    },
    showBack: {
      type: Boolean,
      default: false,
    }
  },
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
