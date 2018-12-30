import React from 'react';
import PropTypes from 'prop-types';

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
    };
  }

  componentDidMount() {
    // Call REST API to get user info
    fetch(this.props.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          name: data.name,
          age: data.age,
          userImgUrl: data.user_img_url,
          numOps: data.numOps,

        });
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  render() {
    
    return (
      <div className="profile">
        <p>
          Yo
        </p>
      </div>
    );
  }
}

Profile.propTypes = {
  ownerUrl: PropTypes.string.isRequired,
  ownerImgUrl: PropTypes.string.isRequired,
  status: PropTypes.string.isRequired
};

export default Profile;
