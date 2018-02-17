import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import { ToastContainer, toast } from 'react-toastify';

import AlarmContainer from '../AlarmContainer'


class App extends Component {
  render() {
    return (
      <div>
        <MuiThemeProvider>
          <AlarmContainer/>
        </MuiThemeProvider>
        <ToastContainer autoClose={2500} position={toast.POSITION.BOTTOM_CENTER}/>
      </div>
    );
  }
}

export default App;
