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
      "black": "#1e2933",
      "blue": "#75a8d3",
      "yellow": "hsl(47, 100%, 62%)",
      "yellowTransparent": "hsla(47, 100%, 62%, 0.5)",
      "lightGray": "hsl(0, 0%, 81%)",
      "grayishBlue": "hsl(217, 19%, 35%)",
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
