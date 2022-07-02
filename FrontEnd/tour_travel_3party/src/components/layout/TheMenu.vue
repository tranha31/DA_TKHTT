<template>
  <div class="menu d-flex flex-column">
    <div class="menu-item">
        <router-link class="tab-router" to="/third/rooms" active-class="active">Danh sách phòng</router-link>
    </div>
    <div class="menu-item">
        <router-link class="tab-router" to="/third/roombook" active-class="active">Danh sách đặt phòng</router-link>
    </div>
    <div class="menu-item">
        <router-link class="tab-router" to="/third/restaurant" active-class="active">Danh sách nhà hàng</router-link>
    </div>
    <div class="menu-item">
        <router-link class="tab-router" to="/third/restaurantbook" active-class="active">Danh sách đặt bàn</router-link>
    </div>
  </div>
</template>

<script>
export default {
    methods:{
    }
}
</script>

<style>
.menu{
    height: 100vh;
    width: 200px;
    background-color: #babec5;
}

.menu-item{
    width: 100%;
    height: auto;
    padding: 10px;
    cursor: pointer;
}

.menu-item:hover{
    background-color: #fff;
}

.tab-router{
    /* padding: 10px 0px 10px 5px; */
    color: #000;
    width: 100%;
    display: block;
}

.tab-router.active{
    font-weight: 600;
}

.level-2:hover{
    background-color: #babec5;
}

.tab-router.level-2{
    padding: 10px 0px 10px 20px;
}

.menu-item:has(.tab-router.active) .level-1{
    font-weight: 600;
}
</style>