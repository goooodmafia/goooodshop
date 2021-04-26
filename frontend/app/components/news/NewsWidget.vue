<template>
  <div class="container">
    <div class="row">
      <NewsItem v-for="(item,index) in items" :item="item" :key="index"/>
    </div>
  </div>
</template>
<script>
import NewsItem from "./NewsItem";

export default {
  components: {NewsItem},
  props:['items']
}
</script>
