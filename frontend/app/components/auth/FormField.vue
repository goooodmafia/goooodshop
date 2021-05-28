<template>
  <validation-provider :rules="{required:true}">
    <b-form-group>
      <b-form-input v-model="value"/>
      <div>error</div>
    </b-form-group>
  </validation-provider>
</template>

<script>
  import {ValidationObserver, ValidationProvider} from "vee-validate";

  export default {
    components: {
      ValidationProvider
    },
    props: ['value']
  }
</script>
