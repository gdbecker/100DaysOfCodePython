import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "AIzaSyAFWej-YqOZZJwHLaK81Z4DImoRknqebD0",
    authDomain: "pythonportfolio-f3945.firebaseapp.com",
    projectId: "pythonportfolio-f3945",
    storageBucket: "pythonportfolio-f3945.appspot.com",
    messagingSenderId: "984187302370",
    appId: "1:984187302370:web:d85d90391950eb7ac7c9bb",
    measurementId: "G-7739520ZR8"
  };

  const app = initializeApp(firebaseConfig);

export const db = getFirestore(app);