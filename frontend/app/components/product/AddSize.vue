<template>
  <div>
    <div class="product-options" v-if="sizes.length > 0">
      <div class="product-size" v-for="(item,index) in sizes" :key="index">

        <div class="product-options__title">Размер:</div>

        <b-form-select
          v-model="item.size"
          :options="getAvailableSizeOptions(item.size)"
          class="rounded-0 product-size__count"
        ></b-form-select>

        <b-form-spinbutton
          v-model="item.count"
          inline
          variant="outline-warning"
          class="rounded-0 product-size__count"
        ></b-form-spinbutton>

        <b-button v-if="(index === (sizes.length-1)) & (index !== (avaliable.length-1))"
                  variant="outline-warning"
                  class="gd-add-btn"
                  @click="addSize()">+
        </b-button>

        <b-button v-else
                  variant="outline-danger"
                  class="gd-add-btn gd-add-btn-del"
                  @click="removeSize(index)">+
        </b-button>

      </div>
    </div>


    <div class="product-options" v-else>
      <div class="product-size">{{ $t('page.product.not_in_stock') }}</div>
    </div>

    <div class="product-additionally">
      <div class="product-additionally__size">
        <nuxt-link :to="localePath('size')" class="size-link">Таблица размеров</nuxt-link>
      </div>
      <!-- <div class="product-additionally__reviews">-->
      <!--   <a href="#" class="reviews-link">Отзывы</a>-->
      <!-- </div>-->
    </div>


    <div class="product-actions">
      <div class="product-actions__btn">
        <b-button class="gd-btn gd-btn--orange-bg gd-btn--to-order" @click="addToCart()">Купить</b-button>
      </div>
      <div class="product-actions__to-fav">
        <a href="#" class="to-favourites">Добавить в избранное</a>
      </div>
    </div>
  </div>

</template>

<script>

import MySpinButton from '~/components/layout/MySpinButton.vue'

export default {

  components: {MySpinButton},

  props: ['avaliable', 'sku'],

  data() {
    return {
      sizes: [],
    }
  },

  watch: {
    avaliable: function () {
      this.initSize()
    }
  },

  methods: {
    getAvailableSizes() {
      let res = []
      this.avaliable.forEach((element) => {
        this.sizes.forEach((size) => {
          if (element === size.size) {
            res.push(element)
          }
        })
      })
      return this.avaliable.filter((el) => !res.includes(el))
    },

    getAvailableSizeOptions(current_size) {
      let r = this.getAvailableSizes()
      r.push(current_size)
      return r
    },

    addSize() {
      let a = this.getAvailableSizes()
      if (a.length > 0) {
        this.sizes.push(
          {
            size: a[0],
            count: 1,
          }
        )
      }
    },

    removeSize(index) {
      this.sizes.splice(index, 1)
    },

    initSize() {
      this.sizes = []
      this.addSize()
    },

    addToCart() {

      this.sizes.forEach((item) => {
        this.$store.dispatch(
          'cart/increaseSize',
          {
            sku: this.sku,
            size: item.size,
            count: item.count
          }
        )
        this.initSize()

      })

    }
  },

}
</script>

<style lang="scss">

//@import "gd/vars";

.gd-prod {
  color: white;
  background-color: transparent;
}

.product-options__title {
  //display: inline-block;
}

.product-size div.form-control, .custom-select {
  //vertical-align: middle;
  background-color: transparent;
  color: white;
  border: 1px solid #91b9ff;
}

.product-size {
  display: flex;
  justify-content: space-between;
}

.product-size .custom-select {
  width: 100px;
  //width: auto;
}

.product-size .custom-select option {
  background-color: #1f4ea3;
}

.product-size div.form-control.focus {
  color: white;
  background-color: transparent;
}

.gd-add-btn {
  color: white;
  border-radius: 50%;
}

.gd-add-btn:focus {
  outline: none;
  box-shadow: none;
}

.gd-add-btn-del {
  transform: rotate(45deg);
}

</style>
