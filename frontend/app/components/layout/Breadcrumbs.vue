<template>
  <div class="row">
    <slot name="sidebar"/>
    <div class="col">
      <div class="heading heading--h2 heading--breadcrumb" v-if="showTitle">
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
      <slot name="default"/>
    </div>
    <slot name="right"/>
  </div>
</template>

<script>


export default {


  props: {
    data:{},
    showTitle: {
      type:Boolean,
      default:true,
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
