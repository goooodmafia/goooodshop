<template>
  <div class="filters">
    <div class="filters__headline">
      <span>Фильтры</span>
    </div>
    <div class="filters__content">

      <FilterComponent v-for="filter in filters" :filter="filter"/>

    </div>
  </div>
</template>
<script>
import FilterComponent from "./filters/FilterComponent";

export default {
  components: {FilterComponent},
  data() {
    return {
      filters: [
        {
          title: 'Тип', name: 'sex', items: [
            {lable: 'Мужское', value: false},
            {lable: 'Женское', value: false},
            {lable: 'Детское', value: false},
          ]
        },
        {
          title: 'Цвет', name: 'color', items: [
            {lable: 'Черное', value: false},
            {lable: 'Белое', value: false},
            {lable: 'Красное', value: false},
            {lable: 'Зеленый', value: false},
            {lable: 'Синий', value: false},
          ]
        },
      ]
    }
  }
}
</script>
