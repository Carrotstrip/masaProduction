import React from 'react';
import PropTypes from 'prop-types';
// import { BrowserRouter as Router, Route } from 'react-router-dom';

// A user profile consists of the following:
// name, picture, year
// # Ops completed
// Hours machined
// Trainings
// anything that would be useful to somebody applying for jobs for impressing people

class Profile extends React.Component {
  /*
  Display a profile
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      fullname: '',
      millStatus: '',
      latheStatus: '',
      cncMillStatu: '',
      cncLatheStatus: '',
      haasStatus: '',
      available: '',
      machineStatuses: []
    };
  }

  componentDidMount() {
    var userUrl = '/api/v1.0' + this.props.match.url
    // console.log(this.props.match.params.uniqname);
    // Call REST API to get user info
    fetch(userUrl, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          fullname: data.fullname,
          millStatus: data.millStatus,
          latheStatus: data.latheStatus,
          cncMillStatus: data.cncMillStatus,
          cncLatheStatus: data.cncLatheStatus,
          haasStatus: data.haasStatus,
          available: data.available,
        });
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  render() {
    
    return (
      <div className="profile">
        <p>
          Yo, {this.state.fullname}<br></br>
          Mill Status: {this.state.millStatus}
        </p>
      </div>
    );
  }
}

Profile.propTypes = {
  // url: PropTypes.string.isRequired,
};

export default Profile;
