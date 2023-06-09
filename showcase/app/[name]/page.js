import React from 'react';
import { IoChevronBack } from 'react-icons/io5';

 function ProjectPage({ searchParams }) { 

  function getHoverClass(type) {
    if (type == "scripting") {
      return "flex flex-row hover:text-scripting";
    } else if (type == "webDev") {
      return "flex flex-row hover:text-webDev";
    } else if (type == "gui") {
      return "flex flex-row hover:text-gui";
    } else if (type == "game") {
      return "flex flex-row hover:text-game";
    } else if (type == "dataScience") {
      return "flex flex-row hover:text-dataScience";
    } else if (type == "api") {
      return "flex flex-row hover:text-api";
    }
  }

  function getShadowClass(type) {
    if (type == "scripting") {
      return "flex w-full min-h-screen rounded-md shadow-scripting shadow-[0_0px_2px]";
    } else if (type == "webDev") {
      return "flex w-full min-h-screen rounded-md shadow-webDev shadow-[0_0px_2px]";
    } else if (type == "gui") {
      return "flex w-full min-h-screen rounded-md shadow-gui shadow-[0_0px_2px]";
    } else if (type == "game") {
      return "flex w-full min-h-screen rounded-md shadow-game shadow-[0_0px_2px]";
    } else if (type == "dataScience") {
      return "flex w-full min-h-screen rounded-md shadow-dataScience shadow-[0_0px_2px]";
    } else if (type == "api") {
      return "flex w-full min-h-screen rounded-md shadow-api shadow-[0_0px_2px]";
    }
  }

  return (
    <main className="flex flex-col w-full min-h-screen p-10 justify-center bg-lightGray xl:px-52">
      <div className="grid grid-cols-2 pb-3 items-end justify-between text-grayishBlue text-lg font-sourceSansProRegular">
        <a href="/" className={getHoverClass(searchParams.type)}><span className="pt-1 pr-2"><IoChevronBack /></span> Back</a>
        <h1 className="font-sourceSansProBold text-right">{searchParams.title}</h1>
      </div>
      <iframe 
        src={searchParams.demo_url}
        height="800" 
        frameborder="0" 
        scrolling="auto" 
        title="Project Demo"
        className={getShadowClass(searchParams.type)}>
      </iframe>
    </main>
  )
}

export default ProjectPage;