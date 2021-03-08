<template>
  <div :class="['wholesale-help__item',{'is-active': show}]" @click="toggle()">
    <div class="wholesale-help__title">{{ item.title }}</div>
    <div class="wholesale-help__content" v-if="show">
      <div class="wholesale-help__content-in" v-html="item.content"/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false
    }
  },
  props:['item'],

  methods: {
    toggle() {
      this.show = !this.show
    }
  }
}
</script>
