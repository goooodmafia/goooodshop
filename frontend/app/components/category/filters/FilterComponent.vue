<template>
  <div class="filters__item accordion__item is-active">
    <div class="filters__title accordion__title">{{ filter.title }}</div>
    <div class="filters__options accordion__content" style="display: block;">
      <div class="f-options">
        <div class="f-options__item" v-for="item in filter.items">
          <input :id="filter.title+'_'+item.lable" type="checkbox" class="f-options__checkbox" :value="item.lable" v-model="item.value">
          <label :for="filter.title+'_'+item.lable" class="f-options__label">{{ item.lable }}</label>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: ['filter']
}
</script>
