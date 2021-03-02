<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <div class="row">
          <Breadcrumbs :data="breacrumbs"/>
        </div>
      </div>
    </template>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>#Контакты</h1>
          </div>
        </div>
      </div>
    </template>

  </Wrapper>
</template>


<script>
  import Wrapper from "../components/layout/Wrapper";
  import Breadcrumbs from "../components/layout/Breadcrumbs";

  export default {

    name: 'Contacts',

    components: {Breadcrumbs, Wrapper},

    data() {
      return {
        breacrumbs: {
          title: 'Контакты',
          breadcrumbs: []
        }
      }
    }
  }
</script>
