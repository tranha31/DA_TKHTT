import Repository from "./repository";

class UserAPI {
    constructor() {
        this.controller = 'auth'
    }

    async getAllUsersByListID(ListUserID) {
        return Repository.post(`${this.controller}/getAllUserById`, { ListUserID: ListUserID});
    }
}

export default new UserAPI();