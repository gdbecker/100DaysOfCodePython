import React from 'react';
import ProjectCard from './components/ProjectCard';

 function Home() {
  return (
    <main className="flex flex-col gap-7 w-full p-10 items-center justify-between bg-lightGray md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 xl:px-52">
      <ProjectCard 
        img_bg="bg-morse-code"
        title="Morse Code Translator"
        demo_url="https://replit.com/@gdbecker/MorseCodeTranslator?embed=true"
        code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%2081"
        type="scripting"
      />

        <ProjectCard 
          img_bg="bg-space-missions"
          title="Space Missions Analysis"
          demo_url="https://www.kaggle.com/embed/garrettbecker/space-missions-analysis?kernelSessionId=132508838"
          code_url=""
          type="dataScience"
        />

        <ProjectCard 
          img_bg="bg-fatal-force"
          title="Fatal Force Analysis"
          demo_url="https://www.kaggle.com/embed/garrettbecker/fatal-force-analysis?kernelSessionId=132688822"
          code_url=""
          type="dataScience"
        />

        <ProjectCard 
          img_bg="bg-determinants-earnings"
          title="Determinants of Earnings Analysis"
          demo_url="https://www.kaggle.com/embed/garrettbecker/determinants-of-earnings-analysis?kernelSessionId=132695898"
          code_url=""
          type="dataScience"
        />

    </main>
  )
}

export default Home;