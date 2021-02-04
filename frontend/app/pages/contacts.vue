<template>
  <Wrapper>
    <template v-slot:header>
      <Breadcrumbs :data="breacrumbs"/>
      <Breadcrumbs :data="breacrumbs2"/>
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

  data(){
    return{
      breacrumbs:{
        title:'Контакты',
        breadcrumbs:[
          {title:'Контакты',link:this.localePath('contacts')},
          {title:'Контакты',link:this.localePath('contacts')},
          {title:'Контакты',link:this.localePath('contacts')}
        ]
      },
      breacrumbs2:{
        title:'Контакты',
        breadcrumbs:[]
      }
    }
  }
}
</script>
