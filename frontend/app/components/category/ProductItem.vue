<template>
  <div class="catalog__item">

    <div class="catalog-unit catalog-unit--catalog">

      <div class="catalog-unit__figure">
        <div v-if="item.new" class="catalog-unit__label">new</div>
        <div v-if="item.hit" class="catalog-unit__label">hit</div>
        <nuxt-link :to="localePath(`/product/${item.sku}`)">
          <img :src="item.thumbnail.link " alt="" class="catalog-unit__img">
        </nuxt-link>
      </div>

      <div class="catalog-unit__details">
        <div class="catalog-unit__price">1530 руб.</div>
        <a href="#" class="catalog-unit__to-cart"></a>
        <div class="catalog-unit__sale">
          <div class="catalog-unit__old-price">2000 руб.</div>
          <div class="catalog-unit__sale-perc">-30%</div>
        </div>
        <div class="catalog-unit__title">
          <nuxt-link :to="localePath(`/product/${item.sku}`)">{{ item.model }}</nuxt-link>
        </div>
        <div>{{ item.colors }}</div>
        <div class="catalog-unit__category"><a href="#">Мужское / Футболки короткий рукав</a></div>
      </div>

      <!-- BEGIN catalog-unit__hover -->
<!--      <div class="catalog-unit__hover">-->
<!--        &lt;!&ndash; BEGIN catalog-slider-nav &ndash;&gt;-->
<!--        <div class="catalog-slider-nav slider">-->
<!--          <div class="catalog-slider-nav__slide slider__slide">-->
<!--            <img src="img/catalog-slider-preview__pic1.jpg" alt="" class="catalog-slider-nav__img">-->
<!--          </div>-->
<!--          <div class="catalog-slider-nav__slide slider__slide">-->
<!--            <img src="img/catalog-slider-preview__pic2.jpg" alt="" class="catalog-slider-nav__img">-->
<!--          </div>-->
<!--          <div class="catalog-slider-nav__slide slider__slide">-->
<!--            <img src="img/catalog-slider-preview__pic3.jpg" alt="" class="catalog-slider-nav__img">-->
<!--          </div>-->
<!--          <div class="catalog-slider-nav__slide slider__slide">-->
<!--            <img src="img/catalog-slider-preview__pic1.jpg" alt="" class="catalog-slider-nav__img">-->
<!--          </div>-->
<!--          <div class="catalog-slider-nav__slide slider__slide">-->
<!--            <img src="img/catalog-slider-preview__pic2.jpg" alt="" class="catalog-slider-nav__img">-->
<!--          </div>-->
<!--          <div class="catalog-slider-nav__slide slider__slide">-->
<!--            <img src="img/catalog-slider-preview__pic3.jpg" alt="" class="catalog-slider-nav__img">-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash; END catalog-slider-nav &ndash;&gt;-->
<!--        &lt;!&ndash; BEGIN catalog-slider-main-wrap &ndash;&gt;-->
<!--        <div class="catalog-slider-main-wrap">-->
<!--          <div class="catalog-unit__label">new</div>-->
<!--          <div class="catalog-slider-main slider">-->
<!--            <div class="catalog-slider-main__slide slider__slide">-->
<!--              <a href="#"><img src="img/catalog__pic1.jpg" alt="" class="catalog-slider-main__img"></a>-->
<!--            </div>-->
<!--            <div class="catalog-slider-main__slide slider__slide">-->
<!--              <a href="#"><img src="img/catalog__pic2.jpg" alt="" class="catalog-slider-main__img"></a>-->
<!--            </div>-->
<!--            <div class="catalog-slider-main__slide slider__slide">-->
<!--              <a href="#"><img src="img/catalog__pic3.jpg" alt="" class="catalog-slider-main__img"></a>-->
<!--            </div>-->
<!--            <div class="catalog-slider-main__slide slider__slide">-->
<!--              <a href="#"><img src="img/catalog__pic1.jpg" alt="" class="catalog-slider-main__img"></a>-->
<!--            </div>-->
<!--            <div class="catalog-slider-main__slide slider__slide">-->
<!--              <a href="#"><img src="img/catalog__pic2.jpg" alt="" class="catalog-slider-main__img"></a>-->
<!--            </div>-->
<!--            <div class="catalog-slider-main__slide slider__slide">-->
<!--              <a href="#"><img src="img/catalog__pic3.jpg" alt="" class="catalog-slider-main__img"></a>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash; END catalog-slider-main-wrap &ndash;&gt;-->
<!--        &lt;!&ndash; BEGIN catalog-unit__details &ndash;&gt;-->
<!--        <div class="catalog-unit__details catalog-unit__details&#45;&#45;hover">-->
<!--          <div class="catalog-unit__price">1530 руб.</div>-->
<!--          <a href="#" class="catalog-unit__to-cart"></a>-->
<!--          <div class="catalog-unit__sale">-->
<!--            <div class="catalog-unit__old-price">2000 руб.</div>-->
<!--            <div class="catalog-unit__sale-perc">-30%</div>-->
<!--          </div>-->
<!--          <div class="catalog-unit__title"><a href="#">Life is Good</a></div>-->
<!--          <div class="catalog-unit__category"><a href="#">Мужское / Футболки короткий рукав</a></div>-->
<!--        </div>-->
<!--        &lt;!&ndash; END catalog-unit__details &ndash;&gt;-->
<!--      </div>-->
      <!-- END catalog-unit__hover -->
    </div>

  </div>
</template>

<script>
export default {
  props:["item"],
}
</script>

<style>
.catalog-unit__figure {
    min-width: 160px;
    min-height: 200px;
    background-color: rgba(255,255,255,0.2);
}
</style>
