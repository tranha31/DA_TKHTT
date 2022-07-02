<template>
  <div class="list-template">
    <div class="header d-flex">
        <BaseInput
        :hasTitle="false"
        :msrequire="false"
        :notNull="false"
        :placeholder="'Nhập mã phòng, mã khách sạn để tìm kiếm'"
        :clas="'w-30'"
        />

        <div class="cancel-multi" @click="showFormCancelMulti">Hủy hàng loạt</div>

        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload"></div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0" id="gridTourOrder">
            <thead>
                <tr>
                    <th class="order">
                        <input type="checkbox" @change="selectedItem($event)"/>
                    </th>
                    <th>Mã đơn hàng</th>
                    <th>Mã khách sạn</th>
                    <th>Số lượng</th>
                    <th>Số phòng</th>
                    <th>Tổng tiền</th>
                    <th>Mã phòng</th>
                    <th>Thời gian giữ phòng</th>
                    <th>Tên người đặt</th>
                    <th>Loại phòng</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in 100" v-bind:key="index">
                    <td class="order">
                        <input type="checkbox"/>
                    </td>
                    <td >SP001</td>
                    <td >KS001</td>
                    <td >2</td>
                    <td >5</td>
                    <td >8.000.000</td>
                    <td>P002</td>
                    <td class="time">20/06/2022</td>
                    <td>TQHA</td>
                    <td>Vip</td>
                    <td class="function" >
                        <div class="d-flex flex-column lst-option">
                            <div class="option" @click="showFormCancelSingle">Hủy phòng</div>
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

  </div>
</template>

<script>
import BaseInput from '../components/base/BaseInput.vue'
import BaseNavigationPage from '../components/base/BaseNavigationPage.vue'
import TheCancel from '../components/form/TheCancel.vue'
import TheCancelMulti from '../components/form/TheCancelMulti.vue'
export default {
    components: { BaseInput, BaseNavigationPage, TheCancel, TheCancelMulti },
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
            showSingleCancel : false,
            showMultiCancel: false,
        }
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

        /**
         * Show form tạo tour
         */
        showFormCancelSingle(){
            this.showSingleCancel = true;
        },

        closeSingleCancel(){
            this.showSingleCancel = false;
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
@import url(../css/content/tourtemplate.css);
@import url(../css/common/table.css);
</style>