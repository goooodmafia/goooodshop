<template>
  <div class="auth auth--header">
    <template v-if="!!this.$apolloHelpers.getToken()">
      <a href="" @click="this.$apolloHelpers.onLogout()" class="auth__item">Выйти</a>
    </template>
    <template v-else>

      <nuxt-link
        :to="localePath('login')"
        class="auth__item auth__item--login"
      >Войти</nuxt-link>
      <!--<a href="" @click="$router.push({query: Object.assign({}, this.$route.query, {login: true})})" class="auth__item auth__item&#45;&#45;login">Войти</a>-->
    </template>
    <!--<a href="" class="auth__item auth__item&#45;&#45;login">Войти</a>-->
    <!--<a href="#" class="auth__item auth__item&#45;&#45;login">Войти</a>-->
    <!--<a href="#popup-reg" class="auth__item popup-opener">Регистрация</a>-->
  </div>
</template>
