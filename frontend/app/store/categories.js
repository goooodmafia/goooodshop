import CATEGORIES from '~/api/query/categories.graphql'
import FILTERS from "~/api/query/filters.graphql"

export const state = () => ({
  list: [],
})

export const mutations = {
  SET_CATEGORIES(state, categories) {
    state.list = categories
  },
}

export const actions = {
  async loadCategories({commit}) {
    let client = this.app.apolloProvider.defaultClient
    const {data} = await client.query({
      query: CATEGORIES,
      variables: {
        languageCode: this.$i18n.locale.toUpperCase()
      }
    })
    commit('SET_CATEGORIES', data.categories)
  },
}
