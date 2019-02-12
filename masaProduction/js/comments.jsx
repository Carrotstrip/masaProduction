import React from 'react';
import PropTypes from 'prop-types';

class Comments extends React.Component {
  /* Display number of likes a like/unlike button for one post
   * Reference on forms https://facebook.github.io/react/docs/forms.html
   */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = { comments: [], url: '', value: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    // Call REST API to get comments 
    // credentials throws username to props
    fetch(this.props.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          url: data.url,
          comments: data.comments,
        });
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    fetch(this.state.url,
      {
        method: 'POST',
        body: JSON.stringify({ text: this.state.value }),
        headers: { 'Content-Type': 'application/json' },
      },
    )
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .catch(error => console.log(error));// eslint-disable-line no-console

    fetch(this.props.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          url: data.url,
          comments: data.comments,
        });
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
    this.setState({ value: '' });
    event.preventDefault();
  }

  render() {
    // Render comments
    return (
      <div className="comments">
        {this.state.comments.map(comment =>
          (<p key={comment.commentid}>
            <a href={comment.owner_show_url}>{comment.owner}</a>
            &nbsp;
            {comment.text}
          </p>),
        )}
        {
          <form id="comment-form" onSubmit={this.handleSubmit} >
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </form>
        }
      </div>
    );
  }
}

Comments.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Comments;
