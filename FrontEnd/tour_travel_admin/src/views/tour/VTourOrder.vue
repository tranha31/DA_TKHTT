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

        <!-- <div class="cancel-multi" @click="showFormCancelMulti">Hủy hàng loạt</div> -->

        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload" @click="reloadData"></div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0" id="gridTourOrder">
            <thead>
                <tr>
                    <!-- <th class="order">
                        <input type="checkbox" @change="selectedItem($event)"/>
                    </th> -->
                    <th>Mã tour</th>
                    <th>Tên tour</th>
                    <th>Người đặt</th>
                    <th>Ngày khởi hành</th>
                    <th>Trạng thái thanh toán</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in listTour" v-bind:key="index">
                    <!-- <td class="order">
                        <input type="checkbox"/>
                    </td> -->
                    <td>{{item.TourCode}}</td>
                    <td>{{item.TourName}}</td>
                    <td>{{item.UserName}}</td>
                    <td class="time">{{item.StartTime}}</td>
                    <td>{{item.IsPayment}}</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option" @click="viewContract(item.TourID)">Xem hợp đồng</div>
                            <div v-if="item.Status != 3" class="option" @click="closeSingleCancel(item.TourID)">Hủy tour</div>
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

    <TheCancel
    v-if="showSingleCancel"
    :title="'Gửi thông báo hủy tour'"
    v-on:closeForm="closeSingleCancel"
    />

    <TheCancelMulti
    v-if="showMultiCancel"
    :title="'Gửi thông báo hủy tour'"
    v-on:closeForm="closeMultiCancel"
    />

    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>

  </div>
</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheCancel from '../../components/form/TheCancel.vue'
import TheCancelMulti from '../../components/form/TheCancelMulti.vue'
import TourAPI from "../../js/api/tourapi.js"
export default {
    components: { BaseInput, BaseNavigationPage, TheCancel, TheCancelMulti, BaseLoad },
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
            showSingleCancel : false,
            showMultiCancel: false,

            showLoad: false,
            searchKey : "",
            listTour : [],
        }
    },
    mounted() {
        if (!sessionStorage.getItem("idAdmin")) {
            this.$router.push({ path: '/admin/login'})
            return
        }
    },
    async created(){
        await this.filter("", 20, 0);
    },
    methods:{
        async filter(search, size, page){
            this.showLoad = true
            await TourAPI.filter(search, size, page, 0, 3)
            .then(res=>{
                this.listTour = [];
                this.listTour = res.data.data;
                this.listTour.forEach(e=>{
                    if(e.IsPayment){
                        e.IsPayment = "Đã thanh toán"
                    }
                    else{
                        e.IsPayment = "Chưa thanh toán"
                    }
                })
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
            this.filter(this.searchKey, this.pageSize, 0)
        },

        filterData(value){
            this.searchKey = value;
            this.filter(this.searchKey, this.pageSize, 0)
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

        selectedItem(e){
            var td = document.querySelectorAll("#gridTourOrder tbody input[type=checkbox]")
            if(e.target.checked){
                td.forEach(t=>{
                    t.setAttribute("checked", "checked");
                })
            }
            else{
                td.forEach(t=>{
                    t.removeAttribute("checked");
                })
            }
        },

        viewContract(id){
            window.open("http://127.0.0.1:5000/tour/gettourtemp?id="+id)
        },

        /**
         * Show form tạo tour
         */
        showFormCancelSingle(){
            this.showSingleCancel = true;
        },

        async closeSingleCancel(id){
            this.showLoad = true
            await TourAPI.cancelTour(id)
            .then(()=>{
                this.filter(this.searchKey, this.pageSize, this.currentPage-1)
            })
            .catch(()=>{
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })
            this.showLoad = false
        },

        showFormCancelMulti(){
            this.showMultiCancel = true;
        },

        closeMultiCancel(){
            this.showMultiCancel = false;
        }
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>