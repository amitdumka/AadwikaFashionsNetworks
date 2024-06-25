// // vueform.config.(js|ts)

import en from '@vueform/vueform/locales/en'
import vueform from '@vueform/vueform/dist/vueform'
import { defineConfig } from '@vueform/vueform'

// You might place these anywhere else in your project
import '@vueform/vueform/dist/vueform.css'

export default defineConfig({
  theme: vueform,
  locales: { en },
  locale: 'en'
})

// vueform.config.(js|ts)

// import en from '@vueform/vueform/locales/en'
// import tailwind from '@vueform/vueform/dist/tailwind'
// import { defineConfig } from '@vueform/vueform'

// export default defineConfig({
//   theme: tailwind,
//   locales: { en },
//   locale: 'en'
// })
