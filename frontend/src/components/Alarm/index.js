import React, { Component } from 'react';
import {Card, CardHeader, CardText} from 'material-ui/Card';

import TimeUpdater from '../TimeUpdater'

class Alarm extends Component {
  renderTime = () => {
    const minute = parseInt(this.props.data.minute)
    const hour = parseInt(this.props.data.hour)
    var displayMinute = minute.toString()
    var displayHour = hour.toString()
    var display12hr = "AM"
    if (minute < 10){
      displayMinute = "0" + minute.toString()
    }
    if (displayHour > 12){
      var newHour = displayHour - 12
      displayHour = newHour.toString()
      display12hr = "PM"
    }
    return `${displayHour}:${displayMinute} ${display12hr}`
  }

  renderDays = () => {
    const dict = {0:"SUN", 1:"MON", 2:"TUE", 3:"WED", 4:"THU",
                  5:"FRI", 6:"SAT"}
    const cronDays = this.props.data.day_of_week
    var displayStr = ""

    // "*" case
    if (cronDays === "*"){
      for (var key in dict){
        if (dict.hasOwnProperty(key)){
          displayStr += `,${dict[key]}`
        }
      }
      return displayStr.substring(1)
    }
    // need to parse days
    else {
      const split = cronDays.split(",")
      for (var i=0; i<split.length; i++){
        var day = dict[split[i]]
        displayStr += `,${day}`
      }
      return displayStr.substring(1)
    }
  }

  render() {
    return (
      <Card>
        <CardHeader
          title={this.renderTime()}
          subtitle={this.renderDays()}
          actAsExpander={true}
          showExpandableButton={true}
        />
        <CardText expandable={true}>
          <TimeUpdater data={this.props.data} 
            updateAlarm={this.props.updateAlarm}
            deleteAlarm={this.props.deleteAlarm}/>
        </CardText>
      </Card>
    );
  }
}

export default Alarm;