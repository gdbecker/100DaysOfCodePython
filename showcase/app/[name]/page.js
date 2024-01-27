'use client'
import React, { useState, useEffect } from 'react';
import LoadingPage from '../loading';
import { usePathname } from 'next/navigation'
import { IoChevronBack } from 'react-icons/io5';
import { FaGithub } from 'react-icons/fa';
import styles from '../styles/dynamicStyles';

import { collection, getDocs } from 'firebase/firestore';
import { db } from './../services/firebase.config';

 function ProjectPage() { 

  // Firebase db variables
  const collectionRef = collection(db, "projects");
  const [project, setProject] = useState([]);

  // State variables
  const [isLoading, setIsLoading] = useState(true);
  const pathname = usePathname()

  // Get specific project
  const getProjects = async () => {
    await getDocs(collectionRef).then((project) => {
      let projectData = project.docs.map((doc) => ({ ...doc.data(), id: doc.id }));
      projectData = projectData.filter(function(p) {
        return p.id == pathname.slice(1);
      });
      setProject(projectData[0]);
      console.log(projectData);
      setIsLoading(false)
    }).catch((err) => {
      console.log(err);
    })
  }

  // Set up app for viewing
  useEffect(() => {
    getProjects();
  }, [])

  // Get specific Tailwind class based on CSS and project types
  function getCSS(category, type) {
    return styles[category][type];
  }

  if (isLoading) {
    return (
      <LoadingPage />
    )
  }

  if (!isLoading) {
    return (
      <main className="flex flex-col w-full min-h-screen p-10 justify-start bg-lightGray 2xl:px-36">

        <h1 className="pb-6 font-sourceSansProBold text-center text-grayishBlue text-xl">{project.title}</h1>

        <div className="grid grid-cols-2 pb-3 items-end justify-between text-grayishBlue text-lg font-sourceSansProRegular">
          <a href="/" className={`flex flex-row ${getCSS('hover', project.types[0])}`}><span className="pt-1 pr-2"><IoChevronBack /></span> Back</a>
          <a href={project.code_url} target="_blank" className={`flex flex-row justify-end ${getCSS('hover', project.types[0])}`}><span className="pt-1 pr-2"><FaGithub /></span> Learn More</a>
        </div>

        {project.demo_url != "" ? 
          (<iframe 
            src={project.demo_url}
            height="800" 
            frameborder="0" 
            scrolling="auto" 
            title="Project Demo"
            className={`flex w-full min-h-screen rounded-md ${getCSS('outline', project.level)} shadow-[0_0px_2px]`}>
          </iframe>) : (<h1 className="font-sourceSansProBold text-center">No live demo available</h1>)
        }

      </main>
    )
  }
  
}

export default ProjectPage;