<template>
  <div class="header d-flex">
      <div class="logo"></div>
      <div class="flex-1"></div>
      <div class="header-container w-half d-flex">
        <div class="header-item-list d-flex">
          <router-link class="router-link" to="/test">
            <div class="item-link">Danh lam</div>
          </router-link>
          <router-link class="router-link" to="/tour">
            <div class="item-link">Tour</div>
          </router-link>
          <router-link class="router-link" to="/hotel">
            <div class="item-link">Khách sạn</div>
          </router-link>
          <router-link class="router-link" to="/register">
            <div class="item-link">Đăng ký</div>
          </router-link>
          <router-link class="router-link" to="/login">
            <div class="item-link">Đăng nhập</div>
          </router-link>
          <router-link class="router-link link-user" to="/user">
            <div class="item-link user"></div>
          </router-link>
        </div>
        <div class="small-header">
          <div class="user"></div>
          <div class="mi mi-24 menu-image" @click="showMenu"></div>
          <div v-if="showM" class="menu-item">
            <router-link class="router-link" to="/test">
              <div class="item-link">Danh lam</div>
            </router-link>
            <router-link class="router-link" to="/tour">
              <div class="item-link">Tour</div>
            </router-link>
            <router-link class="router-link" to="/hotel">
              <div class="item-link">Khách sạn</div>
            </router-link>
            <router-link class="router-link" to="/register">
              <div class="item-link">Đăng ký</div>
            </router-link>
            <router-link class="router-link" to="/login">
              <div class="item-link">Đăng nhập</div>
            </router-link>
          </div>
        </div>
      </div>
      
      
  </div>
</template>

<script>
export default {
    name: "Header",
    components: {},
    props: {},
    data(){
        return{
          showM : false
        }
    },
    methods:{
      /**
       * Hiển thị option
       */
      showMenu(){
        this.showM = !this.showM;
      }
    }
}
</script>

<style>
@import url(../../css/content/header.css);
</style>