<template>
  <Wrapper>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>###test</h1>



            <div>В корзине {{ cartCount }} товаров</div>
            <div>
              <ul>
                <li v-for="product in cart">
                  {{ product }}
                </li>
              </ul>
            </div>
            <div class="btn" @click="onClick">Купить</div>

          </div>
        </div>
      </div>
    </template>
  </Wrapper>


</template>

<script>

import Wrapper from "~/components/layout/Wrapper";

import {mapMutations} from 'vuex'
import {mapGetters} from 'vuex'
import {mapState} from 'vuex'

export default {
  // middleware: 'auth',


  components: {Wrapper},
  computed: {
    ...mapState('cart', ['cart', 'wishes']),
    ...mapGetters('cart', ['cartCount', 'wishesCount']),
  },
  methods: {
    onClick(sku) {
      this.$store.dispatch('cart/addToCart', '14-1817')
    }
  }

}
</script>
