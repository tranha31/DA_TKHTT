<template>
  <div class="hotel-container">
      <div class="search">
            <div class="search-main">
                <div class="search-title">
                  <router-link to="/tour" class="link">Tour &amp; Trải nghiệm</router-link>
                  <router-link to="/hotel" class="link active">Khách sạn</router-link>
                </div>
                <div class="search-content">
                    <BaseInput
                    :clas="'w-40 m-r-20'"
                    :placeholder="'Nhập tên khách sạn'"
                    :hasImage="true"
                    :classImage="'mi-14 icon-search'"
                    />

                    <date-picker v-model="rangeTime" type="date" range placeholder="Ngày nhận - Trả phòng" format='DD-MM-YYYY'></date-picker>
                    
                    <div class="w-30 chooseAmount"></div>

                    <div class="flex-1"></div>
                    <div class="btn btn-save m-l-10" style="min-width: 100px">Tìm kiếm</div>
                </div>
            </div>
        </div>

        <div class="room-main d-flex flex-column">
            <div class="hotel-info d-flex">
                <div v-for="(v, index) in hotelInfo.imageUrl" v-bind:key="index" class="image w-30 slide fade hotelImage" :style="v"></div>
                <div class="d-flex flex-column w-60 infos">
                    <div class="title">{{hotelInfo.name}}</div>
                    <div class="d-flex mb-12" style="align-items:center">
                        <div class="place"></div>
                        <div>{{hotelInfo.place}}</div>
                    </div>
                    <div class="d-flex other-info mb-12">
                        <div v-for="(v, index) in hotelInfo.otherInfo" v-bind:key="index" class="info">{{v}}</div>
                    </div>
                    <div class="star d-flex mb-12">
                        <div v-for="index in hotelInfo.star" v-bind:key="index" class="star-item"></div>
                        
                    </div>
                    <div class="describe mb-12">{{hotelInfo.describe}}</div>

                    <div class="d-flex">
                        <div class="flex-1"></div>
                        <router-link to="/" class="linkHotel">Xem chi tiết</router-link>
                    </div>
                </div>
                
            </div>
            <div class="note">Vui lòng chọn phòng</div>
            <div class="rooms d-flex">
                <div class="room-item-title active">Phòng 1</div>
                <div class="room-item-title">Phòng 2</div>
                <div class="room-item-title">Phòng 3</div>
            </div>
            <div class="grid-room d-flex">
                <div class="room-item w-half">
                    <div v-for="(item, index) in rooms" v-bind:key="index" class="item d-flex flex-column w-full mb-20" :id="item.id">
                        <div class="info d-flex w-full">
                            <div class="image w-half" :style="item.imageUrl"></div>
                            <div class="info-room w-half d-flex flex-column">
                                <div class="title mb-12">{{item.name}}</div>
                                <div>Chỉ từ&nbsp;<span class="price">{{item.rangePrice}}</span>/đêm</div>
                                <div class="flex-1"></div>
                                <div class="d-flex">
                                    <div class="flex-1"></div>
                                    <div class="btn btn-save" @click="showOption(item.id)">Chọn phòng</div>
                                </div>
                            </div>
                        </div>
                        <div class="option d-flex flex-column w-full" style="display: none">
                            <div v-for="(option, i) in item.options" v-bind:key="i" class="option-item d-flex flex-column w-full pd-10">
                                <div class="d-flex center mb-12">
                                    <input type="radio" name="choose-option-room" style="margin-right:10px"/>
                                    <div class="title" style="font-weight: 600;font-size: 16px;">{{option.nameOption}}</div>
                                    <div class="flex-1"></div>
                                    <div class="price-room">{{option.price}}/đêm</div>
                                </div>
                                <div v-for="(op, ind) in option.option" v-bind:key="ind" class="d-flex p-l-10">
                                    <div class="d-flex center">
                                        <div :class="op.type == 'meal'? 'icon-cook' : 'icon-policy'" class="mi mi-14 icon-cook m-r-10"></div>
                                        <div>{{op.name}}</div>
                                    </div>
                                </div>
                                <div class="d-flex">
                                    <div class="flex-1"></div>
                                    <div class="view-more" @click="showFormInforTour(index, i)">Xem chi tiết</div>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>
                <div class="flex-1"></div>
                <div class="payment-div w-half d-flex flex-column">
                    <div class="title mb-20">Thông tin đặt phòng</div>
                    <div class="time d-flex flex-column mb-20 border-bottom pb-12">
                        <div class="sub-title">Thời gian</div>
                        <div class="d-flex">
                            <div class="d-flex flex-column">
                                <div>Nhận phòng</div>
                                <div>20/4/2022</div>
                            </div>
                            <div class="flex-1"></div>
                            <div class="mi mi-24 icon-calendar"></div>
                            <div class="flex-1"></div>
                            <div class="d-flex flex-column">
                                <div>Trả phòng</div>
                                <div>22/4/2022</div>
                            </div>
                        </div>
                    </div>
                    <div class="amount d-flex flex-column mb-20 border-bottom pb-12">
                        <div class="sub-title">Số lượng</div>
                        <div class="d-flex">
                            <div class="w-30">Người lớn: 5</div>
                            <div class="w-30">Trẻ em: 2</div>
                            <div class="w-30">Em bé: 0</div>
                        </div>
                        <div>Số ngày: 2 ngày 1 đêm</div>
                        <div>Số phòng: 3</div>
                    </div>
                    <div class="info-room d-flex flex-column mb-20 border-bottom pb-12">
                        <div class="sub-title">Thông tin phòng</div>
                        <div class="d-flex">
                            <div>Phòng 1: Phòng Vip1</div>
                            <div class="flex-1"></div>
                            <div>1.700.000đ</div>
                        </div>
                        <div class="d-flex">
                            <div>Phòng 1: Phòng Vip2</div>
                            <div class="flex-1"></div>
                            <div>1.700.000đ</div>
                        </div>
                    </div>
                    <div class="d-flex">
                        <div class="sub-title">Tổng cộng</div>
                        <div class="flex-1"></div>
                        <div class="price price-room">2.400.000đ</div>
                    </div>
                    <div class="btn btn-save btn-order">Đặt ngay</div>
                </div>
            </div>
        </div>
        
        <div v-if="showFormInfo" class="information-room">
            <div class="background"></div>
            <div class="content d-flex flex-column">
                <div class="title mb-20">
                    Enjoy 2022 - Chỉ gồm phòng
                    <div class="icon-close" @click="()=>{this.showFormInfo = false}">X</div>
                </div>
                
                <div class="sub-title">Chi tiết gói giá</div>
                <ol>
                    <li>abc</li>
                    <li>abc</li>
                </ol>
                <div class="sub-title">Chính sách hoàn hủy</div>
                <ol>
                    <li>Không hoàn hủy</li>
                </ol>
            </div>
        </div>
        <ThePageInfo/>
  </div>
</template>

<script>
import BaseInput from '../../components/base/BaseInput.vue'
import ThePageInfo from '../../components/layout/ThePageInfo.vue'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
export default {
    components: { ThePageInfo, BaseInput, DatePicker},
    data(){
        return{
            id: null,
            rangeTime: null,
            slideIndex: 0,
            hotelInfo:{
                id: "45555",
                imageUrl: [
                    "background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJp0OefxrRqn4OyMnrvlvhYuNl9H4JzxxoqsdHQgaC7a2Hsm47Pm9zxGCDhQMe55WhWsg&usqp=CAU')",
                    "background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvP5E6vS83_1bDIHOuyDnXfsn9EB-SCfXRpKnV17hJ5PGQOvBI7VZYXWFbLQBxPQSh-k0&usqp=CAU')",
                    "background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqiedwItOpOk3CQKsJZB5pS6N8s9J-XukYnAvljFcmclUVIaKV1wOiBvq800V9BMiXebg&usqp=CAU')"

                ],
                name: "Khách sạn ABC",
                place: "1, HBT, HN",
                star: 5,
                otherInfo: ["Bể bơi 4 mùa", "Vị trí gần trung tâm"],
                describe: "Là sản phẩm căn hộ khách sạn sang trọng và đẳng cấp, Vinpearl Condotel Empire Nha Trang mang đến cho khách hàng không gian lưu trú tiện nghi và hiện đại của khách sạn 5 sao với những trải nghiệm nghỉ dưỡng đỉnh cao ngay trong thành phố biển. Tòa nhà 41 tầng kiêu hãnh tọa lạc giữa trung tâm thành phố giúp cho việc di chuyển thăm quan, mua sắm trở nên hết sức thuận tiện",
            },

            rooms: [
                {
                    id: "444",
                    imageUrl: "background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5XoUvnWVYtffLkb9CBLnWdnMoEI5TQf3nnQ&usqp=CAU')",
                    name: "Phòng Vip 1",
                    rangePrice: "1.700.000đ",
                    options: [
                        {
                            nameOption: "Enjoy 2022 - Chỉ gồm phòng",
                            option: [
                                {
                                    name: "Không bao gồm ăn sáng",
                                    type: "meal",
                                },
                                {
                                    name: "Không hoàn hủy",
                                    type: "policy",
                                }
                            ],
                            price: "1.700.000"
                        },
                        {
                            nameOption: "Enjoy 2022 - Ăn sáng",
                            option: [
                                {
                                    name: "Ăn sáng",
                                    type: "meal",
                                },
                                {
                                    name: "Không hoàn hủy",
                                    type: "policy",
                                }
                            ],
                            price: "1.900.000"
                        },
                    ],
                },

                {
                    id: "555",
                    imageUrl: "background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5XoUvnWVYtffLkb9CBLnWdnMoEI5TQf3nnQ&usqp=CAU')",
                    name: "Phòng Vip 1",
                    rangePrice: "1.700.000đ",
                    options: [
                        {
                            nameOption: "Enjoy 2022 - Chỉ gồm phòng",
                            option: [
                                {
                                    name: "Không bao gồm ăn sáng",
                                    type: "meal",
                                },
                                {
                                    name: "Không hoàn hủy",
                                    type: "policy",
                                }
                            ],
                            price: "1.700.000"
                        },
                        {
                            nameOption: "Enjoy 2022 - Ăn sáng",
                            option: [
                                {
                                    name: "Ăn sáng",
                                    type: "meal",
                                },
                                {
                                    name: "Không hoàn hủy",
                                    type: "policy",
                                }
                            ],
                            price: "1.900.000"
                        },
                    ],
                }
            ],

            showFormInfo: false,
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
        
    },
    methods:{
        /**
         * Hiển thị ảnh tour theo thời gian
         */
        showSlides(){
            let i;
            let slides = document.getElementsByClassName("hotelImage");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
            }
            this.slideIndex++;
            if (this.slideIndex > slides.length) {this.slideIndex = 1}   
            slides[this.slideIndex-1].style.display = "block";
            setTimeout(this.showSlides, 2500); 
        },

        showOption(id){
            var divOption = document.getElementById(id);
            var option = divOption.querySelector(".option");
            if(option.style.display != "none"){
                option.style.display = "none";
            }
            else{
                option.style.display = "flex";
            }
        },

        showFormInforTour(indexItem, indexOption){
            indexItem;
            indexOption;
            this.showFormInfo = true;
        }
    }
}
</script>

<style>
@import url(../../css/content/room.css);
.price-room{
    font-size: 18px;
}
.view-more{
    color: #e89327;
}

.view-more:hover{
    cursor: pointer;
    text-decoration: underline;
}
.btn-order{
    height: 50px;
    font-size: 18px;
    text-align: center;
    margin-top: 40px;
}

.information-room{
    position: fixed;
    height: 100vh;
    width: 100vw;
    top: 0;
    left: 0;
    z-index: 555555;
    display: flex;
    align-items: center;
    justify-content: center;
}

.information-room .background{
    position: absolute;
    width: 100vw;
    height: 100vh;
    background: rgba(0,0,0,.4);
    z-index: -5;
}

.information-room .content{
    position: absolute;
    width: 50%;
    height: 500px;
    background-color: #fff;
    border: 1px solid #babec5;
    border-radius: 5px;
    padding: 20px;
}

.information-room .content .title{
    position: relative;
    font-size: 20px;
    font-weight: 600;
}

.information-room .content .sub-title{
    font-size: 18px;
    font-weight: 600;
    background-color: #babec5;
    padding: 10px;
}

.information-room .content ol{
    width: 100%;
    height: 100px;
}
.information-room .content ol li{
    margin: 20px 30px;
}

.information-room .content .icon-close{
    position: absolute;
    top: 0;
    right: 0;
    cursor: pointer;
}
@media only screen and (max-width: 400px) {
    .price-room{
        font-size: 10px;
    }
}

</style>