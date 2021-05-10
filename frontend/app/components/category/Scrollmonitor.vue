<template>
  <div ref="scrollmonitor">
<!--    <div v-if="this.$apollo.loading" class="text-center">-->
<!--      <font-awesome-icon :icon="['fas', 'circle-notch']" class="orange-text" spin size="6x"/>-->
<!--    </div>-->
  </div>
</template>

<script>
import scrollMonitor from "scrollmonitor";

export default {

  props:['products_has_more'],

  mounted() {
    const elementWatcher = scrollMonitor.create(this.$refs.scrollmonitor);
    elementWatcher.enterViewport(() => {
      if (this.products_has_more) {
        this.$bus.$emit('FETCH_MORE')
      }
    });
  }
}
</script>
