import React from 'react';
import ProjectCard from './components/ProjectCard';

 function Home() {
  return (
    <main className="flex flex-col gap-7 w-full p-10 items-center justify-between bg-grayishBlue md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      <ProjectCard 
        img_bg="bg-3-column-card"
        title="3-Column Preview Card Component"
        demo_url="https://3-column-card-gdbecker.netlify.app"
        code_url="https://www.frontendmentor.io/solutions/3column-card-with-nextjs-sass-voBV4ThwSG"
      />

    </main>
  )
}

export default Home;