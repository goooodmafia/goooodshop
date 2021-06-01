<template>

  <div class="row">
    <div class="col">

      <validation-observer ref="loginobserver" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">

          <!--Email-->
          <div class="row">
            <div class="col-12">
              <validation-provider
                name="email"
                :rules="{ required: true, min: 3 }"
                v-slot="validationContext"
              >
                <b-form-group
                  :label="$t('page.login.loginfield')">
                  <b-form-input
                    type="email"
                    v-model="form.email"
                    autocomplete="on"
                    :state="getValidationState(validationContext)"
                  ></b-form-input>

                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index">{{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>
          </div>

          <!--Пароль-->
          <div class="row">
            <div class="col-12">
              <validation-provider
                name="password"
                :rules="{ required: true }"
                v-slot="validationContext"
              >
                <b-form-group
                  :label="$t('page.login.passfield')"
                >
                  <b-form-input
                    type="password"
                    v-model="form.password"
                    autocomplete="on"
                    :state="getValidationState(validationContext)"
                  ></b-form-input>

                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index">{{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>
          </div>

          <div class="row">
            <div class="col-12">
              <ValidationProvider name="nonFieldErrors" v-slot="validationContext">
                <div class="mb-3" style="color: #dc3545;" v-for="(error, index) in validationContext.errors"
                     :key="index">
                  {{ error }}
                </div>
              </ValidationProvider>
            </div>
          </div>

          <div class="row mt-3">
            <div class="col-12 text-center">
              <nuxt-link :to="localePath('login-password-reset')">{{ $t('page.login.password_reset') }}</nuxt-link>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-12 text-center">
              <nuxt-link :to="localePath('/login/register')">{{ $t('page.login.register') }}</nuxt-link>
            </div>
          </div>

          <div class="row mt-3">
            <div class="col-12 text-center">
              <b-button class="gd-btn" type="submit">{{ $t('page.login.loginbutton') }}</b-button>
            </div>
          </div>

        </b-form>
      </validation-observer>

    </div>
  </div>
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
            e[prop] = res.errors[prop].map((m) => m.message)
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
