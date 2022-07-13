import { http } from './utils'

const AUTH = '/auth'

export default {
    async signIn(data) {
        const response = await http.request({
            method: 'post',
            url: `${AUTH}/login`,
            data: data
        })
        return response.data
    },
    async register(data) {
        const response = await http.request({
            method: 'post',
            url: `${AUTH}/register`,
            data: data
        })
        return response.data
    }
}