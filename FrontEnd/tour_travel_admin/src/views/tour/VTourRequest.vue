<template>
  <div class="list-template">
    <div class="header d-flex">
        <BaseInput
        :hasTitle="false"
        :msrequire="false"
        :notNull="false"
        :placeholder="'Nhập mã tour, tên tour để tìm kiếm'"
        :clas="'w-30'"
        :content="searchKey"
        v-on:changeData="filterData"
        />

        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload" @click="reloadData"></div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0">
            <thead>
                <tr>
                    <th class="order">STT</th>
                    <th>Mã tour</th>
                    <th>Tên tour</th>
                    <th>Người đặt</th>
                    <th>Ngày khởi hành</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in listTour" v-bind:key="index">
                    <td class="order">{{index+1}}</td>
                    <td>{{item.TourCode}}</td>
                    <td>{{item.TourName}}</td>
                    <td>{{item.UserName}}</td>
                    <td class="time">{{item.StartTime}}</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option" @click="showFormRequest(item.TourID)">Xem yêu cầu</div>
                        </div>
                    </td>
                </tr>
                
            </tbody>
        </table>
    </div>

    <BaseNavigationPage
    :totalPage="totalPage"
    :totalrecord="totalRecord"
    :currentPage="currentPage"
    :listNumberPage="numberPage"
    v-on:choosePage="choosePage"
    v-on:changePageSize="changePageSize"
    />

    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>
    
    <TheRequestTour
    v-if="showForm"
    :oTour="oTour"
    :mode="2"
    :oData="oData"
    :TitleTour="titleForm"
    v-on:closeForm="closeForm"
    />
  </div>
</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheRequestTour from '../../components/form/TheRequestTour.vue'
import Tour from '../../js/entity/tour'
import TourAPI from "../../js/api/tourapi.js"
export default {
    components: { BaseInput, BaseNavigationPage, TheRequestTour, BaseLoad },
    data(){
        return{
            totalRecord : 0,
            totalPage: 1,
            currentPage: 1,
            pageSize : 20,
            numberPage: [
                {value: 1, class: "active"},
                {value: 2, class: ""},
                {value: 3, class: ""},
                {value: 5, class: ""},
            ],

            oTour : new Tour(),

            showForm : false,
            listTour : [],

            showLoad: false,
            searchKey : "",
            oData: null,
            titleForm: "Chỉnh sửa",
        }
    },
    mounted() {
        if (!sessionStorage.getItem("idAdmin")) {
            this.$router.push({ path: '/admin/login'})
            return
        }
    },
    async created(){
        await this.filter("", 20, 0, 0);
    },
    methods:{
        async filter(search, size, page, isStop){
            this.showLoad = true
            await TourAPI.filter(search, size, page, isStop, 2)
            .then(res=>{
                this.listTour = [];
                this.listTour = res.data.data;
                this.totalRecord = res.data.totalRecord;
                this.totalPage = res.data.totalPage;
                this.numberPage = [];
                var me = this;
                if(me.totalPage > 4){
                    me.numberPage = [
                        {value: 1, class: "active"},
                        {value: 2, class: ""},
                        {value: 3, class: ""},
                        {value: this.totalPage, class: ""},
                    ];
                }
                else{
                    for(var i=1; i<= me.totalPage; i++){
                        if(i == 1){
                            me.numberPage.push({
                                value: 1,
                                class: "active"
                            });
                        }
                        else{
                            me.numberPage.push({value:i, class: ""});
                        }
                        
                    }
                }
            })
            .catch(()=>{
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })
            this.showLoad = false;
        },

        toast({ title, type, duration }) {
            const main = document.getElementById("toast");
            if (main) {
                const toast = document.createElement("div");
                //auto remove toast
                const autoRemove = setTimeout(function () {
                main.removeChild(toast);
                }, duration + 1000);

                toast.onclick = function (e) {
                if (e.target.closest(".delete-toast")) {
                    main.removeChild(toast);
                    clearTimeout(autoRemove);
                }
                };
                const delay = (duration / 1000).toFixed(2);
                // const icons = {
                //     success: `'fas', 'check-circle'`,
                //     info: 'fas fa-info-circle',
                //     warning: 'fas fa-exclamation-circle',
                //     error: 'fas fa-exclamation-triangle',

                // }
                toast.classList.add("toast-message");
                toast.style.animation = `slideInLeft ease .5s, fadeOut linear 1s ${delay}s forwards`;
                toast.innerHTML = `
                    <div class="icon-toast icon-toast-${type}" id="icon-toast">
                        
                    </div>
                    <div class="content-toast" id="content-toast">${title}</div>
                    <div class="delete-toast delete-toast-${type}" id="delete-toast">
                        
                    </div>`;
                main.appendChild(toast);
            }
        },
        reloadData(){
            this.filter(this.searchKey, this.pageSize, 0, 0)
        },

        filterData(value){
            this.searchKey = value;
            this.filter(this.searchKey, this.pageSize, 0, 0)
        },

        /**
         * Chọn trang
         * @param {Number} page: trang hiện tại
         * @param {Array} list: danh sách trang
         */
        choosePage(page, list){
            //await this.loadData(p, this.condition);
            this.currentPage = page;
            this.numberPage = list;
            
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, 0)
        },

        /**
         * Thay đổi kích thước trang
         * @param {Number} size: Kích thước trang
         */
        changePageSize(size){
            this.pageSize = size;
            this.currentPage = 1;
            
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, 0)
        },
        /**
         * Show form tạo tour
         */
        async showFormRequest(id){
            this.showLoad = true
            await TourAPI.getByID(id)
            .then(res=>{
                var data = res.data
                var tour = new Tour();
                this.oTour = tour;
                this.oTour.Name = data.Master.TourName
                this.oTour.TourCode = data.Master.ContractCode
                this.oTour.CreatedTime = data.Master.CreatedTime
                this.oTour.TotalAmount = Number.parseInt(data.Master.TotalCost)
                this.oTour.Departure = data.Master.ProvinceDestinationName
                this.oTour.DepartureID = data.Master.ProvinceDestinationID
                this.oTour.StartPoint = data.Master.ProvinceStartName
                this.oTour.StartPointID = data.Master.ProvinceStartID
                this.oTour.PickUpPoint = data.Master.PickupAdress
                this.oTour.NumberAdult = Number.parseInt(data.Contract.NumberAdult)
                this.oTour.NumberChild = Number.parseInt(data.Contract.NumberChild)
                this.oTour.NumberBaby = Number.parseInt(data.Contract.NumberBaby)
                this.oTour.TotalDay = Number.parseInt(data.Contract.TotalHour)

                var pickupTime = new Date(data.Master.PickupTime)
                var startTime = new Date(data.Contract.StartTime)
                var endTime = new Date(data.Contract.EndTime)
                this.oTour.PickUpTime = new Date(pickupTime.setTime(pickupTime.getTime() - (7*60*60*1000)))
                this.oTour.StartTime = new Date(startTime.setTime(startTime.getTime() - (7*60*60*1000)))
                this.oTour.EndTime = new Date(endTime.setTime(endTime.getTime() - (7*60*60*1000)))
                
                this.oTour.Sample = data.Info.Sample
                this.oTour.Status = data.Info.Status
                this.oTour.IsPayment = data.Info.IsPayment
                this.oTour.TourID = data.Info.RefID
                
                data.Schedule.forEach(e=>{
                    e.Morning.forEach(k=>{
                        var time = new Date(k.Time)
                        k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    })

                    e.Afternoon.forEach(k=>{
                        var time = new Date(k.Time)
                        k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    })

                    e.Evening.forEach(k=>{
                        var time = new Date(k.Time)
                        k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    })
                })

                data.AttachOption.forEach(e=>{
                    e.Price = e.Price.toString()
                                    .replace(/\D/g, "")
                                    .replace(/\B(?=(\d{3})+(?!\d))/g, ".")
                })

                this.oData = data
                this.titleForm = "Chỉnh sửa"
                this.showForm = true;
                this.mode = 2;

                this.showLoad = false
            })
            .catch(()=>{
                this.showLoad = false
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })
        },

        closeForm(){
            this.showForm = false;
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, 0)
        },
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>