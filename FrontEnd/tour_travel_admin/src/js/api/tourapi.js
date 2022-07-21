import Repository from "./repository";

class TourAPI{
    constructor() {
        this.controler = "tour";
    }
    
    getNewCode(){
        return Repository.get(`${this.controler}/newtourcode`);
    }

    sayMoney(money){
        return Repository.get(`${this.controler}/saymoney?money=${money}`);
    }

    update(body){
        return Repository.post(`${this.controler}/updatetemplate`, body);
    }

    filter(search, size, page, isStop, mode) {
        return Repository.get(`${this.controler}/filter?search=${search}&size=${size}&page=${page}&isStop=${isStop}&mode=${mode}`);
    }

    deleteTemplate(id){
        return Repository.delete(`${this.controler}/deleteTemplate?id=${id}`);
    }

    updateStatusTemplate(id, status){
        return Repository.get(`${this.controler}/updatestatus?id=${id}&status=${status}`);
    }

    getByID(id){
        return Repository.get(`${this.controler}/getbyid?id=${id}`);
    }

}

export default new TourAPI();