import React, { Component } from 'react';
import FloatingActionButton from 'material-ui/FloatingActionButton';
import ContentAdd from 'material-ui/svg-icons/content/add';

const style = {
  marginRight: 20,
};

class NewAlarmButton extends Component {
  render() {
    return (
        <FloatingActionButton secondary={true} mini={true} style={style}><ContentAdd /></FloatingActionButton>
    );
  }
}

export default NewAlarmButton;
