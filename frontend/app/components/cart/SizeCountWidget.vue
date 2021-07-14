<template>
  <td class="basket__cell">
    <div class="row">
      <div class="col basket__headline">Размеры</div>
      <div class="col basket__headline">Количество</div>
      <div class="col basket__headline">Сумма</div>
    </div>
    <!-- <template v-for="s in getSizes">-->
    <template v-for="s in this.item.size">
      <div class="row" v-if="s.count > 0">
<!--      <div class="row">-->
        <div class="col basket__value">{{ s.size }}</div>
        <div class="col basket__value">

<!--          {{ s.count }}-->
          <SizeCountSpinbuttonWidget :size="s.size" :sku="item.sku"/>

        </div>
        <div class="col basket__value">{{ s.count * price }} руб.</div>
      </div>
    </template>

  </td>
</template>

<script>
import SizeCountSpinbuttonWidget from "./SizeCountSpinbuttonWidget";
export default {
  components: {SizeCountSpinbuttonWidget},
  props: ['item', 'price'],

}
</script>

<style>



</style>


<!--<div class="basket__headline">Размеры</div>-->
<!--      <div class="basket__value">XS</div>-->
<!--      <div class="basket__value">S</div>-->
<!--    </td>-->
<!--    <td class="basket__count basket__cell">-->
<!--      <div class="basket__headline basket__headline&#45;&#45;count">Количество</div>-->
<!--      <div class="basket__value">-->
<!--        <div class="number">-->
<!--          <input type="number" class="number__input" min="1" max="999" pattern="[0-9]*" value="1">-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="basket__value">-->
<!--        <div class="number">-->
<!--          <input type="number" class="number__input" min="1" max="999" pattern="[0-9]*" value="2">-->
<!--        </div>-->
<!--      </div>-->
<!--    </td>-->
<!--    <td class="basket__sum basket__cell">-->
<!--      <div class="basket__headline">Сумма</div>-->
<!--      <div class="basket__value">1530 руб.</div>-->
<!--      <div class="basket__value">3060 руб.</div>-->
<!--      <div class="basket__total">4 590 руб.</div>-->
