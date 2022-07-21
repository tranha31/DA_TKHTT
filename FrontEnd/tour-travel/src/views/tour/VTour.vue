<template>
  <div>
    <div class="tour-contain">
        <div class="search">
            <div class="search-main">
                <div class="search-title">
                  <router-link to="/tour" class="link active">Tour &amp; Trải nghiệm</router-link>
                  <router-link to="/test" class="link">Khách sạn</router-link>
                </div>
                <div class="search-content">
                    <BaseInput
                    :clas="'w-half m-r-20'"
                    :placeholder="'Nhập hoạt động'"
                    :hasImage="true"
                    :classImage="'mi-14 icon-search'"
                    />

                    <BaseAutoComplete
                    :clas="'w-30'"
                    :placeholder="'Chọn địa điểm'"
                    :hasImage="true"
                    :classImage="'mi-14 icon-location'"
                    />

                    <div class="flex-1"></div>
                    <div class="btn btn-save m-l-10" style="min-width: 100px">Tìm kiếm</div>
                </div>
            </div>
        </div>
        <div class="grid-content d-flex flex-column">
          <div class="filter mi" :class="showFilter? 'active': ''" title="Lọc dữ liệu" v-title @click="()=>{this.showFilter = !this.showFilter}"></div>
          
          <div v-if="showFilter" class="filter-form d-flex flex-column">
            <div class="title">
              Lọc kết quả
              <div class="icon-close" @click="()=>{this.showFilter = !this.showFilter}">X</div>
            </div>
            <div class="body d-flex flex-column">

              <BaseAutoComplete
              :clas="'w-full'"
              :placeholder="'Điểm khởi hành'"
              :hasTitle="true"
              :title="'Điểm khởi hành'"
              :hasImage="true"
              :classImage="'mi-14 icon-location'"
              />
              <div style="height:20px"></div>

              <BaseAutoComplete
              :clas="'w-full'"
              :placeholder="'Độ dài tour'"
              :hasTitle="true"
              :title="'Thời gian tour'"
              :hasImage="true"
              :classImage="'mi-14 icon-time'"
              />
              <div style="height:20px"></div>
              <label for="price-range" style="font-weight:600">Mức giá: {{priceRange}}tr</label>
              <input type="range" id="price-range" name="price-range" min="0" max="100" v-model="priceRange">


            </div>
            <div class="flex-1"></div>
            <div class="function d-flex">
              <div class="flex-1"></div>
              <div class="btn">Mặc định</div>
              <div class="btn btn-save">Lọc</div>
            </div>
          </div>
          
          <div v-for="(v, index) in contents" v-bind:key="index" class="grid-item d-flex">
            <div class="item-image w-40" :style="v.imageUrl"></div>
            <div class="item-info d-flex flex-column w-60">
              <router-link class="item-title" :to="{ name: 'tour-infor', params: { id: v.id }}" >{{v.title}}</router-link>
              <div class="item-code">Mã tour: <b>{{v.code}}</b></div>
              <div class="d-flex">
                <div v-for="(o, i) in v.otherInfo" v-bind:key="i" class="option">{{o}}</div>
              </div>
              <div class="item-price d-flex">
                <div class="flex-1"></div>
                <div class="price">{{v.price}}</div>
              </div>
              <div class="flex-1"></div>
              <div class="item-action d-flex">
                <div class="item-action-info">{{v.numberBuy}} nguoi da mua</div>
                <div class="flex-1"></div>
                <div class="btn btn-save" @click="showFormCreateTour">Mua ngay</div>
              </div>
            </div>
          </div>
          <div class="grid-item" style="height: 100px; border: unset; padding:0">
            <BaseNavigationPage
            :totalPage="totalPage"
            :totalrecord="totalRecord"
            :currentPage="currentPage"
            :listNumberPage="numberPage"
            v-on:choosePage="choosePage"
            v-on:changePageSize="changePageSize"
            />
          </div>
          
        </div>
      <ChatBox />
    </div>

    <TheCreateTour v-if="showForm"
    v-on:closeForm="closeForm"
    />

    <ThePageInfo/>
  </div>
  
</template>

<script>
import BaseAutoComplete from '../../components/base/BaseAutoComplete.vue'
import BaseInput from '../../components/base/BaseInput.vue'
import ThePageInfo from '../../components/layout/ThePageInfo.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheCreateTour from '../../components/form/TheCreateTour.vue'
import ChatBox from "@/components/base/ChatBox";
export default {
  components: { ThePageInfo, BaseInput, BaseAutoComplete, BaseNavigationPage, TheCreateTour, ChatBox },
  data(){
    return{
      showFilter: false,
      priceRange: 8,
      showForm: false,
      contents: [
        {
          id: '12113',
          imageUrl: "background-image: url('https://booking-static.vinpearl.com/tours/b018892921a94fa0b344a28fc2db0a99_DGH_2236_summer2.jpg')",
          title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
          code: "1111",
          otherInfo: ["3N2D", "Test"],
          price: "8.000.000đ",
          numberBuy: 17
        },
        {
          id: '545454',
          imageUrl: "background-image: url('https://booking-static.vinpearl.com/tours/b018892921a94fa0b344a28fc2db0a99_DGH_2236_summer2.jpg')",
          title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
          code: "1111",
          otherInfo: ["3N2D", "Test"],
          price: "8.000.000đ",
          numberBuy: 17
        },
        {
          id: '45545',
          imageUrl: "background-image: url('https://booking-static.vinpearl.com/tours/b018892921a94fa0b344a28fc2db0a99_DGH_2236_summer2.jpg')",
          title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
          code: "1111",
          otherInfo: ["3N2D", "Test"],
          price: "8.000.000đ",
          numberBuy: 17
        }
      ],

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
    showFormCreateTour(){
      this.showForm = true;
    },

    closeForm(){
      this.showForm = false;
    },
  }
}
</script>

<style>
@import url(../../css/content/tour.css);

.tour-contain .e-autocomplete{
  padding-left: 25px !important;
}

</style>