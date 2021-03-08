<template>
  <div :class="['help__item',{'is-active': show}]" @click="toggle()">
    <div class="help__title">
      <div class="help__title-in">{{ item.title }}&nbsp;<span class="help__arrow"></span></div>
    </div>
    <div class="help__content" v-if="show">
      <div class="help__content-in" v-html="item.content"/>
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
