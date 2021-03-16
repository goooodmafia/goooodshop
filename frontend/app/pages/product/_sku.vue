<template>
  <Wrapper>
    <div class="container">

      <div class="row">
        <div class="col-md-auto col-sm-12">
          <Sidebar :currentpath="currentpath">
            <!-- <Filters :filters="filters"/>-->
          </Sidebar>
        </div>
        <div class="col content">

          <div class="product-head">
            <!--            <a href="#" class="btn btn&#45;&#45;back">Назад</a>-->
            <!--            <nav aria-label="breadcrumb">-->
            <!--              <ol class="breadcrumb breadcrumb&#45;&#45;product">-->
            <!--                <li class="breadcrumb__item"><a href="#" class="breadcrumb__link">Главная</a></li>-->
            <!--                <li class="breadcrumb__item"><a href="#" class="breadcrumb__link">Мужское</a></li>-->
            <!--                <li class="breadcrumb__item"><a href="#" class="breadcrumb__link">Футболки короткий рукав</a></li>-->
            <!--                <li class="breadcrumb__item active" aria-current="page">Free your mind</li>-->
            <!--              </ol>-->
            <!--            </nav>-->

            <nav aria-label="breadcrumb">
              <ol class="mybreadcrumb">
                <li class="mybreadcrumb__item" v-for="(item, index) in breadcrumbs.breadcrumbs">
                  <nuxt-link :to="localePath(item.link)" :class="['mybreadcrumb__link']">{{ item.title }}</nuxt-link>
                </li>
                <li class="mybreadcrumb__item active">{{ breadcrumbs.title }}</li>
              </ol>
            </nav>
          </div>

          <div class="product-wrap">

            <div class="product-slider">

              <div class="product-slider__nav">
                <hooper class="product-slider-nav" ref="slider_nav" :settings="options_nav" group="group"
                        style="height:512px">
                  <slide v-for="item in 4" :key="item">
                    <h3 class="myslidenav">slide {{ item }}</h3>
                  </slide>

                  <navigation slot="hooper-addons"></navigation>

                </hooper>
              </div>

              <div class="product-slider__main">
                <div class="product-slider__label">new</div>

                <hooper ref="slider_main" :settings="options_main" group="group" style="height:554px">

                  <slide v-for="item in 4" :key="item">
                    <h3 class="myslide">slide {{ item }}</h3>
                  </slide>

                </hooper>

              </div>


            </div>

            <div class="product-details">
              <div class="heading product-heading heading--h2">
                <h1>{{ product.model }}</h1>
              </div>
              <div class="product-article">Артикул: {{ product.sku }} <a href="#" class="product-share"
                                                                         title="Поделиться"></a>
              </div>
              <div class="product-price">
                <div class="product-price__new">1530 руб.</div>
                <div class="product-price__holder">
                  <div class="product-price__old">2000 руб.</div>
                  <div class="product-price__sale">-30%</div>
                </div>
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
                  <a href="#" class="btn btn--orange-bg btn--to-order">Купить</a>
                </div>
                <div class="product-actions__to-fav">
                  <a href="#" class="to-favourites">Добавить в избранное</a>
                </div>
              </div>

            </div>
          </div>

          <div class="product-wrap">

            <div class="product-descr">
              <div class="product-descr__item">
                <div class="heading heading--h3 pb-3">
                  <h3>Состав</h3>
                </div>
                <div class="product-descr__text">{{ product.content }}</div>
              </div>
              <div class="product-descr__item">
                <div class="heading heading--h3 pb-3">
                  <h3>Описание</h3>
                </div>
                <div class="characteristics__text">{{ product.description }}</div>

                <div class="product-descr__item">
                  <div class="characteristics">
                    <div class="characteristics__item">
                      <div class="characteristics__title">Бренд</div>
                      <div class="characteristics__value">{{ product.brand }}</div>
                    </div>
                    <div class="characteristics__item">
                      <div class="characteristics__title">Артикул</div>
                      <div class="characteristics__value">{{ product.sku }}</div>
                    </div>
                    <div class="characteristics__item">
                      <div class="characteristics__title">Уход за вещами</div>
                      <div class="characteristics__value">бережная стирка при t не более 40С</div>
                    </div>
                    <div class="characteristics__item">
                      <div class="characteristics__title">Пол</div>
                      <div class="characteristics__value">{{ product.sex }}</div>
                    </div>
                    <div class="characteristics__item">
                      <div class="characteristics__title">Страна производитель</div>
                      <div class="characteristics__value">Россия</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="same-design">
              <div class="heading heading--h3">
                <h3>Товары с этим дизайном</h3>
              </div>
              <div class="same-design__list">
                <CatalogItem :item="item" v-for="(item, index) in fetchproducts" :key="index"/>
              </div>
            </div>

          </div>


        </div>
      </div>

    </div>
  </Wrapper>
</template>

<script>

import Wrapper from "../../components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";

import {Hooper, Slide, Navigation} from 'hooper';

import PRODUCT from "~/api/query/product.graphql"
import FETCHPRODUCTS from "~/api/query/fetchproducts.graphql"
import CatalogItem from "../../components/category/catalog-unit/CatalogItem";

export default {

  name: 'product',

  components: {CatalogItem, Wrapper, Breadcrumbs, Sidebar, Hooper, Slide, Navigation},

  data() {
    return {

      currentpath:[],

      options_main: {
        mouseDrag: false,
        touchDrag: false,
        wheelControl: false,
        keysControl: false,
        infiniteScroll: true,
      },

      options_nav: {
        vertical: true,
        itemsToShow: 4,
        infiniteScroll: true,
      },


      breadcrumbs: {
        title: this.$t('page.help.title'),
        breadcrumbs: [
          {title: 'Главная', link: this.localePath('index')},
          {title: 'Главная', link: this.localePath('index')},
        ],
      },

      fetchproducts: [],

      product: {
        sku: '',
        model: '',
        brand: '',
        description: '',
        content: '',
        thumbnail: {
          link: '',
        },
        new: '',
        hit: '',
        sale: '',
        colors: '',
        glowInTheDark: '',
        glowInTheUv: '',
        slug: '',
      }

    }
  },

  apollo: {
    fetchproducts: {
      query: FETCHPRODUCTS,
      variables() {
        return {
          route: "",
          languageCode: this.$i18n.locale.toUpperCase(),
          limit: 2,
          offset: 0,
          colors: '',
          effects: '',
          tags: this.product.tags.join()
        }
      },
      skip: true,
    },
    product: {
      query: PRODUCT,
      variables() {
        return {
          sku: this.getSku(),
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
    },

  },

  watch: {
    product() {
      this.$apollo.queries.fetchproducts.skip = false
      this.$apollo.queries.fetchproducts.refetch({
        tags: this.product.tags.join()
      })

      const pathArray = this.product.category.link.split('/')
      this.$data.currentpath = pathArray.slice(pathArray.indexOf('category') + 1)
    }
  },

  methods: {
    getSku() {
      return this.$route.params.sku
    }
  },

  // computed: {
  //   currentpath() {
  //     const pathArray = this.product.link.split('/') || []
  //     return pathArray.slice(pathArray.indexOf('category') + 1)
  //   }
  // }

}
</script>

<style>
.myslide {
  text-align: center;
  max-width: 413px;
  min-height: 554px;
  background-color: rgba(255, 255, 255, .3);
}

.myslidenav {
  text-align: center;
  background-color: rgba(255, 255, 255, .3);
  width: 93px;
  height: 119px;
}

.hooper-navigation.is-vertical .hooper-prev, .hooper-navigation.is-vertical .hooper-next {
  right: auto;
  left: calc(50% - 26px);
  fill: white;
}

.hooper-navigation.is-vertical .hooper-prev {
  top: -42px;
}

.hooper-navigation.is-vertical .hooper-next {
  bottom: -32px;
}
</style>
