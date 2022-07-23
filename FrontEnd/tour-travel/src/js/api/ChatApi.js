import { http } from './utils'

const MESSAGE = '/message'

export default {
    async getUserChatRoom(data) {
        const response = await http.request({
            method: 'post',
            url: `${MESSAGE}/chatroom`,
            data: data
        })
        return response.data
    },
    async createNewChat(data) {
        const response = await http.request({
            method: 'post',
            url: `${MESSAGE}/createRoom`,
            data: data
        })
        return response.data
    }
}