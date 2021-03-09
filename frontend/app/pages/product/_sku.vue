<template>
  <Wrapper>
    <div class="container">
      <div class="row">
        <Breadcrumbs :data="breadcrumbs">
          <template v-slot:sidebar>
            <div class="col-md-auto col-sm-12">
              <Sidebar>
                <!-- <Filters :filters="filters"/>-->
              </Sidebar>
            </div>
          </template>

          <template>

          </template>

        </Breadcrumbs>

      </div>
    </div>
  </Wrapper>
</template>

<script>

import Wrapper from "../../components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import Sidebar from "~/components/category/Sidebar";

export default {
  components: {Wrapper, Breadcrumbs, Sidebar},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.help.title'),
        breadcrumbs: [],
      },
    }
  },
}
</script>
