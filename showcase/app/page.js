import React from 'react';
import ProjectCard from './components/ProjectCard';

 function Home() {
  return (
    <main className="flex flex-col items-center justify-center w-full h-full p-10 bg-lightGray md:items-start 2xl:px-52">

      <div className="flex flex-col pb-10 sm:flex-row sm:flex-wrap sm:items-center">
        <h1 className="text-sm text-center font-sourceSansProRegular">Jump to Section</h1>
        <a href="#1"><h1 className="px-2 my-2 h-fit text-level1 min-w-max ring-level1 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden sm:mx-2">01 - BEGINNER</h1></a>
        <a href="#2"><h1 className="px-2 my-2 h-fit text-level2 min-w-max ring-level2 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden sm:mx-2">02 - INTERMEDIATE</h1></a>
        <a href="#3"><h1 className="px-2 my-2 h-fit text-level3 min-w-max ring-level3 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden sm:mx-2">03 - INTERMEDIATE +</h1></a>
        <a href="#4"><h1 className="px-2 my-2 h-fit text-level4 min-w-max ring-level4 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden sm:mx-2">04 - WEB FOUNDATION</h1></a>
        <a href="#5"><h1 className="px-2 my-2 h-fit text-level5 min-w-max ring-level5 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden sm:mx-2">05 - ADVANCED</h1></a>
        <a href="#6"><h1 className="px-2 my-2 h-fit text-level6 min-w-max ring-level6 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden sm:mx-2">06 - PROFESSIONAL</h1></a>
      </div>


      <section id="6" className="pt-4 w-full items-center justify-center">
        <h1 className="px-2 h-full text-level6 max-w-fit ring-level6 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden">06 - PROFESSIONAL</h1>
        <div className="flex flex-col pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          <ProjectCard 
            img_bg="bg-081-morse-code-translator bg-project"
            title="Morse Code Translator"
            demo_url="https://replit.com/@gdbecker/MorseCodeTranslator?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20081%20-%20Morse%20Code%20Translator"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-082-task-manager-django bg-project"
            title="Task Manager Web App - Django"
            // demo_url="https://taskmanager-gdbecker.up.railway.app"
            demo_url="https://replit.com/@gdbecker/Task-Manager-Web-App-Django?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20082%20-%20Task%20Manager%20App%20(Django)"
            type={["webDev", "api"]}
          />

          <ProjectCard 
            img_bg="bg-083-tic-tac-toe-game bg-project"
            title="Tic Tac Toe Game"
            demo_url="https://replit.com/@gdbecker/Tic-Tac-Toe-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20083%20-%20Tic%20Tac%20Toe"
            type={["scripting"]}
          />



          <ProjectCard 
            img_bg="bg-098-space-missions-analysis bg-project"
            title="Space Missions Analysis"
            demo_url="https://www.kaggle.com/embed/garrettbecker/space-missions-analysis?kernelSessionId=132508838"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20098%20-%20Space%20Missions%20Analysis"
            type={["dataScience"]}
          />

          <ProjectCard 
            img_bg="bg-099-fatal-force-analysis bg-project"
            title="Fatal Force Analysis"
            demo_url="https://www.kaggle.com/embed/garrettbecker/fatal-force-analysis?kernelSessionId=132688822"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20099%20-%20Fatal%20Force%20Analysis"
            type={["dataScience"]}
          />

          <ProjectCard 
            img_bg="bg-100-determinants-of-earnings-analysis bg-project"
            title="Determinants of Earnings Analysis"
            demo_url="https://www.kaggle.com/embed/garrettbecker/determinants-of-earnings-analysis?kernelSessionId=132695898"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/06%20-%20Professional/Day%20100%20-%20Determinants%20of%20Earnings%20Analysis"
            type={["dataScience"]}
          />
        </div>
      </section>

      <section id="3" className="pt-4 w-full items-center justify-center">
        <h1 className="px-2 h-full text-level3 max-w-fit ring-level3 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden">03 - INTERMEDIATE +</h1>
        <div className="flex flex-col pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          <ProjectCard 
            img_bg="bg-032-birthday-email-automation bg-project"
            title="Birthday Email Automation"
            demo_url="https://replit.com/@gdbecker/032-Birthday-Email-Automation?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20032%20-%20Birthday%20Email%20Automation"
            type={["auto"]}
          />

          <ProjectCard 
            img_bg="bg-033-iss-email-notifications bg-project"
            title="ISS Email Notifications"
            demo_url="https://replit.com/@gdbecker/033-ISS-Email-Notifications?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20033%20-%20ISS%20Email%20Notifications"
            type={["auto"]}
          />

          <ProjectCard 
            img_bg="bg-034-quizzler-app bg-project"
            title="Quizzler App"
            demo_url="https://replit.com/@gdbecker/034-Quizzler-App?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20034%20-%20Quizzler%20App"
            type={["gui"]}
          />

          <ProjectCard 
            img_bg="bg-035-rain-text-alert bg-project"
            title="Rain Text Alert"
            demo_url="https://replit.com/@gdbecker/035-Rain-Text-Alert?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20035%20-%20Rain%20Text%20Alert"
            type={["api", "auto"]}
          />

          <ProjectCard 
            img_bg="bg-036-stock-text-alert bg-project"
            title="Stock Text Alert"
            demo_url="https://replit.com/@gdbecker/036-Stock-Text-Alert?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20036%20-%20Stock%20Text%20Alert"
            type={["api", "auto"]}
          />

          <ProjectCard 
            img_bg="bg-037-habit-tracker bg-project"
            title="Habit Tracker"
            demo_url="https://replit.com/@gdbecker/037-Habit-Tracker?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20037%20-%20Habit%20Tracker"
            type={["api", "auto"]}
          />

          <ProjectCard 
            img_bg="bg-038-workout-tracker bg-project"
            title="Workout Tracker"
            demo_url="https://replit.com/@gdbecker/038-Workout-Tracker?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20038%20-%20Workout%20Tracker"
            type={["api", "auto"]}
          />

          <ProjectCard 
            img_bg="bg-045-movies-web-scraper bg-project"
            title="Movies Web Scraper"
            demo_url="https://replit.com/@gdbecker/045-Movies-Web-Scraper?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20045%20-%20Movies%20Web%20Scraper"
            type={["webScraping"]}
          />

          <ProjectCard 
            img_bg="bg-047-amazon-price-tracker bg-project"
            title="Amazon Price Tracker"
            demo_url="https://replit.com/@gdbecker/047-Amazon-Price-Tracker?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20047%20-%20Amazon%20Price%20Tracker"
            type={["webScraping", "api"]}
          />

          <ProjectCard 
            img_bg="bg-053-zillow-research bg-project"
            title="Zillow Research Automation"
            demo_url="https://replit.com/@gdbecker/053-Zillow-Research?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/03%20-%20Intermediate%2B/Day%20053%20-%20Zillow%20Research%20Automation"
            type={["webScraping", "api"]}
          />
        </div>
      </section>

      <section id="2" className="pt-4 w-full items-center justify-center">
        <h1 className="px-2 h-full text-level2 max-w-fit ring-level2 ring-2 rounded-sm font-sourceSansProBold text-sm overflow-hidden">02 - INTERMEDIATE</h1>
        <div className="flex flex-col pt-5 pb-10 gap-7 md:grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          <ProjectCard 
            img_bg="bg-015-coffee-machine-basic bg-project"
            title="Coffee Machine - Basic"
            demo_url="https://replit.com/@gdbecker/015-Coffee-Machine-Basic?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20015%20-%20Coffee%20Machine%20(Basic)"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-016-coffee-machine-oop bg-project"
            title="Coffee Machine - OOP"
            demo_url="https://replit.com/@gdbecker/016-Coffee-Machine-OOP?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20016%20-%20Coffee%20Machine%20(OOP)"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-017-quizbrain bg-project"
            title="QuizBrain"
            demo_url="https://replit.com/@gdbecker/017-QuizBrain?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20017%20-%20QuizBrain"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-018-dot-painting-app bg-project"
            title="Dot Painting App"
            demo_url="https://replit.com/@gdbecker/018-Dot-Painting-App?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20018%20-%20Dot%20Painting%20App"
            type={["gui"]}
          />

          <ProjectCard 
            img_bg="bg-019-etch-a-sketch-app bg-project"
            title="Etch-a-Sketch App"
            demo_url="https://replit.com/@gdbecker/019-Etch-a-Sketch-App?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20019%20-%20Etch-a-Sketch%20App"
            type={["gui"]}
          />

          <ProjectCard 
            img_bg="bg-019-turtle-race-game bg-project"
            title="Turtle Race Game"
            demo_url="https://replit.com/@gdbecker/019-Turtle-Race-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20019%20-%20Turtle%20Race%20Game"
            type={["game"]}
          />

          <ProjectCard 
            img_bg="bg-020-021-snake-game-v1 bg-project"
            title="Snake Game V1"
            demo_url="https://replit.com/@gdbecker/020-021-Snake-Game-V1?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20020-021%20-%20Snake%20Game%20V1"
            type={["game"]}
          />

          <ProjectCard 
            img_bg="bg-024-snake-game-v2 bg-project"
            title="Snake Game V2"
            demo_url="https://replit.com/@gdbecker/024-Snake-Game-V2?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20024%20-%20Snake%20Game%20V2"
            type={["game"]}
          />

          <ProjectCard 
            img_bg="bg-022-pong-game bg-project"
            title="Pong Game"
            demo_url="https://replit.com/@gdbecker/022-Pong-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20022%20-%20Pong%20Game"
            type={["game"]}
          />

          <ProjectCard 
            img_bg="bg-023-turtle-crossing-game bg-project"
            title="Turtle Crossing Game"
            demo_url="https://replit.com/@gdbecker/023-Turtle-Crossing-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20023%20-%20Turtle%20Crossing%20Game"
            type={["game"]}
          />

          <ProjectCard 
            img_bg="bg-024-mail-merge-app bg-project"
            title="Mail Merge App"
            demo_url="https://replit.com/@gdbecker/024-Mail-Merge-App?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20024%20-%20Mail%20Merge%20App"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-025-us-states-game bg-project"
            title="US States Game"
            demo_url="https://replit.com/@gdbecker/025-US-States-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20025%20-%20US%20States%20Game"
            type={["game"]}
          />

          <ProjectCard 
            img_bg="bg-026-nato-phonetic-alphabet bg-project"
            title="NATO Phonetic Alphabet"
            demo_url="https://replit.com/@gdbecker/026-NATO-Phonetic-Alphabet?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20026%20-%20NATO%20Phonetic%20Alphabet"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-027-mi-to-km-converter bg-project"
            title="MI to KM Converter"
            demo_url="https://replit.com/@gdbecker/027-MI-to-KM-Converter?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20027%20-%20MI%20to%20KM%20Converter"
            type={["gui"]}
          />

          <ProjectCard 
            img_bg="bg-028-pomodoro-app bg-project"
            title="Pomodoro App"
            demo_url="https://replit.com/@gdbecker/028-Pomodoro-App?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20028%20-%20Pomodoro%20App"
            type={["gui"]}
          />

          <ProjectCard 
            img_bg="bg-029-030-password-manager bg-project"
            title="Password Manager"
            demo_url="https://replit.com/@gdbecker/029-030-Password-Manager?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20029-030%20-%20Password%20Manager"
            type={["gui"]}
          />

          <ProjectCard 
            img_bg="bg-031-flash-card-app bg-project"
            title="Flash Card App"
            demo_url="https://replit.com/@gdbecker/031-Flash-Card-App?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/02%20-%20Intermediate/Day%20031%20-%20Flash%20Card%20App"
            type={["gui"]}
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
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-002-tip-calculator bg-project"
            title="Tip Calculator"
            demo_url="https://replit.com/@gdbecker/002-Tip-Calculator?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20002%20-%20Tip%20Calculator"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-003-treasure-island-game bg-project"
            title="Treasure Island Game"
            demo_url="https://replit.com/@gdbecker/003-Treasure-Island-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20003%20-%20Treasure%20Island%20Game"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-004-rock-paper-scissors bg-project"
            title="Rock - Paper - Scissors"
            demo_url="https://replit.com/@gdbecker/004-Rock-Paper-Scissors?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20004%20-%20Rock%20Paper%20Scissors"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-005-password-generator bg-project"
            title="Password Generator"
            demo_url="https://replit.com/@gdbecker/005-Password-Generator?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20005%20-%20Password%20Generator"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-006-escape-maze-problem bg-project"
            title="Reeborg's World: Escape Maze Problem"
            demo_url="https://replit.com/@gdbecker/006-Escape-Maze-Problem?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20006%20-%20Escape%20Maze%20Problem"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-007-hangman-game bg-project"
            title="Hangman Game"
            demo_url="https://replit.com/@gdbecker/007-Hangman-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20007%20-%20Hangman%20Game"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-008-caesar-cipher bg-project"
            title="Caesar Cipher"
            demo_url="https://replit.com/@gdbecker/008-Caesar-Cipher?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20008%20-%20Caesar%20Cipher"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-009-secret-auction bg-project"
            title="Secret Auction"
            demo_url="https://replit.com/@gdbecker/009-Secret-Auction?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20009%20-%20Secret%20Auction"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-010-calculator bg-project"
            title="Calculator"
            demo_url="https://replit.com/@gdbecker/010-Calculator?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20010%20-%20Calculator"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-011-blackjack-game bg-project"
            title="Blackjack Game"
            demo_url="https://replit.com/@gdbecker/011-Blackjack-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20011%20-%20Blackjack%20Game"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-012-number-guess-game bg-project"
            title="Number Guess Game"
            demo_url="https://replit.com/@gdbecker/012-Number-Guess-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20012%20-%20Number%20Guess%20Game"
            type={["scripting"]}
          />

          <ProjectCard 
            img_bg="bg-013-debugging-practice bg-project"
            title="Debugging Practice"
            demo_url="https://replit.com/@gdbecker/013-Debugging-Practice?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20013%20-%20Debugging%20Practice"
            type={["debugging"]}
          />

          <ProjectCard 
            img_bg="bg-014-higher-lower-game bg-project"
            title="Higher Lower Game"
            demo_url="https://replit.com/@gdbecker/014-Higher-Lower-Game?embed=true"
            code_url="https://github.com/gdbecker/100DaysOfCodePython/tree/main/01%20-%20Beginner/Day%20014%20-%20Higher%20Lower%20Game"
            type={["scripting"]}
          />
        </div>
      </section>

    </main>
  )
}

export default Home;