<template>
  <!--  <div class="container">-->
  <div class="row">
    <div class="col">

      <validation-observer ref="registerobserver" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(onSubmit)">

          <div class="row">

            <!--Имя-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{}" name="name" v-slot="validationContext">
                <b-form-group :label="$t('page.register.name_field')">
                  <b-form-input autofocus autocomplete="name" v-model="form.name"
                                :state="getValidationState(validationContext)"/>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

            <!--Телефон-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{required:true}" name="phone" v-slot="validationContext">
                <b-form-group :label="$t('page.register.phone_field')">
                  <b-form-input autocomplete="tel" v-model="form.phone" type="tel"
                                :state="getValidationState(validationContext)"/>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

            <!--Фамилия-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{}" name="firstName" v-slot="validationContext">
                <b-form-group :label="$t('page.register.first_name_field')">
                  <b-form-input v-model="form.firstName" :state="getValidationState(validationContext)"/>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

            <!--E-mail-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{required:true, email:true}" name="email" v-slot="validationContext">
                <b-form-group :label="$t('page.register.email_field')">
                  <b-form-input autocomplete="email" v-model="form.email" type="email"
                                :state="getValidationState(validationContext)"/>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

            <!--Отчество-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{}" name="secondName" v-slot="validationContext">
                <b-form-group :label="$t('page.register.second_name_field')">
                  <b-form-input v-model="form.secondName" :state="getValidationState(validationContext)"/>

                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

            <!--Текст-->
            <div class="col-md-6 col-sm-12 align-self-end">
              <div class="form-group">
                <div class="pb-2">* поля, обязательные для заполнения</div>
              </div>
            </div>

            <!--Дата рождения-->
            <div class="col-md-4 col-sm-12">
              <validation-provider :rules="{}" name="birthDate" v-slot="validationContext">
                <b-form-group :label="$t('page.register.birth_date_field')">
                  <b-form-datepicker
                    aria-autocomplete="bday"
                    v-model="form.birthDate"
                    :state="getValidationState(validationContext)"
                  ></b-form-datepicker>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

            <!--Пол-->
            <div class="col-md-8 col-sm-12">
              <validation-provider :rules="{required:true}" name="sex" v-slot="validationContext">
                <b-form-group :label="$t('page.register.sex_field')">
                  <b-form-radio-group v-model="form.sex" class="mt-1">
                    <b-form-radio value="NA">Не указан</b-form-radio>
                    <b-form-radio value="male">Мужской</b-form-radio>
                    <b-form-radio value="female">Женский</b-form-radio>
                  </b-form-radio-group>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </div>

          </div>
          <hr class="text-white">
          <div class="row">

            <!--Адрес-->
            <div class="col-md-12 col-sm-12">
              <validation-provider :rules="{}" v-slot="validationContext">
                <b-form-group :label="$t('page.register.address_field')">

                  <client-only placeholder="loading...">
                    <VueDadata
                      :token="$config.dadata_api_key"
                      defaultClass="gd-dadata"
                    ></VueDadata>
                  </client-only>

                  <!--                    <b-form-invalid-feedback-->
                  <!--                      v-for="(error, index) in validationContext.errors"-->
                  <!--                      :key="index"-->
                  <!--                    >-->
                  <!--                      {{ error }}-->
                  <!--                    </b-form-invalid-feedback>-->
                </b-form-group>
              </validation-provider>
            </div>

          </div>
          <hr class="text-white">
          <div class="row">

            <!--Пароль1-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{required:true}" name="password1" v-slot="validationContext">
                <b-form-group :label="$t('page.register.pass_field1')">
                  <b-form-input autocomplete="new-password" v-model="form.password1" type="password"
                                :state="getValidationState(validationContext)"/>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>

              </validation-provider>
            </div>

            <!--Пароль2-->
            <div class="col-md-6 col-sm-12">
              <validation-provider :rules="{required:true}" name="password2" v-slot="validationContext">
                <b-form-group :label="$t('page.register.pass_field2')">
                  <b-form-input autocomplete="new-password" v-model="form.password2" type="password"
                                :state="getValidationState(validationContext)"/>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>

              </validation-provider>
            </div>
          </div>

          <hr class="text-white">

          <div class="row">
            <!--Согласие-->
            <div class="col-md-12 col-sm-12">
              <validation-provider
                :rules="{ required: { allowFalse: false } }"
                v-slot="validationContext">
                <b-form-group>
                  <b-form-checkbox
                    v-model="form.agree"
                    :state="getValidationState(validationContext)"
                  >{{ $t('page.register.personal_field') }}
                  </b-form-checkbox>
                  <b-form-invalid-feedback
                    v-for="(error, index) in validationContext.errors"
                    :key="index"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </b-form-group>

              </validation-provider>
            </div>

          </div>

          <div class="row">
            <div class="col-12">
              <!--Ошибки-->
              <ValidationProvider name="nonFieldErrors" v-slot="validationContext">
                <div class="mb-3" style="color: #dc3545;" v-for="(error, index) in validationContext.errors"
                     :key="index">
                  {{ error }}
                </div>
              </ValidationProvider>
            </div>
          </div>

          <div class="row mt-5">
            <div class="col-12 text-center">
              <b-button class="gd-btn" type="submit">{{
                  $t('page.register.registerbutton')
                }}
              </b-button>
            </div>
          </div>

        </b-form>
      </validation-observer>

    </div>
  </div>
</template>

<script>
import {ValidationObserver, ValidationProvider} from "vee-validate";
import VueDadata from 'vue-dadata'
import REGISTER from '~/api/mutation/register.graphql'
import FormField from "./FormField";

export default {

  components: {
    FormField,
    VueDadata, ValidationProvider, ValidationObserver
  },

  data() {

    return {
      form: {
        name: '',
        firstName: '',
        secondName: '',
        birthDate: '',
        phone: '',
        email: '',
        sex: 'NA',
        address: '',
        password1: '',
        password2: '',
        agree: false,
      }
    }
  },

  methods: {
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },

    async onSubmit() {

      console.log(this.form)
      try {
        const res = await this.$apollo.mutate({
          mutation: REGISTER,
          variables: this.form
        }).then(({data}) => data.register)

        console.log(res)

        if (res.success === true) {
          await this.$apolloHelpers.onLogin(res.token)
          this.$router.push(this.localePath('/profile'))
        } else {
          let e = {}
          for (let prop in res.errors) {
            e[prop] = res.errors[prop].map((m) => m.message)
          }
          console.log(e)
          this.$refs.registerobserver.setErrors(e)
        }
      } catch (e) {
        console.error(e)
      }
    }
  },

}
</script>


<style lang="scss">
@import "assets/scss/gd/vars";

.b-form-btn-label-control.form-control > .btn {
  color: $body-bg;
}

.gd-dadata {
  &__container {
    width: 100%;
    position: relative;
  }

  &__input {

    display: block;
    width: 100%;
    height: calc(1.25em + 0.75rem + 2px);
    padding: 0.375rem 0.75rem;
    font-size: 0.9375rem;
    font-weight: 400;
    line-height: 1.25;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;

    //font-size: 14px;
    //width: 100%;
    //height: 47px;
    outline: none;
    //border-radius: 4px;
    //border: 1px solid #f1c40f;
    //transition: 0.3s;
    box-sizing: border-box;
    //padding: 0 5px;


    &:focus {
      box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075),
      0 0 0 3px rgba(255, 154, 0, 0.1);
      border-color: #ff931e;
    }
  }

  &__suggestions {
    position: absolute;
    z-index: 10;
    width: 100%;
    display: flex;
    flex-direction: column;
    background-color: #fff;
    color: black;

    &-item {
      padding: 10px;
      cursor: pointer;
      transition: 0.3s;

      &-highlight {
        background-color: #ffdfbd;
      }

      &:hover {
        background-color: #ffdfbd;
      }

      &_current {
        background-color: #fff5e7;
      }
    }
  }
}
</style>
