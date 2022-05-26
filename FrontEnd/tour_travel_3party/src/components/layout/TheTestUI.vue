<template>
  <div>
        <BaseLoad
        :load="loading"
        />

        <BasePopUp
        :isShow="showPopUp"
        :type="type"
        :message="message"
        :title="title"
        :action1="action1"
        :action2="action2"
        :action3="action3"
        :show="optionPopUp"
         />

        <date-picker v-model="time1" type="date" range placeholder="Select date range" format='DD-MM-YYYY'></date-picker>
        

        <BaseNavigationPage
        :totalPage="totalPage"
        :totalrecord="totalRecord"
        :currentPage="currentPage"
        :listNumberPage="numberPage"
        v-on:choosePage="choosePage"
        v-on:changePageSize="changePageSize"
        />

        <BaseInput
        :clas="'w-half'"
        :msrequire="true"
        :hasTitle="true"
        :title="'Mã nhà cung cấp'"
        :notNull="true"
        :content="contentInput"
        :read="read"
        :isNumber="true"
        v-on:changeData="(value)=>{this.contentInput = value;}"
        />

        <BaseAutoComplete
        :clas="'w-half'"
        :msrequire="true"
        :hasTitle="true"
        :title="'Mã nhà cung cấp'"
        :notNull="true"
        :dataFields="dataFields"
        :dataItem="dataItem"
        :content="contentCBB"
        v-on:returnValue="(value)=>{this.contentCBB = value}"
        />
        
        <div id="toast"></div>
  </div>
</template>

<script>
import BaseLoad from '../base/BaseLoad.vue'
import BasePopUp from '../base/BasePopUp.vue'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import BaseNavigationPage from '../base/BaseNavigationPage.vue';
import BaseInput from '../base/BaseInput.vue';
import BaseAutoComplete from '../base/BaseAutoComplete.vue';

export default {
  components: {BasePopUp, BaseLoad, DatePicker, BaseNavigationPage, BaseInput, BaseAutoComplete },

    data(){
        return{
            time1 : null,
            loading: false,
            showPopUp : false,
            type: "error",
            message: null,
            title: null,
            action1: "Hủy",
            action2 : "Đóng",
            action3 : "Lưu",
            optionPopUp : [false, false],

            dataItem:[
                {Id: "1", Game: "Football"},
                {Id: "2", Game: "Basketball"}
            ],
            dataFields: {value: "Game"},
            contentCBB: "Tesst",
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

            read: false,
            contentInput : "555",
        }
    },
    created(){
        
    },
    methods:{
        /**
         * Chọn trang
         * @param {Number} page: trang hiện tại
         * @param {Array} list: danh sách trang
         */
        choosePage(page, list){
            //await this.loadData(p, this.condition);
            this.currentPage = page;
            this.numberPage = list;
            
            this.toast({
                title: "Test toast message",
                type: "error",
                duration: 3000,
            });
        },

        /**
         * Thay đổi kích thước trang
         * @param {Number} size: Kích thước trang
         */
        changePageSize(size){
            this.pageSize = size;
            this.currentPage = 1;
            
            //await this.loadData(p, this.condition);
        },

        /**
         * Khởi tạo toast
         */
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
    }
}
</script>

<style>

</style>