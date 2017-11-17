<template>
    <div class="user-detail">
        <view-switch :views="['list']"  @switchView="switchView"/>
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <div class="main-content">
            <user-from v-if="activeView =='form'" :user="newUserForm" />
            <user-info v-if="activeView =='info'" 
            @changeChildInfo="changeChildInfo"
            :checkChild="checkChild" 
            :userForm="userForm" 
            :groups="groups"
            :permissions="permissions">
        </div>
    </div>
</template>
<script>
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    import  {SERVER_USER} from '@/server_address'; 
    import localStore from '@/utils/local_store'; 
    import  {default as FormTop} from '@/pages/common/form_top';
    import  {default as UserFrom} from './user_form';
    import  {default as UserInfo} from './user_info';
    export default {
        name:"user_detail",
        data(){
            let activeView = localStore.get("user_detail_view");
            if (activeView == "" || activeView == null ){
                activeView = "info";
            }
            return{
                formTopBtns:{
                    create:true,
                },
                activeView:activeView,
                loadding:false,
                userForm:{},
                groups:[],
                permissions:[],
                newUserForm:{},
            }
        },
        components:{
            UserFrom,
            UserInfo,
            FormTop,
            ViewSwitch,
        },
        methods:{
            getUserInfo(){
                this.loadding = true;
                let id  = this.$route.params.id;
                if (id!='new'){
                    this.userForm.id = id;
                    this.$ajax.get(SERVER_USER+this.userForm.id).then(response=>{
                        this.loadging = false;
                        let status = response['status'];
                        let data = response['data'];
                        if (status ==200){
                            this.userForm = data;
                            this.groups = this.userForm.groups;
                            let groupLen = this.groups.length;
                            let permissionDict = {};
                            for(let i=0;i<groupLen;i++){
                                let group  = this.groups[i];
                                let permissionLen = group.permissions.length;
                                for(let j=0;j<permissionLen;j++){
                                    let permission = group.permissions[j];
                                    permissionDict[permission.id] = permission
                                }
                            }
                            let permissions = [];
                            for(let key in permissionDict){
                                permissions.push(permissionDict[key]);
                            }
                            this.permissions = permissions;                            
                        }
                    });
                }else{
                    this.userForm = this.newUserFrom;
                }
            },
            switchView(view){
                localStore.set("user_home_view",view);
                this.$router.push('/user/');
            },
        },
        created:function(){
            this.getUserInfo();
        },
        watch: {
            // 如果路由有变化，会再次执行该方法
            '$route': 'getUserInfo'
        },
    }
</script>

