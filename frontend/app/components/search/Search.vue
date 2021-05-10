<template>
  <form v-on:submit.prevent="submit" class="form search--header form--search">
    <div class="form__field form__field--search">
      <input
        v-model="search"
        ref="search"
        type="search"
        class="form__input form__input--search"
        placeholder="Поиск"
      >
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
      // this.$router.push({path: '/category/', query: {search: this.search}})
      // this.$router.push({path: this.localePath('category'), query: {search: this.search}});
      this.$nuxt.$options.router.push(
        {
          path: this.localePath('/category/'),
          // params: {
          //
          // },s
          query: {
            search: this.search
          }
        }
      );
    }
  }
}
</script>
