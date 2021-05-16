<template>


  <div class="filters__item accordion__item is-active" v-if="filter.items && filter.items.length>1">
    <div class="filters__title accordion__title">{{ filter.title }}</div>
    <div class="filters__options accordion__content" style="display: block;">
      <div class="f-options">
        <FilterComponentItem v-for="item in filter.items" :filter="filter" :item="item" :key="item.label"/>
      </div>
    </div>
  </div>
</template>
<script>
import FilterComponentItem from "./FilterComponentItem";
export default {
  components: {FilterComponentItem},
  props: ['filter'],


  // computed:{
  //   showFilters(){
  //     filter.items.length>1
  //     && filter.items.length>1
  //   }
  // }
}
</script>
