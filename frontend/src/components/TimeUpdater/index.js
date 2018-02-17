import React, { Component } from 'react';
import Toggle from 'material-ui/Toggle';
import Checkbox from 'material-ui/Checkbox';
import FlatButton from 'material-ui/FlatButton';
import TimePicker from 'material-ui/TimePicker';

class TimeUpdater extends Component {
  constructor(props) {
    super(props)

    this.state = {...props.data, time: null,
                  SUN: false, MON: false, TUE: false, WED: false,
                  THU: false, FRI: false, SAT: false}
    
    // parse time
    var date = new Date()
    var hour = parseInt(props.data.hour)
    var minute = parseInt(props.data.minute)
    date.setHours(hour, minute, 0)
    this.state.time = date
    
    // parse days
    let cronDays = props.data.day_of_week
    let dayDict = {"0":"SUN", "1":"MON", "2":"TUE", "3":"WED", "4":"THU", "5":"FRI", "6":"SAT"}
    var day = ""
    if (cronDays === "*"){
      for (var prop in dayDict){
        day = dayDict[prop]
        this.state[day] = true
      }
    } else {
      const split = cronDays.split(",")
      for (var i=0; i<split.length; i++){
        day = dayDict[split[i]]
        this.state[day] = true
      }
    }
  }

  deleteAlarm = () => {
    let id = this.props.data.id
    this.props.deleteAlarm(id)
  }

  updateAlarm = () => {
    let dayDict = {"SUN":"0", "MON":"1", "TUE":"2", "WED":"3", "THU":"4", "FRI":"5", "SAT":"6"}
    var day_of_week = ""
    // evaluate "*" case
    var isAllTrue = true
    for (var prop in dayDict){
      isAllTrue = isAllTrue && this.state[prop]
    }
    if (isAllTrue){
      day_of_week = "*"
    } 
    // evaluate individual case
    else{
      for (var prop in dayDict){
        if (this.state[prop]){
          day_of_week += `,${dayDict[prop]}`
        }
      }
      day_of_week = day_of_week.substring(1)
    }

    console.log(day_of_week)
    let id = this.props.data.id
    var data = { id: id, 
                minute: this.state.time.getMinutes().toString(),
                hour: this.state.time.getHours().toString(),
                day_of_week: day_of_week,
                active: this.state.active
              }
    this.props.updateAlarm(id, data)
  }

  checkClick = (event, isInputChecked) => {
    var obj = {}
    obj[event.target.id] = isInputChecked
    this.setState(obj)
  }

  toggleClick = () => {
    this.setState({active: !this.state.active})
  }

  timeClick = (event, newTime) => {
    this.setState({time: newTime})
  }

  renderCheckboxes = () => {
    let days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return days.map((day, key) => {
      let dayState = this.state[day]
      return <Checkbox key={key} id={day} label={day} checked={dayState} onCheck={this.checkClick}/>
    })
  }

  render() {
    return (
      <div>
        <TimePicker defaultTime={this.state.time} onChange={this.timeClick} hintText="12hr Format"/>
        <Toggle toggled={this.state.active} onClick={this.toggleClick}/>
        {this.renderCheckboxes()}
        <FlatButton label="update" primary={true} onClick={this.updateAlarm}/>
        <FlatButton label="delete" secondary={true} onClick={this.deleteAlarm}/>
      </div>
    );
  }
}

export default TimeUpdater;