import { http, prepareParams } from './utils'

const SEARCH = 'search'
const SEARCH_ALL = 'searchAll'
const SEARCH_BY_ID = 'searchById'

const HOTEL = '/hotel'
const RESTAURANT = '/restaurant'
const ROOM = '/room'

function getSearchPath(basePath, segment = SEARCH) {
    return `${basePath}/${segment}`
}

const PATHS = {
    HOTELS: {
        BASE: HOTEL,
        SEARCH: getSearchPath(HOTEL),
        SEARCH_ALL: getSearchPath(HOTEL, SEARCH_ALL),
        SEARCH_BY_ID: getSearchPath(HOTEL, SEARCH_BY_ID)
    },
    RESTAURANTS: {
        BASE: RESTAURANT,
        SEARCH: getSearchPath(RESTAURANT),
        SEARCH_ALL: getSearchPath(RESTAURANT, SEARCH_ALL),
        SEARCH_BY_ID: getSearchPath(RESTAURANT, SEARCH_BY_ID),
        SEARCH_BY_HOTEL: getSearchPath(ROOM, 'searchRestaurantByHotel')
    },
    ROOMS: {
        BASE: ROOM,
        SEARCH: getSearchPath(ROOM),
        SEARCH_ALL: getSearchPath(ROOM, SEARCH_ALL),
        SEARCH_BY_ID: getSearchPath(ROOM, SEARCH_BY_ID),
        SEARCH_BY_HOTEL: getSearchPath(ROOM, 'searchRoomByHotel')
    },
}

export default {
    async getAllHotels() {
        const response = await http.request({
            method: 'get',
            url: PATHS.HOTELS.SEARCH_ALL
        })
        return response.data
    },
    async getHotelById(data) {
        const response = await http.request({
            method: 'post',
            url: PATHS.HOTELS.SEARCH_BY_ID,
            data: data
        })
        return response.data
    },
    async getHotelByAmount(data) {
        const response = await http.request({
            method: 'get',
            url: `${HOTEL}/searchHotel`,
            data: data
        })
        return response.data
    },
    async getAllRestaurants() {
        const response = await http.request({
            method: 'get',
            url: PATHS.RESTAURANTS.SEARCH_ALL
        })
        return response.data
    },
    async getRestaurantsByHotel(data) {
        const response = await http.request({
            method: 'post',
            url: PATHS.RESTAURANTS.SEARCH_BY_HOTEL,
            data: data
        })
        return response.data
    },
    async getAllRooms() {
        const response = await http.request({
            method: 'get',
            url: PATHS.ROOMS.SEARCH_ALL
        })
        return response.data
    },
    async getRoomsByHotel(data) {
        const response = await http.request({
            method: 'post',
            url: PATHS.ROOMS.SEARCH_BY_HOTEL,
            data: data
        })
        return response.data
    },
}