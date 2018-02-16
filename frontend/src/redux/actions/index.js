import axios from 'axios'

import {BASE_URL} from '../../config'


// CRUD async action constants
// export const REQUEST_CREATE_ALARM = "REQUEST_CREATE_ALARM"
export const CREATE_ALARM = "CREATE_ALARM"

// export const REQUEST_READ_ALARMS = "REQUEST_READ_ALARMS"
export const READ_ALARMS = "READ_ALARMS"

// export const REQUEST_UPDATE_ALARM = "REQUEST_UPDATE_ALARM"
export const UPDATE_ALARM = "UPDATE_ALARM"

// export const REQUEST_DELETE_ALARM = "REQUEST_DELETE_ALARM"
export const DELETE_ALARM = "DELETE_ALARM"

// synchronous actions
const addAlarm = (alarm) => {
    return {
        type: CREATE_ALARM,
        alarm: alarm
    }
}

const readAlarms = (alarms) => {
    return {
        type: READ_ALARMS,
        alarms: alarms
    }
}

const updateAlarm = (id, alarm) => {
    return {
        type: UPDATE_ALARM,
        id: id,
        alarm: alarm
    }
}

const deleteAlarm = (id) => {
    return {
        type: DELETE_ALARM,
        id: id
    }
}

// helper function to configure axios instance
const axiosCreator = () => {
    return axios.create({baseURL : BASE_URL})
}

// asynchronous action creators
export const actionCreators = {
    createAlarm: (alarm) => (dispatch, getState) => {
        let fetchTask = axiosCreator().post('/api/alarms/', alarm)
            .then(response => {
                dispatch(addAlarm(response.data))
            })
            .catch(error => {})
    },
    readAlarms: () => (dispatch, getState) => {
        let fetchTask = axiosCreator().get('/api/alarms/')
            .then(response => {
                dispatch(readAlarms(response.data))
            })
            .catch(error => {})
    },
    updateAlarm: (id, alarm) => (dispatch, getState) => {
        let url = `/api/alarms/${id}/`
        let fetchTask = axiosCreator().put(url, alarm)
            .then(response => {
                dispatch(updateAlarm(id, response.data))
            })
            .catch(error => {})
    },
    deleteAlarm: (id) => (dispatch, getState) => {
        let url = `/api/alarms/${id}/`
        let fetchTask = axiosCreator().delete(url)
            .then(response => {
                dispatch(deleteAlarm(id))
            })
            .catch(error => {})
    }
}