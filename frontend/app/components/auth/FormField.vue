<template>

</template>

<script>
  import {ValidationObserver, ValidationProvider} from "vee-validate";

  export default {
    components: {
      ValidationProvider
    },
    props: ['modelValue']
  }
</script>
