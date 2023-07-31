import React from 'react'
import Link from 'next/link'
import { FaGithub } from 'react-icons/fa';

function ProjectCard({ id, img_bg, title, demo_url, code_url, type, level }) {

  function getOutlineClass(type) {
    if (type == "Scripting") {
      return "shadow-scripting";
    } else if (type == "Web Development") {
      return "shadow-webDev";
    } else if (type == "GUI") {
      return "shadow-gui";
    } else if (type == "Game") {
      return "shadow-game";
    } else if (type == "Data Science") {
      return "shadow-dataScience";
    } else if (type == "API") {
      return "shadow-api";
    } else if (type == "Automation") {
      return "shadow-auto";
    } else if (type == "Debugging") {
      return "shadow-debugging";
    } else if (type == "Web Scraping") {
      return "shadow-webScraping";
    } else if (type == "Design") {
      return "shadow-design";
    }
  }

  function getLabel(type) {
    if (type == "Scripting") {
      return (
        <p className="px-2 h-full text-scripting w-fit my-1 ring-scripting ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">SCRIPTING</p>
      );
    } else if (type == "Web Development") {
      return (
        <p className="px-2 h-full text-webDev w-fit my-1 ring-webDev ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">WEB DEV</p>
      );
    } else if (type == "GUI") {
      return (
        <p className="px-2 h-full text-gui w-fit my-1 ring-gui ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">GUI</p>
      );
    } else if (type == "Game") {
      return (
        <p className="px-2 h-full text-game w-fit my-1 ring-game ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">GAME</p>
      );
    } else if (type == "Data Science") {
      return (
        <p className="px-2 h-full text-dataScience w-fit my-1 ring-dataScience ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">DATA SCIENCE</p>
      );
    } else if (type == "API") {
      return (
        <p className="px-2 h-full text-api w-fit my-1 ring-api ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">API</p>
      );
    } else if (type == "Automation") {
      return (
        <p className="px-2 h-full text-auto w-fit my-1 ring-auto ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">AUTOMATION</p>
      );
    } else if (type == "Debugging") {
      return (
        <p className="px-2 h-full text-debugging w-fit my-1 ring-debugging ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">DEBUGGING</p>
      );
    } else if (type == "Web Scraping") {
      return (
        <p className="px-2 h-full text-webScraping w-fit my-1 ring-webScraping ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">WEB SCRAPING</p>
      );
    } else if (type == "Design") {
      return (
        <p className="px-2 h-full text-design w-fit my-1 ring-design ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]">DESIGN</p>
      );
    }
  }

  function getShadowClass(type) {
    if (type == "Scripting") {
      return "link-shadow-scripting";
    } else if (type == "Web Development") {
      return "link-shadow-webDev";
    } else if (type == "GUI") {
      return "link-shadow-gui";
    } else if (type == "Game") {
      return "link-shadow-game";
    } else if (type == "Data Science") {
      return "link-shadow-dataScience";
    } else if (type == "API") {
      return "link-shadow-api";
    } else if (type == "Automation") {
      return "link-shadow-auto";
    } else if (type == "Debugging") {
      return "link-shadow-debugging";
    } else if (type == "Web Scraping") {
      return "link-shadow-webScraping";
    } else if (type == "Design") {
      return "link-shadow-design";
    }
  }

  function getHoverClass(type) {
    if (type == "Scripting") {
      return "hover:text-scripting";
    } else if (type == "Web Development") {
      return "hover:text-webDev";
    } else if (type == "GUI") {
      return "hover:text-gui";
    } else if (type == "Game") {
      return "hover:text-game";
    } else if (type == "Data Science") {
      return "hover:text-dataScience";
    } else if (type == "API") {
      return "hover:text-api";
    } else if (type == "Automation") {
      return "hover:text-auto";
    } else if (type == "Debugging") {
      return "hover:text-debugging";
    } else if (type == "Web Scraping") {
      return "hover:text-webScraping";
    } else if (type == "Design") {
      return "hover:text-design";
    }
  }

  function getLinkHref(demo_url) {
    if (demo_url.includes('railway')) {
      return demo_url;
    } else {
      return (
        {
          pathname: `/${id}` ,
          // query: {
          //   demo_url: `${demo_url}`,
          //   title: `${title}`,
          //   code_url: `${code_url}`,
          //   type: `${type[0]}`,
          // }
        }
      );
    }
  }

  function getLevelClass(level) {
    if (level == "1") {
      return "border-l-level1 border-b-level1 text-level1";
    } else if(level == "2") {
      return "border-l-level2 border-b-level2 text-level2";
    } else if(level == "3") {
      return "border-l-level3 border-b-level3 text-level3";
    } else if(level == "4") {
      return "border-l-level4 border-b-level4 text-level4";
    } else if(level == "5") {
      return "border-l-level5 border-b-level5 text-level5";
    } else if(level == "6") {
      return "border-l-level6 border-b-level6 text-level6";
    }
  }

  function getLevelLabel(level) {
    if (level == "1") {
      return "01 - BEGINNER";
    } else if(level == "2") {
      return "02 - INTERMEDIATE";
    } else if(level == "3") {
      return "03 - INTERMEDIATE +";
    } else if(level == "4") {
      return "04 - WEB FOUNDATION";
    } else if(level == "5") {
      return "05 - ADVANCED";
    } else if(level == "6") {
      return "06 - PROFESSIONAL";
    }
  }

  return (
    <div className={`flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white ${ getOutlineClass(type.split(",")[0]) } shadow-[0_0px_4px]`}>
      <div className={`flex flex-row h-44 ${ img_bg }`}>
        <div className="flex flex-row h-fit w-full justify-end">
          <span className={`flex bg-white px-2 py-1 rounded-bl-md border-l-2 border-b-2 ${ getLevelClass(level) } text-sm font-sourceSansProBold lg:text-[0.75rem]`}>{getLevelLabel(level)}</span>
        </div>
      </div>
      <div className="px-5 py-3 pb-1 text-gray">
        <div className="flex flex-row items-center justify-between">
          <Link 
            href={getLinkHref(demo_url)}
            className="py-2 text-xl font-sourceSansProBold relative no-underline lg:text-md"><span className={getShadowClass(type.split(",")[0])}>{title}</span></Link>
        </div>
        <div className="grid grid-cols-2 items-center justify-between py-3 font-sourceSansProRegular text-md lg:text-sm">
          <Link href={code_url} target="_blank" className={`flex flex-row project-link text-lg ${ getHoverClass(type.split(",")[0]) }`}><FaGithub /> <p className="text-sm pl-2">Learn More</p></Link>
          <div className="flex flex-col items-end justify-end">
            <div className="flex flex-col items-end">
              {type.split(",").map((t) => getLabel(t))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProjectCard;