<template>
    <div id="user-info">
        <el-row :gutter="20" >
            <el-form :inline="true" ref="userForm" :model="userForm" class="form-read-only">
                <el-col :span="24">
                    <el-form-item label="用户名">
                        <span>{{userForm.username}}</span>
                    </el-form-item>
                    <el-form-item label="中文">
                        <span>{{userForm.username_zh}}</span>
                    </el-form-item>
                    <el-form-item label="邮箱">
                        <span>{{userForm.email}}</span>
                    </el-form-item>
                    <el-form-item label="电话">
                        <span>{{userForm.mobile}}</span>
                    </el-form-item>
                    <el-form-item label="超级用户">
                        <span v-if="userForm.is_superuser">是</span>
                        <span v-else>否</span>
                    </el-form-item>
                    <el-form-item label="是否有效">
                        <span v-if="userForm.is_active">是</span>
                        <span v-else>否</span>
                    </el-form-item>
                    <el-form-item label="所属部门">
                        <span v-if="userForm.department">{{userForm.department.name}}</span>
                        <span v-else></span>
                    </el-form-item>
                    <el-form-item label="职位">
                        <span v-if="userForm.position">{{userForm.position.name}}</span>
                        <span v-else></span>
                    </el-form-item>
                    <el-form-item label="最近登录">
                        <span>{{userForm.last_login | stringTimeFormat}}</span>
                    </el-form-item>
                </el-col>
            </el-form>  
        </el-row> 
        <el-tabs class='user-tabs' v-model="activeName" type="border-card" @tab-click="handleClick">
            <el-tab-pane label="用户组" name="group">
                <group-list  :groups="groups" />
            </el-tab-pane>
            <el-tab-pane label="权限信息" name="project_bug">
                <permission-list :permissions="permissions"/>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>
<script>
    
    import localStore from '@/utils/local_store'; 
    import  {SERVER_USER} from '@/server_address';
    import  {default as GroupList} from '@/pages/system/group/group_list';
    import  {default as PermissionList} from '@/pages/system/permission/permission_list';
    export default {
        name:"user-info",
        props:["userForm","permissions","groups"],
        data(){
            return{
                formTopBtns:{
                    edit:true,
                    create:this.$store.state.userinfo.is_superuser
                },
                userForm:{},
                activeName:'group',
                groups:[],
                permissions:[],
            }
        },
        components:{
            GroupList,
            PermissionList,
        },
        methods:{
             
            handleClick(val){
            },
            formTopAction(action){
                if(action=='edit'){
                    this.$router.push('/user/' + this.userForm.id);
                }else if(action =='create'){
                    this.$router.push('/user/new');
                } 
            }
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

