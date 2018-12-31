import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Profile from './profile';



ReactDOM.render(
    <Router>
        <div>
          <Route path='/u/:uniqname/' component={Profile} />
        </div>
    </Router>,
  document.getElementById('reactEntry'),
);
