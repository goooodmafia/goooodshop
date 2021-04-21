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

            <validation-observer ref="newpasswordobserver" v-slot="{ handleSubmit }">
              <b-form @submit.stop.prevent="handleSubmit(onSubmit)">
                <validation-provider
                  name="newPassword1"
                  :rules="{ required: true, min: 3, }"
                  v-slot="validationContext"
                >
                  <b-form-group
                    id="email-group"
                    :label="$t('page.password_reset.password1')"
                    label-for="email-input"
                  >
                    <b-form-input
                      id="email-input"
                      name="email-input"
                      v-model="form.newPassword1"
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

                <validation-provider
                  name="newPassword2"
                  :rules="{ required: true, min: 3, }"
                  v-slot="validationContext"
                >
                  <b-form-group
                    id="email-group"
                    :label="$t('page.password_reset.password2')"
                    label-for="email-input"
                  >
                    <b-form-input
                      id="email-input"
                      name="email-input"
                      v-model="form.newPassword2"
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
                    {{ error }}
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
import {ValidationObserver, ValidationProvider} from "vee-validate";
import PASSWORDRESET from "~/api/mutation/passwordReset.graphql"

export default {
  name: 'NewPassword',

  components: {Breadcrumbs, Wrapper, ValidationObserver, ValidationProvider},

  data() {
    return {
      breacrumbs: {
        title: this.$t('page.password_reset.title'),
        breadcrumbs: [],
      },

      form: {
        newPassword1: null,
        newPassword2: null,
      }
    }
  },

  methods: {
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },

    async onSubmit() {
      const credentials = this.form
      const token = this.$route.params.token
      try {
        const res = await this.$apollo.mutate({
          mutation: PASSWORDRESET,
          variables: {...credentials, token: token}
        }).then(({data}) => data && data.passwordReset)
        console.log(res)
        if (res.success === true) {
          this.$nuxt.error({ statusCode: 200, message: "Пароль успешно сменен" })
          // this.$router.push(this.localePath('/login'))
        } else {
          let e = {}
          for (let prop in res.errors) {
            e[prop] = res.errors[prop].map((m)=>m.message)
          }
          this.$refs.newpasswordobserver.setErrors(e)
        }
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
