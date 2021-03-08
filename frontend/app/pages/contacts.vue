<template>
  <Wrapper>
    <template v-slot:header>
      <div class="container">
        <Breadcrumbs :data="breacrumbs"/>
      </div>
    </template>
    <template>
      <div class="container contacts-block">
        <div class="row">
          <div class="col">
            <div class="contacts-block__wrap">
              <div class="contacts-block__details" v-html="contacts_map"/>
              <div class="contacts-block__map">
                <yandex-map
                  :coords="coords"
                  :zoom="17"
                >
                  <ymap-marker
                    marker-id="123"
                    :coords="coords"
                    :icon="markerIcon"
                  />
                </yandex-map>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container" v-html="contacts_shops"/>

      <div class="container" v-html="contacts_credentials"/>


    </template>

  </Wrapper>
</template>


<script>


import Wrapper from "../components/layout/Wrapper";
import Breadcrumbs from "../components/layout/Breadcrumbs";

export default {

  name: 'Contacts',

  components: {Breadcrumbs, Wrapper,},

  data() {
    return {
      contacts_map: null,
      contacts_shops: null,
      contacts_credentials: null,
      breacrumbs: {
        title: this.$t('page.contacts.title'),
        breadcrumbs: [],
      },

      coords: [
        // 55.793278,
        // 37.489294,
        55.79321156892391,
        37.489256999999995,
      ],

      markerIcon: {
        layout: 'default#image',
        imageHref: 'map-marker.svg',
        imageSize: [56, 77],
        imageOffset: [-28, -77],
      }
    }
  },

  async asyncData({app}) {
    const contacts_map = await import(`~/content/contacts/contacts_map_${app.i18n.locale}.md`)
    const contacts_shops = await import(`~/content/contacts/contacts_shops_${app.i18n.locale}.md`)
    const contacts_credentials = await import(`~/content/contacts/contacts_credentials_${app.i18n.locale}.md`)
    return {
      contacts_map: contacts_map.html,
      contacts_shops: contacts_shops.html,
      contacts_credentials: contacts_credentials.html,
    }
    // return {contacts_map: app.$md.render('### md text')}
  }
}
</script>

<style>
.ymap-container {
  height: 100%;
}
</style>
