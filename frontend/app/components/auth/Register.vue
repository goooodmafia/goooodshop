<template>
  <validation-observer ref="registerobserver" v-slot="{ handleSubmit }">
    <b-form @submit.stop.prevent="handleSubmit(onSubmit)">

      <!--Имя-->
      <validation-provider
        :name="$t('page.register.name_field')"
        :rules="{ required: true, min: 3 }"
        v-slot="validationContext"
      >
        <b-form-group id="name-group" :label="$t('page.register.name_field')" label-for="name-input">
          <b-form-input
            id="name-input"
            name="name-input"
            type="text"
            v-model="form.name"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="name-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="name-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <!--Фамилия-->
      <validation-provider
        :name="$t('page.register.first_name_field')"
        :rules="{}"
        v-slot="validationContext"
      >
        <b-form-group id="first_name-group" :label="$t('page.register.first_name_field')" label-for="first_name-input">
          <b-form-input
            id="first_name-input"
            name="first_name-input"
            type="text"
            v-model="form.first_name"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="first_name-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="first_name-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <!--Отчество-->
      <validation-provider
        :name="$t('page.register.second_name_field')"
        :rules="{}"
        v-slot="validationContext"
      >
        <b-form-group id="second_name-group" :label="$t('page.register.second_name_field')"
                      label-for="second_name-input">
          <b-form-input
            id="second_name-input"
            name="second_name-input"
            type="text"
            v-model="form.second_name"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="second_name-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="second_name-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <!--Дата рождения-->
      <validation-provider
        :name="$t('page.register.birth_date_field')"
        :rules="{ required: true}"
        v-slot="validationContext"
      >
        <b-form-group id="birth_date-group" :label="$t('page.register.birth_date_field')" label-for="birth_date-input">
          <b-form-datepicker
            id="birth_date-input"
            name="birth_date-input"
            v-model="form.birth_date"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="birth_date-live-feedback"
          ></b-form-datepicker>

          <b-form-invalid-feedback id="birth_date-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <!--Адресс-->
      <client-only placeholder="loading...">
        <VueDadata token="91887366306ab608f3ce2fdb6577c82847376590"></VueDadata>
      </client-only>


      <!--Email-->
      <validation-provider
        :name="$t('page.register.email_field')"
        :rules="{ required: true, min: 3 }"
        v-slot="validationContext"
      >
        <b-form-group id="email-group" :label="$t('page.register.email_field')" label-for="email-input">
          <b-form-input
            id="email-input"
            name="email-input"
            type="email"
            v-model="form.email"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="email-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="email-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <!--Пароль1-->
      <validation-provider :name="$t('page.register.pass_field1')" :rules="{ required: true }"
                           v-slot="validationContext">
        <b-form-group id="password1-group" :label="$t('page.register.pass_field1')" label-for="password1-input">
          <b-form-input
            id="password1-input"
            name="password1-input"
            type="password"
            v-model="form.password1"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="password-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="password1-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <!--Пароль2-->
      <validation-provider :name="$t('page.register.pass_field2')" :rules="{ required: true }"
                           v-slot="validationContext">
        <b-form-group id="password2-group" :label="$t('page.register.pass_field2')" label-for="password2-input">
          <b-form-input
            id="password2-input"
            name="password2-input"
            type="password"
            v-model="form.password2"
            autocomplete="on"
            :state="getValidationState(validationContext)"
            aria-describedby="password2-live-feedback"
          ></b-form-input>

          <b-form-invalid-feedback id="password2-live-feedback" v-for="(error, index) in validationContext.errors"
                                   :key="index">{{ error }}
          </b-form-invalid-feedback>
        </b-form-group>
      </validation-provider>

      <ValidationProvider name="nonFieldErrors" v-slot="validationContext">
        <div class="mb-3" style="color: #dc3545;" v-for="(error, index) in validationContext.errors" :key="index">
          {{ error }}
        </div>
      </ValidationProvider>

      <!--      <div class="mb-3">-->
      <!--        <nuxt-link :to="localePath('login-password-reset')">{{ $t('page.login.password_reset') }}</nuxt-link>-->
      <!--      </div>-->
      <!--      <div class="mb-3">-->
      <!--        <nuxt-link :to="localePath('/login/register')">{{ $t('page.login.register') }}</nuxt-link>-->
      <!--      </div>-->

      <b-button type="submit" variant="primary">{{ $t('page.register.registerbutton') }}</b-button>
    </b-form>
  </validation-observer>
</template>

<script>
  import {ValidationObserver, ValidationProvider} from "vee-validate";
  import VueDadata from 'vue-dadata'

  export default {

    components: {
      VueDadata, ValidationProvider, ValidationObserver
    },

    data() {
      const dadata_api_key = process.env.DADATA_API_KEY
      return {
        dadata_api_key: dadata_api_key,
        form: {
          name: '',
          first_name: '',
          second_name: '',
          birth_date: '',
          phone: '',
          email: '',
          sex: '',
          address: '',
          password1: '',
          password2: '',
        }
      }
    },
    methods: {
      getValidationState({dirty, validated, valid = null}) {
        return dirty || validated ? valid : null;
      },

      async onSubmit() {

      }
    },
    created() {

    }
  }
</script>
