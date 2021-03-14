<template>


    <div class="catalog-unit catalog-unit--catalog">

      <Figure :item="item"/>

      <Details :item="item"/>

      <!-- Hover-->
    </div>

</template>

<script>
import Details from "./Details";
import Figure from "./Figure";
export default {
  components: {Figure, Details},
  props:["item"],
}
</script>

<style>
.catalog-unit__figure {
    min-width: 160px;
    min-height: 200px;
    background-color: rgba(255,255,255,0.2);
}
</style>
