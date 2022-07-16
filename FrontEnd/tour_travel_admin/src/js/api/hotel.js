import Repository from "./repository";

class HotelAPI {
    constructor() {
        this.controller = 'hotel'
    }

    async getAll() {
        return Repository.get(`${this.controller}/searchAll`);
    }

    async getById(id) {
        return Repository.post(`${this.controller}/searchById`, { HotelID: id });
    }
}

export default new HotelAPI();