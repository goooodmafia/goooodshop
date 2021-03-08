<template>
  <div class="container">
    <div v-for="item in items" class="row">
      <div class="col" v-html="$md.render(item.data)"/>
    </div>
  </div>
</template>

<script>

export default {
  props: [
    'items'
  ],

}
</script>
