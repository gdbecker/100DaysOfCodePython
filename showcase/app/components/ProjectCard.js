import React from 'react'
import Link from 'next/link'
import { FaGithub } from 'react-icons/fa';

function ProjectCard({ img_bg, title, demo_url, code_url, type }) {

  function getOutlineClass(type) {
    if (type == "scripting") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-scripting shadow-[0_0px_4px]";
    } else if (type == "webDev") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-webDev shadow-[0_0px_4px]";
    } else if (type == "gui") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-gui shadow-[0_0px_4px]";
    } else if (type == "game") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-game shadow-[0_0px_4px]";
    } else if (type == "dataScience") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-dataScience shadow-[0_0px_4px]";
    } else if (type == "api") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-api shadow-[0_0px_4px]";
    } else if (type == "auto") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-auto shadow-[0_0px_4px]";
    } else if (type == "debugging") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-debugging shadow-[0_0px_4px]";
    } else if (type == "webScraping") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-webScraping shadow-[0_0px_4px]";
    } else if (type == "design") {
      return "flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white shadow-design shadow-[0_0px_4px]";
    }
  }

  function getLabel(type) {
    if (type == "scripting") {
      return (
        <p className="px-2 h-full text-scripting w-fit my-1 ring-scripting ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">SCRIPTING</p>
      );
    } else if (type == "webDev") {
      return (
        <p className="px-2 h-full text-webDev w-fit my-1 ring-webDev ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">WEB DEV</p>
      );
    } else if (type == "gui") {
      return (
        <p className="px-2 h-full text-gui w-fit my-1 ring-gui ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">GUI</p>
      );
    } else if (type == "game") {
      return (
        <p className="px-2 h-full text-game w-fit my-1 ring-game ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">GAME</p>
      );
    } else if (type == "dataScience") {
      return (
        <p className="px-2 h-full text-dataScience w-fit my-1 ring-dataScience ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">DATA SCIENCE</p>
      );
    } else if (type == "api") {
      return (
        <p className="px-2 h-full text-api w-fit my-1 ring-api ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">API</p>
      );
    } else if (type == "auto") {
      return (
        <p className="px-2 h-full text-auto w-fit my-1 ring-auto ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">AUTOMATION</p>
      );
    } else if (type == "debugging") {
      return (
        <p className="px-2 h-full text-debugging w-fit my-1 ring-debugging ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">DEBUGGING</p>
      );
    } else if (type == "webScraping") {
      return (
        <p className="px-2 h-full text-webScraping w-fit my-1 ring-webScraping ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">WEB SCRAPING</p>
      );
    } else if (type == "design") {
      return (
        <p className="px-2 h-full text-design w-fit my-1 ring-design ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">DESIGN</p>
      );
    }
  }

  function getShadowClass(type) {
    if (type == "scripting") {
      return "link-shadow-scripting";
    } else if (type == "webDev") {
      return "link-shadow-webDev";
    } else if (type == "gui") {
      return "link-shadow-gui";
    } else if (type == "game") {
      return "link-shadow-game";
    } else if (type == "dataScience") {
      return "link-shadow-dataScience";
    } else if (type == "api") {
      return "link-shadow-api";
    } else if (type == "auto") {
      return "link-shadow-auto";
    } else if (type == "debugging") {
      return "link-shadow-debugging";
    } else if (type == "webScraping") {
      return "link-shadow-webScraping";
    } else if (type == "design") {
      return "link-shadow-design";
    }
  }

  function getHoverClass(type) {
    if (type == "scripting") {
      return "flex flex-row project-link text-lg hover:text-scripting";
    } else if (type == "webDev") {
      return "flex flex-row project-link text-lg hover:text-webDev";
    } else if (type == "gui") {
      return "flex flex-row project-link text-lg hover:text-gui";
    } else if (type == "game") {
      return "flex flex-row project-link text-lg hover:text-game";
    } else if (type == "dataScience") {
      return "flex flex-row project-link text-lg hover:text-dataScience";
    } else if (type == "api") {
      return "flex flex-row project-link text-lg hover:text-api";
    } else if (type == "auto") {
      return "flex flex-row project-link text-lg hover:text-auto";
    } else if (type == "debugging") {
      return "flex flex-row project-link text-lg hover:text-debugging";
    } else if (type == "webScraping") {
      return "flex flex-row project-link text-lg hover:text-webScraping";
    } else if (type == "design") {
      return "flex flex-row project-link text-lg hover:text-design";
    }
  }

  function getLinkHref(demo_url) {
    if (demo_url.includes('railway')) {
      return demo_url;
    } else {
      return (
        {
          pathname: `/${title}` ,
          query: {
            demo_url: `${demo_url}`,
            title: `${title}`,
            code_url: `${code_url}`,
            type: `${type[0]}`,
          }
        }
      );
    }
  }

  return (
    <div className={getOutlineClass(type[0])}>
      <div className={`flex flex-row h-44 ${ img_bg }`}></div>
      <div className="px-5 py-3 pb-1 text-gray">
        <div className="flex flex-row items-center justify-between">
          <Link 
            href={getLinkHref(demo_url)}
            className="py-2 text-xl font-sourceSansProBold relative no-underline lg:text-md"><span className={getShadowClass(type[0])}>{title}</span></Link>
        </div>
        <div className="grid grid-cols-2 items-center justify-between py-3 font-sourceSansProRegular text-md lg:text-sm">
          <Link href={code_url} target="_blank" className={getHoverClass(type[0])}><FaGithub /> <p className="text-sm pl-2">Learn More</p></Link>
          <div className="flex flex-col items-end justify-end">
            <div className="flex flex-col items-end">
              {type.map((t) => getLabel(t))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProjectCard;