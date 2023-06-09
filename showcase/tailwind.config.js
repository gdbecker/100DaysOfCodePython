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
      "blue": "hsl(207, 52%, 64%)",
      "blueTransparent": "hsla(207, 52%, 64%, 0.7)",
      "yellow": "hsl(47, 100%, 62%)",
      "yellowTransparent": "hsla(47, 100%, 62%, 0.7)",
      "lightGray": "hsl(0, 0%, 81%)",
      "grayishBlue": "hsl(217, 19%, 35%)",
      "scripting": "#b5bedd",
      "webDev": "#f48c24",
      "gui": "#ec2c4c",
      "game": "#37bae8",
      "dataScience": "#f4b404",
      "api": "#b1dc52", 
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
