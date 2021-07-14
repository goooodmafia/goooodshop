<template>
  <div class="container">
    <div class="row">
      <div class="col">

        <validation-observer ref="getpriceobserver" v-slot="{ handleSubmit }">
          <b-form @submit.stop.prevent="handleSubmit(onSubmit)" class="form form--feedback">
            <div class="form__heading"><span>Получить оптовый прайс‑лист:</span></div>

<!--            <div class="form__row form__row&#45;&#45;wholesale">-->
<!--              <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--                <validation-provider-->
<!--                  name="email"-->
<!--                  :rules="{ required: true, min: 3 }"-->
<!--                  v-slot="validationContext"-->
<!--                >-->
<!--                  <b-form-group-->
<!--                    :label="$t('page.login.loginfield')">-->
<!--                    <b-form-input-->
<!--                      type="email"-->
<!--                      v-model="form.email"-->
<!--                      autocomplete="on"-->
<!--                      :state="getValidationState(validationContext)"-->
<!--                    ></b-form-input>-->

<!--                    <b-form-invalid-feedback-->
<!--                      v-for="(error, index) in validationContext.errors"-->
<!--                      :key="index">{{ error }}-->
<!--                    </b-form-invalid-feedback>-->
<!--                  </b-form-group>-->
<!--                </validation-provider>-->
<!--              </div>-->
<!--            </div>-->

          </b-form>
        </validation-observer>

<!--        <form action="#" class="form form&#45;&#45;feedback">-->
<!--          <div class="form__heading"><span>Получить оптовый прайс‑лист:</span></div>-->
<!--          &lt;!&ndash; BEGIN form__row &ndash;&gt;-->
<!--          <div class="form__row form__row&#45;&#45;wholesale">-->
<!--            <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--              <div class="form__field">-->
<!--                <label class="form__label" for="name">Имя, фамилия*:</label>-->
<!--                <input type="text" id="name" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--              <div class="form__field">-->
<!--                <label class="form__label" for="phone">Телефон*:</label>-->
<!--                <input type="text" id="phone" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--              <div class="form__field">-->
<!--                <label class="form__label" for="company">Компания:</label>-->
<!--                <input type="text" id="company" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--              <div class="form__field">-->
<!--                <label class="form__label" for="where">Откуда Вы узнали о нас:</label>-->
<!--                <input type="text" id="where" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--          &lt;!&ndash; END form__row &ndash;&gt;-->
<!--          &lt;!&ndash; BEGIN form__row &ndash;&gt;-->
<!--          <div class="form__row form__row&#45;&#45;wholesale">-->
<!--            <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--              <div class="form__field">-->
<!--                <label class="form__label" for="email">Эл. почта*:</label>-->
<!--                <input type="text" id="email" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--              <div class="form__field">-->
<!--                <label class="form__label" for="email">Город*:</label>-->
<!--                <input type="text" id="city" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="form__col form__col&#45;&#45;dbl-wholesale">-->
<!--              <div class="form__field form__field&#45;&#45;textarea">-->
<!--                <label class="form__label" for="interest">Чем вызван интерес к нашему прайс-листу:</label>-->
<!--                <input type="text" id="interest" class="form__input">-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--          &lt;!&ndash; END form__row &ndash;&gt;-->
<!--          &lt;!&ndash; BEGIN form__row &ndash;&gt;-->
<!--          <div class="form__row form__row&#45;&#45;wholesale">-->
<!--            <div class="form__wrap-text form__wrap-text&#45;&#45;wholesale">-->
<!--              <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--                <div class="form__note">* поля, обязательные для заполнения</div>-->
<!--              </div>-->
<!--              <div class="form__col form__col&#45;&#45;input-wholesale">-->
<!--                <div class="form__guarantee form__guarantee&#45;&#45;wholesale">Мы гарантируем конфиденциальность оставленной-->
<!--                  Вами информации.-->
<!--                </div>-->
<!--              </div>-->
<!--              <div class="form__col form__col&#45;&#45;dbl-wholesale">-->
<!--                <div class="form__consent form__consent&#45;&#45;wholesale">-->
<!--                  <input id="consent" type="checkbox" class="form__checkbox" checked="">-->
<!--                  <label for="consent" class="form__label form__label&#45;&#45;checkbox">Отправляя данную форму Вы выражаете-->
<!--                    согласие на обработку персональных данных.-->
<!--                  </label>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--          &lt;!&ndash; END form__row &ndash;&gt;-->
<!--          <div class="form__actions">-->
<!--            <div class="form__actions-in">-->
<!--              <button class="form__button btn">Отправить</button>-->
<!--            </div>-->
<!--          </div>-->
<!--        </form>-->

      </div>
    </div>
  </div>
</template>

<script>

import GETPRICE from '~/api/mutation/getPrice.graphql'
import {ValidationObserver, ValidationProvider} from "vee-validate";

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
    async onSubmit() {
      const credentials = this.form
      try {
        const res = await this.$apollo.mutate({
          mutation: GETPRICE,
          variables: credentials
        })
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
