import React, { Component } from 'react'
import { connect } from 'react-redux'
import AppBar from 'material-ui/AppBar'

import NewAlarmButton from '../NewAlarmButton'
import Alarm from '../Alarm'
import { actionCreator } from '../../redux/actions'

const mapStateToProps = state => {
  return {alarms : state.alarms}
}

class AlarmContainer extends Component {
  componentWillMount(){
    this.props.readAlarms()
  }

  renderAlarms = () => {
    return this.props.alarms.map((alarm) =>
      <Alarm key={alarm.id} data={alarm} 
        updateAlarm={this.props.updateAlarm}
        deleteAlarm={this.props.deleteAlarm}/>
    )
  }

  render() {
    return (
      <div>
        <AppBar
            title="Sunrise IoT Controller"
            iconElementRight={<NewAlarmButton createAlarm={this.props.createAlarm}/>} // need to pass create function
        />
        {this.renderAlarms()}
      </div>
    );
  }
}

export default connect(mapStateToProps, actionCreator)(AlarmContainer)
