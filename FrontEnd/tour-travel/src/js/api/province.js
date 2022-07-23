import Repository from "./repository";

class ProvinceAPI{
    constructor() {
        this.controler = "province";
    }
    /**
     * Phương thức lấy tất cả dữ liệu
     * create by: TQHa (11/10/2021)
     */
    getAll() {
        return Repository.get(`${this.controler}/all`);
    }

    getByID(id){
        return Repository.get(`${this.controler}/byid?id=${id}`);
    }
}

export default new ProvinceAPI();