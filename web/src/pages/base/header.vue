<template>
    <el-header style="text-align: right; font-size: 12px">
        <el-dropdown @command="handleCommand">
            <span>{{userinfo.username_zh  || userinfo.username}}</span>
            <i class="el-icon-arrow-down el-icon--right"></i>
            <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="logout">退出</el-dropdown-item>
                <el-dropdown-item command="self_info">个人信息</el-dropdown-item>
                <el-dropdown-item command="go_admin" v-if="userinfo.is_superuser">进入后台</el-dropdown-item>
            </el-dropdown-menu>
        </el-dropdown>

    </el-header>
</template>
<script>
    import  {SERVER_USER_LOGOUT} from '@/server_address';
    import localStore from '@/utils/local_store';
    import { mapState } from 'vuex';
    export default {
        name:"header",
        data(){
            return{

            }
        },
        computed:{
           ...mapState({
               userinfo: state => state.userinfo
           })
        },
        methods:{
             handleCommand(command) {
                if (command =="logout"){
                    this.$ajax.get(SERVER_USER_LOGOUT).then(response=>{
                        if (response.status ==200){
                            localStore.remove('userinfo');
                            this.$router.push("/login");
                        }
                    });
                }else if(command =="self_info"){
                    this.$router.push("/user/"+this.userinfo.id);

                }else if(command =="go_admin"){

                }
            }
        }
    }
</script>

