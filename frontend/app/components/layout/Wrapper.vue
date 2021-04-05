<template>

  <main class="main-content">
    <div class="header-class">
      <ContentBlock :items="content['header_top']"/>
      <slot name="header"></slot>
      <ContentBlock :items="content['header_bottom']"/>
    </div>

    <div class="default-class">
      <ContentBlock :items="content['default_top']"/>
      <slot name="default"></slot>
      <ContentBlock :items="content['default_bottom']"/>
    </div>

    <div class="footer-class">
      <ContentBlock :items="content['default_bottom']"/>
      <slot name="footer"></slot>
      <ContentBlock :items="content['footer_bottom']"/>
    </div>
  </main>

</template>
<script>
// import Header from "./Header";
// import Footer from "./Footer";

import CONTENT from "~/api/query/content.graphql"
import ContentBlock from "./ContentBlock";

export default {
  components: {
    ContentBlock,
    // Footer,
    // Header,
  },

  data() {
    return {
      content: {
        header_top: [],
        header_bottom: [],
        default_top: [],
        default_bottom: [],
        footer_top: [],
        footer_bottom: [],
      }
    }
  },

  apollo: {
    content: {
      query: CONTENT,
      variables() {
        return {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
      update(data) {
        return data
      }
    },
  }

}
</script>
