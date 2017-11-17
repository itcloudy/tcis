import * as types from './mutations-types'

export default {
    [types.GLOBAL_SET_USERINFO](state, userinfo) {
        state.userinfo = userinfo;
        state.isBackgroundUser = userinfo.isBackground;
    },

}