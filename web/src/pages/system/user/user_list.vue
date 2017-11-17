<template>
    <div>
        <el-table
            v-loading.body="loading"
            ref="multipleTable"
            :data="users"
            @row-dblclick = "goUserDetail"
            style="width: 100%">
            <el-table-column
            type="selection"
            width="55">
            </el-table-column>
            <el-table-column
            prop="username"
            label="用户名">
            </el-table-column>
            <el-table-column
            prop="username_zh"
            label="用户名中文">
            </el-table-column>
             <el-table-column
            prop="email"
            label="邮箱">
            </el-table-column>
            <el-table-column
            prop="mobile"
            label="电话">
            </el-table-column>
            <el-table-column
            label="所属部门">
                <template v-if="scope.row.department" scope="scope">
                {{scope.row.department.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="职位">
                <template v-if="scope.row.position" scope="scope">
                {{scope.row.position.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="是否有效">
                <template scope="scope"> 
                    <span v-if="scope.row.is_active">是</span>
                    <span v-else>否</span>
                </template>
            </el-table-column>
            <el-table-column
            label="超级用户">
                <template scope="scope"> 
                    <span v-if="scope.row.is_superuser">是</span>
                    <span v-else>否</span>
                </template>
            </el-table-column>
            <el-table-column
            label="上次登录时间">
                <template v-if="scope.row.last_login" scope="scope">
                {{scope.row.last_login | stringTimeFormat}}
                </template>
            </el-table-column>
            <el-table-column label="操作" v-if="userinfo.is_superuser" align="center">
                <template scope="scope" >
                    <el-button
                    v-if="scope.row.is_active"
                    type="danger"
                    size="mini"
                    class="table-btn"
                    @click="disableUser(scope.$index, scope.row)">无效</el-button>
                    <el-button
                    v-else
                    type="danger"
                    size="mini"
                    class="table-btn"
                    @click="activeUser(scope.$index, scope.row)">有效</el-button>
                    <el-button
                    type="info"
                    size="mini"
                    class="table-btn"
                    @click="resetPassword(scope.$index, scope.row)">重置密码</el-button>
                </template>
            </el-table-column>
        </el-table>
        <reset-password 
        :dialogResetPassword="dialogResetPassword" 
        :userId="resetUserId" 
        @dialogResetPasswordVisible="dialogResetPasswordVisible"/>
    </div>
</template>
<script>
    import  {SERVER_USER_ACTIVE} from '@/server_address';
    import  {default as ResetPassword} from './reset_password';
    import { mapState } from 'vuex';
    export default {
        name:"",
        props:['users'],
        data(){
            return{
                resetUserId:null,
                dialogResetPassword:false,
            }
        },
        components:{
            ResetPassword,
        },
        methods:{
            goUserDetail(row, event){
                this.$router.push('/user/'  +row.id);
            },
            userActiveAction(userIds,active){
                let params = {
                    user_ids:userIds,
                    is_active:active
                }
                this.$ajaxt.put(SERVER_USER_ACTIVE,params).then(response=>{
                    if (response.status ==200){
                        this.$message({
                            type: 'success',
                            message: '操作成功'
                        }); 
                    }
                }).catch(() => {
                    this.$message({
                        type: 'error',
                        message: '操作失败'
                    });          
                });
            },
            disableUser(index,row){
                this.$confirm('无效之后该用户不能登录，是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.userActiveAction([row.id],false);
                }).catch(info => {
                    this.$message({
                        type: 'info',
                        message: '已取消无效'
                    });          
                });
            },
            activeUser(index,row){
                this.$confirm('有效之后该用户可以登录，是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.userActiveAction([row.id],true);
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消有效'
                    });          
                });
            },
            resetPassword(index,row){
                this.resetUserId = row.id;
                this.dialogResetPassword = true;
            },
            dialogResetPasswordVisible(){
                this.dialogResetPassword= false;
            }
        },
        computed:{
           ...mapState({
               userinfo: state => state.userinfo
           })
        }
    }
</script>
