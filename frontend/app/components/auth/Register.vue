<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <FormField v-model:value="form.name"/>
      </div>
    </div>
<!--    <validation-observer ref="registerobserver" v-slot="{ handleSubmit }">-->
<!--      <b-form @submit.stop.prevent="handleSubmit(onSubmit)">-->

<!--        <div class="row">-->

<!--          -->
<!--          -->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Имя&ndash;&gt;-->
<!--            <validation-provider-->
<!--              :rules="{ required: true, min: 3 }"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group id="name-group" :label="$t('page.register.name_field')" label-for="name-input">-->
<!--                <b-form-input-->
<!--                  id="name-input"-->
<!--                  name="name-input"-->
<!--                  type="text"-->
<!--                  v-model="form.name"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="name-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="name-live-feedback" v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->

<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Телефон&ndash;&gt;-->
<!--            <validation-provider-->
<!--              :name="$t('page.register.phone_field')"-->
<!--              :rules="{ required: true}"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group id="phone-group" :label="$t('page.register.phone_field')" label-for="name-input">-->
<!--                <b-form-input-->
<!--                  id="phone-input"-->
<!--                  name="phone-input"-->
<!--                  type="text"-->
<!--                  v-model="form.phone"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="phone-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="phone-live-feedback" v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->

<!--        </div>-->

<!--        <div class="row">-->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Фамилия&ndash;&gt;-->
<!--            <validation-provider-->
<!--              :name="$t('page.register.first_name_field')"-->
<!--              :rules="{}"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group id="first_name-group" :label="$t('page.register.first_name_field')"-->
<!--                            label-for="first_name-input">-->
<!--                <b-form-input-->
<!--                  id="first_name-input"-->
<!--                  name="first_name-input"-->
<!--                  type="text"-->
<!--                  v-model="form.first_name"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="first_name-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="first_name-live-feedback"-->
<!--                                         v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Email&ndash;&gt;-->
<!--            <validation-provider-->
<!--              :name="$t('page.register.email_field')"-->
<!--              :rules="{ required: true, min: 3 }"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group id="email-group" :label="$t('page.register.email_field')" label-for="email-input">-->
<!--                <b-form-input-->
<!--                  id="email-input"-->
<!--                  name="email-input"-->
<!--                  type="email"-->
<!--                  v-model="form.email"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="email-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="email-live-feedback" v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="row">-->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Отчество&ndash;&gt;-->
<!--            <validation-provider-->
<!--              :name="$t('page.register.second_name_field')"-->
<!--              :rules="{}"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group id="second_name-group" :label="$t('page.register.second_name_field')"-->
<!--                            label-for="second_name-input">-->
<!--                <b-form-input-->
<!--                  id="second_name-input"-->
<!--                  name="second_name-input"-->
<!--                  type="text"-->
<!--                  v-model="form.second_name"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="second_name-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="second_name-live-feedback"-->
<!--                                         v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            <b-form-group>-->
<!--              <span>* поля, обязательные для заполнения</span>-->
<!--            </b-form-group>-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="row">-->
<!--          <div class="col-md-4 col-sm-12">-->
<!--            &lt;!&ndash;Дата рождения&ndash;&gt;-->
<!--            <validation-provider-->
<!--              :name="$t('page.register.birth_date_field')"-->
<!--              :rules="{}"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group id="birthDate-group" :label="$t('page.register.birth_date_field')"-->
<!--                            label-for="birthDate-input">-->
<!--                <b-form-datepicker-->
<!--                  id="birthDate-input"-->
<!--                  name="birthDate-input"-->
<!--                  v-model="form.birthDate"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="birtDate-live-feedback"-->
<!--                ></b-form-datepicker>-->

<!--                <b-form-invalid-feedback id="birthDate-live-feedback"-->
<!--                                         v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--          <div class="col-md-8 col-sm-12 justify-content-md-right">-->
<!--            &lt;!&ndash;Пол&ndash;&gt;-->
<!--            <b-form-group label="Пол" v-slot="{ ariaDescribedby }">-->
<!--              <b-form-radio-group-->
<!--                id="radio-slots"-->
<!--                v-model="selected"-->
<!--                :options="options"-->
<!--                button-variant="warning"-->
<!--                :aria-describedby="ariaDescribedby"-->
<!--                name="radio-options-slots"-->
<!--              >-->
<!--              </b-form-radio-group>-->
<!--            </b-form-group>-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="row">-->
<!--          <div class="col-md-12 col-sm-12">-->
<!--            &lt;!&ndash;Адресс&ndash;&gt;-->
<!--            <validation-provider-->
<!--              name="address"-->
<!--              v-slot="validationContext"-->
<!--            >-->
<!--              <b-form-group-->
<!--                :label="$t('page.register.address_field')"-->
<!--              >-->

<!--                <client-only placeholder="loading...">-->
<!--                  <VueDadata-->
<!--                    token="91887366306ab608f3ce2fdb6577c82847376590"-->
<!--                    defaultClass="gd-dadata"-->
<!--                  ></VueDadata>-->
<!--                </client-only>-->

<!--                <b-form-invalid-feedback id="address-live-feedback"-->
<!--                                         v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->

<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="row">-->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Пароль1&ndash;&gt;-->
<!--            <validation-provider :name="$t('page.register.pass_field1')" :rules="{ required: true }"-->
<!--                                 v-slot="validationContext">-->
<!--              <b-form-group id="password1-group" :label="$t('page.register.pass_field1')" label-for="password1-input">-->
<!--                <b-form-input-->
<!--                  id="password1-input"-->
<!--                  name="password1-input"-->
<!--                  type="password"-->
<!--                  v-model="form.password1"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="password-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="password1-live-feedback" v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--          <div class="col-md-6 col-sm-12">-->
<!--            &lt;!&ndash;Пароль2&ndash;&gt;-->
<!--            <validation-provider :name="$t('page.register.pass_field2')" :rules="{ required: true }"-->
<!--                                 v-slot="validationContext">-->
<!--              <b-form-group id="password2-group" :label="$t('page.register.pass_field2')" label-for="password2-input">-->
<!--                <b-form-input-->
<!--                  id="password2-input"-->
<!--                  name="password2-input"-->
<!--                  type="password"-->
<!--                  v-model="form.password2"-->
<!--                  autocomplete="on"-->
<!--                  :state="getValidationState(validationContext)"-->
<!--                  aria-describedby="password2-live-feedback"-->
<!--                ></b-form-input>-->

<!--                <b-form-invalid-feedback id="password2-live-feedback" v-for="(error, index) in validationContext.errors"-->
<!--                                         :key="index">{{ error }}-->
<!--                </b-form-invalid-feedback>-->
<!--              </b-form-group>-->
<!--            </validation-provider>-->
<!--          </div>-->
<!--        </div>-->

<!--        <div class="row">-->
<!--          <div class="col-12">-->
<!--            &lt;!&ndash;Ошибки&ndash;&gt;-->
<!--            <ValidationProvider name="nonFieldErrors" v-slot="validationContext">-->
<!--              <div class="mb-3" style="color: #dc3545;" v-for="(error, index) in validationContext.errors" :key="index">-->
<!--                {{ error }}-->
<!--              </div>-->
<!--            </ValidationProvider>-->
<!--          </div>-->
<!--        </div>-->

<!--        &lt;!&ndash;      <div class="mb-3">&ndash;&gt;-->
<!--        &lt;!&ndash;        <nuxt-link :to="localePath('login-password-reset')">{{ $t('page.login.password_reset') }}</nuxt-link>&ndash;&gt;-->
<!--        &lt;!&ndash;      </div>&ndash;&gt;-->
<!--        &lt;!&ndash;      <div class="mb-3">&ndash;&gt;-->
<!--        &lt;!&ndash;        <nuxt-link :to="localePath('/login/register')">{{ $t('page.login.register') }}</nuxt-link>&ndash;&gt;-->
<!--        &lt;!&ndash;      </div>&ndash;&gt;-->

<!--        <b-button class="gd-btn" type="submit" variant="primary">{{ $t('page.register.registerbutton') }}</b-button>-->
<!--      </b-form>-->
<!--    </validation-observer>-->
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
      const dadata_api_key = process.env.DADATA_API_KEY
      return {
        selected: 'n/a',
        options: [
          {text: 'Не укахан', value: 'n/a'},
          {text: 'Мужской', value: 'men'},
          {text: 'Женский', value: 'woman'}
        ],
        dadata_api_key: dadata_api_key,
        form: {
          name: '',
          firstName: '',
          secondName: '',
          birthDate: '',
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
        try {
          const res = await this.$apollo.mutate({
            mutation: REGISTER,
            variables: this.form
          }).then(({data}) => data.register)

          console.log(res)

          if (res.success === true) {
            // await this.$apolloHelpers.onLogin(res.token)
            // this.$router.push(this.localePath('/'))
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
    created() {

    }
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
