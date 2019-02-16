import React from 'react';
import Redirect from 'react-router-dom';
import Image from './image';
// import { Document, Page } from 'react-pdf';
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
      designCheck: '',
      partDeleted: false
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleDelete = this.handleDelete.bind(this);
    this.handleClaim = this.handleClaim.bind(this);
  }

  handleChange(event) {
    this.setState({ 
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    var updateUrl = '/api/v1.0/parts/' + this.props.match.params.partId + '/update/'
    var data = new FormData();
    data.append('productionCheck', this.state.productionCheck);
    data.append('designCheck', this.state.designCheck);
    fetch(updateUrl,
      {
        method: 'POST',
        body: data
      },
    )
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then(this.props.history.push('/parts/'))
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

  handleDelete(event) {
    event.preventDefault()
    var deleteUrl = '/api/v1.0/parts/' + this.props.match.params.partId + '/delete/'
    // Call REST API to get user info
    fetch(deleteUrl, { method: 'POST', credentials: 'same-origin' })
      .then(this.props.history.push('/parts/'))
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  handleClaim(event) {
    var claimUrl = '/api/v1.0/parts/' + this.props.match.params.partId + '/claim/'
    // Call REST API to get user info
    fetch(claimUrl, { method: 'POST', credentials: 'same-origin' })
      .then(this.props.history.push('/parts/'))
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  render() {
    return (
      <div className="PartPage">
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
        <input type="submit" name="update" value="update part"/>
      </form>
      <form action="" method="post" onSubmit={this.handleDelete} >
          <input type="submit" name="delete" value="delete part"/>
      </form>
        {/* <OBJModel src={`${this.state.cadModel}`} texPath="/uploads/" /> */}
        {/* <OBJModel src={`cube.obj`} texPath="/uploads/" /> */}
        {/* <Image url={`/uploads/${this.state.drawing}/`} /> */}
        {/* <Document file={`/uploads/${this.state.drawing}/`} >
          <Page pageNumber={1} />
        </Document> */}
        <a href={`/uploads/${this.state.drawing}/`} download>download drawing</a>
        <form action="" method="post" onSubmit={this.handleClaim} >
          <input type="submit" name="claim" value="claim part"/>
        </form>
      </div>
    );
  }
}

export default PartPage;
