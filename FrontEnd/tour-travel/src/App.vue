<template>
  <div id="app">
    <TheHeader></TheHeader>
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import TheHeader from './components/layout/TheHeader.vue'
export default {
  name: 'App',
  components: {
    TheHeader
  }
}
</script>

<style>
@import url(css/common/common.css);
@import url(css/common/toast.css);
@import url(css/common/color.css);
#app{
  position: relative;
  overflow-x: hidden;
  height: 100vh;
}
.main-content{
  position: absolute;
  top: 60px;
  left: 0px;
  width: 100vw;
  height: calc(100vh - 60px);
}
</style>
