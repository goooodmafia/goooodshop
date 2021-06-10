<template>
  <Wrapper>
    <div class="container cabinet">
      <Breadcrumbs :data="breacrumbs"/>

      <div class="row">
        <div class="col-lg-3">
          <Sidebar :currentpath="currentpath" :items="items">
          </Sidebar>
        </div>


        <div class="col-lg-9">
          <div class="personal-data">

            <div class="personal-data__item">
              <div class="personal-data__value">
                <span class="personal-data__label">{{ $t('page.profile.name_field') }}</span> {{ user.name }}
              </div>
            </div>
            <div class="personal-data__item">
              <div class="personal-data__value">
                <span class="personal-data__label">{{ $t('page.profile.firstname_field') }}</span> {{ user.firstName }}
              </div>
            </div>
            <div class="personal-data__item">
              <div class="personal-data__value">
                <span class="personal-data__label">{{ $t('page.profile.secondname_field') }}</span> {{
                  user.secondName
                }}
              </div>
            </div>
            <div class="personal-data__item">
              <div class="personal-data__value">
                <span class="personal-data__label">{{ $t('page.profile.phone_field') }}</span> {{ user.phone }}
              </div>
            </div>
            <div class="personal-data__item">
              <div class="personal-data__value">
                <span class="personal-data__label">{{ $t('page.profile.email_field') }}</span> {{ user.email }}
              </div>
            </div>
            <div class="personal-data__item">
              <div class="personal-data__value">
                <span class="personal-data__label">{{ $t('page.profile.password_field') }}</span> *******
              </div>
              <div class="personal-data__edit">
                <nuxt-link :to="localePath('/login/password-reset')" class="edit-link">Изменить</nuxt-link>
              </div>
            </div>
          </div>
        </div>
        <!--          <hr/>-->
        <!--          {{ user }}-->
        <!--          <hr/>-->
        <!--          <pre>-->
        <!--          {{ users }}-->
        <!--          </pre>-->
        <!--          <hr/>-->
      </div>
    </div>

  </Wrapper>
</template>

<script>
import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";
import USER from "~/api/query/user.graphql"
import USERS from "~/api/query/users.graphql"

export default {
  components: {Breadcrumbs, Wrapper, Sidebar},

  data() {
    return {
      user:{
        name:'_____',
        firstName:'_____',
        secondName:'_____',
        phone:'_____',
        email:'_____',
      },
      breacrumbs: {
        title: 'Личные данные',
        breadcrumbs: [
          {link: '/profile', title: this.$t('page.profile.title')}
        ],
      },
      items: [
        {path: '/profile', name: 'ЛИЧНЫЕ ДАННЫЕ', slug: "/profile", children: []},
        {path: '/profile/orders', name: 'ИСТОРИЯ ЗАКАЗОВ', slug: "/profile/orders", children: []},
        {path: 'static/downloads/good-opt.xls', name: 'ОПТОВЫЙ ПРАЙС-ЛИСТ', slug: "", children: []},
      ]
    }
  },

  computed: {
    currentpath() {
      const pathArray = [this.$route.fullPath]
      // return pathArray.slice(pathArray.indexOf('category') + 1)
      return pathArray
    }
  },

  apollo: {
    users: {
      query: USERS
    },
    user: {
      query: USER
    }
  }

}
</script>
