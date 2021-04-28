<template>
  <MediaQueryProvider :queries="$options.queries" ssr fallback="md">
    <div style="display: flex;flex-direction: column;min-height: 100vh;">

      <Header></Header>

      <Nuxt/>

      <Footer :class="border?'footer':'footer--border'"></Footer>
      <transition name="fade">
        <div v-if="showOverlay" class="overlay" style="display: block;" @click="onOverlayClick()"/>
      </transition>
    </div>
  </MediaQueryProvider>
</template>

<script>
import {MediaQueryProvider} from "vue-component-media-queries";

import Header from "../components/layout/header/Header";
import Footer from "~/components/layout/Footer";


export default {

  queries: {
    // xs: '(max-width: 576px)',
    // sm: '(max-width: 768px)',
    // md: '(max-width: 992px)',
    // lg: '(max-width: 1200px)',
    // xl: '(max-width: 1400px)',
    // xxl: '(min-width: 1400px)',

    xs: '(min-width: 0px)',
    sm: '(min-width: 576px)',
    md: '(min-width: 768px)',
    lg: '(min-width: 992px)',
    xl: '(min-width: 1200px)',
    xxl: '(min-width: 1400px)',
  },

  components: {Header, Footer, MediaQueryProvider},

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

  methods: {
    onOverlayClick() {
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
