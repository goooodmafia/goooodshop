<template>
  <validation-observer ref="loginobserver" v-slot="{ handleSubmit }">
    <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
      <validation-provider
        :name="$t('page.login.loginfield')"
        :rules="{ required: true, min: 3 }"
        v-slot="validationContext"
      >
        <b-form-group id="email-group" label="Email" label-for="email-input">
          <b-form-input
            id="email-input"
            name="email-input"
            type="email"
            v-model="form.email"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="email-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="login-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <validation-provider :name="$t('page.login.passfield')" :rules="{ required: true }" v-slot="validationContext">
        <b-form-group id="password-group" label="Password" label-for="password-input">
          <b-form-input
            id="password-input"
            name="password-input"
            type="password"
            v-model="form.password"
            autocomplete="on"
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
          {{ error }}
        </div>
      </ValidationProvider>

      <div class="mb-3">
        <nuxt-link :to="localePath('login-password-reset')">{{ $t('page.login.password_reset') }}</nuxt-link>
      </div>
      <div class="mb-3">
        <nuxt-link :to="localePath('/login/register')">{{ $t('page.login.register') }}</nuxt-link>
      </div>

      <b-button type="submit" variant="primary">{{ $t('page.login.loginbutton') }}</b-button>
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
        if (res.success === true) {
          await this.$apolloHelpers.onLogin(res.token)
          this.$router.push(this.localePath('/'))
        } else {

                    let e = {}
          for (let prop in res.errors) {
            e[prop] = res.errors[prop].map((m)=>m.message)
          }

          this.$refs.loginobserver.setErrors(e)
        }
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
