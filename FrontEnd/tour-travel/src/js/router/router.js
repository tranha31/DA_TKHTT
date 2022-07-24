import VTour from "../../views/tour/VTour.vue"
import VTourInfor from "../../views/tour/VTourInfor.vue"
import VRoom from "../../views/room/VRoom.vue"
import VHotel from "@/views/hotel/VHotel"
import Hotel from "@/components/layout/Hotel"
import LogInUI from "@/components/layout/LogInUI"
import RegisterUI from "@/components/layout/RegisterUI"
import UserUI from "@/components/layout/UserUI"

export default class Router {
    routes = [
        { path: '/tour', name: 'tour', component: VTour },
        { path: '/tours/:search/:toId', name: 'tours', component: VTour },
        { path: '/tour/:id', name: 'tour-infor', component: VTourInfor },
        { path: '/hotel/room/:id', name: 'room-hotel', component: VRoom },
        { path: '/hotel/:id', name: 'hotel-detail', component: Hotel },
        { path: '/hotel', name: 'hotel', component: VHotel },
        { path: '/login', name: 'login', component: LogInUI },
        { path: '/register', name: 'register', component: RegisterUI },
        { path: '/user', name: 'user', component: UserUI },
    ]
}