import Vue from 'vue'
import Vuex from 'vuex'

// 根级state、actions、getters、mutations
import state from './state';
import actions from './actions';
import getters from './getters';
import mutations from './mutations';


Vue.use(Vuex)
const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
    state,
    actions,
    getters,
    mutations,
    modules: {
//        adminPartner, //合作伙伴

    },
    strict: debug,
})
