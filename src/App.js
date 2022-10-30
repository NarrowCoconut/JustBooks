import { useState } from 'react'
import axios from "axios";
import logo from './logo.svg';
import './App.css';
// app details:
// 1. create an about me and contact me section at the top of the page
// 2. populate the books section with information from the database
// 3. the database server is managed by a flask app
// 4. the flask app is running on a virtual machine
// 5. the virtual machine is running on a local network
// 6. the books section populates 3 books at a time, and the user can scroll down to load more books
// 7. the user can click on a book to see more information about it
function App() {

   // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {
    axios({
      method: "GET",
      url:"/profile",
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.about}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        {/* new line start*/}
        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
            </div>
        }
         {/* end of new line */}
      </header>
    </div>
  );
}

export default App;
