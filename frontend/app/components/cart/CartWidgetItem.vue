<template>
  <tr class="basket__row">

    <td class="basket__wrap basket__cell">
      <div class="basket__figure">
        <a href="#">
          <b-img :src="item.thumbnail" alt="" width="110" height="145" />
        </a>
      </div>
      <div class="basket__details">
        <div class="basket__headline">Наименование</div>
        <div class="basket__title">
          <nuxt-link :to="localePath(`/product/${item.sku}`)">{{ item.model }}</nuxt-link>
        </div>
        <div class="basket__article">Артикул: {{ item.sku }}</div>
        <!-- <div class="basket__color">Цвет: Черный</div>-->
      </div>
    </td>
    <td class="basket__price basket__cell">
      <div class="basket__headline">Цена за единицу</div>
      <div class="basket__value">{{ item.price }} руб.</div>
    </td>
    <td class="basket__size basket__cell">
      <div class="basket__headline">Размеры</div>
      <div class="basket__value">XS</div>
      <div class="basket__value">S</div>
    </td>
    <td class="basket__count basket__cell">
      <div class="basket__headline basket__headline--count">Количество</div>
      <div class="basket__value">
        <div class="number">
          <input type="number" class="number__input" min="1" max="999" pattern="[0-9]*" value="1">
        </div>
      </div>
      <div class="basket__value">
        <div class="number">
          <input type="number" class="number__input" min="1" max="999" pattern="[0-9]*" value="2">
        </div>
      </div>
    </td>
    <td class="basket__sum basket__cell">
      <div class="basket__headline">Сумма</div>
      <div class="basket__value">1530 руб.</div>
      <div class="basket__value">3060 руб.</div>
      <div class="basket__total">4 590 руб.</div>
    </td>
    <td class="basket__to-fav basket__cell">
      <a href="#" class="to-favourites">В избранное</a></td>
    <td class="basket__del basket__cell">
      <a href="#" class="btn btn--delete" title="Удалить"></a>
    </td>

  </tr>
</template>
<script>

export default {
  props: ['item']
}
</script>
