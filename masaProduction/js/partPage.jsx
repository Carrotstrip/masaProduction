import React from 'react';
import PropTypes from 'prop-types';
import Image from './image';
// import {OBJModel} from 'react-3d-viewer'

class PartPage extends React.Component {
  /* 
  This is a thumbnail for a PartPage that has already been approved. It consists of:
  A 3D model view that you can interact with (with download link)
  Every page of the drawing (with download link)
  Responsible machinist
  Designer
  Deadline
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.myRef = React.createRef();
    this.state = {
      cadModel: '',
      drawing: '',
      machinist: '',
      designer: '',
      deadline: '',
      productionCheck: '',
      designCheck: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ 
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    event.preventDefault()
    var editUrl = '/api/v1.0/request/'
    // var editUrl = '/api/v1.0' + this.props.match.url + '/' 
    var data = new FormData();
    data.append('title', 'mydata')
    data.append('fullName', this.state.fullName);
    data.append('uniqname', this.state.uniqname);
    data.append('password', this.state.password);
    if(this.profilePic.files[0]) {
      data.append('profilePic', this.profilePic.files[0]);
    }
    data.append('millStatus', this.state.millStatus);
    data.append('latheStatus', this.state.latheStatus);
    data.append('cncMillStatus', this.state.cncMillStatus);
    data.append('cncLatheStatus', this.state.cncLatheStatus);
    data.append('haasStatus', this.state.haasStatus);
    data.append('available', this.state.available);
    console.log(data)
    console.log(editUrl)
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

  componentDidMount() {
    var partPageUrl = '/api/v1.0/parts/' + this.props.match.params.partId + '/'
    // Call REST API to get part info
    fetch(partPageUrl, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        console.log(data)
        this.setState({
          machinist: data.machinist,
          designer: data.designer,
          deadline: data.deadline,
          cadModel: data.cadModel,
          drawing: data.drawing,
          productionCheck: data.productionCheck,
          designCheck: data.designCheck
        });
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  render() {
    return (
      <div className="PartPage">
        <p>
          {`/uploads/${this.state.cadModel}`}
          {/* <OBJModel src={'/uploads/' + this.state.cadModel} texPath="" /> */}
          <table id="userTable">
          <tr>
            <th>designer</th>
            <th>responsible machinist</th>
            <th>deadline</th>
            <th>production check</th>
            <th>design check</th>
          </tr>
          <tr>
            <td>{this.state.designer}</td>
            <td>{this.state.machinist}</td>
            <td>{this.state.deadline}</td>
            <td>
              <select name="productionCheck" onChange={this.handleChange}>
                <option hidden value="default">select one</option>
                <option value="yes">yes</option>
                <option value="no">no</option>
              </select>
              {this.state.productionCheck}
            </td>
            <td>
              <select name="designCheck" onChange={this.handleChange}>
                <option hidden value="default">select one</option>
                <option value="yes">yes</option>
                <option value="no">no</option>
              </select>
              {this.state.designCheck}
            </td>
          </tr> 
        </table>
        <form ref={this.myRef} action="" method="post" onSubmit={this.handleSubmit} encType="multipart/form-data">
          <input type="submit" name="update" value="submit"/>
        </form>
          {/* <OBJModel src={`${this.state.cadModel}`} texPath="/uploads/" /> */}
          {/* <OBJModel src={`cube.obj`} texPath="/uploads/" /> */}
          <Image url={`/uploads/${this.state.drawing}`} />
        </p>
      </div>
    );
  }
}

export default PartPage;
