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
            <div class="btn" @click="showFormHotel">Thêm mới</div>
        </div>
    </div>

    <div class="grid-detail">
        <table class="tabel-detail" cellspacing="0">
            <thead>
                <tr>
                    <th class="order">STT</th>
                    <th>Mã khách sạn</th>
                    <th>Tên khách sạn</th>
                    <th>Vị trí</th>
                    <th>Số điện thoại</th>
                    <th>Email</th>
                    <th>Số lượng phòng</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in loadedHotelDatas" v-bind:key="index">
                    <td class="order">{{Number(index) + 1}}</td>
                    <td>{{item.HotelCode}}</td>
                    <td>{{item.Name}}</td>
                    <td>{{item.Address}}</td>
                    <td>{{item.PhoneNumber}}</td>
                    <td>{{item.Email}}</td>
                    <td class="number">50</td>
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

    <TheHotelForm
    v-if="showForm"
    v-on:closeForm="closeForm"
    @response-action="handleAfterSaveNewHotel($event)"
    />
  </div>
</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheHotelForm from '../../components/form/TheHotelForm.vue'
import HotelAPI from '../../js/api/hotel'
export default {
    components: { BaseInput, BaseNavigationPage, TheHotelForm },
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
            loadedHotelDatas: []
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
        showFormHotel(){
            this.showForm = true;
        },

        closeForm(){
            this.showForm = false;
        },
        async initData() {
          const hotelResponse = await HotelAPI.getAll()
          this.loadedHotelDatas = hotelResponse.data
        },
        handleAfterSaveNewHotel(val) {
          this.showForm = false;
          if (val === 'Insert New Hotel Success!') {
            this.$notify({
              group: 'default',
              title: 'Success',
              text: val,
              duration: 3000,
              type: 'success',
              position: 'bottom right'
            })
          } else {
            this.$notify({
              group: 'default',
              title: 'Error',
              text: 'Error occur when insert new hotel',
              duration: 3000,
              type: 'error',
              position: 'bottom right'
            })
          }
        }
    },
    async mounted() {
        if (!sessionStorage.getItem("idAdmin")) {
            this.$router.push({ path: '/admin/login'})
            return
        }
        else{
            await this.initData()
        }
      
    }
  
}
</script>

<style>
@import url(../../css/content/tourtemplate.css);
@import url(../../css/common/table.css);
</style>