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
            ###restore pass
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>
import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";

export default {
  components: {Breadcrumbs, Wrapper},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.restore.title'),
        breadcrumbs: [],
      },
    }
  },
}
</script>
