// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  extends: ['./modules/ui-pro'],
  modules: [
    './modules/inventory/src/module',
    '@nuxt/eslint',
    '@nuxt/ui',
    '@nuxt/fonts',
    '@logto/nuxt',
    '@vueform/nuxt',
    '@vueuse/nuxt',
    'nuxt-pdfeasy'
  ],
  ui: {
    icons: ['heroicons', 'simple-icons'],
    safelistColors: ['primary', 'red', 'orange', 'green']
  },
  colorMode: {
    disableTransition: true
  },
  devtools: {
    enabled: true
  },
  typescript: {
    strict: false
  },
  future: {
    compatibilityVersion: 4
  },
  eslint: {
    config: {
      stylistic: {
        commaDangle: 'never',
        braceStyle: '1tbs'
      }
    }
  },
  runtimeConfig: {
    logto: {
      endpoint: 'https://fieioi.logto.app/',
      appId: 'wgoenbdw50jy73qdl5zin',
      appSecret: 'IPi29V8EzJx1D9fp5ooKoA5Bo6I2d8qE',
      cookieEncryptionKey: 'n4TmbfenxMgOvWKA3NpO9BjrICSAJrkD' // Random-generated
    }
  },
  logto: {
    postCallbackRedirectUri: '/',
    postLogoutRedirectUri: '/',
    fetchUserInfo: true,
    pathnames: {
      signIn: '/login',
      signOut: '/logout',
      callback: '/auth/callback'
    }
  }
})
