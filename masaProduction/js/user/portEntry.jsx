import React from 'react';
import PropTypes from 'prop-types';

class PortEntry extends React.Component {
  /*
  Display a post
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
    };
  }


  // componentDidMount() {
  //   // Call REST API to get 
  //   fetch(this.props.url, { credentials: 'same-origin' })
  //     .then((response) => {
  //       if (!response.ok) throw Error(response.statusText);
  //       return response.json();
  //     })
  //     .then((data) => {
  //       this.setState({
  //         owner: data.owner,
  //         age: data.age,
  //         owner_img_url: data.owner_img_url,
  //         img_url: data.img_url,
  //         owner_show_url: data.owner_show_url,
  //         post_show_url: data.post_show_url,
  //       });
  //     })
  //     .catch(error => console.log(error));// eslint-disable-line no-console
  // }

  render() {
    const portEntryStyle = {
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
      <div className="portEntry" style={portEntryStyle}>
        <p>
          This is a portfolio entry
        </p>
      </div>
    );
  }
}

PortEntry.propTypes = {
  url: PropTypes.string.isRequired,
};

export default PortEntry;
