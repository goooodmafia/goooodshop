<template>
  <div class="filters">
    <div class="filters__headline" @click="dropdown=!dropdown">
      <span>Фильтры</span>
    </div>
    <div class="filters__content" :style="{display: dropdown ? 'block':'none'}">

      <FilterComponent v-for="filter in filters" :filter="filter" :key="filter.title"/>

    </div>
  </div>
</template>
<script>
import FilterComponent from "./filters/FilterComponent";

export default {

  components: {FilterComponent},
  props:['filters'],

  data() {
    return {
      dropdown: false
    }
  },

}
</script>
<style>
.filters {
  width: 100%;
}
</style>
