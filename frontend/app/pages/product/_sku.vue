<template>
  <Wrapper>
    <div class="container">
      <Breadcrumbs :data="breadcrumbs()" :showTitle="false" :showBack="true">
        <template v-slot:sidebar>
          <div class="col-md-auto col-sm-12">
            <Sidebar :currentpath="currentpath" :items="categories"/>
          </div>
        </template>


        <template>
          <div class="product-wrap">
            <div class="product-slider">
              <div class="product-slider__nav">
                <hooper class="product-slider-nav"
                        ref="slider_nav"
                        :settings="options_nav"
                        group="group"
                        style="height: 512px"
                >
                  <template v-if="product.mediaFiles.length>0">
                    <slide v-for="(item,index) in product.mediaFiles" :key="index">
                      <div @click="$refs.slider_nav.slideTo(index)">
                        <b-img-lazy
                          blank-color="rgba(255, 255, 255, .3)"
                          height="119px"
                          center
                          :src="item.src"
                        />
                      </div>
                    </slide>
                  </template>
                  <template v-else>
                    <slide>
                      <b-img-lazy
                        blank="true"
                        blank-color="rgba(255, 255, 255, .3)"
                        height="119px"
                        width="90px"
                        center
                      />
                    </slide>
                  </template>
                  <!--                  <navigation slot="hooper-addons"></navigation>-->
                  <navigation slot="hooper-addons">
                    <div slot="hooper-prev"
                         class="slider-button slider-button--prev"></div>
                    <div slot="hooper-next"
                         class="slider-button slider-button--next"></div>
                  </navigation>

                </hooper>
              </div>

              <div class="product-slider__main">
                <div class="product-slider__label">new</div>
                <hooper ref="slider_main"
                        :settings="options_main"
                        group="group"
                        style="height:auto"
                >
<!--                  style="height: "-->
                  <template v-if="product.mediaFiles.length>0">
                    <slide v-for="(item, index) in product.mediaFiles" :key="index">
                      <inner-image-zoom :src="item.src" :zoom="2" :zoomSrc="item.src" :fullscreenOnMobile="true"/>
                      <!--                      <div @click="openGallery(index)">-->
                      <!--                        <b-img-lazy blank-color="rgba(255, 255, 255, .3)" height="554px" center :src="item.src"/>-->
                      <!--                      </div>-->
                    </slide>
                  </template>
                  <template v-else>
                    <slide>
                      <b-img-lazy blank="true" blank-color="rgba(255, 255, 255, .3)" height="554px" width="413" center/>
                    </slide>
                  </template>
                </hooper>
              </div>
            </div>

            <div class="product-details">
              <div class="heading product-heading heading--h2">
                <h1>{{ product.model }}</h1>
              </div>
              <div class="product-article">Артикул: {{ product.sku }}
<!--                <a href="#" class="product-share" title="Поделиться">-->
                <script src="https://yastatic.net/share2/share.js"></script>
                  <div
                    class="ya-share2 product-share"
                    data-curtain data-shape="round"
                    data-limit="0"
                    data-more-button-type="short"
                    data-services="vkontakte,facebook,odnoklassniki,telegram,viber,whatsapp"></div>

<!--              </a>-->
              </div>
              <div class="product-price">
                <div class="product-price__new">{{ product.price }} руб.</div>
                <!-- <div class="product-price__holder">-->
                <!--   <div class="product-price__old">2000 руб.</div>-->
                <!--   <div class="product-price__sale">-30%</div>-->
                <!-- </div>-->
              </div>



              <AddSize :avaliable="avaliableSizes()" :sku="getSku()" :price="product.price"/>


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
                <CatalogItem :item="item" v-for="(item, index) in same_products.items" :key="index"/>
              </div>
            </div>

          </div>

          <div class="similar">
            <div class="heading heading--h2">
              <h4>Похожие товары</h4>
            </div>
            <div class="similar__list">
              <CatalogItem :item="item" v-for="(item, index) in simular_products.items" :key="index" class="simular_catalog"/>
            </div>
          </div>


        </template>

      </Breadcrumbs>

    </div>
<!--    <light-box v-if="product && product.mediaFiles.length>0" ref="lightbox" :media="product.mediaFiles"-->
<!--               :showThumbs="false" :showLightBox="false"></light-box>-->

  </Wrapper>
</template>

<script>

import Wrapper from "../../components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";
import CatalogItem from "../../components/category/catalog-unit/CatalogItem";

import {Hooper, Slide, Navigation} from 'hooper';

import PRODUCT from "~/api/query/product.graphql"
import PRODUCTS from "~/api/query/products.graphql"
import AddSize from "../../components/product/AddSize";


export default {

  name: 'product',

  components: {AddSize, CatalogItem, Wrapper, Breadcrumbs, Sidebar, Hooper, Slide, Navigation},

  data() {
    return {
      currentpath: [],

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

      product: {
        sku: '',
        model: '',
        brand: '',
        description: '',
        content: '',
        thumbnail: {
          link: '',
        },
        sex:'',
        mediaFiles: [],
        new: '',
        hit: '',
        sale: '',
        colors: '',
        glowInTheDark: '',
        glowInTheUv: '',
        slug: '',
      },
      same_products: {items: []},
      simular_products:{items:[]}
    }
  },

  apollo: {
    product: {
      query: PRODUCT,
      variables() {
        return {
          sku: this.getSku(),
          languageCode: this.$i18n.locale.toUpperCase(),
        }
      },
    },

    same_products: {
      query: PRODUCTS,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          pageSize: 2,
          page: 1,
          route: '',
          sizes: '',
          colors: '',
          effects: '',
          // tags: this.product.tags.join(),
          tags: '',
          hit: false,
          new: false,
          query: this.product.model,
          order: 'Random'
        }
      },
      skip: true,
      update: data => data.products
    },

    simular_products: {
      query: PRODUCTS,
      variables() {
        return {
          languageCode: this.$i18n.locale.toUpperCase(),
          pageSize: 4,
          page: 1,
          route: '',
          sizes: '',
          colors: '',
          effects: '',
          tags: '',
          hit: false,
          new: false,
          query: '',
          order: 'Random'
        }
      },
      skip: true,
      update: data => data.products
    },
  },

  watch: {
    product() {
      this.$apollo.queries.same_products.skip = false
      this.$apollo.queries.same_products.refetch({
        tags: this.product.tags.join()
      })

      this.$apollo.queries.simular_products.skip = false
      this.$apollo.queries.simular_products.refetch({
        route: this.product.category.link
      })

      const pathArray = this.product.category.link.split('/')
      this.$data.currentpath = pathArray.slice(pathArray.indexOf('category') + 1)
    }
  },

  methods: {
    // getRoute(){
    //   return this.$route.path
    // },
    getSku() {
      return this.$route.params.sku
    },
    openGallery(index) {
      this.$refs.lightbox.showImage(index)
    },
    breadcrumbs() {
      return {
        title: this.product && this.product.model,
        breadcrumbs: this.product && this.product.breadcrumbs,
      }
    },

    avaliableSizes() {
      let res = []
      if(this.product.sizes) {
        this.product.sizes.forEach((el) => {
          if (el.count > 0) {
            res.push(el.size)
          }
        })
      }
      return res
    }
  },


  computed: {
    categories() {
      return this.$store.state.categories.list
    },
  },

}
</script>

<style>
.myslide {
  text-align: center;
  max-width: 413px;
  background-color: rgba(255, 255, 255, .3);
}

.myslidenav {
  text-align: center;
  background-color: rgba(255, 255, 255, .3);
  width: 93px;
}


.hooper-navigation.is-vertical .hooper-prev, .hooper-navigation.is-vertical .hooper-next {
  left: calc(50% - 16px);
  /*  right: auto;*/
  /*  fill: white;*/
}

.simular_catalog {
    margin: 0;
}

</style>
