<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container">
        <div class="row justify-content-md-center my-5">
          <div class="col-sm-12 col-md-6">
            <validation-observer ref="resetpasswordobserver" v-slot="{ handleSubmit }">
              <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
                <validation-provider
                  :name="$t('page.login.loginfield')"
                  :rules="{ required: true, min: 3, }"
                  v-slot="validationContext"
                >
                  <b-form-group
                    id="email-group"
                    :label="$t('page.password_reset.emailfield')"
                    label-for="email-input"
                  >
                    <b-form-input
                      id="email-input"
                      name="email-input"
                      v-model="form.email"
                      autocomplete="on"
                      :state="getValidationState(validationContext)"
                      aria-describedby="email-live-feedback"
                    ></b-form-input>
                    <b-form-invalid-feedback
                      id="login-live-feedback" v-for="(error, index) in validationContext.errors"
                      :key="index">
                      {{ error }}
                    </b-form-invalid-feedback>
                  </b-form-group>
                </validation-provider>

                <ValidationProvider name="nonFieldErrors" v-slot="validationContext">
                  <div class="mb-3" style="color: #dc3545;" v-for="(error, index) in validationContext.errors"
                       :key="index">
                    {{ error.message }}
                  </div>
                </ValidationProvider>


                <b-button type="submit" variant="primary">{{ $t('page.password_reset.submit') }}</b-button>
              </b-form>
            </validation-observer>

          </div>
        </div>
      </div>
    </template>
  </Wrapper>
</template>

<script>
import Wrapper from "~/components/layout/Wrapper";
import Breadcrumbs from "~/components/layout/Breadcrumbs";
import SENDPASSWORDRESETEMAIL from '~/api/mutation/sendPasswordResetEmail.graphql'
import {ValidationObserver, ValidationProvider} from "vee-validate";

export default {

  name: 'PasswordReset',

  components: {Breadcrumbs, Wrapper, ValidationProvider, ValidationObserver},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.password_reset.title'),
        breadcrumbs: [],
      },

      form: {
        email: null,
      }
    }
  },

  methods: {
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },

    async onSubmit() {
      const credentials = this.form
      try {
        const res = await this.$apollo.mutate({
          mutation: SENDPASSWORDRESETEMAIL,
          variables: credentials
        }).then(({data}) => data && data.sendPasswordResetEmail)
        console.log(res)
        if (res.success === true) {
          this.$nuxt.error({ statusCode: 200, message: "Проверьте почту" })
          // this.$router.push(this.localePath('/login'))
        } else {
          this.$refs.resetpasswordobserver.setErrors(res.errors)
        }
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
