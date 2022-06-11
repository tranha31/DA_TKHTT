<template>
  <div class="restaurant-page-container">
    <div class="header">
      <div class="header-restaurant-info">
        <label>{{ restaurantName }}</label>
        <span>{{ restaurantAddr }}</span>
        <span>{{ restaurantPhone }}</span>
        <span>{{ restaurantRate }}</span>
      </div>
      <div>
        <button
            class="btn-default"
            @click="reservationTable()"
        >
          Reservation now
        </button>
      </div>
    </div>
    <div class="body">
      <div class="body-restaurant-info">
        <label>{{ restaurantName }}</label>
        <h2>{{ restaurantDescription }}</h2>
        <span>
          <h3>Time</h3>
          <h3>{{ restaurantDateStart - restaurantDateEnd }}</h3>
        </span>
        <span>
          <h3>Food</h3>
          <h3>{{ restaurantFood }}</h3>
        </span>
        <span>
          <h3>Contact</h3>
          <h3>{{ restaurantPhone }}</h3>
        </span>
      </div>
      <div class="order-table-container">
        <div class="menu">
          <label>Menu</label>
          <perfect-scrollbar>
            <div v-for="dish in menu" :key="dish.id">
              <div class="dish-icon"></div>
              <div>{{ dish.name }}</div>
              <div>{{ dish.price }}</div>
              <InputInfoTemplate
                  item="Number"
                  :can-editing="true"
                  input-type="number"
                  display-inline="inline-block"
              />
            </div>
          </perfect-scrollbar>
        </div>
        <div class="order">
          <label>Reservation</label>
          <div class="order-form">
            <InputInfoTemplate
                item="Number of person"
                :can-editing="true"
                input-type="number"
            />
            <InputInfoTemplate
                item="Time"
                :can-editing="true"
                input-type="text"
            />
          </div>
          <div>
            <button
                class="btn-default"
                @click="reservationTable()"
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
      restaurantName: '',
      restaurantAddr: '',
      restaurantPhone: null,
      restaurantRate: null,
      restaurantDateStart: null,
      restaurantDateEnd: null,
      restaurantFood: null,
      restaurantDescription: '',
      menu: []
    }
  },
  methods: {
    reservationTable() {

    }
  }
}
</script>

<style>

</style>