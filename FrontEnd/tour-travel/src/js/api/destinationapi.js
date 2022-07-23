import Repository from "./repository";

class DestinationAPI{
    constructor() {
        this.controler = "destination";
    }
    /**
     * Phương thức lấy tất cả dữ liệu
     * create by: TQHa (11/10/2021)
     */
    getAll(search, size, page) {
        return Repository.get(`${this.controler}/all?search=${search}&size=${size}&page=${page}`);
    }

    getByID(id){
        return Repository.get(`${this.controler}/byid?id=${id}`);
    }

    update(body){
        return Repository.post(`${this.controler}/update`, body);
    }

    delete(id){
        return Repository.delete(`${this.controler}/delete?id=${id}`);
    }

    getDesInProvince(id){
        return Repository.get(`${this.controler}/inprovince?id=${id}`);
    }
}

export default new DestinationAPI();