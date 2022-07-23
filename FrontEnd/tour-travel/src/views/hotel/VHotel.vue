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
                :clas="'w-half'"
                placeholder="Nhập tên khách sạn"
                :hasImage="true"
                :classImage="'mi-14 icon-search'"
            />
            <BaseInput
                :clas="'w-half'"
                placeholder="Ngày nhận phòng"
            />
            <BaseInput
                :clas="'w-half'"
                placeholder="Ngày trả phòng"
            />
            <BaseInput
                :clas="'w-half'"
                placeholder="Số phòng"
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
                placeholder="Dịch vụ"
                :hasTitle="true"
                title="Dịch vụ"
                :hasImage="true"
                :classImage="'mi-14 icon-location'"
            />
            <div style="height:20px"></div>

            <BaseAutoComplete
                :clas="'w-full'"
                placeholder="Loại hình lưu trú"
                :hasTitle="true"
                title="Loại hình lưu trú"
                :hasImage="true"
                :classImage="'mi-14 icon-time'"
            />
            <div style="height:20px"></div>
            <label for="price-range" style="font-weight:600">Khoảng giá (VNĐ)</label>
            <input type="range" id="price-range" name="price-range" min="0" max="100" v-model="priceRange">
            <div class="price-range-number d-flex">
              <h3>0</h3>
              <h3>100tr</h3>
            </div>
          </div>
        </div>
        <div v-for="(content, index) in contents" v-bind:key="index" class="grid-item d-flex">
          <div class="item-image w-40" :style="content.imageUrl"></div>
          <div class="item-info d-flex flex-column w-60">
            <label style="font-size: 24px;">{{content.Name}}</label>
            <div class="item-code">{{content.Address}}</div>
            <div class="flex-1"></div>
            <div class="d-flex more-info">
              <div v-for="(o, i) in content.SortDescribed" v-bind:key="i" class="more">{{o}}</div>
            </div>
            <div class="flex-1"></div>
            <div class="item-price d-flex">
              <div>
                <div class="icon rate-icon d-flex" v-for="index in content.Rank" :key="index"></div>
              </div>
              <div class="flex-1"></div>
              <div>Chỉ từ</div>
              <div class="price">{{content.price}}</div>
              <div>phòng/đêm</div>
            </div>
            <div class="flex-1"></div>
            <div class="item-action d-flex">
              <div class="show-detail" @click="directToDetailHotel(content.HotelID)">Xem chi tiết</div>
              <div class="flex-1"></div>
              <div class="btn btn-save" @click="showFormOrderHotel">Đặt ngay</div>
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
    <ThePageInfo/>
  </div>

</template>

<script>
import BaseAutoComplete from '../../components/base/BaseAutoComplete.vue'
import BaseInput from '../../components/base/BaseInput.vue'
import ThePageInfo from '../../components/layout/ThePageInfo.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import InfotypeApi from "@/js/api/InfotypeApi"
import ChatBox from "@/components/base/ChatBox";

export default {
  name: 'VHotel',
  components: { ThePageInfo, BaseInput, BaseAutoComplete, BaseNavigationPage, ChatBox },
  data(){
    return{
      showFilter: false,
      priceRange: 50,
      contents: [],
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
    showFormOrderHotel(){
    },

    closeForm(){
      this.showForm = false;
    },
    directToDetailHotel(idHotel) {
      this.$router.push({ path: `/hotel/${idHotel}`})
    }
  },
  async created() {
    this.contents = await InfotypeApi.getAllHotels()
    this.contents = this.contents.slice(0, 3)
    this.contents.forEach(hotel => {
      hotel.price = '8.000.000đ'
      hotel.imageUrl = "background-image: url('https://booking-static.vinpearl.com/tours/b018892921a94fa0b344a28fc2db0a99_DGH_2236_summer2.jpg')"

      let otherInfos = JSON.parse(JSON.stringify(hotel.SortDescribed))
      hotel.SortDescribed = []
      otherInfos = otherInfos.replace('{', '').replace('}', '').split(', ')
      otherInfos.forEach(info => {
        hotel.SortDescribed.push(info.split(':')[1].trim())
      })
    })
  }
}
</script>

<style scoped>
@import url(../../css/content/tour.css);

.tour-contain .e-autocomplete{
  padding-left: 25px !important;
}

.price-range-number {
  justify-content: space-between;
}

.search-main {
  width: 90%;
}

.more-info {
  justify-content: space-around;
}

.more {
  padding: 10px;
  background-color: #ffffff;
  text-align: center;
  border-radius: 5px;
  border: solid 1px #e89327;
  color: #e89327;
}

.item-price {
  align-items: baseline;
}

.rate-icon {
  background-size: contain;
  background-repeat: no-repeat;
  background-image: url(../../assets/imgs/Image/star.png);
  width: 25px;
  height: 25px;
  display: inline-block;
}
</style>