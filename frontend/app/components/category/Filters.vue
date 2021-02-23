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

export default {

  components: {FilterComponent},
  props:['filters'],

}
</script>
