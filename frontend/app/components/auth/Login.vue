<template>
  <validation-observer ref="observer" v-slot="{ handleSubmit }">
      <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
        <validation-provider
          name="Login"
          :rules="{ required: true, min: 3 }"
          v-slot="validationContext"
        >
          <b-form-group id="login-group" label="Login" label-for="login-input">
            <b-form-input
              id="login-input"
              name="login-input"
              v-model="form.login"
              :state="getValidationState(validationContext)"
              aria-describedby="login-live-feedback"
            ></b-form-input>

            <b-form-invalid-feedback id="login-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
          </b-form-group>
        </validation-provider>

        <validation-provider name="Password" :rules="{ required: true }" v-slot="validationContext">
          <b-form-group id="password-group" label="Password" label-for="password-input">
            <b-form-select
              id="password-input"
              name="password-input"
              v-model="form.pass"
              :state="getValidationState(validationContext)"
              aria-describedby="password-live-feedback"
            ></b-form-select>

            <b-form-invalid-feedback id="password-live-feedback">{{ validationContext.errors[0] }}</b-form-invalid-feedback>
          </b-form-group>
        </validation-provider>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button class="ml-2" @click="resetForm()">Reset</b-button>
      </b-form>
    </validation-observer>
</template>

<script>
import {ValidationProvider, ValidationObserver} from "vee-validate";

export default {

  components: {
    ValidationProvider, ValidationObserver
  },

  data() {
    return {
      form: {
        login: null,
        pass: null
      }
    };
  },
  methods: {
    getValidationState({ dirty, validated, valid = null }) {
      return dirty || validated ? valid : null;
    },
    resetForm() {
      this.form = {
        login: null,
        pass: null
      };

      this.$nextTick(() => {
        this.$refs.observer.reset();
      });
    },
    onSubmit() {
      console.log("Form submitted!");
      console.log(this.form);
    }
  }
}
</script>
