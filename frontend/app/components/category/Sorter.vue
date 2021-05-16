<template>
  <div class="sorting sorting--catalog">
    <div class="sorting__title">Сортировать по:</div>
    <div class="sorting__list">
      <div
        @click="sort(item)"
        v-for="item in sortingItems"
        :class="[
                  'sorting__item',
                  {'sorting__item--decrease':item.sortOrder},
                  {'sorting__item--increase':!item.sortOrder},
                  {'active':item.active}
                  ]"
      >{{ item.title }}
      </div>
    </div>
  </div>
</template>

<script>

export default {

  // props:['order'],

  data() {
    return {
      sortingItems: [
        {
          title: 'новизне',
          sortEnum: 'Order',
          active: true,
          sortOrder: true
        },
        {
          title: 'цене',
          sortEnum: 'Price',
          active: false,
          sortOrder: true
        },
        {
          title: 'скидкам',
          sortEnum: 'Sale',
          active: false,
          sortOrder: true
        }
      ],
    }
  },

  methods:{
    sort(current) {
      if (current.active) {
        current.sortOrder = !current.sortOrder
      } else {
        current.sortOrder = true
      }
      this.sortingItems.forEach((element) => {
        element.active = false
      })
      current.active = true

      this.$bus.$emit('SET_PAGE', 1)
      this.$bus.$emit('SET_ORDER', (current.sortEnum + (current.sortOrder ? 'Inc' : 'Dec')))
      // this.$bus.$emit('REFETCH')
    }
  }
}
</script>
