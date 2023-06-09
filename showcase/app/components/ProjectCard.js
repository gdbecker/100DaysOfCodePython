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
            type: `${type}`,
          }
        }
      );
    }
  }

  return (
    <div className={getOutlineClass(type)}>
      <div className={`flex flex-row h-44 ${ img_bg }`}></div>
      <div className="px-5 py-3 pb-1 text-gray">
        <div className="flex flex-row items-center justify-between">
          <Link 
            href={getLinkHref(demo_url)}
            target="_blank"
            className="py-2 text-xl font-sourceSansProBold relative no-underline lg:text-md"><span className={getShadowClass(type)}>{title}</span></Link>
        </div>
        <div className="grid grid-cols-2 items-center justify-between py-3 font-sourceSansProRegular text-md lg:text-sm">
          <Link href={code_url} target="_blank" className={getHoverClass(type)}><FaGithub /> <p className="text-sm pl-2">Learn More</p></Link>
          <div className="flex flex-col items-end justify-end">
            {getLabel(type)}
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProjectCard;