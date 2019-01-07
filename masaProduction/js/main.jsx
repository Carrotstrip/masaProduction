import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, browserHistory } from 'react-router-dom';
import Profile from './profile';
import Home from './home'
import Parts from './parts'
import Request from './request'
import PartPage from './partPage'

ReactDOM.render(
    <Router history={browserHistory} >
        <div>
          <Route exact path='/' component={Home} />
          <Route path='/u/:uniqname/' component={Profile} />
          <Route exact path='/parts/' component={Parts} />
          <Route path='/parts/:partId' component={PartPage} />
          <Route path='/request/' component={Request} />
        </div>
    </Router>,
  document.getElementById('reactEntry'),
);
