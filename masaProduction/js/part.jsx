import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom'
import Image from './image';
import {OBJModel} from 'react-3d-viewer'

class Part extends React.Component {
  /* 
  This is a thumbnail for a part that has already been approved. It consists of:
  A 3D model view that you can interact with (with download link)
  Every page of the drawing (with download link)
  Responsible machinist
  Designer
  Deadline
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      cadModel: '',
      drawing: '',
      machinist: '',
      designer: '',
      deadline: ''
    };
  }


  componentDidMount() {
    var partUrl = '/api/v1.0/parts/' + this.props.id
    // Call REST API to get part info
    fetch(partUrl, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        console.log(data)
        this.setState({
          machinist: data.machinist,
          designer: data.designer,
          cadModel: data.cadModel,
          drawing: data.drawing,
          deadline: data.deadline
        });
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  render() {
    const PartStyle = {
      padding: 10,
      margin: 10,
      backgroundColor: '#ffde00',
      color: '#333',
      display: 'inline-block',
      fontFamily: 'monospace',
      fontSize: 12,
      textAlign: 'left',
      wordWrap: 'break-word',
      border: '2px solid red',
    };
    return (
      <span className="Part" style={PartStyle} >
        <p>
          <OBJModel src={`/uploads/${this.state.cadModel}`} texPath="" width={200} height={200} />
          {/* <OBJModel src="/uploads/cube.obj" texPath="" width={200} height={200} /> */}
          <Image url={`/uploads/${this.state.drawing}`} />
          <ul>
            <li>Lead Machinist: {this.state.machinist}</li>
            <li>Lead Designer: {this.state.designer}</li>
            <li>Deadline: {this.state.deadline}</li>
            <li><Link to={`/parts/${this.props.id}`}>more detail</Link></li>
          </ul>
        </p>
      </span>
    );
  }
}
Part.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Part;
