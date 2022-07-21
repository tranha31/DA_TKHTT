<template>
  <div class="list-template">
    <div class="header d-flex">
        <BaseInput
        :hasTitle="false"
        :msrequire="false"
        :notNull="false"
        :placeholder="'Nhập tên, địa điểm để tìm kiếm'"
        :clas="'w-30'"
        :content="searchKey"
        v-on:changeData="filterData"
        />

        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload" @click="reloadData"></div>
            <div class="btn" @click="showFormPlace">Thêm mới</div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0">
            <thead>
                <tr>
                    <th class="order">STT</th>
                    <th>Tên điểm du lịch</th>
                    <th>Địa chỉ</th>
                    <th>Tỉnh</th>
                    <th>Huyện</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in lstDestination" v-bind:key="index">
                    <td class="order">{{index + 1}}</td>
                    <td>{{item.Name}}</td>
                    <td>{{item.Place}}</td>
                    <td>{{item.ProvinceName}}</td>
                    <td>{{item.DistrictName}}</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option" @click="editRecord(item.RefID, 2)">Xem</div>
                            <div class="option" @click="editRecord(item.RefID, 1)">Sửa</div>
                            <div class="option" @click="deleteRecord(item.RefID)">Xóa</div>
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

    <ThePlaceForm
    v-if="showForm"
    :destination="oDestinationDetail"
    :listImage="listImage"
    :modeTemplate="modeTemplate"
    :title="title"
    :disabled="disabled"
    :isView="isView"
    v-on:closeForm="closeForm"
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
        v-on:confirmAction3="()=>{this.showPopUp = false;}"
      />
  </div>
</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import ThePlaceForm from '../../components/form/ThePlaceForm.vue'
import Destination from '../../js/entity/destination'
import DestinationAPI from '../../js/api/destinationapi'
import BaseLoad from '../../components/base/BaseLoad.vue'
import BasePopUp from '../../components/base/BasePopUp.vue'
export default {
    components: { BaseInput, BaseNavigationPage, ThePlaceForm, BaseLoad, BasePopUp },
    data(){
        return{
            totalRecord : 500,
            totalPage: 5,
            currentPage: 1,
            pageSize : 20,
            numberPage: [
                {value: 1, class: "active"},
                {value: 2, class: ""},
                {value: 3, class: ""},
                {value: 5, class: ""},
            ],
            searchKey : "",
            showForm:  false,
            oDestinationDetail : new Destination(),
            listImage : [],
            modeTemplate : 0,
            title : "Thêm mới",
            lstDestination : [],
            showLoad : false,

            showPopUp : false,
            type: "error",
            message: null,
            titleP: null,
            action1: "Hủy",
            action2 : "Đóng",
            action3 : "Lưu",
            optionPopUp : [false, false],

            disabled: false,
            isView : false,
        }
    },
    async created(){
        await this.filter("", 20, 0);
    },
    methods:{
        async filter(search, size, page){
            this.showLoad = true
            await DestinationAPI.getAll(search, size, page)
            .then(res=>{
                this.lstDestination = [];
                this.lstDestination = res.data.data;
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
        /**
         * Chọn trang
         * @param {Number} page: trang hiện tại
         * @param {Array} list: danh sách trang
         */
        choosePage(page, list){
            //await this.loadData(p, this.condition);
            this.currentPage = page;
            this.numberPage = list;
            
            this.filter(this.searchKey, this.pageSize, this.currentPage-1)
        },

        /**
         * Thay đổi kích thước trang
         * @param {Number} size: Kích thước trang
         */
        changePageSize(size){
            this.pageSize = size;
            this.currentPage = 1;
            
            this.filter(this.searchKey, this.pageSize, this.currentPage-1)
        },

        /**
         * Show form tạo tour
         */
        showFormPlace(){
            this.showForm = true;
            var oDestination = new Destination();
            this.oDestinationDetail = oDestination;
            this.oDestinationDetail.id = this.uuidv4();
            this.listImage = [];
            this.modeTemplate = 0;
            this.title = "Thêm mới";
            this.disabled = false;
            this.isView = false;
        },

        closeForm(){
            this.showForm = false;
            this.filter(this.searchKey, this.pageSize, 0)
        },

        reloadData(){
            this.filter(this.searchKey, this.pageSize, 0)
        },

        filterData(value){
            this.searchKey = value;
            this.filter(this.searchKey, this.pageSize, 0)
        },

        async deleteRecord(id){
            await DestinationAPI.delete(id)
            .then(res=>{
                if(res.data.error == "ExistReperence"){
                    this.showPopUp = true;
                    this.titleP = "Cảnh báo";
                    this.message = "Địa điểm đã được sử dụng. Bạn không thể xóa.";
                }
                else{
                    this.filter(this.searchKey, this.pageSize, this.currentPage - 1)
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

        async editRecord(id, modeTemplate){
            await DestinationAPI.getByID(id)
            .then(res=>{
                var data = res.data.data[0]
                
                var oDestination = new Destination();
                var ticketPrice = JSON.parse(data.TicketPrice)
                oDestination.id = data.RefID;
                oDestination.name = data.Name;
                oDestination.address = data.Place;
                oDestination.pronvinceName = data.ProvinceName;
                oDestination.districtName = data.DistrictName;
                oDestination.describled = data.Described;
                oDestination.adultPrice = ticketPrice.Adult;
                oDestination.childPrice = ticketPrice.Child;
                oDestination.babyPrice = ticketPrice.Baby;
                oDestination.provinceID = data.ProvinceID;
                oDestination.districtID = data.DistrictID;
                oDestination.used = data.IsUsed;

                this.oDestinationDetail = oDestination;
                var lstImage = this.listImage
                this.listImage = [];
                this.modeTemplate = modeTemplate;

                lstImage = res.data.image;
                this.listImage = lstImage;

                if(oDestination.used == 1){
                    this.disabled = true;
                }
                else{
                    this.disabled = false;
                }
                if(this.modeTemplate == 2){
                    this.isView = true;
                    this.title = "Xem";
                    this.disabled = true;
                }
                else{
                    this.isView = false;
                    this.title = "Chỉnh sửa";
                }
                this.showForm = true;
            })
        },

        uuidv4() {
            return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
                (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
            );
        }
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>