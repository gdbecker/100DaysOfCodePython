import React from 'react';
import ProjectCard from './components/ProjectCard';

 function Home() {
  return (
    <main className="flex flex-col items-center justify-center w-full h-full p-10 bg-lightGray md:items-start xl:px-52">

      <div className="flex flex-col pb-10 md:flex-row md:justify-between">
        <h1 className="text-sm text-center font-sourceSansProRegular">-- Jump to Section --</h1>
        <a href="#6"><h1 className="px-2 my-2 h-full text-level6 min-w-max ring-level6 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden md:mx-2 md:my-0">06 - PROFESSIONAL</h1></a>
        <a href="#1"><h1 className="px-2 my-2 h-full text-level1 min-w-max ring-level1 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden md:mx-2 md:my-0">01 - BEGINNER</h1></a>
      </div>


      <section id="6" className="pt-4 w-full items-center justify-center">
        <h1 className="px-2 h-full text-level6 max-w-fit ring-level6 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden">06 - PROFESSIONAL</h1>
        <div className="flex flex-col pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
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
            // demo_url="https://taskmanager-gdbecker.up.railway.app"
            demo_url="https://replit.com/@gdbecker/Task-Manager-Web-App-Django?embed=true"
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
      </section>

      <section id="1" className="pt-4 w-full items-center justify-center">
        <h1 className="px-2 h-full text-level1 max-w-fit ring-level1 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden">01 - BEGINNER</h1>
        <div className="flex flex-col pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          <ProjectCard 
            img_bg="bg-001-band-name-generator bg-project"
            title="Band Name Generator"
            demo_url="https://replit.com/@gdbecker/001-Band-Name-Generator?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20001%20-%20Band%20Name%20Generator"
            type="scripting"
          />

          <ProjectCard 
            img_bg="bg-002-band-name-generator bg-project"
            title="Tip Calculator"
            demo_url="https://replit.com/@gdbecker/002-Tip-Calculator?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20002%20-%20Tip%20Calculator"
            type="scripting"
          />

          <ProjectCard 
            img_bg="bg-003-treasure-island-game bg-project"
            title="Treasure Island Game"
            demo_url="https://replit.com/@gdbecker/003-Treasure-Island-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20003%20-%20Treasure%20Island%20Game"
            type="scripting"
          />

          <ProjectCard 
            img_bg="bg-004-rock-paper-scissors bg-project"
            title="Rock - Paper - Scissors"
            demo_url="https://replit.com/@gdbecker/004-Rock-Paper-Scissors?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20004%20-%20Rock%20Paper%20Scissors"
            type="scripting"
          />
        </div>
      </section>

    </main>
  )
}

export default Home;