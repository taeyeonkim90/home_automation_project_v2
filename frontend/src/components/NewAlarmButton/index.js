import React, { Component } from 'react';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';

const style = {
  marginRight: 20,
};

class NewAlarmButton extends Component {
  createNewAlarm = () => {
    const defaultAlarm = {
      "minute" : "0",
      "hour" : "0",
      "day_of_week" : "*",
      "active" : false
    }
    this.props.createAlarm(defaultAlarm)
  }

  render() {
    return (
        <FloatingActionButton secondary={true} mini={true} style={style} onClick={this.createNewAlarm}>
          <ContentAdd />
        </FloatingActionButton>
    );
  }
}

export default NewAlarmButton;
