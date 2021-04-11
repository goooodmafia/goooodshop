<template>
  <Wrapper>
    <div class="container">
      <Breadcrumbs :data="breacrumbs">
        <template v-slot:sidebar>
          <div class="col-md-auto col-sm-12">
            <Sidebar :currentpath="currentpath" :items="items">
            </Sidebar>
          </div>
        </template>

        <template>
          ### Orders
        </template>
      </Breadcrumbs>
    </div>

  </Wrapper>
</template>

<script>
import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";

export default {
  components: {Breadcrumbs, Wrapper, Sidebar},

  data() {
    return {
      breacrumbs: {
        title: 'История заказов',
        breadcrumbs: [
          {link: '/profile', title: this.$t('page.profile.title')}
        ],
      },
      items: [
        {path: '/profile', name: 'ЛИЧНЫЕ ДАННЫЕ', slug: "/profile", children: []},
        {path: '/profile/orders', name: 'ИСТОРИЯ ЗАКАЗОВ', slug: "/profile/orders", children: []},
        {path: '/static/downloads/good-opt.xls', name: 'ОПТОВЫЙ ПРАЙС-ЛИСТ', slug: "", children: []},
      ]
    }
  },

  computed: {
    currentpath() {
      const pathArray = [this.$route.fullPath]
      // return pathArray.slice(pathArray.indexOf('category') + 1)
      return pathArray
    }
  }

}
</script>
