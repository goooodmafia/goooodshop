<template>
  <div class="filters">
    <div class="filters__headline">
      <span>Фильтры</span>
    </div>
    <div class="filters__content">

      <FilterComponent v-for="filter in filters" :filter="filter" :key="filter.title"/>

    </div>
  </div>
</template>
<script>
import FilterComponent from "./filters/FilterComponent";
import FILTERS from '~/api/query/filters'

export default {

  data(){
    return {
      filters:null
    }
  },
  components: {FilterComponent},
  apollo:{
    filters:{
      query:FILTERS,
      variables() {
        return {
          route: this.$route.path
            .replace('\/' + this.$i18n.locale, '/')
            .replace('\/\/', '/'),
        }
      }
    }
  },

  mounted() {
    this.$bus.$emit('filters_change', this.filters)
  },

  watch:{
    filters(newFilters, oldFilters) {
      console.log('filters event')
      this.$bus.$emit('filters_change', newFilters)
    }
  }
}
</script>
