import React from 'react';
import Image from 'next/image';
import Logo from '../../public/python.svg';
import Avatar from '../../public/gdbecker.jpeg';

function Navigation() {

  return (
    <div class="flex h-16 p-10 items-center justify-between overflow-hidden border-lightGray border-b-2 bg-grayishBlue">
      <div className="flex items-center justify-between">
        <a class="flex items-center justify-center" href="" target="_blank">
          <h1 className="font-sourceSansProBold tracking-wide text-sm text-yellow md:text-lg">100 Days of Code:</h1>
          <Image 
            src={Logo}
            alt="Frontend Mentor Logo"
            className="pr-2 mx-2 w-10 h-10 border-lightGray border-r-2 md:w-12 md:h-12 md:mx-none"
          />
        </a>
        <h1 className="font-sourceSansProRegular tracking-wider text-sm text-blue md:text-lg">Showcase</h1>
      </div>
      <a class="flex items-center justify-center" href="https://github.com/gdbecker/100DaysOfCodePython/tree/main" target="_blank">
        <Image 
          src={Avatar}
          alt="Profile Photo"
          width={75}
          height={75}
          className="w-10 h-10 rounded-full md:w-12 md:h-12"
        />
      </a>
    </div>
  )
}

export default Navigation;