import * as assert from "assert";

export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: '-\xa0 - Интернет магазин GOOD – купить клубную молодежную одежду оптом и в розницу, магазин молодежной одежды',
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''}
    ],
    link: [
      {rel: "apple-touch-icon", sizes: "57x57", href: "/static/favicon/apple-icon-57x57.png"},
      {rel: "apple-touch-icon", sizes: "60x60", href: "/static/favicon/apple-icon-60x60.png"},
      {rel: "apple-touch-icon", sizes: "72x72", href: "/static/favicon/apple-icon-72x72.png"},
      {rel: "apple-touch-icon", sizes: "76x76", href: "/static/favicon/apple-icon-76x76.png"},
      {rel: "apple-touch-icon", sizes: "114x114", href: "/static/favicon/apple-icon-114x114.png"},
      {rel: "apple-touch-icon", sizes: "120x120", href: "/static/favicon/apple-icon-120x120.png"},
      {rel: "apple-touch-icon", sizes: "144x144", href: "/static/favicon/apple-icon-144x144.png"},
      {rel: "apple-touch-icon", sizes: "152x152", href: "/static/favicon/apple-icon-152x152.png"},
      {rel: "apple-touch-icon", sizes: "180x180", href: "/static/favicon/apple-icon-180x180.png"},
      {rel: "icon", type: "image/png", sizes: "192x192", href: "/static/favicon/android-icon-192x192.png"},
      {rel: "icon", type: "image/png", sizes: "32x32", href: "/static/favicon/favicon-32x32.png"},
      {rel: "icon", type: "image/png", sizes: "96x96", href: "/static/favicon/favicon-96x96.png"},
      {rel: "icon", type: "image/png", sizes: "16x16", href: "/static/favicon/favicon-16x16.png"},
      {rel: "manifest", href: "/static/favicon/manifest.json"},
      {name: "msapplication-TileColor", content: "#ffffff"},
      {name: "msapplication-TileImage", content: "/static/favicon/ms-icon-144x144.png"},
      {name: "theme-color", content: "#ffffff"},
      {rel:'stylesheet', href:'https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600,700&display=swap&subset=cyrillic-ext'}
    ],
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
    '@fortawesome/fontawesome-svg-core/styles.css',
    '~/assets/scss/style.scss',
    'hooper/dist/hooper.css',
    'vue-inner-image-zoom/lib/vue-inner-image-zoom.css',
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
    {src: '~/plugins/vue-image-lightbox.js', ssr: false},
    // {src: '~/plugins/vue-router-back-button.js', mode: 'client'},
    // {src: '~/plugins/vue-hooper'},
    {src: '~/plugins/vee-validate'},
    {src: '~/plugins/vue-inner-image-zoom'},
    // {src: '~/plugins/vue-media-query-mixin.js', ssr: false},
    {src: '~/plugins/v-video-embed.js', ssr: false}
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
    // '@nuxtjs/axios',
    // '@nuxtjs/auth',

    '~/modules/markdown',

    'portal-vue/nuxt'
  ],


  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    transpile: ["vee-validate/dist/rules"],

    extend(config, {isDev, isClient}) {
      //   config.module.rules.push({
      //     test: /\.html$/i,
      //     loader: 'html-loader',
      //     options:{}
      //   })

      // config.resolve.alias['bootstrap-vue$'] = 'bootstrap-vue/src/index.js'
      // config.module.rules.push({
      //   test: /\.js$/,
      //   // exclude: /node_modules\/(?!bootstrap-vue\/src\/)/,
      //   loader: 'babel-loader',
      //   options: {
      //     presets: ['env']
      //   }
      //
      // })
    },

    babel: {compact: true},

  },

  bootstrapVue: {
    bootstrapCSS: false,
    bootstrapVueCSS: false,
    icons: false,

    componentPlugins: [],
    directivePlugins: [],
    components: [],
    directives: [],

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

    authenticationType: 'JWT',

    clientConfigs: {
      default: '~/plugins/apollo-config.js',
      // default: process.env.APOLLO_CLIENT_HTTP || 'http://localhost:8000/graphql',
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
  },

  publicRuntimeConfig: {
    httpEndpoint: process.env.APOLLO_CLIENT_HTTP || 'http://localhost:8000/graphql',
  },

  router: {
    // middleware: ["auth"],
  },

  // auth: {
  //   redirect: {
  //     login: '/login',
  //     logout: '/',
  //     callback: '/login',
  //   },
  //   strategies: {
  //     google: {
  //       // clientId: "128977390614-6bdbk2511vkb8gnv831mipjqohghagci.apps.googleusercontent.com", # v5
  //       client_id: "128977390614-6bdbk2511vkb8gnv831mipjqohghagci.apps.googleusercontent.com",
  //       // responseType: 'code',
  //       // accessType: 'offline',
  //       responseType: 'token',
  //       grantType: 'authorization_code',
  //       // codeChallengeMethod: 'S256',
  //       // redirect_uri:"http://localhost:3000/",
  //     }
  //   }
  // }


}
