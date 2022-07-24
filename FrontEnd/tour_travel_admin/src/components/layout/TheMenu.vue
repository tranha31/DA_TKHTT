<template>
  <div class="menu d-flex flex-column">
    <div class="menu-item">
        <router-link class="tab-router" to="/admin/dashboard" active-class="active">Bàn làm việc</router-link>
    </div>
    <div class="menu-item d-flex flex-column">
        <div class="tab-router level-1">Tour du lịch</div>
        <router-link class="tab-router level-2" to="/admin/tourtemplate" active-class="active">Danh sách tour mẫu</router-link>
        <router-link class="tab-router level-2" to="/admin/tourorder" active-class="active">Danh sách đặt tour</router-link>
        <router-link class="tab-router level-2" to="/admin/tourrequest" active-class="active">Danh sách chờ xác nhận</router-link>
        <router-link class="tab-router level-2" to="/admin/tourcancel" active-class="active">Danh sách ND hủy</router-link>
    </div>
    <div class="menu-item">
        <router-link class="tab-router" to="/admin/hotel" active-class="active">Khách sạn</router-link>
    </div>
    <div class="menu-item">
        <router-link class="tab-router" to="/admin/chat" active-class="active">Tin nhắn</router-link>
    </div>
    <div class="menu-item">
        <router-link class="tab-router" to="/admin/place" active-class="active">Điểm du lịch</router-link>
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