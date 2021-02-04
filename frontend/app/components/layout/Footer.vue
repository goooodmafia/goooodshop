<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-sm-6 col-md-4 col-lg-3 footer__logo">
          <Logo class="logo--footer"/>
        </div>
        <div class="col-md-8 col-lg-4 col-xl-5 footer__menu">
          <div class="bottom-menu">
            <div class="bottom-menu__col">
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Мужское</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Женское</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Детское</a></div>
            </div>
            <div class="bottom-menu__col">
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Купить оптом</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Бренд GOOD</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Новинки</a></div>
            </div>
            <div class="bottom-menu__col">
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Помощь</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Доставка</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Контакты</a></div>
            </div>
            <div class="bottom-menu__col">
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Таблица размеров</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Отзывы</a></div>
              <div class="bottom-menu__item"><a href="#" class="bottom-menu__link">Статьи</a></div>
            </div>
          </div>
        </div>
        <div class="col-sm-4 col-md-2 col-lg-2 footer__lang">
          <LangSwitcher class="lang-toggle--footer"/>
        </div>
        <div class="col-sm-4 col-sm-offset-4 col-md-3 col-lg-3 col-xl-2 footer__contacts">
          <div class="contacts contacts--footer">
            <div class="phone phone--lg"><a href="tel:+74991904900" class="phone__link">8 (499) 190-49-00</a></div>
            <div class="callback"><a href="#popup-callback" class="callback__link popup-opener">Обратный звонок</a>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4 col-lg-3 footer__slogan">
          <div class="slogan slogan--footer">Лучший выбор<br> флюро-одежды в Европе</div>
        </div>

        <div class="col-md-8 col-lg-4 col-xl-5 footer__wrap">
          <div class="footer__holder">
            <div class="footer__delivery">
              <div class="delivery">
                <div class="delivery__title">Способы доставки</div>
                <div class="delivery__list">
                  <div class="delivery__item"><img src="~/assets/img/icon__delivery-1.svg" alt="" class="delivery__img">
                  </div>
                  <div class="delivery__item"><img src="~/assets/img/icon__delivery-2.svg" alt="" class="delivery__img">
                  </div>
                  <div class="delivery__item"><img src="~/assets/img/icon__delivery-3.svg" alt="" class="delivery__img">
                  </div>
                  <div class="delivery__item"><img src="~/assets/img/icon__delivery-4.svg" alt="" class="delivery__img">
                  </div>
                  <div class="delivery__item"><img src="~/assets/img/icon__delivery-5.svg" alt="" class="delivery__img">
                  </div>
                  <div class="delivery__item"><img src="~/assets/img/icon__delivery-6.svg" alt="" class="delivery__img">
                  </div>
                </div>
              </div>
            </div>
            <div class="footer__payments">
              <div class="payments">
                <div class="payments__title">Способы оплаты</div>
                <div class="payments__list">
                  <div class="payments__item"><img src="~/assets/img/icon__payment-1.svg" alt="" class="payments__img">
                  </div>
                  <div class="payments__item"><img src="~/assets/img/icon__payment-2.svg" alt="" class="payments__img">
                  </div>
                  <div class="payments__item"><img src="~/assets/img/icon__payment-3.svg" alt="" class="payments__img">
                  </div>
                  <div class="payments__item"><img src="~/assets/img/icon__payment-4.svg" alt="" class="payments__img">
                  </div>
                  <div class="payments__item"><img src="~/assets/img/icon__payment-5.svg" alt="" class="payments__img">
                  </div>
                  <div class="payments__item"><img src="~/assets/img/icon__payment-6.svg" alt="" class="payments__img">
                  </div>
                  <div class="payments__item"><img src="~/assets/img/icon__payment-7.svg" alt="" class="payments__img">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-4 col-md-3 col-lg-2 footer__social">
          <div class="social social--footer">
            <a href="#" class="social__item social__item--vk" title="ВКонтакте">ВКонтакте</a>
            <a href="#" class="social__item social__item--instagram" title="Instagram">Instagram</a>
            <a href="#" class="social__item social__item--fb" title="Facebook">Facebook</a>
            <a href="#" class="social__item social__item--tw" title="Twitter">Twitter</a>
          </div>
        </div>
        <div class="col-md-4 col-lg-3 col-xl-2 footer__partnership">
          <div class="partnership">
            <p>Приглашаем к сотрудничеству дизайнеров и художников.</p>
            <p>Ваши работы отправляйте на наш адрес: <a href="mailto:info@gooood.ru">info@gooood.ru</a></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Logo from "./Logo";
import LangSwitcher from "./LangSwitcher";

export default {
  components: {LangSwitcher, Logo}
}
</script>
