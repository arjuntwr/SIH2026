/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        gov: {
          navy: '#0B2545',
          'navy-dark': '#06172B',
          'navy-light': '#133E87',
          ashoka: '#003366',
          green: '#137547',
          'green-dark': '#0D6E44',
          'green-light': '#E8F5E9',
          saffron: '#D97706',
          'saffron-light': '#FEF3C7',
          sand: '#F8F9FA',
          slate: '#334155',
          border: '#E2E8F0',
          accent: '#1D4ED8'
        }
      },
      fontFamily: {
        sans: ['Inter', 'Noto Sans Devanagari', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace']
      },
      boxShadow: {
        'gov-sm': '0 1px 3px 0 rgba(11, 37, 69, 0.08), 0 1px 2px -1px rgba(11, 37, 69, 0.08)',
        'gov-md': '0 4px 6px -1px rgba(11, 37, 69, 0.1), 0 2px 4px -2px rgba(11, 37, 69, 0.08)',
        'gov-lg': '0 10px 15px -3px rgba(11, 37, 69, 0.12), 0 4px 6px -4px rgba(11, 37, 69, 0.08)',
      }
    },
  },
  plugins: [],
}
