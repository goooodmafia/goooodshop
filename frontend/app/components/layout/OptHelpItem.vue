<template>
  <div :class="['wholesale-help__item',{'is-active': show}]" >
    <div class="wholesale-help__title" @click="toggle()">{{ item.title }}</div>
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
