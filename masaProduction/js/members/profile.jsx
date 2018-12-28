import React from 'react';
import PropTypes from 'prop-types';

// A user profile consists of the following:
// # Ops completed
// Hours machined
// Trainings
// anything that would be useful to somebody applying for jobs

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
    // Call REST API to get number of likes
    fetch(this.props.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          owner: data.owner,
          age: data.age,
          owner_img_url: data.owner_img_url,
          img_url: data.img_url,
          owner_show_url: data.owner_show_url,
          post_show_url: data.post_show_url,
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

// Post.propTypes = {
//   ownerUrl: PropTypes.string.isRequired,
//   ownerImgUrl: PropTypes.string.isRequired,
//   status: PropTypes.string.isRequired
// };

export default Profile;
