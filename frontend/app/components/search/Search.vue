<template>
  <form action="#" class="form search--header form--search">
    <div class="form__field form__field--search">
      <input
        v-model="search"
        @submit="submit"
        ref="search"
        type="search"
        class="form__input form__input--search"
        placeholder="Поиск"
      >
      <b-icon icon="search"></b-icon>
    </div>
  </form>

<!--  <b-input-group>-->
<!--    <b-form-input></b-form-input>-->
<!--    <b-input-group-append>-->
<!--      <b-input-group-text>-->
<!--        <b-icon icon="search"></b-icon>-->
<!--      </b-input-group-text>-->
<!--    </b-input-group-append>-->
<!--  </b-input-group>-->
</template>
<script>
export default {

  data() {
    return {
      search: ''
    }
  },

  methods: {
    submit() {
      console.log(this.search)
    }
  }
}
</script>
