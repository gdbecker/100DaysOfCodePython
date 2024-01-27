import React from 'react'
import Link from 'next/link'
import { FaGithub } from 'react-icons/fa';
import styles from '../styles/dynamicStyles';

function ProjectCard({ id, img, title, code_url, types, level }) {

  // Get specific Tailwind class based on CSS and project types
  function getCSS(category, type) {
    return styles[category][type];
  }

  function getLabel(type) {
    return (
      <p className={`px-2 h-full ${getCSS('label', type)} w-fit my-1 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden lg:text-[0.75rem]`}>{type.toUpperCase()}</p>
    );
  }

  return (
    <div className={`flex w-full max-h-fit flex-col rounded-md overflow-hidden bg-white ${getCSS('outline', level)} shadow-[0_0px_4px]`} x-intersect="$el.classList.add('fade-in-fwd')">
      <div 
        className={"flex flex-row h-44 bg-project"}
        style={{
          backgroundImage: `url(${ img }.jpg)`
        }}
      >
        <div className="flex flex-row h-fit w-full justify-end">
          <span className={`flex bg-white px-2 py-1 rounded-bl-md border-l-2 border-b-2 ${getCSS('levelClass', level)} text-sm font-sourceSansProBold lg:text-[0.75rem]`}>{getCSS('levelLabel', level)}</span>
        </div>
      </div>
      <div className="flex-auto grid grid-cols-1 px-5 py-3 pb-1 text-gray">
        <div className="flex flex-row items-center justify-between">
          <Link 
            href={{
              pathname: `/${id}`
            }}
            className="py-2 text-xl font-sourceSansProBold relative no-underline lg:text-md"><span className={`${getCSS('shadow', types[0])}`}>{title}</span></Link>
        </div>
        <div className="grid grid-cols-2 items-end justify-between py-3 font-sourceSansProRegular text-md lg:text-sm">
          <Link href={code_url} target="_blank" className={`flex flex-row project-link text-lg ${getCSS('hover', types[0])}`}><FaGithub /> <p className="text-sm pl-2">Learn More</p></Link>
          <div className="flex flex-col items-end justify-end">
            <div className="flex flex-col items-end">
              {types.map((t) => getLabel(t))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProjectCard;