import React from 'react';
import DatePicker from "react-datepicker";

// import "react-datepicker/dist/react-datepicker.css";

class Request extends React.Component {
  /* Display number of likes a like/unlike button for one post
   * Reference on forms https://facebook.github.io/react/docs/forms.html
   */

  constructor(props) {
    // Initialize mutable state
    super(props);
    this.myRef = React.createRef();
    // this.state.url is the api endpoint for requests
    this.state = {
      url: '',
      partName: '',
      partNumber: '',
      leadDesigner: '',
      leadMachinist: '',
      cadModel: '',
      drawing: '',
      deadline: new Date()
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ 
      [event.target.name]: event.target.value
    });
  }

  handleDateChange(date) {
    this.setState({
      deadline: date
    });
  }

  handleSubmit(event) {
    var requestUrl = "/api/v1.0/request/"
    var data = new FormData();
    var deadline = new Intl.DateTimeFormat('en-US').format(this.state.deadline)
    console.log(deadline)
    data.append('cadModel', this.cadModel.files[0]);
    data.append('drawing', this.drawing.files[0]);
    data.append('partName', this.state.partName);
    data.append('partNumber', this.state.partNumber);
    data.append('designer', this.state.leadDesigner);
    data.append('deadline', deadline);
    fetch(requestUrl,
      {
        method: 'POST',
        body: data
      },
    )
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .catch(error => console.log(error)); // eslint-disable-line no-console
  }

  render() {
    // Render request
    return (
      <div className="request">
        {
          <form ref={this.myRef} id="typedInfo" onSubmit={this.handleSubmit} action="" method="post" encType="multipart/form-data">
            <label>part name</label>
            <input name="partName" type="text" value={this.state.partName} onChange={this.handleChange} /><br></br>
            <label>part number</label>
            <input name="partNumber" type="text" value={this.state.partNumber} onChange={this.handleChange} /><br></br>
            <label>lead designer</label>
            <input name="leadDesigner" type="text" value={this.state.leadDesigner} onChange={this.handleChange} /><br></br>
            <label>deadline</label>
            <DatePicker
              selected={this.state.deadline}
              onChange={this.handleDateChange}
              minDate={new Date()}
              placeholderText="Click to select a date"
              dateFormat="MM/dd/yyyy"
            /><br></br>
            {/* <input name="deadline" type="text" value={this.state.deadline} onChange={this.handleChange} /> */}
            <label>CAD model</label>
            <input ref={(ref) => { this.cadModel = ref; }} name="cadModel" type='file' /><br></br>
            <label>drawing</label>
            <input ref={(ref) => { this.drawing = ref; }} name="drawing" type='file' /><br></br>
            <input type="submit" name="submit" value="submit"/>
          </form>
        }
      </div>
    );
  }
}

export default Request;
