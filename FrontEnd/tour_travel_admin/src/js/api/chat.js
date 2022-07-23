import Repository from "./repository";

class ChatAPI {
    constructor() {
        this.controller = 'message'
    }

    async getAllChatRoom() {
        return Repository.get(`${this.controller}/searchAll`);
    }

    async getAllChatRoomByAmount(amount) {
        return Repository.get(`${this.controller}/searchAll?amount=${amount}`);
    }
}

export default new ChatAPI();