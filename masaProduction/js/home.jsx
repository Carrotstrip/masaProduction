import React from 'react';
import PropTypes from 'prop-types';
import { BrowserRouter as Router, Route } from 'react-router-dom';

// A user Home consists of the following:
// name, picture, year
// # Ops completed
// Hours machined
// Trainings
// anything that would be useful to somebody applying for jobs for impressing people

class Home extends React.Component {
  /*
  Display a Home
  */

  render() {
    
    return (
      <div className="main">
        Welcome to the MASA Production site! This site is meant to streamline the logistics of producing parts.
        The layout is as follows:

        <ul>
          <li>Members: contains data on all production members</li>
          <li>Parts: contains all information on approved parts</li>
          <li>Readers: contains all parts awaiting approval, and serves as a public platform for deciding approval</li>
        </ul>

        The site is built with:

        <ul>
          <li>Python: serverside scripting</li>
          <li>Flask: Python serverside framework</li>
          <li>Javascript: clientside scripting</li>
          <li>React: Javascript clientside library</li>
          <li>SQLite3: database</li>
          <li>nginx: reverse proxy</li>
          <li>gunicorn: WSGI HTTP server</li>
        </ul>

        Want to help make the site better?
        Fork it on Github <a href="https://github.com/Carrotstrip/masaProduction">here!</a>
        <br></br>
        -by Austin Wolfgram, Jacob Fedrigon and BIG CHUNGUS
      </div>
    );
  }
}

export default Home;
