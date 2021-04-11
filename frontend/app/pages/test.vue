<template>
  <Wrapper>
    <template>
      <div class="container">
        <div class="row">
          <div class="col">
            <h1>###test</h1>
          </div>
        </div>
      </div>
    </template>
  </Wrapper>


</template>

<script>

import Wrapper from "~/components/layout/Wrapper";

export default {
  middleware: 'auth',

  components: {Wrapper}
}
</script>
