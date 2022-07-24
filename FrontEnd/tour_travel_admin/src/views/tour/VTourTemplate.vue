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

        <input type="checkbox" id="checkBoxFilterNotUse" @change="loadDataForEventNotUse"/>
        <label>Không hiển thị tour Tạm ngừng sử dụng</label>

        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload" @click="reloadData"></div>
            <div class="btn" @click="showFormCreateTour">Thêm mới</div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0">
            <thead>
                <tr>
                    <th class="order">STT</th>
                    <th>Trạng thái</th>
                    <th>Mã tour</th>
                    <th>Tên tour</th>
                    <th>Thời gian tạo tour</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in listTour" v-bind:key="index">
                    <td class="order">{{index+1}}</td>
                    <td>{{item.Status}}</td>
                    <td>{{item.TourCode}}</td>
                    <td>{{item.TourName}}</td>
                    <td class="time">{{item.StartTime}}</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option" @click="showContract(item.TourID)">Xem</div>
                            <div class="option" @click="editTour(item.TourID)">Sửa</div>
                            <div v-if="item.Status == 'Đang sử dụng'" class="option" @click="updateStatusTemplate(item.TourID, 0)">Tạm ngừng</div>
                            <div v-else class="option" @click="updateStatusTemplate(item.TourID, 1)">Sử dụng</div>
                            <div class="option" @click="deleteTemplate(item.TourID)">Xóa</div>
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

    <TheCreateTour
    v-if="showForm"
    :oTour="oTour"
    :mode="mode"
    :oData="oData"
    :TitleTour="titleForm"
    v-on:closeForm="closeForm"
    ref="tourtemplate"
    />

    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>

    <BasePopUp
    :isShow="showPopUp"
        :type="type"
        :message="message"
        :title="titleP"
        :action1="action1"
        :action2="action2"
        :action3="action3"
        :show="optionPopUp"
        v-on:confirmAction="confirmDelete"
        v-on:cancelAction="()=>{this.showPopUp = false; this.idDelete = ''}"
        v-on:confirmAction3="()=>{this.showPopUp = false;}"
    />
  </div>

</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import BasePopUp from '../../components/base/BasePopUp.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheCreateTour from '../../components/form/TheCreateTour.vue'
import Tour from '../../js/entity/tour'
import TourAPI from "../../js/api/tourapi.js"

export default {
    components: { BaseInput, BaseNavigationPage, TheCreateTour, BaseLoad, BasePopUp},
    data(){
        return{
            totalRecord : 0,
            totalPage: 0,
            currentPage: 1,
            pageSize : 20,
            numberPage: [
                {value: 1, class: "active"},
                {value: 2, class: ""},
                {value: 3, class: ""},
                {value: 5, class: ""},
            ],

            listTour : [],

            showForm : false,
            oTour : new Tour(),
            mode : 1,

            showLoad: false,
            searchKey : "",

            showPopUp : false,
            type: "error",
            message: null,
            titleP: null,
            action1: "Hủy",
            action2 : "Đóng",
            action3 : "Xóa",
            optionPopUp : [true, false],

            idDelete: "",
            oData: null,
            titleForm: "Thêm mới",
        }
    },
    async created(){
        await this.filter("", 20, 0, 0);
    },
    methods:{
        async filter(search, size, page, isStop){
            this.showLoad = true
            await TourAPI.filter(search, size, page, isStop, 1)
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
            var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
            var isStop = 0;
            if(checkNotUse){
                isStop = 1;
            }
            this.filter(this.searchKey, this.pageSize, 0, isStop)
        },

        filterData(value){
            this.searchKey = value;
            var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
            var isStop = 0;
            if(checkNotUse){
                isStop = 1;
            }
            this.filter(this.searchKey, this.pageSize, 0, isStop)
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
            
            var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
            var isStop = 0;
            if(checkNotUse){
                isStop = 1;
            }
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, isStop)
        },

        /**
         * Thay đổi kích thước trang
         * @param {Number} size: Kích thước trang
         */
        changePageSize(size){
            this.pageSize = size;
            this.currentPage = 1;
            
            var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
            var isStop = 0;
            if(checkNotUse){
                isStop = 1;
            }
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, isStop)
        },

        loadDataForEventNotUse(){
            var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
            var isStop = 0;
            if(checkNotUse){
                isStop = 1;
            }
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, isStop)
        },

        deleteTemplate(id){
            this.idDelete = id;
            this.showPopUp = true;
            this.type = "warning";
            var tourCocde = this.listTour.filter(e=>e.TourID == id)[0].TourCode
            this.message = "Bạn có chắc chắn muốn xóa tour " + tourCocde + " không?"
            this.optionPopUp = [true, false]
        },

        async confirmDelete(){
            this.showPopUp = false;
            var id = this.idDelete
            await TourAPI.deleteTemplate(id)
            .then(res=>{
                if(res.data.error == "ExistInCart"){
                    this.showPopUp = true;
                    this.type = "warning";
                    this.message = "Tour đã có người dùng thêm vào giỏ hàng. Không thể xóa."
                    this.optionPopUp = [false, false]
                    this.idDelete = ""
                }
                else{
                    var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
                    var isStop = 0;
                    if(checkNotUse){
                        isStop = 1;
                    }
                    this.filter(this.searchKey, this.pageSize, this.currentPage-1, isStop)
                }
                
            })
            .catch(()=>{
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })
        },

        async updateStatusTemplate(id, status){
            await TourAPI.updateStatusTemplate(id, status)
            .then(()=>{
                var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
                var isStop = 0;
                if(checkNotUse){
                    isStop = 1;
                }
                this.filter(this.searchKey, this.pageSize, this.currentPage-1, isStop)
            })
            .catch(()=>{
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })
        },

        showContract(id){
            window.open("http://127.0.0.1:5000/tour/gettourtemp?id="+id)
        },

        /**
         * Show form tạo tour
         */
        showFormCreateTour(){
            var tour = new Tour();
            this.oTour = tour;
            this.oTour.Sample = 1
            this.oTour.Status = 1
            this.oTour.IsPayment = 0
            this.oTour.TourID = null
            this.mode = 1;
            this.oData = null
            this.titleForm = "Thêm mới"
            this.showForm = true;
            
        },

        closeForm(){
            this.showForm = false;
            var checkNotUse = document.getElementById("checkBoxFilterNotUse").checked;
            var isStop = 0;
            if(checkNotUse){
                isStop = 1;
            }
            this.filter(this.searchKey, this.pageSize, this.currentPage-1, isStop)
        },

        async editTour(id){
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
            
            
        }
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>