/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    colors: { 
      "white": "hsl(0, 0%, 100%)",
      "black": "hsl(209, 26%, 16%)",
      "blue": "hsl(207, 52%, 64%)",
      "blueTransparent": "hsla(207, 52%, 64%, 0.7)",
      "yellow": "hsl(47, 100%, 62%)",
      "yellowTransparent": "hsla(47, 100%, 62%, 0.7)",
      "lightGray": "hsl(0, 0%, 81%)",
      "grayishBlue": "hsl(217, 19%, 35%)",
      "scripting": "hsl(227, 37%, 79%)",
      "scriptingTransparent": "hsla(227, 37%, 79%, 0.7)",
      "webDev": "hsl(30, 90%, 55%)",
      "webDevTransparent": "hsla(30, 90%, 55%, 0.7)",
      "gui": "hsl(350, 83%, 55%)",
      "guiTransparent": "hsla(350, 83%, 55%, 0.7)",
      "game": "hsl(196, 79%, 56%)",
      "gameTransparent": "hsla(196, 79%, 56%, 0.7)",
      "dataScience": "hsl(44, 97%, 49%)",
      "dataScienceTransparent": "hsla(44, 97%, 49%, 0.7)",
      "api": "hsl(79, 66%, 59%)", 
      "apiTransparent": "hsla(79, 66%, 59%, 0.7)",
    },
    extend: {
      fontFamily: {
        sourceSansProRegular: "SourceSansPro-Regular",
        sourceSansProBold: "SourceSansPro-Bold",
      },
    },
  },
  plugins: [],
}
