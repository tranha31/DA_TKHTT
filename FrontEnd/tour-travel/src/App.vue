<template>
  <div id="app">
    <TheHeader></TheHeader>
    <div class="main-content">
      <router-view></router-view>
    </div>
    <notifications
        group="default"
        :closeOnClick="true"
        position="bottom right"
        :duration="-1"
        :ignoreDuplicates="true"
    />
    <notifications
        group="user-found"
        :closeOnClick="true"
        :duration="-1"
        position="bottom right"
        :ignoreDuplicates="true"
    />
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

.vue-notification {
  padding: 10px;
  margin: 0 5px 5px;

  font-size: 12px;

  color: #ffffff;
  background: #44a4fc;
  border-left: 5px solid #187fe7;
}

.vue-notification.warn {
  background: #ffb648;
  border-left-color: #f48a06;
  position: relative;
}

.vue-notification::before {
   content: '\00D7';
   position: absolute;
   right: 5px;
   top: 0;
 }

.vue-notification.error {
   background: #e54d42;
   border-left-color: #b82e24;
   position: relative;
}

.vue-notification.success {
  background: #68cd86;
  border-left-color: #42a85f;
  position: relative;
}

.vue-notification.success::before {
   content: '\00D7';
   position: absolute;
   right: 5px;
   top: 0;
 }
</style>
