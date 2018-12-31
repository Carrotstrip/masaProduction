import React from 'react';
import PropTypes from 'prop-types';
import PortEntry from './portEntry';


class Portfolio extends React.Component {
  /*
  Take in all of the portEntries that the API call returns and display them
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
        this.setState({
          url: data.url,
          next: data.next,
          results: data.results,
        });
      })
      .then(() => {
        history.replaceState(this.state, '', '');
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  render() {
    return (
      <div className="portfolio">
        <ul>
          {this.state.results.map(result =>
            <PortEntry key={result.postid} url={result.url} />,
          )}
        </ul>
      </div>
    );
  }
}

Posts.propTypes = {
  url: PropTypes.string.isRequired,
};

export default Posts;
