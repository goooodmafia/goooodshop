<template>
  <b-form-spinbutton
    v-model="count"
    inline
    variant="outline-warning"
    class="rounded-0 product-size__count form-spinbutton"
  ></b-form-spinbutton>
</template>

<script>
export default {
  props: ['size','sku', 'price'],

  computed: {
    count: {
      get() {
        return this.$store.getters['cart/getCountBySize'](this.sku, this.size)
      },
      set(value) {
        // this.$store.commit('cart/SET_SIZE', {sku:this.sku, size:this.size, count: value})
        this.$store.commit('cart/SET_SIZE', {
          sku:this.sku,
          size:this.size,
          count: value,
          price: this.price
        })
      }
    }
  }
}
</script>

<style>
.size_count_container {
  display: inline-grid;
  grid-template-columns: auto auto auto;
}
.col.basket__headline, .col.basket__value{
  padding-left: 10px;
  padding-right: 10px;
}

.form-spinbutton.form-control {
  background-color: transparent;
  color: white;
  border: 1px solid #91b9ff;
}
.form-spinbutton.form-control.focus {
  color: white;
  background-color: transparent;
}
.custom-select option {
  background-color: #1f4ea3;
}
</style>
