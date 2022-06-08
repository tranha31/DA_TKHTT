<template>
  <div id="app">
    <TheHeader></TheHeader>
    <div class="main-content">
      <TheTestUI></TheTestUI>
    </div>
  </div>
</template>

<script>
import TheHeader from './components/layout/TheHeader.vue'
import TheTestUI from './components/layout/TheTestUI.vue'
export default {
  name: 'App',
  components: {
    TheHeader,
    TheTestUI
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
  top: 60px;
  left: 0px;
  width: 100vw;
  height: calc(100vh - 60px);
}
</style>
