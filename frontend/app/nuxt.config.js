import * as assert from "assert";

export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'app',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    '@fortawesome/fontawesome-svg-core/styles.css',
    '~/assets/scss/style.scss',
    'hooper/dist/hooper.css',
  ],
  loading: {
    color: '#fc982e',
  },

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [

    // { src: '@/plugins/markdown-it-vue-light', ssr: false }
    {src: '~/plugins/bus.js'},
    {src: '~/plugins/vue-fontawesome'},
    {src: '~/plugins/ymapPlugin.js', mode: 'client'},
    // {src: '~/plugins/vue-router-back-button.js', mode: 'client'},
    // {src: '~/plugins/vue-hooper'},
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    'nuxt-i18n',
    '@nuxtjs/apollo',
    // '@nuxtjs/markdownit',
    // '@nuxt/content'

    '~/modules/markdown'
  ],


  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    // extend(config, {isDev, isClient}) {
    //   config.module.rules.push({
    //     test: /\.html$/i,
    //     loader: 'html-loader',
    //     options:{}
    //   })
    // }

    babel: {compact: true}

  },

  bootstrapVue: {
    bootstrapCSS: false,
    bootstrapVueCSS: false,

    components: []
  },

  i18n: {
    locales: [
      {
        code: 'en',
        name: 'En',
        domain: 'en.localhost:3000',
        file: 'en.json',
      },
      {
        code: 'ru',
        name: 'Rus',
        domain: 'localhost:3000',
        file: 'ru.json',
      }
    ],

    lazy: true,
    langDir: 'locales/',
    defaultLocale: 'ru',
    vueI18n: {
      fallbackLocale: 'ru',
    },
    differentDomains: true,
    detectBrowserLanguage: false,
  },

  apollo: {
    errorHandler: '~/plugins/apollo-error-handler.js',
    fetchPolicy: 'no-cache',

    clientConfigs: {
      default: '~/plugins/apollo-config.js',
      // default: {
        // httpEndpoint: 'http://localhost/graphql',
        // httpEndpoint: 'http://localhost:8000/graphql',
        // httpEndpoint: 'http://backend_app:8000/graphql',
      // }
    }
  },

  markdown: {
    preset: 'default',
    html: true,
    // linkify: true,
    // breaks: true,
    injected: true,
  },

  static: {},

  server: {
    host: process.env.HOST || '0.0.0.0',
    port: process.env.PORT || '3000',
  }


}
