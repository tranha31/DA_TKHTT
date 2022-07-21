<template>
  <div id="app">
    <TheMenu/>
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
