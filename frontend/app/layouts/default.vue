<template>
  <div style="display: flex;flex-direction: column;min-height: 100vh;">

    <Header></Header>

    <Nuxt/>

    <Footer :class="border?'footer':'footer--border'"></Footer>
  </div>
</template>

<script>

import Header from "../components/layout/header/Header";
import Footer from "~/components/layout/Footer";

export default {
  components: {Header, Footer},


  computed: {
    border() {
      return !this.$route.matched.map((r) => {
        return (r.components.default.options ? r.components.default.options.footerBorder : false)
      })[0]
    },
  },

}
</script>
