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
                    :content="search"
                    v-on:changeData="(value)=>{this.search = value}"
                    />

                    <BaseAutoComplete
                    :clas="'w-30'"
                    :placeholder="'Chọn tỉnh muốn du lịch'"
                    :hasImage="true"
                    :classImage="'mi-14 icon-location'"
                    :content="toName"
                    :dataFields="dataProvinceField"
                    :dataItem="lstProvince"
                    v-on:returnValue="chooseDestinationPoint"
                    />

                    <div class="flex-1"></div>
                    <div class="btn btn-save m-l-10" style="min-width: 100px" @click="filterData">Tìm kiếm</div>
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
              :content="fromName"
              :dataFields="dataProvinceField"
              :dataItem="lstProvince"
              v-on:returnValue="chooseStartPoint"
              />
              <div style="height:20px"></div>
              <BaseInput
              :clas="'w-full'"
              :hasTitle="true"
              :title="'Độ dài tour (giờ)'"
              :placeholder="'Nhập giờ'"
              :isNumber="true"
              :hasImage="true"
              :classImage="'mi-14 icon-time'"
              :content="tourTime"
              v-on:changeData="(value)=>{this.tourTime = value}"
              />
              <div style="height:20px"></div>
              <label for="price-range" style="font-weight:600">Mức giá: {{priceRange}}tr</label>
              <input type="range" id="price-range" name="price-range" min="0" max="100" v-model="priceRange">


            </div>
            <div class="flex-1"></div>
            <div class="function d-flex">
              <div class="flex-1"></div>
              <div class="btn" @click="filterDataDefault">Mặc định</div>
              <div class="btn btn-save" @click="filterData">Lọc</div>
            </div>
          </div>
          
          <div v-for="(v, index) in contents" v-bind:key="index" class="grid-item d-flex">
            <img class="item-image w-40" :src="v.imageUrl">
            <div class="item-info d-flex flex-column w-60">
              <router-link class="item-title" :to="{ name: 'tour-infor', params: { id: v.id }}" >{{v.title}}</router-link>
              <div class="item-code" style="margin-left:10px">Mã tour: <b>{{v.code}}</b></div>
              <div class="d-flex" style="margin-left:10px">
                <div v-for="(o, i) in v.otherInfo" v-bind:key="i" class="option">{{o}}</div>
              </div>
              <div class="item-price d-flex">
                <div class="flex-1"></div>
                <div class="price">{{v.price}}</div>
              </div>
              <div class="flex-1"></div>
              <div class="item-action d-flex">
                <div class="flex-1"></div>
                <div class="btn btn-save" @click="showFormCreateTour(v.id)">Mua ngay</div>
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
    :oTour="oTour"
    :mode="1"
    :oData="oData"
    :TitleTour="'Khởi tạo tour'"
    v-on:closeForm="closeForm"
    />
    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>

    <ThePageInfo/>
  </div>
  
</template>

<script>
import BaseAutoComplete from '../../components/base/BaseAutoComplete.vue'
import BaseInput from '../../components/base/BaseInput.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import ThePageInfo from '../../components/layout/ThePageInfo.vue'
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheCreateTour from '../../components/form/TheCreateTour.vue'
import ChatBox from "@/components/base/ChatBox";
import Tour from '../../js/entity/tour'
import TourAPI from "../../js/api/tourapi"
import ProvinceAPI from "../../js/api/province"
export default {
  components: { ThePageInfo, BaseInput, BaseAutoComplete, BaseNavigationPage, TheCreateTour, ChatBox, BaseLoad },
  data(){
    return{
      showFilter: false,
      priceRange: 3,
      tourTime: 78,
      search : "",
      toID : "",
      fromID : "",
      showForm: false,
      contents: [],
      showLoad: false,
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

      lstProvince : [],
      dataProvinceField : {value: "ProvinceName"},
      fromName : "",
      toName : "",
      oTour : new Tour(),
      oData: null,
    }
  },
  watch:{
      '$route'(to, from){
          this.search = to.params.search;
          this.toID = to.params.toId;
          if(this.search == undefined || this.search == 'undefined'){
            this.search = ""
          }
          if(this.toID == undefined || this.toID == 'undefined'){
            this.toID = ""
            this.toName = ""
          }
          
          from;
      }
  },
  async mounted() {
    
  },
  async created(){
    this.search = this.$route.params.search;
    this.toID = this.$route.params.toId;

    if(this.search == undefined || this.search == 'undefined'){
      this.search = ""
    }
    if(this.toID == undefined || this.toID == 'undefined'){
      this.toID = ""
    }

    await ProvinceAPI.getAll()
    .then(res=>{
        this.lstProvince = res.data;
    })

    this.lstProvince.forEach(e=>{
      if(e.ProvinceID == this.toID){
        this.toName = e.ProvinceName
      }
    })

    await this.filter(this.search,this.toID,"", this.tourTime, this.priceRange, 20, 0)
  },

  methods:{

    async filter(search, toID, fromID, time, price, size, page){
      price = Number.parseInt(price.toString().replaceAll(".", ""))
      price = price * 1000000
      this.showLoad = true
      await TourAPI.filterSideUser(search, toID, fromID, time, price, size, page)
      .then(res=>{
        this.bindData(res.data)
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

    bindData(data){
      this.contents = []
      var listTour = data.data
      var listImage = data.listImage
      this.totalRecord = data.totalRecord
      this.totalPage = data.totalPage

      for(var i=0; i<listTour.length; i++){
        var item = listTour[i]
        var tourID = item.TourID
        var image = listImage[i]
        var randIndex = Math.floor(Math.random() * image.Image.length)
        image = image.Image[randIndex]
        var price = item.Price.toString().replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VNĐ";
        var otherInfo = [item.TimeOfTour.toString() + " giờ"]
        this.contents.push({
          id: tourID,
          imageUrl: image,
          title: item.TourName,
          code: item.TourCode,
          otherInfo: otherInfo,
          price: price
        })
      }

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
          for(i=1; i<= me.totalPage; i++){
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
    },

    filterData(){
      this.filter(this.search, this.toID, this.fromID, this.tourTime, this.priceRange, this.pageSize, 0)
    },

    filterDataDefault(){
      this.fromID = ""
      this.tourTime = 72
      this.priceRange = 3
      this.fromName = ""
      this.filter(this.search, this.toID, this.fromID, this.tourTime, this.priceRange, this.pageSize, 0)
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

    chooseDestinationPoint(pName){
      var me = this;
      var province = this.lstProvince.filter(x=>x.ProvinceName == pName);
      if(province.length == 1){
        me.toID = province[0].ProvinceID
      }
    },

    chooseStartPoint(pName){
      var me = this;
      var province = this.lstProvince.filter(x=>x.ProvinceName == pName);
      this.fromName = pName
      if(province.length == 1){
        me.fromID = province[0].ProvinceID
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

        this.filter(this.search, this.toID, this.fromID, this.tourTime, this.priceRange, this.pageSize, this.currentPage - 1)
    },

    /**
     * Thay đổi kích thước trang
     * @param {Number} size: Kích thước trang
     */
    changePageSize(size){
        this.pageSize = size;
        this.currentPage = 1;
        
        this.filter(this.search, this.toID, this.fromID, this.tourTime, this.priceRange, this.pageSize, this.currentPage - 1)
    },

    /**
     * Show form tạo tour
     */
    async showFormCreateTour(id){
      this.showLoad = true
      await TourAPI.getByID(id)
      .then(res=>{
          var data = res.data
          var tour = new Tour();
          this.oTour = tour;
          this.oTour.Name = data.Master.TourName
          this.oTour.TourCode = data.Master.ContractCode
          this.oTour.CreatedTime = data.Master.CreatedTime
          this.oTour.TotalAmount = Number.parseInt(data.Master.TotalCost)
          this.oTour.Departure = data.Master.ProvinceDestinationName
          this.oTour.DepartureID = data.Master.ProvinceDestinationID
          this.oTour.StartPoint = data.Master.ProvinceStartName
          this.oTour.StartPointID = data.Master.ProvinceStartID
          this.oTour.PickUpPoint = data.Master.PickupAdress
          this.oTour.NumberAdult = Number.parseInt(data.Contract.NumberAdult)
          this.oTour.NumberChild = Number.parseInt(data.Contract.NumberChild)
          this.oTour.NumberBaby = Number.parseInt(data.Contract.NumberBaby)
          this.oTour.TotalDay = Number.parseInt(data.Contract.TotalHour)

          var pickupTime = new Date(data.Master.PickupTime)
          var startTime = new Date(data.Contract.StartTime)
          var endTime = new Date(data.Contract.EndTime)
          this.oTour.PickUpTime = new Date(pickupTime.setTime(pickupTime.getTime() - (7*60*60*1000)))
          this.oTour.StartTime = new Date(startTime.setTime(startTime.getTime() - (7*60*60*1000)))
          this.oTour.EndTime = new Date(endTime.setTime(endTime.getTime() - (7*60*60*1000)))
          
          this.oTour.Sample = data.Info.Sample
          this.oTour.Status = 0
          this.oTour.IsPayment = data.Info.IsPayment
          this.oTour.TourID = "0000"
          
          data.Schedule.forEach(e=>{
              e.Morning.forEach(k=>{
                  var time = new Date(k.Time)
                  k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
              })

              e.Afternoon.forEach(k=>{
                  var time = new Date(k.Time)
                  k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
              })

              e.Evening.forEach(k=>{
                  var time = new Date(k.Time)
                  k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
              })
          })

          data.AttachOption.forEach(e=>{
              e.Price = e.Price.toString()
                              .replace(/\D/g, "")
                              .replace(/\B(?=(\d{3})+(?!\d))/g, ".")
          })

          this.oData = data
          this.showForm = true;

          this.showLoad = false
      })
      .catch(()=>{
          this.showLoad = false
          this.toast({
              title: "Có lỗi xảy ra. Vui lòng thử lại",
              type: "error",
              duration: 3000,
          });
      })
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