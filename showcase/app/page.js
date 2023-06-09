import React from 'react';
import ProjectCard from './components/ProjectCard';

 function Home() {
  return (
    <main className="flex flex-col items-center justify-center w-full h-full p-10 bg-lightGray md:items-start xl:px-52">

      <h1 className="px-2 h-full text-mediumYellow min-w-max ring-mediumYellow ring-2 rounded-sm font-interBold text-sm overflow-hidden">POWER BI</h1>

      <div className="flex flex-col w-full pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">    

        <ProjectCard 
          img_bg="bg-morse-code"
          title="Morse Code Translator"
          demo_url="https://replit.com/@gdbecker/MorseCodeTranslator?embed=true"
          code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%2081%20-%20Morse%20Code%20Translator"
          type="scripting"
        />

        <ProjectCard 
          img_bg="bg-task-manager-django"
          title="Task Manager Web App - Django"
          demo_url="https://taskmanager-gdbecker.up.railway.app"
          code_url="https://github.com/gdbecker/TaskManager"
          type="webDev"
        />

        <ProjectCard 
          img_bg="bg-tic-tac-toe"
          title="Tic Tac Toe Game"
          demo_url="https://replit.com/@gdbecker/Tic-Tac-Toe-Game?embed=true"
          code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%2083%20-%20Tic%20Tac%20Toe"
          type="scripting"
        />

        <ProjectCard 
          img_bg="bg-space-missions"
          title="Space Missions Analysis"
          demo_url="https://www.kaggle.com/embed/garrettbecker/space-missions-analysis?kernelSessionId=132508838"
          code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%2098%20-%20Space%20Missions%20Analysis"
          type="dataScience"
        />

        <ProjectCard 
          img_bg="bg-fatal-force"
          title="Fatal Force Analysis"
          demo_url="https://www.kaggle.com/embed/garrettbecker/fatal-force-analysis?kernelSessionId=132688822"
          code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%2099%20-%20Fatal%20Force%20Analysis"
          type="dataScience"
        />

        <ProjectCard 
          img_bg="bg-determinants-earnings"
          title="Determinants of Earnings Analysis"
          demo_url="https://www.kaggle.com/embed/garrettbecker/determinants-of-earnings-analysis?kernelSessionId=132695898"
          code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20100%20-%20Determinants%20of%20Earnings%20Analysis"
          type="dataScience"
        />

      </div>

    </main>
  )
}

export default Home;