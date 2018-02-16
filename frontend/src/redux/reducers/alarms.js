import {CREATE_ALARM, READ_ALARMS, UPDATE_ALARM, DELETE_ALARM} from '../actions'

const alarms = (state = [], action) => {
    switch (action.type) {
      case CREATE_ALARM:
        return [
          ...state,
          action.alarm
        ]
      case READ_ALARMS:
        return action.alarms
      case UPDATE_ALARM:
        return state.map(alarm =>
          (alarm.id === action.id) 
            ? action.alarm
            : alarm
        )
      case DELETE_ALARM:
        return state.filter(alarm => alarm.id !== action.id)
      default:
        return state
    }
  }
  
  export default alarms