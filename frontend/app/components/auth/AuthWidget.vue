<template>
  <div class="auth auth--header">
    <template v-if="!!this.$apolloHelpers.getToken()">
      <a href="" @click="logout" class="auth__item">{{ $t('page.login.logout') }}</a>
       <nuxt-link
        @click.native="onLinkClick"
        :to="localePath('profile')"
        class="auth__item"
      >{{ $t('page.login.profile') }}</nuxt-link>
    </template>
    <template v-else>

      <nuxt-link
        @click.native="onLinkClick"
        :to="localePath('login')"
        class="auth__item auth__item--login"
      >{{ $t('page.login.login') }}</nuxt-link>
      <!--<a href="" @click="$router.push({query: Object.assign({}, this.$route.query, {login: true})})" class="auth__item auth__item&#45;&#45;login">Войти</a>-->
      <nuxt-link
        @click.native="onLinkClick"
        :to="localePath('/login/register')"
        class="auth__item popup-opener"
      >{{ $t('page.login.register') }}
      </nuxt-link>
    </template>
    <!--<a href="" class="auth__item auth__item&#45;&#45;login">Войти</a>-->
    <!--<a href="#" class="auth__item auth__item&#45;&#45;login">Войти</a>-->
    <!--<a href="#popup-reg" class="auth__item popup-opener">Регистрация</a>-->
  </div>
</template>

<script>
export default {
  methods: {
    onLinkClick() {
      this.$bus.$emit('MOBILEMENU_HIDE')
    },
    logout() {
      this.$apolloHelpers.onLogout()
      this.onLinkClick()
    }
  }
}
</script>
