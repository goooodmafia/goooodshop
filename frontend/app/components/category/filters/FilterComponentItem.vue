<template>
  <div class="f-options__item">
    <input :id="filter.title+'_'+item.lable" type="checkbox" class="f-options__checkbox" :value="item.lable"
           v-model="filter_value">
    <label
      :for="filter.title+'_'+item.lable"
      class="f-options__label">{{ item.lable }}<span
      class="f-options__count">&NonBreakingSpace;({{ item.count }})</span></label>
  </div>
</template>

<script>
export default {
  props: ['item', 'filter'],

  data() {
    return {
      filter_value: false
    }
  },
  watch: {
    filter_value: function(val) {
      this.$bus.$emit('SET_FILTER', this.filter.name, this.item.lable, this.filter_value);
      // this.$bus.$emit('SET_FILTER');
      // or generate/simulate a native events (not sure how, but its outside Vue's realm I think
    }
  }
}
</script>
