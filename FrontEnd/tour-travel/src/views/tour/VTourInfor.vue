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
          <div class="overview mb-30">
              <div class="title">{{object.title}}</div>
              <div class="d-flex">
                  <div v-for="(v, index) in object.imageUrl" v-bind:key="index" class="image w-60 slide fade slideTour" :style="v"></div>
                  <div class="d-flex flex-column w-40" style="padding-left: 20px">
                    <div class="d-flex p-b-20">
                      <div>Mã tour: {{object.code}}</div>
                      <div class="flex-1"></div>
                      <div class="item-action-info">{{object.numberBuy}} nguoi da mua</div>
                    </div>
                    <div class="price p-b-30">{{object.price}}</div>
                    <div class="d-flex p-b-30">
                        <div class="btn btn-save" @click="showFormCreateTour">Đặt tour ngay</div>
                        <div class="flex-1"></div>
                        <div class="mi mi-32 icon-cart"></div>
                    </div>
                    <div class="w-full d-flex">
                        <div class="mi mi-14 icon-tick m-r-10"></div>
                        <span>Gá tốt nhất</span>
                    </div>
                    <div class="w-full d-flex">
                        <div class="mi mi-14 icon-tick m-r-10"></div>
                        <span>Thanh toán tức thì</span>
                    </div>
                    <div class="w-full d-flex">
                        <div class="mi mi-14 icon-tick m-r-10"></div>
                        <span>Trải nghiệm hoàn hảo</span>
                    </div>
                  </div>
                  
              </div>
          </div>
          
          <div class="tour-infor mb-30">
            <div class="d-flex option">
                <div class="option-item active" @click="changeInfo(0)">Thông tin tour</div>
                <div class="option-item" @click="changeInfo(1)">Lịch trình</div>
                <div class="option-item" @click="changeInfo(2)">Chính sách hoàn hủy</div>
                <div class="option-item" @click="changeInfo(3)">Hướng dẫn</div>
            </div>
            <div class="content">{{contentInfor}}</div>
          </div>

          <div class="suggest-tour">
              <div class="title mb-30">Sản phẩm tương tự</div>
              <div class="suggest-container d-flex">
                  <div class="prev" @click="showPrevSuggest()"></div>
                  <div class="next" @click="showNextSuggest()"></div>
                  <div v-for="(v, index) in suggestItem" v-bind:key="index" class="suggest-item d-flex flex-column w-33 fade">
                      <div class="image" :style="v.imageUrl"></div>
                      <router-link class="title" :title="v.title" :to="{ name: 'tour-infor', params: { id: v.id }}">{{v.title}}</router-link>
                      <div class="flex-1"></div>
                      <div class="d-flex other-info">
                        <div class="item-action-info">{{v.numberBuy}} nguoi da mua</div>
                        <div class="flex-1"></div>
                        <div class="price">{{v.price}}</div>
                      </div>
                  </div>
              </div>
          </div>
        </div>
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
import TheCreateTour from '../../components/form/TheCreateTour.vue'
import ThePageInfo from '../../components/layout/ThePageInfo.vue'
export default {
    components: { ThePageInfo, BaseInput, BaseAutoComplete, TheCreateTour},
    data(){
        return{
            id: null,
            slideIndex : 0,
            suggestIndex: 0,
            showForm: false,
            object: {
                id: this.id,
                imageUrl: ["background-image: url('https://booking-static.vinpearl.com/tours/b018892921a94fa0b344a28fc2db0a99_DGH_2236_summer2.jpg')",
                            "background-image: url('https://booking-static.vinpearl.com/images/eced0942f0e547fa80057ffa78c26a8d__D8H1543%20(1).jpg')",
                            "background-image: url('https://booking-static.vinpearl.com/images/d2759680ab6a4b8585e899c455b221ce__D8H6905%20(1).jpg')"],
                title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
                code: "1111",
                price: "8.000.000đ",
                numberBuy: 17
            },

            suggestItem:[
                {
                    id: '2222',
                    imageUrl: "background-image: url('https://booking-static.vinpearl.com/tours/b018892921a94fa0b344a28fc2db0a99_DGH_2236_summer2.jpg')",
                    title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
                    code: "1111",
                    price: "5.000.000đ",
                    numberBuy: 17
                },
                {
                    id: '2222',
                    imageUrl: "background-image: url('https://booking-static.vinpearl.com/images/eced0942f0e547fa80057ffa78c26a8d__D8H1543%20(1).jpg')",
                    title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
                    code: "1111",
                    price: "5.000.000đ",
                    numberBuy: 17
                },
                {
                    id: '2222',
                    imageUrl: "background-image: url('https://booking-static.vinpearl.com/images/d2759680ab6a4b8585e899c455b221ce__D8H6905%20(1).jpg')",
                    title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
                    code: "1111",
                    price: "5.000.000đ",
                    numberBuy: 17
                },
                {
                    id: '2222',
                    imageUrl: "background-image: url('https://booking-static.vinpearl.com/images/7b91d191da7a44b0888a8ef846e247eb_IMG_5419%20(1).jpg')",
                    title: "[Hà Nội - Ninh Bình] Tour du lich trai nghiem Dam Van Long - Ninh Binh",
                    code: "1111",
                    price: "5.000.000đ",
                    numberBuy: 17
                },

            ],

            contentInfor: null,


        }
    },
    watch:{
        '$route'(to, from){
            this.id = to.params.id;
            from;
        }
    },
    async created(){
        this.id = this.$route.params.id;
    },
    mounted(){
        this.showSlides();
        this.setUpShowSuggest();
        
    },
    methods:{
        /**
         * Hiển thị ảnh tour theo thời gian
         */
        showSlides(){
            let i;
            let slides = document.getElementsByClassName("slideTour");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
            }
            this.slideIndex++;
            if (this.slideIndex > slides.length) {this.slideIndex = 1}   
            slides[this.slideIndex-1].style.display = "block";
            setTimeout(this.showSlides, 2500); 
        },

        /**
         * Thay đổi thông tin hiển thị 
         */
        changeInfo(index){
            var infos =  document.getElementsByClassName("option-item");
            for (var i = 0; i < infos.length; i++) {
                infos[i].classList.remove("active");  
            }
            infos[index].classList.add("active");
        },

        setUpShowSuggest(){
            let i;
            let items = document.getElementsByClassName("suggest-item");
            for (i = 0; i < items.length; i++) {
                if(i < 3){
                    items[i].style.display = "flex";
                    items[i].style.left = i*33.733333333 + "%";
                }
                else{
                    items[i].style.display = "none";
                }
            }
            
        },

        /**
         * Dịch toàn bộ sang bên phải
         */
        showPrevSuggest(){
            let i;
            let items = document.getElementsByClassName("suggest-item");
            let len = items.length;
            for (i = 0; i < items.length; i++) {
                items[i].style.display = "none";
            }
            if(this.suggestIndex == 0){
                items[len-1].style.display = "flex";
                items[len-1].style.left =  "0";

                items[0].style.display = "flex";
                items[0].style.left =  "33.733333333%";

                items[1].style.display = "flex";
                items[1].style.left =  33.733333333*2 + "%";

                this.suggestIndex = len - 1;
                
            }
            else if(this.suggestIndex == len-1){
                items[len-2].style.display = "flex";
                items[len-2].style.left =  "0";

                items[len-1].style.display = "flex";
                items[len-1].style.left =  "33.733333333%";

                items[0].style.display = "flex";
                items[0].style.left =  33.733333333*2 + "%";

                this.suggestIndex = this.suggestIndex - 1;
                if(this.suggestIndex < 0) {
                    this.suggestIndex = 0;
                }
            }
            else if(this.suggestIndex == 1){
                items[0].style.display = "flex";
                items[0].style.left =  "0";

                items[1].style.display = "flex";
                items[1].style.left =  "33.733333333%";

                items[2].style.display = "flex";
                items[2].style.left =  33.733333333*2 + "%";

                this.suggestIndex = 0;
            }
            else{
                var index = this.suggestIndex;
                items[index-1].style.display = "flex";
                items[index-1].style.left =  "0";

                items[index].style.display = "flex";
                items[index].style.left =  "33.733333333%";

                items[index+1].style.display = "flex";
                items[index+1].style.left =  33.733333333*2 + "%";

                this.suggestIndex = this.suggestIndex - 1;
                if(this.suggestIndex < 0) {
                    this.suggestIndex = 0;
                }
            }
        },

        /**
         * Dịch toàn bộ qua trái
         */
        showNextSuggest(){
            let i;
            let items = document.getElementsByClassName("suggest-item");
            let len = items.length;
            for (i = 0; i < items.length; i++) {
                items[i].style.display = "none";
            }
            if(this.suggestIndex == 0){
                items[1].style.display = "flex";
                items[1].style.left =  "0";

                items[2].style.display = "flex";
                items[2].style.left = "33.733333333%";

                let index = this.suggestIndex + 3 == len ? len-1 : this.suggestIndex + 3;
                items[index].style.display = "flex";
                items[index].style.left =  33.733333333*2 + "%";

                this.suggestIndex = 1;
                
            }
            else if(this.suggestIndex == len-1){
                items[0].style.display = "flex";
                items[0].style.left =  "0";

                items[1].style.display = "flex";
                items[1].style.left =  "33.733333333%";

                items[2].style.display = "flex";
                items[2].style.left =  33.733333333*2 + "%";

                this.suggestIndex = 0;
            }
            else if(this.suggestIndex == len-2){
                items[len-1].style.display = "flex";
                items[len-1].style.left =  "0";

                items[0].style.display = "flex";
                items[0].style.left =  "33.733333333%";

                items[1].style.display = "flex";
                items[1].style.left =  33.733333333*2 + "%";

                this.suggestIndex = len-1;
            }
            else{
                items[this.suggestIndex+1].style.display = "flex";
                items[this.suggestIndex+1].style.left =  "0";

                items[this.suggestIndex+2].style.display = "flex";
                items[this.suggestIndex+2].style.left =  "33.733333333%";

                let inDex = this.suggestIndex+3 == len ? 0 : this.suggestIndex+3;
                items[inDex].style.display = "flex";
                items[inDex].style.left =  33.733333333*2 + "%";

                this.suggestIndex = this.suggestIndex + 1;
                if(this.suggestIndex == len) {
                    this.suggestIndex = 0;
                }
            }
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
@import url(../../css/content/tourinfor.css);

.tour-contain .e-autocomplete{
  padding-left: 25px !important;
}

</style>