import React from 'react'
import { FaGithub } from 'react-icons/fa';

function ProjectCard({ img_bg, title, demo_url, code_url }) {

  return (
    <div className="flex w-full h-full flex-col rounded-sm overflow-hidden shadow-lightGray shadow-[0_0px_5px]">
      <div className={`flex flex-row h-52 ${ img_bg }`}></div>
      <div className="px-6 py-3 text-white">
        <div className="flex flex-row items-center justify-between">
          <a href={code_url} target="_blank" className="py-2 text-xl font-sourceSansProBold hover:underline lg:text-md">{title}</a>
        </div>
        <div className="flex flex-row items-center justify-left py-3 font-sourceSansProRegular text-md lg:text-sm">
          <a href={demo_url} target="_blank" className="project-link italic mr-3 md:text-md"><span className="link-shadow">Live Demo</span></a>
          <a href={code_url} target="_blank" className="project-link italic mr-3 hover:text-yellow"><FaGithub /></a>
        </div>
      </div>
    </div>
  )
}

export default ProjectCard;