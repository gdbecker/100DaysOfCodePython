import React from 'react';
import { IoChevronBack } from 'react-icons/io5';
import { FaGithub } from 'react-icons/fa';

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
    } else if (type == "auto") {
      return "flex flex-row hover:text-auto";
    } else if (type == "debugging") {
      return "flex flex-row hover:text-debugging";
    } else if (type == "webScraping") {
      return "flex flex-row hover:text-webScraping";
    } else if (type == "design") {
      return "flex flex-row hover:text-design";
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
    } else if (type == "auto") {
      return "flex w-full min-h-screen rounded-md shadow-auto shadow-[0_0px_2px]";
    } else if (type == "debugging") {
      return "flex w-full min-h-screen rounded-md shadow-debugging shadow-[0_0px_2px]";
    } else if (type == "webScraping") {
      return "flex w-full min-h-screen rounded-md shadow-webScraping shadow-[0_0px_2px]";
    } else if (type == "design") {
      return "flex w-full min-h-screen rounded-md shadow-design shadow-[0_0px_2px]";
    }
  }

  return (
    <main className="flex flex-col w-full min-h-screen p-10 justify-start bg-lightGray 2xl:px-36">

      <h1 className="pb-6 font-sourceSansProBold text-center text-grayishBlue text-xl">{searchParams.title}</h1>

      <div className="grid grid-cols-2 pb-3 items-end justify-between text-grayishBlue text-lg font-sourceSansProRegular">
        <a href="/" className={getHoverClass(searchParams.type)}><span className="pt-1 pr-2"><IoChevronBack /></span> Back</a>
        <a href={searchParams.code_url} target="_blank" className={`justify-end ${getHoverClass(searchParams.type)}`}><span className="pt-1 pr-2"><FaGithub /></span> Learn More</a>
      </div>

      {searchParams.demo_url != "" ? 
        (<iframe 
          src={searchParams.demo_url}
          height="800" 
          frameborder="0" 
          scrolling="auto" 
          title="Project Demo"
          className={getShadowClass(searchParams.type)}>
        </iframe>) : (<h1 className="font-sourceSansProBold text-center">No live demo available</h1>)
      }

    </main>
  )
}

export default ProjectPage;