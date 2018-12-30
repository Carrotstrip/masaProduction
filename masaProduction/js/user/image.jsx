import React from 'react';
import PropTypes from 'prop-types';

class Image extends React.Component {
  /* Display image for a post
   */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {};
    // this.handleClick = this.handleClick.bind(this);
  }

  render() {
    // Render number of likes
    return (
      <div className="image">
        <p>
          <img src={this.props.url} alt="user profile pic" width={200} height={200} />
        </p>
      </div>
    );
  }
}

Image.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Image;
