<template>
  <div class="menu__item">
    <nuxt-link @click.native="onLinkClick" :to="localePath(item.path)" class="menu__link">{{ item.name }}</nuxt-link>
    <div v-if="dropdown" class="menu-dropdown" style="display: block">
      <div class="menu-dropdown__item" v-for="(child,index) in item.children" :key="index">
        <nuxt-link
          @click.native="onLinkClick"
          :to="localePath({path:child.path, hash:child.hash})"
          class="menu-dropdown__link"
        >{{ child.name }}
        </nuxt-link>
      </div>
    </div>
    <div v-if="item.children.length>0" class="dropdown-toggle" @click="dropdown=!dropdown"></div>
  </div>
</template>
<script>
export default {
  props: ['item'],
  data() {
    return {
      // mobileShow: false,
      dropdown: false
    }
  },

  methods:{
    onLinkClick() {
      this.$bus.$emit('MOBILEMENU_HIDE')
    }
  }
}
</script>

