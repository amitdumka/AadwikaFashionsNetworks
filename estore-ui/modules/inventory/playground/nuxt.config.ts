export default defineNuxtConfig({
  modules: ['../src/module','@nuxt/eslint',
    '@nuxt/ui',
    '@nuxt/fonts',
    '@vueuse/nuxt'],
  inventory: {},
  devtools: { enabled: true },
})
