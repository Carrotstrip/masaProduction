import React from 'react';
import PropTypes from 'prop-types';
import Likes from './likes';
import Comments from './comments';
import Image from './image';
import UserInfo from './userinfo';

class Post extends React.Component {
  /* 
  Display a post
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = {
      owner: '',
      age: '',
      owner_img_url: '',
      img_url: '',
      owner_show_url: '',
      post_show_url: '',
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
    const postStyle = {
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
      <div className="post" style={postStyle}>
        <p>
          <UserInfo
            name={this.state.owner}
            age={this.state.age}
            img_url={this.state.owner_img_url}
            owner_show_url={this.state.owner_show_url}
            post_show_url={this.state.post_show_url}
          />
          <Image url={this.state.img_url} />
          <Comments url={`${this.props.url}comments/`} />
          <Likes url={`${this.props.url}likes/`} />
        </p>
      </div>
    );
  }
}

Post.propTypes = {
  ownerUrl: PropTypes.string.isRequired,
  ownerImgUrl: PropTypes.string.isRequired,
  status: PropTypes.
};

export default Post;
