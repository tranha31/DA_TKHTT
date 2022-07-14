<template>
  <div class="restaurant-page-container d-flex flex-column">
    <div class="header-hotel-container d-flex">
      <div class="header-restaurant-info">
        <div>
          <label>{{ hotelName }}</label>
        </div>
        <div class="mt-12">
          <span class="mr-12">
            <div class="icon white mi-24 location-icon d-flex" style="display: inline-block"></div>
            {{ hotelAddr }}
          </span>
          <span class="mr-12">
            <div class="icon white mi-24 phone-icon d-flex" style="display: inline-block"></div>
            {{ hotelPhone }}
          </span>
          <span class="mr-12">
            <div class="icon white mi-24 mail-icon d-flex" style="display: inline-block"></div>
            {{ hotelMail }}
          </span>
          <span class="mr-12">
            <div class="icon white mi-24 rate-icon d-flex" style="display: inline-block"></div>
            {{ hotelRate }}
          </span>
        </div>
      </div>
    </div>
    <div class="body-hotel-container">
      <div class="tabs d-flex">
        <div class="tab-item" :style="{'border-bottom': showOverview ? 'solid #e89327 3px' : 'solid #949494 2px'}">
          <label :style="{'color': showOverview ? '#e89327' : ''}" @click="chooseOverview()">Overview</label>
        </div>
        <div class="tab-item" :style="{'border-bottom': showRoom ? 'solid #e89327 3px' : 'solid #949494 2px'}">
          <label :style="{'color': showRoom ? '#e89327' : ''}" @click="chooseRoom()">Room</label>
        </div>
        <div class="tab-item" :style="{'border-bottom': showCulinary ? 'solid #e89327 3px' : 'solid #949494 2px'}">
          <label :style="{'color': showCulinary ? '#e89327' : ''}" @click="chooseCulinary()">Culinary</label>
        </div>
      </div>
      <div class="tab-container">
        <div class="tab-overview" v-if="showOverview">
          <div class="overview-overview pb-36">
            <div class="mb-12">
              <label>{{ hotelName }}</label>
              <h3>{{ hotelDescription }}</h3>
              <span style="display: inline-block" class="mr-20 mt-12">
                <div class="icon black mi-14 area-icon d-flex mr-12" style="display: inline-block"></div>
                <span style="font-size: 16px;">Area</span>
                <h3>{{ hotelArea }}</h3>
              </span>
              <span style="display: inline-block" class="mr-20 mt-12">
                <div class="icon black mi-14 number-icon d-flex mr-12" style="display: inline-block"></div>
                <span style="font-size: 16px;">Number of rooms</span>
                <h3>{{ hotelTotalRooms }}</h3>
              </span>
            </div>
            <div class="hotel-image-list d-flex mt-12">
              <div class="icon black mi-14 next-icon d-flex mr-12" style="display: inline-block"></div>
              <div class="hotel-image"
                   v-for="image in hotelImages"
                   :key="image.id"
              >
              </div>
              <div class="icon black mi-14 pre-icon d-flex mr-12" style="display: inline-block"></div>
            </div>
          </div>
          <div class="overview-room pb-36">
            <div class="mb-12">
              <label>Room Category</label>
            </div>
            <div class="overview-room-info d-flex">
              <div
                  v-for="room in hotelRooms"
                  :key="room.id"
                  class="d-flex flex-column"
                  style="border: solid #949494 1px; border-radius: 4px;"
              >
                <div class="overview-room-img"></div>
                <div style="padding: 8px;">
                  <div class="d-flex flex-column">
                    <label style="font-size: 14px">{{ room.name }}</label>
                    <div>
                       <span style="display: inline-block" class="mr-20 mt-12">
                        <div class="icon black mi-14 area-icon d-flex mr-12" style="display: inline-block"></div>
                        <span style="font-size: 12px;">{{ room.area }}</span>
                      </span>
                      <span style="display: inline-block" class="mr-20 mt-12">
                        <div class="icon black mi-14 people-icon d-flex mr-12" style="display: inline-block"></div>
                        <span style="font-size: 12px;">{{ room.adults }} adults - {{ room.kids }} kids</span>
                      </span>
                    </div>
                    <div class="mt-12">Price: {{ room.price }}</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="action-overview d-flex">
              <button
                  class="btn-default-overview white"
                  style="margin-top: 20px; font-weight: bold;"
              >
                Book now
              </button>
            </div>
          </div>
          <div class="overview-culinary d-flex">
            <div class="overview-culinary-img"></div>
            <div style="width: 50%">
              <label>Culinary</label>
              <h3>{{ hotelCulinaryDescription }}</h3>
            </div>
          </div>
        </div>
        <div class="tab-room d-flex flex-column" v-if="showRoom">
          <div>
            <label>Room Category</label>
            <h3>{{ hotelRoomDescription }}</h3>
          </div>
          <div class="room-room-info d-flex flex-column">
            <div
                v-for="room in hotelRooms"
                :key="room.id"
                class="d-flex mb-12"
                style="border: solid #949494 1px; border-radius: 4px; padding: 10px;"
            >
              <div class="room-room-img"></div>
              <div style="padding: 8px; width: 60%;" class="d-flex flex-column">
                <label>{{ room.name }}</label>
                <div>
                       <span style="display: inline-block" class="mr-20 mt-12">
                        <div class="icon black mi-14 area-icon d-flex mr-12" style="display: inline-block"></div>
                        <span style="font-size: 16px;">{{ room.area }}</span>
                       </span>
                  <span style="display: inline-block" class="mr-20 mt-12">
                        <div class="icon black mi-14 people-icon d-flex mr-12" style="display: inline-block"></div>
                        <span style="font-size: 16px;">{{ room.adults }} adults - {{ room.kids }} kids</span>
                    </span>
                </div>
                <div class="mt-12">{{ room.description }}</div>
                <div class="mt-12">Price: {{ room.price }}</div>
                <div>
                  <button
                      class="btn-default-overview white mt-12"
                      style="margin-left: 70%"
                  >
                    Book now
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="showCulinary">
          <div>
            <label>Culinary</label>
            <h3>
              {{ hotelCulinaryDescription }}
            </h3>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
// import {PerfectScrollbar} from 'vue2-perfect-scrollbar'
// import knife from '../../assets/imgs/Image/knife.png'
// import InputInfoTemplate from "@/components/base/InputInfoTemplate"
import Footer from "@/components/layout/TheFooter"
import InfotypeApi from "@/js/api/InfotypeApi"

export default {
  name: 'Hotel',
  components: {
    // PerfectScrollbar,
    // knife
    // InputInfoTemplate,
    Footer
  },
  data() {
    return {
      hotelName: null,
      hotelAddr: null,
      hotelPhone: null,
      hotelMail: null,
      hotelRate: null,
      hotelDescription: 'Là sản phẩm căn hộ khách sạn sang trọng và đẳng cấp, ABC mang đến cho khách hàng không gian lưu trú tiện nghi và hiện đại của khách sạn 5 sao với những trải nghiệm nghỉ dưỡng đỉnh cao ngay trong thành phố biển. Tòa nhà 41 tầng kiêu hãnh tọa lạc giữa trung tâm thành phố giúp cho việc di chuyển thăm quan, mua sắm trở nên hết sức thuận tiện và mang lại cho du khách cảm nhận trọn vẹn về nhịp sống hiện đại đầy sôi động.',
      showOverview: false,
      showRoom: false,
      showCulinary: false,
      hotelArea: null,
      hotelTotalRooms: '50',
      hotelImages: [
        {
          'background-image': 'url(../../assets/imgs/Image/hotel3.jpg)'
        },
        {
          'background-image': 'url(../../assets/imgs/Image/hotel3.jpg)'
        },
        {
          'background-image': 'url(../../assets/imgs/Image/hotel3.jpg)'
        },
        {
          'background-image': 'url(../../assets/imgs/Image/hotel3.jpg)'
        },
        {
          'background-image': 'url(../../assets/imgs/Image/hotel3.jpg)'
        }
      ],
      hotelRooms: [
        {
          name: 'Room 1',
          area: '37 m2',
          adults: 2,
          kids: 2,
          price: '1.500.000',
          description: 'Với diện tích 32-37m², Phòng Studio, 2 giường đơn là phòng khách sạn thiết kế hiện đại, sang trọng, tích hợp đầy đủ tiện nghi cho kỳ lưu trú của bạn. Vị trí thuận tiện, du khách có thể thoải mái tham quan, khám phá các điểm du lịch nổi tiếng, là lựa chọn lý tưởng'
        },
        {
          name: 'Room 2',
          area: '37 m2',
          adults: 2,
          kids: 2,
          price: '1.500.000',
          description: 'Với diện tích 32-37m², Phòng Studio, 2 giường đơn là phòng khách sạn thiết kế hiện đại, sang trọng, tích hợp đầy đủ tiện nghi cho kỳ lưu trú của bạn. Vị trí thuận tiện, du khách có thể thoải mái tham quan, khám phá các điểm du lịch nổi tiếng, là lựa chọn lý tưởng'
        },
        {
          name: 'Room 3',
          area: '37 m2',
          adults: 2,
          kids: 2,
          price: '1.500.000',
          description: 'Với diện tích 32-37m², Phòng Studio, 2 giường đơn là phòng khách sạn thiết kế hiện đại, sang trọng, tích hợp đầy đủ tiện nghi cho kỳ lưu trú của bạn. Vị trí thuận tiện, du khách có thể thoải mái tham quan, khám phá các điểm du lịch nổi tiếng, là lựa chọn lý tưởng'
        }
      ],
      hotelCulinaryDescription: 'Với ba nhà hàng và quán bar sang trọng, tầm nhìn toàn cảnh thành phố Hà Nộ năng động, các đầu bếp 5 sao tài ba và dịch vụ khách hàng chuyên nghiệp, ABC mang đến cho thực khách những trải nghiệm khó quên, đánh thức vị giác với ẩm thực biển và địa phương đặc sắc, ẩm thực quốc tế tinh hoa, những loại rượu vang thượng hạng và nhiều thức uống hấp dẫn, sáng tạo khác.',
      hotelRoomDescription: 'Nghỉ dưỡng tiện nghi và thời thượng trong những căn hộ khách sạn có đầy đủ tiện ích từ phòng nghỉ, phòng khách, bàn làm việc, phòng bếp, bàn ăn...và đặc biệt là tầm nhìn toàn cảnh thành phố sôi động khiến kỳ nghỉ dù ngắn hay dài, dù là chuyến du lịch khám phá hay công tác đều có những trải nghiệm Nha Trang thật thoải mái và đáng nhớ'
    }
  },
  methods: {
    chooseOverview() {
      this.showOverview = true
      this.showRoom = false
      this.showCulinary = false
    },
    chooseRoom() {
      this.showOverview = false
      this.showRoom = true
      this.showCulinary = false
    },
    chooseCulinary() {
      this.showOverview = false
      this.showRoom = false
      this.showCulinary = true
    },
    async initData() {
      const currentHotel = await InfotypeApi.getHotelById({
        HotelID: this.$route.params.id
      })

      if (currentHotel) {
        this.hotelName = currentHotel[0].Name
        this.hotelAddr = currentHotel[0].Address
        this.hotelDescription = currentHotel[0].Described
        this.hotelPhone = currentHotel[0].PhoneNumber
        this.hotelMail = currentHotel[0].Email
        this.hotelRate = currentHotel[0].Rank
        this.hotelArea = currentHotel[0].Acreage
        this.hotelCulinaryDescription = currentHotel[0].DescribedRestaurant
        this.hotelRoomDescription = currentHotel[0].DescribedRoom
      }
    }
  },
  async mounted() {
    this.showOverview = true
    await this.initData()
  }
}
</script>

<style scoped>
@import url(../../css/common/icon.css);
.restaurant-page-container {
}

.header-hotel-container {
  background-image: url(../../assets/imgs/Image/restaurant1.jpg);
  height: 500px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  color: #ffffff;
  padding: 20px 40px 20px 40px;
  justify-content: space-between;
}

label {
  font-weight: bold;
  font-size: 20px;
}

.area-icon {
  background-image: url(../../assets/imgs/Image/square.png);
}

.number-icon {
  background-image: url(../../assets/imgs/Image/square.png);
}

.people-icon {
  background-image: url(../../assets/imgs/Image/user.png);
}

.body-hotel-container {
  padding: 20px 180px 80px 180px;
}

h3 {
  font-weight: lighter;
}

.tabs {
  justify-content: center;
  /*border-bottom: solid #949494 2px;*/
}

.tab-item {
  width: 30%;
  text-align: center;
}

.tab-item label {
  cursor: pointer;
}

.tab-container {
  margin-top: 40px;
  padding-bottom: 24px;
}

.overview-overview {
  border-bottom: solid #949494 1px;
}

.hotel-image {
  background-image: url(../../assets/imgs/Image/hotel3.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 180px;
  height: 100px;
}

.hotel-image-list {
  justify-content: space-around;
}

.overview-room {
  border-bottom: solid #949494 1px;
}

.overview-room-info {
  justify-content: space-around;
}

.overview-room-img {
  background-image: url(../../assets/imgs/Image/hotel3.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 100%;
  height: 100px;
}

.overview-culinary {
  justify-content: space-around;
  padding: 20px 0px 0px 0px;
}

.overview-culinary-img {
  background-image: url(../../assets/imgs/Image/hotel2.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 30%;
  height: 200px;
}

.room-room-info {
  padding: 36px 200px 36px 200px;
}

.room-room-img {
  background-image: url(../../assets/imgs/Image/hotel3.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 40%;
  height: 240px;
}

.action-overview {
  justify-content: center;
  align-items: center;
}

.btn-default-overview {
  margin-right: 0px;
  background-color: #e89327;
  border: none;
  border-radius: 2px;
  padding: 4px 16px 4px 16px;
  cursor: pointer;
}
</style>