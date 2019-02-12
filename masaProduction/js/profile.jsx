import React from 'react';
import Image from './image'

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
      cncMillStatus: '',
      cncLatheStatus: '',
      haasStatus: '',
      available: '',
      filename: ''
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
          img_url: data.img_url
        });
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  render() {
    
    return (
      <div className="profile">
        <div className="profilePic">
          <profileData>
            <Image url={this.state.img_url} width={200} height={200} />
            {/* <img src={this.state.img_url} alt="profilePic" width={100} height={100} /> */}
            {this.state.fullname}
          </profileData>
        </div>


        <table id="userTable">
          <tr>
            <th>mill status</th>
            <th>lathe status</th>
            <th>cnc mill status</th>
            <th>cnc lathe status</th>
            <th>haas status</th>
            <th>available</th>
          </tr>
          <tr>
            <td>{this.state.millStatus}</td>
            <td>{this.state.latheStatus}</td>
            <td>{this.state.cncMillStatus}</td>
            <td>{this.state.cncLatheStatus}</td>
            <td>{this.state.haasStatus}</td>
            <td>{this.state.available}</td>
          </tr> 
        </table>
      </div>
    );
  }
}

export default Profile;
