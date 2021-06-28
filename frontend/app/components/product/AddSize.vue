<template>
  <div class="product-options" v-if="sizes.length > 0">
    <div class="product-size" v-for="item,index in sizes" :key="index">
      <!--  <div class="product-size">-->
      <div class="product-options__title">Размер:</div>
      <!--    <p class="">Размер:</p>-->

      <!--    <b-dropdown id="dropdown-dropup" dropup text="Drop-Up" variant="primary" class="m-2">-->
      <!--      <b-dropdown-item href="#">Action</b-dropdown-item>-->
      <!--      <b-dropdown-item href="#">Another action</b-dropdown-item>-->
      <!--      <b-dropdown-item href="#">Something else here</b-dropdown-item>-->
      <!--    </b-dropdown>-->

      <!--    <b-dropdown text="Dropdown Button" variant="outline-warning">-->
      <!--    </b-dropdown>-->

      <b-form-select
        v-model="item.size"
        :options="getAvailableSizes().push(item.size)"
        class="rounded-0 product-size__count"
      ></b-form-select>

      <b-form-spinbutton
        v-model="item.count"
        inline
        variant="outline-warning"
        class="rounded-0 product-size__count"
      ></b-form-spinbutton>

      <!--    <MySpinButton :value="value" @input="someMethod($event)"/>-->

      <!--    <b-badge variant="success">В корзине</b-badge>-->
      <!--      <template v-if="index === (avaliable.length-1)"/>-->

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

      <!--    <div class="product-size__select">-->
      <!--      <div class="select-wrap select-wrap&#45;&#45;size">-->
      <!--        <div class="fs-dropdown fs-light" id="fs-dropdown__2-dropdown" tabindex="0" role="listbox" aria-haspopup="true"-->
      <!--             aria-live="polite" aria-labelledby="fs-dropdown__2-dropdown-selected">-->
      <!--          <select class="select-block fs-dropdown-element" tabindex="-1">-->
      <!--            <option value="">XS</option>-->
      <!--            <option value="">S</option>-->
      <!--            <option value="">M</option>-->
      <!--            <option value="">L</option>-->
      <!--            <option value="">XL</option>-->
      <!--            <option value="">XXL</option>-->
      <!--            <option value="">3XL</option>-->
      <!--            <option value="">4XL</option>-->
      <!--          </select>-->
      <!--          <button type="button" class="fs-dropdown-selected" id="fs-dropdown__2-dropdown-selected" tabindex="-1">XS-->
      <!--          </button>-->
      <!--          <div class="fs-dropdown-options fs-scrollbar-element fs-scrollbar fs-light">-->
      <!--            <div class="fs-scrollbar-bar" style="height: 0px;">-->
      <!--              <div class="fs-scrollbar-track fs-touch-element"-->
      <!--                   style="touch-action: pan-x; height: 0px; margin-bottom: 0px; margin-top: 0px;">-->
      <!--                <button type="button" class="fs-scrollbar-handle" aria-hidden="true" tabindex="-1"></button>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--            <div class="fs-scrollbar-content">-->
      <!--              <button type="button"-->
      <!--                      class="fs-dropdown-item fs-dropdown-item_selected" data-value=""-->
      <!--                      role="option" aria-selected="true">XS</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">S</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">M</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">L</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">XL</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">XXL</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">3XL</button>-->
      <!--              <button type="button" class="fs-dropdown-item" data-value="" role="option">4XL</button>-->
      <!--            </div>-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--    </div>-->


      <!--    <div class="product-size__count">-->
      <!--      <div class="number">-->
      <!--        <div class="fs-number fs-light">-->
      <!--          <input type="number" class="number__input fs-number-element" min="1" max="999" pattern="[0-9]*" value="1">-->
      <!--          <button type="button" class="fs-number-arrow fs-number-up" aria-hidden="true" tabindex="-1"></button>-->
      <!--          <button type="button" class="fs-number-arrow fs-number-down" aria-hidden="true" tabindex="-1"></button>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--    </div>-->


      <!--    <div class="product-size__add-del">-->
      <!--      <a href="javascript:void(0);" class="gd-btn gd-btn&#45;&#45;add-bdr" title="Добавить"></a>-->
      <!--    </div>-->
    </div>
  </div>


  <div class="product-options" v-else>
    <div class="product-size">{{ $t('page.product.not_in_stock') }}</div>
  </div>

</template>

<script>

  import MySpinButton from '~/components/layout/MySpinButton.vue'

  export default {

    components: {MySpinButton},

    props: ['avaliable'],

    data() {
      return {
        sizes: [],
        // sizes: [{size: "M", count: 1,}],
        // avaliable: [
        //   '2XS',
        //   'XS',
        //   'S',
        //   'S',
        //   'M',
        //   'L',
        //   'XL',
        //   '2XL',
        //   '3XL',
        //   '4XL',
        // ]
      }
    },

    methods: {
      getAvailableSizes() {
        console.log('call')
        let res = []
        this.avaliable.forEach((element) => {
          this.sizes.forEach((size) => {

            if (element === size.size) {
              // console.log(`${element} === ${size.size}`)
              res.push(element)
            }
          })
        })
        return this.avaliable.filter((el) => !res.includes(el))
      },

      addSize() {
        let a = this.getAvailableSizes()
        console.log(a)
        console.log(this.sizes)
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
    },

    created() {
      this.addSize()
    }
  }
</script>

<style lang="scss">

  //@import "gd/vars";

  .gd-prod {
    color: white;
    background-color: transparent;
  }

  .product-options__title {
    display: inline-block;
  }

  .product-size div.form-control, .custom-select {
    vertical-align: middle;
    background-color: transparent;
    color: white;
    border: 1px solid #91b9ff;
  }

  .product-size .custom-select {
    width: auto;
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
