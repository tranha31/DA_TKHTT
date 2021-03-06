import VDashBoard from "../../views/VDashBoard.vue"
import VTourTemplate from "../../views/tour/VTourTemplate.vue"
import VTourOrder from "../../views/tour/VTourOrder.vue"
import VTourRequest from "../../views/tour/VTourRequest.vue"
import VTourCancel from "../../views/tour/VTourCancel.vue"
import VHotelList from "../../views/hotel/VHotelList.vue"
import VPlace from "../../views/place/VPlace.vue"
import VChat from "../../views/chat/VChat.vue"
import VLogin from "../../views/VLogin.vue"

export default class Router{
    routes = [
        {path: '/admin/dashboard', name: 'dashboard', component: VDashBoard},
        {path: '/admin/tourtemplate', name: 'template', component: VTourTemplate},
        {path: '/admin/tourorder', name: 'tourorder', component: VTourOrder},
        {path: '/admin/tourrequest', name: 'tourrequest', component: VTourRequest},
        {path: '/admin/tourcancel', name: 'tourcancel', component: VTourCancel},
        {path: '/admin/hotel', name: 'hotel', component: VHotelList},
        {path: '/admin/place', name: 'place', component: VPlace},
        {path: '/admin/chat', name: 'chat', component: VChat},
        {path: '/admin/login', name: 'login', component: VLogin},
    ]
}