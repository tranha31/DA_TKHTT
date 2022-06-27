<template>
  <div class="list-template">
    <div class="header d-flex">
        <BaseInput
        :hasTitle="false"
        :msrequire="false"
        :notNull="false"
        :placeholder="'Nhập tên, địa điểm để tìm kiếm'"
        :clas="'w-30'"
        />

        <div class="flex-1"></div>
        <div class="option-button d-flex">
            <div class="reload"></div>
            <div class="btn" @click="showFormPlace">Thêm mới</div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0">
            <thead>
                <tr>
                    <th class="order">STT</th>
                    <th>Tên địa điểm</th>
                    <th>Vị trí</th>
                    <th>Tỉnh</th>
                    <th>Huyện</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in 100" v-bind:key="index">
                    <td class="order">1</td>
                    <td>Chùa Bái Đính</td>
                    <td>Gia Viễn, Ninh Bình</td>
                    <td>Ninh Bình</td>
                    <td>Gia Viễn</td>
                    <td class="function">
                        <div class="d-flex flex-column lst-option">
                            <div class="option">Xem</div>
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

    <ThePlaceForm
    v-if="showForm"
    v-on:closeForm="closeForm"
    />
  </div>
</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import ThePlaceForm from '../../components/form/ThePlaceForm.vue'
export default {
    components: { BaseInput, BaseNavigationPage, ThePlaceForm },
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

            showForm:  false,
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

        /**
         * Show form tạo tour
         */
        showFormPlace(){
            this.showForm = true;
        },

        closeForm(){
            this.showForm = false;
        },
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>