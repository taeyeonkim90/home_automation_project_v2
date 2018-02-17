import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AlarmContainer from '../AlarmContainer'

import './App.css';

class App extends Component {
  render() {
    return (
      <MuiThemeProvider>
        <AlarmContainer/>
      </MuiThemeProvider>
    );
  }
}

export default App;
