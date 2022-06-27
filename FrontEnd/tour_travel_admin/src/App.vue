<template>
  <div id="app">
    <TheMenu/>
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import TheMenu from './components/layout/TheMenu.vue'


export default {
  name: 'App',
  components: {
    TheMenu
  }
}
</script>

<style>
@import url(css/common/common.css);
@import url(css/common/toast.css);
#app{
  position: relative;
}
.main-content{
  position: absolute;
  top: 0px;
  left: 200px;
  width: calc(100vw - 200px);
  height: 100vh;
}
</style>
