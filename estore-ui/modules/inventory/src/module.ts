import { defineNuxtModule, addPlugin, createResolver, addComponentsDir } from '@nuxt/kit'

// Module options TypeScript interface definition
export interface ModuleOptions {}

export default defineNuxtModule<ModuleOptions>({
  meta: {
    name: 'inventory',
    configKey: 'inventory',
  },
  // Default configuration options of the Nuxt module
  defaults: {},
  setup(_options, _nuxt) {
    const resolver = createResolver(import.meta.url)

    addComponentsDir({
      path: resolver.resolve('./runtime/components/invoices'),
      prefix: 'AINV-',
      isAsync: true,
      global: true,
      watch: true,
    })

    // Do not add the extension since the `.ts` will be transpiled to `.mjs` after `npm run prepack`
    addPlugin(resolver.resolve('./runtime/plugin'))
    _nuxt.hook('pages:extend', (pages) => {
      console.log(`Discovered ${pages.length} pages`)
    })
  },
})
