import Repository from "./repository";

class UserAPI{
    constructor() {
        this.controler = "auth";
    }
    
    getUserInfo(){
        return Repository.get(`${this.controler}/info`);
    }

    getAdmin(data){
        return Repository.post(`${this.controler}/admin/login`, data);
    }
}

export default new UserAPI();