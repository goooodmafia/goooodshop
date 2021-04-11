<template>
  <validation-observer ref="loginobserver" v-slot="{ handleSubmit }">
    <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
      <validation-provider
        name="Email"
        :rules="{ required: true, min: 3 }"
        v-slot="validationContext"
      >
        <b-form-group id="email-group" label="Email" label-for="email-input">
          <b-form-input
            id="email-input"
            name="email-input"
            v-model="form.email"
            :state="getValidationState(validationContext)"
            aria-describedby="email-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="login-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <validation-provider name="Password" :rules="{ required: true }" v-slot="validationContext">
        <b-form-group id="password-group" label="Password" label-for="password-input">
          <b-form-input
            id="password-input"
            name="password-input"
            type="password"
            v-model="form.password"
            :state="getValidationState(validationContext)"
            aria-describedby="password-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="password-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <ValidationProvider name="nonFieldErrors" v-slot="validationContext">
        <div class="mb-3" style="color: #dc3545;" v-for="(error, index) in validationContext.errors" :key="index">
          {{ error.message }}
        </div>
      </ValidationProvider>

      <b-button type="submit" variant="primary">{{ $t('page.login.loginbutton')}}</b-button>
    </b-form>
  </validation-observer>
</template>

<script>
import {ValidationProvider, ValidationObserver} from "vee-validate";

import TOKENAUTH from '~/api/mutation/tokenAuth.graphql'
import CATEGORY from "~/api/query/category.graphql"

export default {

  components: {
    ValidationProvider, ValidationObserver
  },

  data() {
    return {
      form: {
        email: null,
        password: null
      }
    };
  },
  methods: {
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },
    // resetForm() {
    //   this.form = {
    //     email: null,
    //     password: null
    //   };
    //   this.$nextTick(() => {
    //     this.$refs.observer.reset();
    //   });
    // },
    async onSubmit() {
      const credentials = this.form
      try {
        const res = await this.$apollo.mutate({
          mutation: TOKENAUTH,
          variables: credentials
        }).then(({data}) => data && data.tokenAuth)
        console.log(res)
        if (res.success === true) {
          await this.$apolloHelpers.onLogin(res.token)
          this.$router.push(this.localePath('/'))
        } else {
          this.$refs.loginobserver.setErrors(res.errors)
        }
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
