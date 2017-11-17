import babelpolyfill from 'babel-polyfill'
import Vue from 'vue'
import App from './App'
import router from './router';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import store from './store'
import Vuex from 'vuex'

import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
import localStore from '@/utils/local_store';
import stringTimeFormat from '@/utils/filters';
import axios from 'axios';
const XSRFCOOKIENAME = 'csrftoken';
const XSRFHEADERNAME = 'X_CSRFTOKEN';
axios.defaults.xsrfCookieName = XSRFCOOKIENAME;
axios.defaults.xsrfHeaderName = XSRFHEADERNAME;

Vue.prototype.$ajax = axios;


import echarts from 'echarts';
import "@/styles/index.scss";
Vue.prototype.$echarts = echarts;
Vue.filter('stringTimeFormat', stringTimeFormat);

Vue.use(ElementUI)

Vue.use(Vuex)

router.beforeEach((to, from, next) => {
    // NProgress.start();
    if (to.path == '/login') {
        localStore.remove('userinfo');
        next();
    } else {
        let user = JSON.parse(localStore.get('userinfo'));
        if (!user) {
            next({ path: '/login' });
        } else {
            next();
        }
    }
});

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')