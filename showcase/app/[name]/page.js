'use client'
import React, { useState, useEffect } from 'react';
import LoadingPage from '../loading';
import { usePathname } from 'next/navigation'
import { IoChevronBack } from 'react-icons/io5';
import { FaGithub } from 'react-icons/fa';

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
      let projectData = project.docs.map((doc) => ({ ...doc.data(), id: doc.id }))
      projectData = projectData.filter(function(p) {
        return p.id == pathname.slice(1);
      });
      setProject(projectData[0])
      console.log(projectData)
      setIsLoading(false)
    }).catch((err) => {
      console.log(err);
    })
  }

  // Set up app for viewing
  useEffect(() => {
    getProjects();
  }, [])

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

  function getShadowClass(level) {
    if (level == "1") {
      return "shadow-level1" 
    } else if (level == "2") {
      return "shadow-level2" 
    } else if (level == "3") {
      return "shadow-level3" 
    } else if (level == "4") {
      return "shadow-level4" 
    } else if (level == "5") {
      return "shadow-level5" 
    } else if (level == "6") {
      return "shadow-level6" 
    }

    // if (type == "Scripting") {
    //   return "shadow-scripting";
    // } else if (type == "Web Dev") {
    //   return "shadow-webDev";
    // } else if (type == "GUI") {
    //   return "shadow-gui";
    // } else if (type == "Game") {
    //   return "shadow-game";
    // } else if (type == "Data Science") {
    //   return "shadow-dataScience";
    // } else if (type == "API") {
    //   return "shadow-api";
    // } else if (type == "Automation") {
    //   return "shadow-auto";
    // } else if (type == "Debugging") {
    //   return "shadow-debugging";
    // } else if (type == "Web Scraping") {
    //   return "shadow-webScraping";
    // } else if (type == "Design") {
    //   return "shadow-design";
    // }
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
          <a href="/" className={`flex flex-row ${ getHoverClass(project.type.split(",")[0]) }`}><span className="pt-1 pr-2"><IoChevronBack /></span> Back</a>
          <a href={project.code_url} target="_blank" className={`flex flex-row justify-end ${getHoverClass(project.type.split(",")[0])}`}><span className="pt-1 pr-2"><FaGithub /></span> Learn More</a>
        </div>

        {project.demo_url != "" ? 
          (<iframe 
            src={project.demo_url}
            height="800" 
            frameborder="0" 
            scrolling="auto" 
            title="Project Demo"
            className={`flex w-full min-h-screen rounded-md ${ getShadowClass(project.level) } shadow-[0_0px_2px]`}>
          </iframe>) : (<h1 className="font-sourceSansProBold text-center">No live demo available</h1>)
        }

      </main>
    )
  }
  
}

export default ProjectPage;