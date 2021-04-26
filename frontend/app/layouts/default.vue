<template>
  <div style="display: flex;flex-direction: column;min-height: 100vh;">

    <Header></Header>

    <Nuxt/>

    <Footer :class="border?'footer':'footer--border'"></Footer>
    <transition name="fade">
      <div v-if="showOverlay" class="overlay" style="display: block;" @click="onOverlayClick()"/>
    </transition>
  </div>
</template>

<script>

import Header from "../components/layout/header/Header";
import Footer from "~/components/layout/Footer";

export default {
  components: {Header, Footer},

  data() {
    return {
      showOverlay: false
    }
  },

  computed: {
    border() {
      return !this.$route.matched.map((r) => {
        return (r.components.default.options ? r.components.default.options.footerBorder : false)
      })[0]
    },
  },

  mounted() {
    this.$bus.$on('MOBILEMENU_HIDE', () => {
      this.showOverlay = false
    })

    this.$bus.$on('MOBILEMENU_SHOW', () => {
      this.showOverlay = true
    })
  },

  methods:{
    onOverlayClick(){
      this.$bus.$emit('MOBILEMENU_HIDE')
    }
  }

}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  display: block;
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
{
  display: block;
  opacity: 0;
}
</style>
