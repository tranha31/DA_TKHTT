import axios from 'axios'
import Vue from 'vue'

const localhost_URL = 'http://localhost:5000'

const http = axios.create({
    baseURL: localhost_URL,
    timeout: 30000
})

http.defaults.timeout = 30000

http.interceptors.request.use(
    async config => {
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

http.interceptors.response.use(
    res => res,
    error => {
        let msg = 'API request failed'
        if (error && error.response && error.response.data) {
            msg = error.response.data.message || error.response.data
        }

        Vue.notify({
            group: 'default',
            type: 'error',
            title: 'Error',
            text: msg
        })
        return Promise.reject(error)
    }
)

const prepareParams = function(params) {
    var str = ''
    for (var key in params) {
        if (str !== '') str += '&'
        if (!params[key]) continue
        str += key + '=' + encodeURIComponent(params[key])
    }
    return str
}

export {
    http,
    prepareParams
}