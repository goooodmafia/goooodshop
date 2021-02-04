<template>
  <header class="header">
    <div class="header__top">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-6">
            <div class="row">
              <div class="col header__nav">
                <div class="nav nav--header">
                  <div class="nav__in">
                    <div class="nav__item">
                      <nuxt-link class="nav__link" :to="localePath('index')">Помощь</nuxt-link>
                    </div>
                    <div class="nav__item">
                      <nuxt-link class="nav__link" :to="localePath('index')">Доставка</nuxt-link>
                    </div>
                    <div class="nav__item">
                      <nuxt-link class="nav__link" :to="localePath('contacts')">Контакты</nuxt-link>
                    </div>
                    <div class="nav__item">
                      <nuxt-link class="nav__link" :to="localePath('index')">Таблица размеров</nuxt-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-12 col-lg-6">
            <div class="row justify-content-sm-end">
              <div class="col-sm-auto col-md-auto col-lg header__auth">
                <div class="auth auth--header">
                  <a href="#popup-login" class="auth__item auth__item--login popup-opener">Войти</a>
                  <a href="#popup-reg" class="auth__item popup-opener">Регистрация</a>
                </div>
              </div>
              <div class="col-auto header__lang">
                <LangSwitcher class="lang-toggle--header"/>
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
              <div class="col header__slogan">
                <div class="slogan slogan--header">Лучший выбор<br class="hidden-md"> флюро-одежды в Европе</div>
              </div>
              <div class="col header__contacts">
                <div class="contacts contacts--header">
                  <div class="phone"><a href="tel:+74991904900" class="phone__link">8 (499) 190-49-00</a></div>
                  <div class="callback"><a href="#popup-callback" class="callback__link popup-opener">Обратный
                    звонок</a></div>
                </div>
              </div>
            </div>
          </div>
          <div class="col col-sm-auto col-md-auto col-lg-6">
            <div class="row justify-content-end align-items-center">
              <Search/>
              <HeaderCart/>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="header__menu">
      <HeaderMenu/>
    </div>
  </header>
</template>
<script>
import Logo from "./Logo";
import Search from "../search/Search";
import HeaderCart from "../cart/HeaderCart";
import HeaderMenu from "../header/HeaderMenu";
import LangSwitcher from "./LangSwitcher";

export default {
  components: {LangSwitcher, HeaderMenu, HeaderCart, Search, Logo}
}
</script>
