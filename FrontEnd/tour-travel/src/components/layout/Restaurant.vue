<template>
  <div class="restaurant-page-container d-flex flex-column">
    <div class="header-res-container d-flex">
      <div class="header-restaurant-info">
        <div>
          <label>{{ restaurantName }}</label>
        </div>
        <div class="mt-12">
          <span class="mr-12">
            <div class="icon white mi-24 location-icon d-flex" style="display: inline-block"></div>
            {{ restaurantAddr }}
          </span>
          <span class="mr-12">
            <div class="icon white mi-24 phone-icon d-flex" style="display: inline-block"></div>
            {{ restaurantPhone }}
          </span>
          <span class="mr-12">
            <div class="icon white mi-24 rate-icon d-flex" style="display: inline-block"></div>
            {{ restaurantRate }}
          </span>
        </div>
      </div>
      <div>
        <button
            class="btn-default white"
            @click="reservationTable()"
        >
          Reservation now
        </button>
      </div>
    </div>
    <div class="body-res-container">
      <div class="body-restaurant-info">
        <label>{{ restaurantName }}</label>
        <h3>{{ restaurantDescription }}</h3>
        <span style="display: inline-block" class="mr-20 mt-12">
          <div class="icon black mi-24 time-icon d-flex" style="display: inline-block"></div>
          <span style="font-size: 16px;">Time</span>
          <h3>{{ restaurantDateStart }} - {{ restaurantDateEnd }}</h3>
        </span>
        <span style="display: inline-block" class="mr-20 mt-12">
          <div class="icon black mi-24 food-icon d-flex" style="display: inline-block"></div>
          <span style="font-size: 16px;">Food</span>
          <h3>{{ restaurantFood }}</h3>
        </span>
        <span style="display: inline-block" class="mr-20 mt-12">
          <div class="icon black mi-24 phone2-icon d-flex" style="display: inline-block"></div>
          <span style="font-size: 16px;">Contact</span>
          <h3>{{ restaurantPhone }}</h3>
        </span>
      </div>
      <div class="order-table-container d-flex mt-12">
        <div class="menu mr-20">
          <label>Menu</label>
          <perfect-scrollbar>
            <div v-for="dish in menu" :key="dish.id" class="dish-item d-flex">
              <div>
                <div class="icon black mi-18 food-icon" style="display: inline-block"></div>
                <span>{{ dish.name }}</span>
              </div>
              <div>{{ dish.price }}</div>
<!--              <InputInfoTemplate-->
<!--                  item="Number"-->
<!--                  :can-editing="true"-->
<!--                  input-type="number"-->
<!--                  display-inline="inline-block"-->
<!--              />-->
            </div>
          </perfect-scrollbar>
        </div>
        <div class="order d-flex flex-column">
          <label>Reservation</label>
          <div class="order-form">
            <InputInfoTemplate
                item="Number of person"
                :can-editing="true"
                input-type="number"
                width-input="100%"
            />
            <InputInfoTemplate
                item="Time"
                :can-editing="true"
                input-type="text"
                width-input="100%"
            />
          </div>
          <div>
            <button
                class="btn-default white mt-12"
                @click="reservationTable()"
                style="margin-left: 50%; margin-top: 50px;"
            >
              Reservation now
            </button>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import {PerfectScrollbar} from 'vue2-perfect-scrollbar'
// import knife from '../../assets/imgs/Image/knife.png'
import InputInfoTemplate from "@/components/base/InputInfoTemplate"
import Footer from "@/components/layout/TheFooter"

export default {
  name: 'Restaurant',
  components: {
    PerfectScrollbar,
    // knife
    InputInfoTemplate,
    Footer
  },
  data() {
    return {
      restaurantName: 'Nha hang 01',
      restaurantAddr: '12 HBT, HN',
      restaurantPhone: '0987765320',
      restaurantRate: '5',
      restaurantDateStart: '8 AM',
      restaurantDateEnd: '9 PM',
      restaurantFood: "Chinese food",
      restaurantDescription: 'Garnet là nhà hàng À la Carte với phong cách thiết kế hiện đại, cùng với thực đơn đa dạng mang đến cho khách hàng của Vinpearl Condotel Empire Nha Trang những trải nghiệm ẩm thực tinh tế và không gian sang trọng, lãng mạn.',
      menu: [
          {
            name: 'Mon 1',
            price: '1.500.000'
          },
        {
          name: 'Mon 1',
          price: '1.500.000'
        }
      ],
      image: '../../assets/imgs/Image/white-place.png'
    }
  },
  methods: {
    reservationTable() {

    }
  }
}
</script>

<style>
@import url(../../css/common/icon.css);
.restaurant-page-container {
}

.header-res-container {
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

.location-icon {
  background-image: url(../../assets/imgs/Image/white-place.png);
}

.phone-icon {
  background-image: url(../../assets/imgs/Image/phone.png);
}

.rate-icon {
  background-image: url(../../assets/imgs/Image/star.png);
}

.time-icon {
  background-image: url(../../assets/imgs/Image/alarm-clock-32.png);
}

.food-icon {
  background-image: url(../../assets/imgs/Image/knife.png);
}

.phone2-icon {
  background-image: url(../../assets/imgs/Image/phone-7-32.png);
}

.body-res-container {
  padding: 20px 180px 80px 180px;
}

h3 {
  font-weight: lighter;
}

.order-table-container {
}

.menu {
  border: solid #949494 1px;
  border-radius: 4px;
  width: 30%;
  padding: 20px;
}

.order {
  width: 30%;
  border: solid #949494 1px;
  border-radius: 4px;
  padding: 10px;
}

.dish-item {
  justify-content: space-between;
}

</style>