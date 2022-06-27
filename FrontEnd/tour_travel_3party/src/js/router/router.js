import VRoom from "../../views/VRoom"
import VRoomBook from "../../views/VRoomBook"
import VRestaurant from "../../views/VRestaurant"
import VRestaurantBook from "../../views/VRestaurantBook"

export default class Router{
    routes = [
        {path: '/third/rooms', name: 'room', component: VRoom},
        {path: '/third/roombook', name: 'roombook', component: VRoomBook},
        {path: '/third/restaurant', name: 'restaurant', component: VRestaurant},
        {path: '/third/restaurantbook', name: 'restaurantbook', component: VRestaurantBook},
    ]
}