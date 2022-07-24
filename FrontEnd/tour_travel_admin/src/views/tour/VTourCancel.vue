<template>
  <div class="list-template">
    <div class="header d-flex">
        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload" @click="reloadData"></div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0" id="gridTourOrder">
            <thead>
                <tr>
                    <th>Mã tour</th>
                    <th>Tên tour</th>
                    <th>Người đặt</th>
                    <th>Số điện thoại</th>
                    <th>Thời gian hủy</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in listTour" v-bind:key="index">
                    <td>{{item.TourCode}}</td>
                    <td>{{item.TourName}}</td>
                    <td>{{item.Name}}</td>
                    <td>{{item.PhoneNumber}}</td>
                    <td>{{item.TimeCancel}}</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option" @click="viewContract(item.TourID)">Xem hợp đồng</div>
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

  </div>
</template>

<script>
import BaseLoad from '../../components/base/BaseLoad.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TourAPI from "../../js/api/tourapi.js"
export default {
    components: { BaseNavigationPage, BaseLoad },
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
        await this.filter(20, 0);
    },
    methods:{
        async filter(size, page){
            this.showLoad = true
            await TourAPI.getListCancel(size, page)
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
            this.filter(this.pageSize, 0)
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
            
            this.filter(this.pageSize, this.currentPage-1)
        },

        /**
         * Thay đổi kích thước trang
         * @param {Number} size: Kích thước trang
         */
        changePageSize(size){
            this.pageSize = size;
            this.currentPage = 1;
            
            this.filter(this.pageSize, this.currentPage-1)
        },

        viewContract(id){
            window.open("http://127.0.0.1:5000/tour/gettourtemp?id="+id)
        },

        
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>