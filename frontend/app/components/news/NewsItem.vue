<template>

  <div class="col-12 col-sm-6 news__item">
    <nuxt-link
      v-if="item.link"
      class="news__figure"
      :to="localePath(item.link)"
      :style="{ backgroundImage: `url(${item.image})` }"
    >
      <div class="news__date">{{ item.viewDate }}</div>
      <div class="news__actions">
        <nuxt-link class="gd-btn" :to="localePath(item.link)">Купить</nuxt-link>
      </div>
    </nuxt-link>
    <div
      v-else
      class="news__figure"
      :style="{ backgroundImage: `url(${item.image})` }"
    >
      <div class="news__date">{{ item.viewDate }}</div>
    </div>
    <div class="news__title">
      <nuxt-link v-if="item.link" :to="localePath(item.link)">{{ item.title }}</nuxt-link>
      <template v-else>{{ item.title }}</template>
    </div>
    <div class="news__text">{{ item.description }}</div>
  </div>

</template>
<script>
export default {
  props: ['item']
}
</script>
