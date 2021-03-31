<template>
  <div class="catalog-unit catalog-unit--catalog">

    <Figure :item="item">
      <img class="my-catalog-slider-main-img" :src="item.thumbnail"/>
    </Figure>

    <Details :item="item"/>

  </div>

</template>

<script>
import Details from "./Details";
import Figure from "./Figure";

export default {
  components: {Details, Figure},
  props: {
    item: {},
  },
}
</script>

<style lang="scss">
//.catalog-unit__figure {
//  min-width: 160px;
//  min-height: 200px;
//  background-color: rgba(255, 255, 255, 0.2);
//}
//
//.catalog-unit__hover {
//  background-color: transparent;
//}


</style>
