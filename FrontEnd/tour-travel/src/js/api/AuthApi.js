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
    },
    async getUserInformation(data) {
        const response = await http.request({
            method: 'post',
            url: `${AUTH}/getUserById`,
            data: data
        })
        return response.data
    },
    async updateGeneralInfos(data) {
        const response = await http.request({
            method: 'post',
            url: `${AUTH}/updateUserInfos`,
            data: data
        })
        return response.data
    },
    async updatePassword(data) {
        const response = await http.request({
            method: 'post',
            url: `${AUTH}/updatePassword`,
            data: data
        })
        return response.data
    }
}