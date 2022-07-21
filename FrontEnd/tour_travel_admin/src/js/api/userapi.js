import Repository from "./repository";

class UserAPI{
    constructor() {
        this.controler = "auth";
    }
    
    getUserInfo(){
        return Repository.get(`${this.controler}/info`);
    }
}

export default new UserAPI();