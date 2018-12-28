import InfiniteScroll from 'react-infinite-scroll-component';
import React from 'react';
import PropTypes from 'prop-types';
import Post from './post';


class Posts extends React.Component {
  /* 
  Take in all of the posts that the API call returned and display them
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = { url: '', next: '', results: [] };
    this.fetchMoreData = this.fetchMoreData.bind(this);
  }

  componentDidMount() {
    fetch(this.props.url, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        if (performance.navigation.type === performance.navigation.TYPE_BACK_FORWARD) {
          this.setState(history.state);
        }
        else {
        this.setState({
          url: data.url,
          next: data.next,
          results: data.results,
        });
        }
      })
      .then(() => {
        history.replaceState(this.state, '', '');
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  fetchMoreData() {
    fetch(this.state.next, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          url: data.url,
          next: data.next,
          results: (this.state.results).concat(data.results),
        });
      })
      .then(() => {
        history.replaceState(this.state, '', '');
        console.log("history.state")
        console.log(history.state)
      })
      .catch(error => console.log(error));// eslint-disable-line no-console
  }

  render() {
    return (
      <div className="posts">
        <ul>
          <InfiniteScroll
            dataLength={this.state.results.length}
            next={this.fetchMoreData}
            hasMore={true}
            loader={<h4>Loading...</h4>}
          >
            {this.state.results.map(result =>
              <Post key={result.postid} url={result.url} />,
            )}
          </InfiniteScroll>
        </ul>
      </div>
    );
  }
}

Posts.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Posts;
