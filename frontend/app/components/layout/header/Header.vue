<template>
  <header class="header">
    <div class="header__top">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-6">
            <div class="row">
              <portal to="mobile-portal-nav-header" :disabled="mediaQueries.lg" class="col header__nav">
                <div class="nav nav--header">
                  <div class="nav__in">
                    <div class="nav__item">
                      <nuxt-link @click.native="onLinkClick" class="nav__link" :to="localePath('help')">Помощь
                      </nuxt-link>
                    </div>
                    <div class="nav__item">
                      <nuxt-link @click.native="onLinkClick" class="nav__link" :to="localePath('delivery')">Доставка
                      </nuxt-link>
                    </div>
                    <div class="nav__item">
                      <nuxt-link @click.native="onLinkClick" class="nav__link" :to="localePath('contacts')">Контакты
                      </nuxt-link>
                    </div>
                    <div class="nav__item">
                      <nuxt-link @click.native="onLinkClick" class="nav__link" :to="localePath('size')">Таблица
                        размеров
                      </nuxt-link>
                    </div>
                  </div>
                </div>
              </portal>

            </div>
          </div>
          <div class="col-md-12 col-lg-6">
            <div class="row justify-content-sm-end">
              <portal to="mobile-portal-auth-header" :disabled="mediaQueries.lg"
                      class="col-sm-auto col-md-auto col-lg header__auth">
                <AuthWidget/>
              </portal>

              <div class="col header__slogan d-lg-none">
                <portal-target name="slogan-portal" slim/>
              </div>
              <div class="col-auto header__lang">
                <portal to="mobile-portal-lang-toggle-header" :disabled="mediaQueries.sm">
                  <LangSwitcher class="lang-toggle--header"/>
                </portal>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="header__main">
      <div class="container">
        <div class="row">
          <div class="col-12 col-sm">
            <div class="row align-items-center">
              <div class="col col-sm-auto col-md-auto col-lg col-xl-auto header__logo">
                <Logo class="logo--header"/>
              </div>
              <portal to="slogan-portal" :disabled="mediaQueries.lg" class="col header__slogan">
                <div class="slogan slogan--header">Лучший выбор<br class="hidden-md"> флюро-одежды в Европе</div>
              </portal>
              <portal to="mobile-portal-contacts-header" :disabled="mediaQueries.md" class="col header__contacts">
                <div class="contacts contacts--header">
                  <div class="phone"><a href="tel:+74991904900" class="phone__link">8 (499) 190-49-00</a></div>
                  <div class="callback"><a href="#popup-callback" class="callback__link popup-opener">Обратный
                    звонок</a></div>
                </div>
              </portal>
            </div>
          </div>
          <div class="col col-sm-auto col-md-auto col-lg-6">
            <div class="row justify-content-end align-items-center">
              <div class="col-md col-lg-auto header__search">
                <portal to="mobile-portal-search-header" :disabled="mediaQueries.lg">
                  <Search/>
                </portal>
              </div>

              <!--              <div class="col-auto header__cart">-->
              <portal to="mobile-portal-cart-header" :disabled="mediaQueries.sm" class="col-auto header__cart">
                <HeaderCart/>
              </portal>
              <!--              </div>-->
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="header__menu">
      <div class="container">
        <portal to="mobile-portal-menu" :disabled="mediaQueries.lg">
          <HeaderMenu/>
        </portal>
      </div>
    </div>
    <div :class="['burger', {'opened':mobileShow}]" @click="onBurgerClick()">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
    <transition name="fade">
      <div v-if="mobileShow" class="mobile-menu" style="display: block;">
        <!--        <portal-target name="mobile-portal-header"/>-->
        <portal-target slim name="mobile-portal-cart-header"/>
        <portal-target slim name="mobile-portal-menu"/>
        <portal-target slim name="mobile-portal-nav-header"/>
        <portal-target slim name="mobile-portal-contacts-header"/>
        <portal-target slim name="mobile-portal-auth-header"/>
        <portal-target slim name="mobile-portal-lang-toggle-header"/>
        <portal-target slim name="mobile-portal-search-header"/>
        <!--        <portal-target name="mobile-portal" multiple/>-->
      </div>
    </transition>
  </header>
</template>
<script>

import Logo from "~/components/layout/Logo";
import Search from "~/components/search/Search";
import HeaderCart from "~/components/cart/HeaderCart";
import HeaderMenu from "~/components/layout/header/HeaderMenu";
import LangSwitcher from "~/components/layout/LangSwitcher";
import AuthWidget from "~/components/auth/AuthWidget";

export default {

  inject: ['mediaQueries'],

  components: {AuthWidget, LangSwitcher, HeaderMenu, HeaderCart, Search, Logo},

  data() {
    return {
      mobileShow: false,
    }
  },
  methods: {
    onBurgerClick() {

      if (this.mobileShow) {
        // hide
        this.$bus.$emit('MOBILEMENU_HIDE')
      } else {
        // show
        this.$bus.$emit('MOBILEMENU_SHOW')
      }
    },
    onLinkClick() {
      this.$bus.$emit('MOBILEMENU_HIDE')
    }

  },
  mounted() {
    this.$bus.$on('MOBILEMENU_SHOW', () => {
      this.mobileShow = true
    })
    this.$bus.$on('MOBILEMENU_HIDE', () => {
      this.mobileShow = false
    })
  }
}
</script>
