<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container">
        ### Login
<!--        <Login/>-->
      </div>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Login from "~/components/auth/Login";


export default {

  name: 'Login',

  components: {Breadcrumbs, Wrapper, Login},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.login.title'),
        breadcrumbs: [],
      },
    }
  },
}
</script>
