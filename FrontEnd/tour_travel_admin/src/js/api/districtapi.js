import Repository from "./repository";

class DistrictAPI{
    constructor() {
        this.controler = "district";
    }
    /**
     * Phương thức lấy tất cả dữ liệu
     * create by: TQHa (11/10/2021)
     */
    getAll(id) {
        return Repository.get(`${this.controler}/inprovince?pid=${id}`);
    }

    getByID(id){
        return Repository.get(`${this.controler}/byid?id=${id}`);
    }
}

export default new DistrictAPI();