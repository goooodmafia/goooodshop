<template>
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

    <slot/>

  </div>
</template>

<script>



export default {



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
