<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <NewsWidget :items="news.items"/>

      <div ref="newsscrollmonitor">
        <div v-if="this.$apollo.loading" class="text-center">
          <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>
        </div>
      </div>

    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import NewsWidget from "../../components/news/NewsWidget";
import NEWS from "~/api/query/news.graphql"
import scrollMonitor from "scrollmonitor";

export default {

  name: 'news',

  components: {NewsWidget, Breadcrumbs, Wrapper},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.news.title'),
        breadcrumbs: [],
      },
      page: 1,
      news: [],
    }
  },

  apollo: {
    news: {
      query: NEWS,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          pageSize: 12,
          page: 1,
        }
      },
    }
  },

  methods: {
    fetchMoreNews() {
      if (this.news.hasNext) {
        this.page++
        this.$apollo.queries.news.fetchMore({
          variables: {
            page: this.page
          },
          updateQuery: function (existing, incoming) {
            return {
              news: [...existing.news, ...incoming.fetchMoreResult.news]
            }
          },
        })
      }
    }
  },
  mounted() {
    const elementWatcher = scrollMonitor.create(this.$refs.newsscrollmonitor);
    elementWatcher.enterViewport(() => {
      if (this.news) {
        this.fetchMoreNews();
      }
    });
  },
}
</script>
