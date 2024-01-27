'use client'
import React, { useState, useEffect } from 'react';
import LoadingPage from './loading';
import ProjectCard from './components/ProjectCard';
import { BiSearch } from 'react-icons/bi'
import { BiChevronDown } from 'react-icons/bi'
import { collection, getDocs, doc } from 'firebase/firestore';
import { db } from './services/firebase.config';

 function Home() {

  // Firebase db variables
  const collectionRef = collection(db, "projects");
  const [projects, setProjects] = useState([]);
  const [filteredProjects, setFilteredProjects] = useState([]);

  // State variables
  const [isLoading, setIsLoading] = useState(true);
  const [projectSearch, setProjectSearch] = useState('');
  const [typeSelect, setTypeSelect] = useState('Filter by Type');
  const [types, setTypes] = useState([]);
  const [levelSelect, setLevelSelect] = useState('Filter by Level');
  const [levels, setLevels] = useState([]);

  // Update project to search
  const onChangeProjectSearch = (e) => {
    setProjectSearch(e.currentTarget.value);

    filterProjects(e.currentTarget.value, typeSelect, levelSelect);
  }

  // Update type to filter
  const handleTypeChange = (e) => {
    setTypeSelect(e.target.name);

    filterProjects(projectSearch, e.target.name, levelSelect);
  };

  // Update difficulty level to filter
  const handleLevelChange = (e) => {
    setLevelSelect(e.target.name);

    filterProjects(projectSearch, typeSelect, e.target.name);
  };

  // Filter by project name search, type, and level
  const filterProjects = (projectName, type, level) => {
    if (projectName != "" && type != "Filter by Type" && level != "Filter by Level") {
      let f =  projects.filter(function(p) {
        return p.types.includes(type) && p.level == level && p.title.toLowerCase().includes(projectName.toLowerCase());
      });

      setFilteredProjects(f);
    } else if (type != "Filter by Type" && level != "Filter by Level") {
      let f =  projects.filter(function(p) {
        return p.types.includes(type) && p.level == level;
      });

      setFilteredProjects(f);
    } else if (type != "Filter by Type" && projectName != "") {
      let f =  projects.filter(function(p) {
        return p.types.includes(type) && p.title.toLowerCase().includes(projectName.toLowerCase());
      });

      setFilteredProjects(f);
    } else if (level != "Filter by Level" && projectName != "") {
      let f =  projects.filter(function(p) {
        return p.level == level && p.title.toLowerCase().includes(projectName.toLowerCase());
      });

      setFilteredProjects(f);
    } else if (type != "Filter by Type") {
      let f =  projects.filter(function(p) {
        return p.types.includes(type);
      });

      setFilteredProjects(f);
    } else if (level != "Filter by Level") {
      let f =  projects.filter(function(p) {
        return p.level == level;
      });

      setFilteredProjects(f);
    } else if (projectName != "") {
      let f =  projects.filter(function(p) {
        return p.title.toLowerCase().includes(projectName.toLowerCase());
      });

      setFilteredProjects(f);
    } else {
      setFilteredProjects(projects);
    }
  }

  // Get project types list
  const grabTypes = (projects) => {
    let allTypes = projects.map(p => p.types);
    let allTypesMerge = allTypes.flat(1);
    let typeList = [...new Set(allTypesMerge)].sort();

    typeList = typeList.map(p => {
      return({type: p});
    });

    typeList.unshift({type: "Filter by Type"})
    setTypes(typeList);
  }

  // Get difficulty levels list
  const grabLevels = (projects) => {
    let allLevels = projects.map(p => p.level);
    let levelsList = [...new Set(allLevels)].sort();

    levelsList = levelsList.map(p => {
      return({level: p});
    });

    levelsList.unshift({level: "Filter by Level"})
    setLevels(levelsList);
  }

  // Get all projects
  const getProjects = async () => {
    await getDocs(collectionRef).then((project) => {
      let projectData = project.docs.map((doc) => ({ ...doc.data(), id: doc.id }));
      projectData = projectData.filter((project) => project.active);
      projectData.sort(function (first, second) {
        return second.level - first.level || first.title.localeCompare(second.title)
      })
      setProjects(projectData);
      setFilteredProjects(projectData);
      grabTypes(projectData);
      grabLevels(projectData);
      setIsLoading(false);
    }).catch((err) => {
      console.log(err);
    })
  }

  // Set up app for viewing
  useEffect(() => {
    getProjects();
  }, [])

  if (isLoading) {
    return (
      <LoadingPage />
    )
  }

  if (!isLoading) {
    return (
      <main className="flex flex-col items-center justify-center w-full h-full p-10 bg-lightGray 2xl:px-36">

        <h1 className="pb-9 text-justify text-grayishBlue leading-7 md:w-[50vw]">
          This is a collection of projects I made through the <a href="https://www.udemy.com/course/100-days-of-code/" target="_blank" className="hover:text-yellow">100 Days of Code: Python course from Angela Yu</a>. 
          Almost 100 projects are housed here that cover a variety of topics such as console-based scripting, games and other 
          GUI applications, data science analysis, automation, API connectivity and web application development. I had a lot of fun 
          solidifying my Python skills with all of these projects, and learned so much by diving into this 100 day coding challenge. 
          Take a look and explore each of my projects' Github pages and live demos!
        </h1>

        <div className="flex flex-col w-full py-5 justify-between md:flex-row md:min-h-fit">
          <div className="flex flex-row w-full items-center justify-between pl-5 shadow-md rounded-md bg-white md:w-[40%]">
            <h1 className="font-interRegular text-gray"><BiSearch /></h1>
            <input 
              className="flex w-full p-4 bg-white text-gray text-xs font-interRegular rounded-md focus:outline-none"
              placeholder="Search for a project!"
              id="projectSearch" 
              type="text" 
              value={projectSearch}
              onChange={e => onChangeProjectSearch(e)}
            />
          </div>
          <details className="flex dropdown w-[100%] my-2 md:my-0 md:w-[28%] lg:w-[20%] xl:w-[15%]">
            <summary className="flex flex-row items-center justify-between h-full mb-[2px] btn w-full rounded-md border-0 shadow-md no-animation bg-white text-veryDarkBlue-Light hover:bg-white">
              <h1 
                className="flex normal-case text-xs font-interRegular"
              >{levelSelect}</h1>
              <BiChevronDown className="text-sm"/>
            </summary>
            <ul className="flex px-2 py-4 shadow menu dropdown-content z-[1] rounded-md w-full bg-white text-gray">
              {levels.map((l) => (
                <li
                  onClick={(e) => handleLevelChange(e)}
                  className="text-xs font-interRegular"
                >
                  <a 
                    className="px-4 py-1 rounded-none hover:bg-white"
                    name={l.level}
                  >
                    {l.level}
                  </a>
                </li>
              ))}
            </ul>
          </details>
          <details className="flex dropdown w-[100%] my-0 md:my-0 md:w-[28%] lg:w-[20%] xl:w-[15%]">
            <summary className="flex flex-row items-center justify-between h-full mb-[2px] btn w-full rounded-md border-0 shadow-md no-animation bg-white text-veryDarkBlue-Light hover:bg-white">
              <h1 
                className="flex normal-case text-xs font-interRegular"
              >{typeSelect}</h1>
              <BiChevronDown className="text-sm"/>
            </summary>
            <ul className="flex px-2 py-4 shadow menu dropdown-content z-[1] rounded-md w-full bg-white text-gray">
              {types.map((t) => (
                <li
                  onClick={(e) => handleTypeChange(e)}
                  className="text-xs font-interRegular"
                >
                  <a 
                    className="px-4 py-1 rounded-none hover:bg-white"
                    name={t.type}
                  >
                    {t.type}
                  </a>
                </li>
              ))}
            </ul>
          </details>
        </div>


        <section className="pt-4 w-full items-center justify-center">
          <div className="flex flex-col pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">

            {filteredProjects.map(({ id, img, title, code_url, types, level }, index) =>
              <ProjectCard 
                key={index}
                index={index}
                id={id}
                img={img}
                title={title}
                code_url={code_url}
                types={types}
                level={level}
              />
            )}
          </div>
        </section>
      </main>
    )
  }
  
}

export default Home;