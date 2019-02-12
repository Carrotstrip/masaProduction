import React from 'react';
import PropTypes from 'prop-types';
import Part from './part';


class Readers extends React.Component {
  /* 
  Take in all of the Parts that the API call returned and display them
  */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.state = { 
      url: '',
      results: []
    };
  }

  componentDidMount() {
    var partsUrl = "/api/v1.0/parts/"
    fetch(partsUrl, { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        this.setState({
          url: data.url,
          next: data.next,
          results: data.results
        });
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  render() {
    return (
      <div className="Parts">
        <ul>
            {this.state.results.map(result =>
              <Part key={result.id} id={result.id} url={result.url} />,
            )}
        </ul>
      </div>
    );
  }
}

export default Readers;
