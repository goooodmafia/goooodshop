<template>
  <div class="news news--index">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <div class="heading heading--h2">
            <h2>Новинки</h2>
          </div>
        </div>
        <div class="col">
          <div class="news__all">
            <nuxt-link :to="localePath('/news')">все номинки</nuxt-link>
          </div>
        </div>
      </div>
    </div>
    <client-only>
      <NewsWidget :items="items"/>
    </client-only>
  </div>
</template>
<script>
import NewsWidget from "./NewsWidget";

export default {
  components: {NewsWidget},

  props: ['items']
}
</script>
