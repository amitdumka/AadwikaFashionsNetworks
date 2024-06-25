import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default <Partial<Config>>{
  theme: {
    extend: {
      fontFamily: {
        sans: ['DM Sans', ...defaultTheme.fontFamily.sans]
      }
    }
  }
}
// tailwind.config.(js|ts)

// module.exports = {
//   content: [
//     // ... your project files, eg.:
//     // './index.html',
//     // './src/**/*.{vue,js,ts,jsx,tsx}',
//     './vueform.config.ts', // or where `vueform.config.js` is located. Change `.js` to `.ts` if required.
//     './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
//     './node_modules/@vueform/vueform/themes/tailwind/**/*.js'
//   ],
//   darkMode: 'class',
//   theme: {
//     extend: {}
//   },
//   plugins: [require('@vueform/vueform/tailwind')]
// }
