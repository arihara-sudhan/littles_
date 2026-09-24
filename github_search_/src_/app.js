import React, { useState, useEffect } from 'react';
import './App.css';

const GHUBACCESSTOKEN = "YOUR_ACCESS_TOKEN_HERE";

const fetchLangs = async (langs_url, setLangs) => {
  try {
    const response = await fetch(langs_url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${GHUBACCESSTOKEN}`,
        'X-GitHub-Api-Version': '2022-11-28'
      }
    });
    const langsData = await response.json();
    setLangs(Object.keys(langsData));
  } catch (error) {
    console.error('Error fetching repos:', error);
    setLangs([]);
  }
}


function Langs({ langs_url }) {
  const [langs, setLangs] = useState([]);

  useEffect(() => {
    if (langs_url) {
      fetchLangs(langs_url, setLangs);
    }
  }, [langs_url]);
  return (
    <div className='langs'>
      {langs.join(" | ")}
    </div>
  )
}


const fetchRepos = async (repos_url, setRepos) => {
  try {
    const response = await fetch(repos_url, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${GHUBACCESSTOKEN}`,
        'X-GitHub-Api-Version': '2022-11-28'
      }
    });
    const reposData = await response.json();
    setRepos(reposData);
  } catch (error) {
    console.error('Error fetching repos:', error);
    setRepos([]);
  }
}


function Repos({ repos_url }) {
  const [repos, setRepos] = useState([]);

  useEffect(() => {
    if (repos_url) {
      fetchRepos(repos_url, setRepos);
    }
  }, [repos_url]);

  return (
    <div className='repos'>
      {repos && repos.map(repo => (
        <div className='repoInfo'>
          <p id="reponame">{repo.name}</p>
          <p>{repo.description}</p>
          <div id='starforks'>
            <span>{repo.forks} FORKS</span>
            <span>{repo.stargazers_count} STARS</span>
            <Langs langs_url={repo.languages_url} />
          </div>
          <hr/>
        </div>
      ))}
    </div>
  )
}

const fetchUser = async (username, setUser) => {
  try {
    const response = await fetch(`https://api.github.com/users/${username}`, {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${GHUBACCESSTOKEN}`,
        'X-GitHub-Api-Version': '2022-11-28'
      }
    });
    const userData = await response.json();
    setUser(userData);
  } catch (error) {
    console.error('Error fetching user data:', error);
    setUser(null);
  }
}

function SearchBar({ setUser }) {
  const [username, setUsername] = useState('');

  const handleSearch = () => {
    fetchUser(username, setUser);
  }

  return (
    <div className="Bar">
      <img src="https://cdn.icon-icons.com/icons2/2157/PNG/512/github_git_hub_logo_icon_132878.png" id="logo-git" alt="GitHub Logo"/>
      <input type="text" onChange={(e) => setUsername(e.target.value)} />
      <button onClick={handleSearch}>SEARCH</button>
    </div>
  );
}

function App() {
  // DESTRUCTING : allows you to extract values from arrays, object
  /*
  // ARRAY DESTRUCTING
    const numbers = [1, 2, 3, 4, 5];

    // Extracting values from the array
    const [first, second, third] = numbers;

    console.log(first);  // Output: 1
    console.log(second); // Output: 2
    console.log(third);  // Output: 3

  // OBJECT DESTRUCTING
    const person = {
      name: 'John Doe',
      age: 30,
      city: 'New York'
    };

    // Extracting values from the object
    const { name, age, city } = person;

    console.log(name);  // Output: John Doe
    console.log(age);   // Output: 30
    console.log(city);  // Output: New York
  */
  const [user, setUser] = useState(null);

  return (
    <div className="App">
        <SearchBar setUser={setUser} />
        {user && (
          <div className="User-info">
            <img id="avatar" src={user.avatar_url} alt="AvatarImg"/>
            <span id="name">{user.login}</span>
            <span id="bio">{user.bio}</span>
            <span id="follows">
              <span>Followers: {user.followers}</span>
              <span>Following: {user.following}</span>
            </span>
            <hr/>
            <Repos repos_url={user.repos_url} />
          </div>
        )}
    </div>
  );
}

export default App;
