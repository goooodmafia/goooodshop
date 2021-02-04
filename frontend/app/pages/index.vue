<template>
  <Wrapper class="main-content--index">
    <template v-slot:header>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>#header</h1>
            <h1>#header</h1>
            <h1>#header</h1>
            <h1>#header</h1>
          </div>
        </div>
      </div>
    </template>

    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>app</h1>
            <h1>app</h1>
            <h1>app</h1>
            <h1>app</h1>
          </div>
        </div>
      </div>
    </template>

    <template v-slot:footer>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>#footer</h1>
            <h1>#footer</h1>
            <h1>#footer</h1>
            <h1>#footer</h1>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>


<script>

import Wrapper from "../components/layout/Wrapper";

export default {
  footerBorder: true,
  components: {
    Wrapper,
  }

}
</script>

