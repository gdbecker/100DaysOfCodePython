import React from 'react';

function Footer() {

  return (
    <div className="h-fit p-5 font-sourceSansProRegular text-center text-black text-sm border-grayishBlue border-t-2 bg-lightGray 2xl:px-36">
      Course from <a href="https://www.udemy.com/course/100-days-of-code/" target="_blank" className="text-blue hover:text-yellow">Udemy</a>. 
      Designed and developed with ❤️ by <a href="https://github.com/gdbecker/100DaysOfCodePython/tree/main" target="_blank" className="text-blue hover:text-yellow">Garrett Becker</a>. &copy; 2023-{new Date().getFullYear()} All rights reserved.
    </div>
  )
}

export default Footer;