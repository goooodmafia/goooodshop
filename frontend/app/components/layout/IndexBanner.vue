<template>
  <div class="main-slider">
    <div class="js-slider slider main-slider__wrapper">
      <hooper style="height: 100%" :settings="settings">

        <slide v-for="(item,key) in items" :key="key">
          <div class="main-slider__slide slider__slide"
               :style="{backgroundImage: 'url(' + item.img + ')', backgroundColor:item.color}">
            <div class="container">
              <div class="row">
                <div class="col">
                  <div class="main-slider__content">
                    <div class="main-slider__holder">
                      <div class="main-slider__heading heading heading--h1">
                        <div v-html="item.title"/>
                      </div>
                      <div class="main-slider__text" v-html="item.description"/>
                      <div class="main-slider__actions">
                        <nuxt-link :to="localePath(item.link)" class="btn">Купить</nuxt-link>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </slide>

        <slide>
          <client-only>
            <div style="
              height: 459px;
              width: auto;
              background: radial-gradient(black, transparent);"
            >
              <video-embed class="h-100" src="https://coub.com/view/u7bqv"></video-embed>
            </div>
          </client-only>
        </slide>
        <slide>
          <client-only>
            <div style="
              height: 459px;
              width: auto;
              background: radial-gradient(black, transparent);"
            >
              <video-embed class="h-100" src="https://www.youtube.com/watch?v=0CwAi4lKlSA&list=PLrTgFeRLRdBLDXMIi86uXpnRQEspQkrbQ&index=2"></video-embed>
            </div>
          </client-only>
        </slide>

        <navigation slot="hooper-addons"></navigation>
        <pagination slot="hooper-addons"></pagination>

      </hooper>
    </div>
  </div>
</template>


<script>

import {Hooper, Slide, Navigation, Pagination} from 'hooper';


export default {

  components: {Hooper, Slide, Navigation, Pagination},

  props: ['items'],

  data() {
    return {
      settings: {
        mouseDrag: true,
        touchDrag: true,
        wheelControl: false,
        keysControl: false,
        infiniteScroll: true
      }
    }
  }
}
</script>

<style>
.main-slider .hooper-navigation {
  /*opacity: 0;*/
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  max-width: 1300px;
  -webkit-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  transform: translateX(-50%);
}

.main-slider .hooper-navigation .hooper-prev, .main-slider .hooper-navigation .hooper-next {
  fill: white;
}


.hooper-slide.is-active.is-current .main-slider__heading {
  animation: slider__heading 1s linear;
  animation-fill-mode: forwards;
  -webkit-animation-fill-mode: forwards;
  animation-iteration-count: 1;
  -webkit-animation-iteration-count: 1;
}

.hooper-slide.is-active.is-current .main-slider__text {
  animation: slider__text 1s linear;
  animation-delay: 250ms;
  animation-fill-mode: forwards;
  -webkit-animation-fill-mode: forwards;
  animation-iteration-count: 1;
  -webkit-animation-iteration-count: 1;
}

.hooper-slide.is-active.is-current .main-slider__actions {
  animation: slider__actions 1s cubic-bezier(.785, .135, .15, .86);
  animation-delay: 500ms;
  animation-fill-mode: forwards;
  -webkit-animation-fill-mode: forwards;
  animation-iteration-count: 1;
  -webkit-animation-iteration-count: 1;
}

@keyframes slider__heading {
  to {
    width: 100%;
  }
}

@keyframes slider__text {
  to {
    opacity: 1;
  }
}

@keyframes slider__actions {
  to {
    left: 0;
    opacity: 1;
  }
}

</style>
