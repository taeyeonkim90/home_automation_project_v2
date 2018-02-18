import axios from 'axios'
import { toast } from 'react-toastify';

import BASE_URL from '../../config'


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
export const actionCreator = {
    createAlarm: (alarm) => (dispatch, getState) => {
        axiosCreator().post('/api/alarms/', alarm)
            .then(response => {
                dispatch(addAlarm(response.data))
                toast.success("created a new alarm")
            })
            .catch(error => toast.error("could not create an alarm"))
    },
    readAlarms: () => (dispatch, getState) => {
        axiosCreator().get('/api/alarms/')
            .then(response => {
                dispatch(readAlarms(response.data))
                toast.success("finished loading all alarms")
            })
            .catch(error => toast.error("could not read alarms"))
    },
    updateAlarm: (id, alarm) => (dispatch, getState) => {
        let url = `/api/alarms/${id}/`
        axiosCreator().put(url, alarm)
            .then(response => {
                dispatch(updateAlarm(id, response.data))
                toast.success("updated an alarm")
            })
            .catch(error => toast.error("could not update an alarm"))
    },
    deleteAlarm: (id) => (dispatch, getState) => {
        let url = `/api/alarms/${id}/`
        axiosCreator().delete(url)
            .then(response => {
                dispatch(deleteAlarm(id))
                toast.success("deleted an alarm")
            })
            .catch(error => toast.error("could not delete an alarm"))
    }
}