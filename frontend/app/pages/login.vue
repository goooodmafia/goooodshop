<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container">
        <div class="row justify-content-md-center my-5">
          <div class="col-sm-12 col-md-6">
            <Login/>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>


import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Login from "~/components/auth/Login";


export default {



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
