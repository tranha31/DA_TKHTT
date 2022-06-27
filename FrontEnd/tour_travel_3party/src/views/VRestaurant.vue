<template>
  <div class="list-template">
    <div class="header d-flex">
        <BaseInput
        :hasTitle="false"
        :msrequire="false"
        :notNull="false"
        :placeholder="'Nhập mã khách sạn, tên khách sạn để tìm kiếm'"
        :clas="'w-30'"
        />


        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload"></div>
            <div class="btn" @click="showFormRestaurant">Thêm mới</div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0" id="gridTourOrder">
            <thead>
                <tr>
                    <th class="order">
                        STT
                    </th>
                    <th>Mã khách sạn</th>
                    <th>Mã nhà hàng</th>
                    <th>Tên nhà hàng</th>
                    <th>Loại đồ ăn</th>
                    <th>Giờ mở cửa</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in 100" v-bind:key="index">
                    <td class="order">
                        1
                    </td>
                    <td>K001</td>
                    <td>NH001</td>
                    <td>Nhà hàng hải sản</td>
                    <td>Buffet</td>
                    <td class="time">8:00</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option">Sửa</div>
                            <div class="option">Xóa</div>
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

    <TheRestaurantForm
    v-if="showForm"
    v-on:closeForm="closeForm"
    />
  </div>
</template>

<script>
import BaseInput from '../components/base/BaseInput.vue'
import BaseNavigationPage from '../components/base/BaseNavigationPage.vue'
import TheRestaurantForm from '../components/form/TheRestaurantForm.vue'
export default {
    components: { BaseInput, BaseNavigationPage, TheRestaurantForm},
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
            showForm : true,
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
        showFormRestaurant(){
            this.showForm = true;
        },

        closeForm(){
            this.showForm = false;
        },
    }
  
}
</script>

<style>
@import url(../css/content/tourtemplate.css);
@import url(../css/common/table.css);
</style>