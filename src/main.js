import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import { Button, Select } from 'element-ui';
import axios from 'axios'
import 'normalize.css'
import VCalendar from 'v-calendar';
import $ from 'jquery';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

// import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import './assets/css/vendor.css'
import './assets/css/style.css'
import './assets/css/responsive.css'

// import './assets/js/main'
// import './assets/js/vendor'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.use(ElementUI);
// Use v-calendar & v-date-picker components
Vue.use(VCalendar, {
  componentPrefix: 'vc',  // Use <vc-calendar /> instead of <v-calendar />
});

Vue.config.productionTip = false
// 全局注册 $
Vue.prototype.$ = $

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')


