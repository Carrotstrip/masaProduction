import React from 'react';
import PropTypes from 'prop-types';
import Image from './image';
import {OBJModel} from 'react-3d-viewer'

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
    this.state = {
      cadModel: '',
      drawing: '',
      machinist: '',
      designer: '',
      deadline: ''
    };
  }


  // componentDidMount() {
  //   var PartPageUrl = '/api/v1.0/parts/' + this.props.id
  //   // Call REST API to get part info
  //   fetch(partUrl, { credentials: 'same-origin' })
  //     .then((response) => {
  //       if (!response.ok) throw Error(response.statusText);
  //       return response.json();
  //     })
  //     .then((data) => {
  //       console.log(data)
  //       this.setState({
  //         machinist: data.machinist,
  //         designer: data.designer,
  //         cadModel: data.cadModel
  //       });
  //     })
  //     .catch(error => console.log(error));// eslint-disable-line no-console
  // }

  render() {
    const PartPageStyle = {
      padding: 10,
      margin: 10,
      backgroundColor: '#ffde00',
      color: '#333',
      display: 'inline-block',
      fontFamily: 'monospace',
      fontSize: 12,
      textAlign: 'center',
      border: '2px solid red',
    };
    return (
      <div className="PartPage" style={PartPageStyle} >
        <p>
          Hi
        </p>
      </div>
    );
  }
}
PartPage.propTypes = {
  url: PropTypes.string.isRequired,
};

export default PartPage;
