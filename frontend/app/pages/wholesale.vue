<template xmlns="http://www.w3.org/1999/html">
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>

      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="wholesale-intro">
              <div class="wholesale-intro__descr" v-html="opt_about"/>

              <div class="wholesale-intro__slider">
                <div class="simple-slider simple-slider--wholesale">
                  <div class="js-slider slider simple-slider__wrapper">
                    <div class="simple-slider__slide slider__slide"
                         style="background-image:url(img/article/wholesale/simple-slider__pic1.jpg);"></div>
                    <div class="simple-slider__slide slider__slide"
                         style="background-image:url(img/article/wholesale/simple-slider__pic2.jpg);"></div>
                  </div>
                  <div class="simple-slider__buttons"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container wholesale-benefits">
        <div class="row" v-html="opt_benefits"/>
      </div>

      <div class="container">
        <div class="row">
          <div class="col">
            <div class="wholesale-help" id="wholesale-help">
              <div class="heading heading--orange heading--h3 pb-4">
                <h2>Помощь для оптовиков</h2>
              </div>
              <div class="wholesale-help__items">
                <OptHelpItem :item="item" v-for="(item, key) in opt_help" :key="key"/>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="row">
          <div class="col" v-html="opt_delivery"/>
        </div>
      </div>

    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "../components/layout/Wrapper";
import Breadcrumbs from "../components/layout/Breadcrumbs";
import OptHelpItem from "../components/layout/OptHelpItem";

export default {

  name: 'Wholesale',

  components: {Breadcrumbs, Wrapper, OptHelpItem},

  data() {
    return {
      opt_about: null,
      opt_benefits: null,
      opt_help: null,
      opt_delivery: null,

      breacrumbs: {
        title: this.$t('page.wholesale.title'),
        breadcrumbs: [],
      },
    }
  },
  async asyncData({app}) {
    const opt_about = await import(`~/content/wholesale/opt_about_${app.i18n.locale}.md`)
    const opt_benefits = await import(`~/content/wholesale/opt_benefits_${app.i18n.locale}.md`)
    const opt_help = await import(`~/content/wholesale/opt_help_${app.i18n.locale}.json`)
    const opt_delivery = await import(`~/content/wholesale/opt_delivery_${app.i18n.locale}.md`)
    return {
      opt_about: opt_about.html,
      opt_benefits: opt_benefits.html,
      opt_help: opt_help.default,
      opt_delivery: opt_delivery.html,
    }
  }
}
</script>
