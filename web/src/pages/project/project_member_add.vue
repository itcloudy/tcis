<template>
    <el-dialog  :visible="dialogProjectMemberAddAdd" width="25%" center :show-close="false" title="添加项目成员">
        <el-form :model="passwordForm" :rules="rules" ref="resetPwd">
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="passwordForm.password" />
            </el-form-item>
             <el-form-item label="确认密码"  prop="confirmPassword">
                <el-input type="password" v-model="passwordForm.confirmPassword" />
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="cancelProjectMemberAddAdd">取 消</el-button>M
            <el-button type="primary" @click="confirmProjectMemberAddAdd">确 定</el-button>
        </div>
    </el-dialog>
</template>
<script>

    import  {SERVER_USER_RESET_PASSWORD} from '@/server_address';
    export default {
        name:"reset_password",
        props:["userId","dialogProjectMemberAddAdd"],
        data(){
            var validatePass1 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if(!(/^[a-zA-Z0-9_-]{6,16}$/.test(value))){
                    callback(new Error('密码至少6位,由大小写字母和数字,-,_组成'));
                } else {
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入确认密码'));
                } else if(!(/^[a-zA-Z0-9_-]{6,16}$/.test(value))){
                    callback(new Error('密码至少6位,由大小写字母和数字,-,_组成'));
                } else if (value !== this.passwordForm.password) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return{
                passwordForm:{
                    password:"",
                    confirmPassword:"",
                },
                rules: {
                    password:[
                        { required: true, message: '请输入密码', trigger: 'blur' },
                        { validator: validatePass1, trigger: 'blur' }
                    ],
                    confirmPassword:[
                        { required: true, message: '请输入确认密码', trigger: 'blur' },
                        { validator: validatePass2, trigger: 'blur' }
                    ],
                }
            }
        },
        methods:{
            confirmProjectMemberAddAdd(){
                this.$refs["resetPwd"].validate((valid)=>{
                    if(valid){
                        let params ={
                            user_id:this.userId,
                            password:this.passwordForm.password,
                            confirm_password:this.passwordForm.confirmPassword
                        }
                        this.$ajax.post(SERVER_USER_RESET_PASSWORD,params).then(response=>{
                            if(response.status==200){
                                
                            }
                        });
                        this.$emit("dialogProjectMemberAddAddVisible");
                    } 
                });

                
            },
            cancelProjectMemberAddAdd(){
                this.$emit("dialogProjectMemberAddAddVisible");
            }
        },
        watch:{
            dialogProjectMemberAddAdd:function(){
                if (!this.dialogProjectMemberAddAdd){
                    this.$refs["resetPwd"].resetFields();
                }
            }
        }
        
    }
</script>

