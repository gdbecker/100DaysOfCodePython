import './styles/globals.css'
import Navigation from './components/Navigation'
import Footer from './components/Footer'

export const metadata = {
  title: '100 Days of Code: Python Showcase',
  description: 'Project Showcase from 100 Days of Code for Python!',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body x-data>
        {/* Alpine Plugins */}
        <script defer src="https://cdn.jsdelivr.net/npm/@alpinejs/intersect@3.x.x/dist/cdn.min.js"></script>
        
        {/* Alpine Core */}
        <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
      
        <Navigation />
        {children}
        <Footer />

      </body>
    </html>
  )
}
