import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import vTitle from 'vuejs-title'
import Notifications from 'vue-notification'
import store from "@/js/store/store"
import VueSocketIO from 'vue-socket.io'


Vue.config.productionTip = false
Vue.use(VueRouter);
Vue.use(vTitle);
Vue.use(Notifications)
Vue.use(new VueSocketIO({
  debug: true,
  connection: 'http://localhost:3000',
}))

import Router from '../src/js/router/router.js'
var route = new Router();
var routes = route.routes;
const router = new VueRouter({
  mode: 'history',
  base : process.env.BASE_URL,
  routes
})

Vue.directive("click-outside", {
  bind: function(element, binding, vnode) {
    element.clickOutsideEvent = function(event) {
      //  check that click was outside the el and his children
      if (!(element === event.target || element.contains(event.target))) {
        // and if it did, call method provided in attribute value
        vnode.context[binding.expression](event);
        // binding.value(); run the arg
      }
    };
    document.body.addEventListener("click", element.clickOutsideEvent);
  },
  unbind: function(element) {
    document.body.removeEventListener("click", element.clickOutsideEvent);
  },
});

new Vue({
  render: h => h(App),
  router,
  store,
}).$mount('#app')
