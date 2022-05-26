import Repository from "./repository";

export default class BaseAPI {

    constructor() {
        this.controler = null;
    }
    /**
     * Phương thức lấy tất cả dữ liệu
     */
    getAll() {
        return Repository.get(`${this.controler}`);
    }

    /**
     * Lấy đối tượng theo id
     * @param {*} id 
     */
     getById(id){
        return Repository.get(`${this.controler}/${id}`);
    }

    /**
     * Hàm cập nhật dữ liệu
     * @param {*} body 
     */
    update(body) {
        return Repository.put(`${this.controler}`, body);
    }
    
    /**
     * Thêm mới
     * @param {*} body 
     * @returns 
     */
    addNew(body){
        return Repository.post(`${this.controler}`, body);
    }

    /**
     * Xóa đối tượng
     * @param {*} listId : ds id cần xóa 
     * @returns 
     */
    delete(listId){
        return Repository.delete(`${this.controler}`, {data: listId});
    }
}