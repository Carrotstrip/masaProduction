import React from 'react';

class Edit extends React.Component {

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.myRef = React.createRef();
    // this.state.url is the api endpoint for requests
    this.state = {
      url: '',
      fullName: '',
      uniqname: '',
      password: '',
      profilePic: '',
      millStatus: '',
      latheStatus: '',
      cncMillStatus: '',
      cncLatheStatus: '',
      haasStatus: '',
      available: '',
      img_url: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    var userUrl = '/api/v1.0/u/' + this.props.match.params.uniqname + '/'
    // Call REST API to get user info
    fetch(userUrl, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          fullName: data.fullname,
          uniqname: data.uniqname,
          password: data.password,
          profilePic: data.profilePic,
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

  handleChange(event) {
    this.setState({ 
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    event.preventDefault()
    // var editUrl = '/api/v1.0/request/'
    var editUrl = '/api/v1.0' + this.props.match.url  
    console.log(editUrl)  
    var data = new FormData();
    data.append('title', 'mydata')
    data.append('fullName', this.state.fullName);
    data.append('uniqname', this.state.uniqname);
    data.append('password', this.state.password);
    if(this.profilePic.files[0]) {
      console.log('added pic')
      data.append('profilePic', this.profilePic.files[0]);
    }
    data.append('millStatus', this.state.millStatus);
    data.append('latheStatus', this.state.latheStatus);
    data.append('cncMillStatus', this.state.cncMillStatus);
    data.append('cncLatheStatus', this.state.cncLatheStatus);
    data.append('haasStatus', this.state.haasStatus);
    data.append('available', this.state.available);
    console.log(data)
    fetch(editUrl,
      {
        method: 'POST',
        body: data
      },
    )
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  render() {
    // Render Edit
    return (
      <div className="edit">
        current statuses
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

            <td>
            <select name="millStatus" onChange={this.handleChange}>
              <option hidden value="default">select one</option>
              <option value="untrained">untrained</option>
              <option value="user">user</option>
              <option value="operator">operator</option>
              <option value="mentor">mentor</option>
            </select>
             {this.state.millStatus}
            </td>
            <td>
            <select name="latheStatus" onChange={this.handleChange}>
              <option hidden value="default">select one</option>
              <option value="untrained">untrained</option>
              <option value="user">user</option>
              <option value="operator">operator</option>
              <option value="mentor">mentor</option>
            </select>
             {this.state.latheStatus}</td>
            <td>
            <select name="cncMillStatus" onChange={this.handleChange}>
              <option hidden value="default">select one</option>
              <option value="untrained">untrained</option>
              <option value="user">user</option>
              <option value="operator">operator</option>
              <option value="mentor">mentor</option>
            </select>
             {this.state.cncMillStatus}</td>
            <td>
            <select name="cncLatheStatus" onChange={this.handleChange}>
              <option hidden value="default">select one</option>
              <option value="untrained">untrained</option>
              <option value="user">user</option>
              <option value="operator">operator</option>
              <option value="mentor">mentor</option>
            </select>
             {this.state.cncLatheStatus}</td>
            <td>
            <select name="haasStatus" onChange={this.handleChange}>
              <option hidden value="default">select one</option>
              <option value="untrained">untrained</option>
              <option value="user">user</option>
              <option value="operator">operator</option>
              <option value="mentor">mentor</option>
            </select>
             {this.state.haasStatus}</td>
            <td>
            <select name="available" onChange={this.handleChange}>
              <option hidden value="default">select one</option>
              <option value="yes">yes</option>
              <option value="no">no</option>
            </select>
             {this.state.available}
            </td>
          </tr> 
        </table>
        <form ref={this.myRef} action="" method="post" onSubmit={this.handleSubmit} encType="multipart/form-data">
          <input ref={(ref) => { this.profilePic = ref; }} type="file" name="profilePic"/>
          <input type="text" name="fullName" value={this.state.fullName} onChange={this.handleChange} placeholder="update fullName"/>
          <input type="text" name="uniqname" value={this.state.uniqname} onChange={this.handleChange} placeholder= "update uniqname"/>
          <input type="submit" name="update" value="submit"/>
        </form>
      </div>
    );
  }
}

export default Edit;
