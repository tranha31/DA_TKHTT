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

    filterSideUser(search, destinationID, startID, time, price, size, page) {
        return Repository.get(`${this.controler}/user/filter?search=${search}&destinationID=${destinationID}&startID=${startID}&time=${time}&price=${price}&size=${size}&page=${page}`);
    }

    getListTourSuggest(tourID, toID){
        return Repository.get(`${this.controler}/user/suggest?tourID=${tourID}&toID=${toID}`);
    }

    updateTour(body){
        return Repository.post(`${this.controler}/updatetour`, body);
    }

    addToCart(body){
        return Repository.post(`${this.controler}/addtocart`, body);
    }

    deleteInCart(tourID, userID){
        return Repository.delete(`${this.controler}/deleteincart?tourID=${tourID}&userID=${userID}`);
    }

    getInCart(userID){
        return Repository.get(`${this.controler}/getcart?userID=${userID}`);
    }

    getTourOrder(userID){
        return Repository.get(`${this.controler}/getlistorder?userID=${userID}`);
    }
}

export default new TourAPI();