import './styles/globals.css'
import Navigation from './components/Navigation'

export const metadata = {
  title: '100 Days of Code: Python Showcase',
  description: 'Project Showcase from 100 Days of Code for Python!',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
      
        <Navigation />
        {children}

        <footer className="text-center font-sourceSansProRegular text-sm">
          Course from <a href="https://www.udemy.com/course/100-days-of-code/" target="_blank" className=" font-sourceSansProRegular hover:text-blue">Udemy</a>. 
          Coded by <a href="https://github.com/gdbecker/100DaysOfCodePython/tree/main" target="_blank" className="font-sourceSansProRegular hover:text-blue">Garrett Becker</a>.
        </footer>
      </body>
    </html>
  )
}
