<template>
    <el-col :span="12"  :group="group" class="group-card" v-if="show">
        <el-card class="box-card">
            <div slot="header" class="clearfix" >
                <span @click="goGroup" style="color:rgb(102, 177, 255);font-size:150%;">{{group.name}}</span>
                <i class="el-icon-info" style="color:rgb(102, 177, 255);font-size:150%;" @click="goGroup"></i>
                <i style="float: right;margin-left:10px;color:red;font-size:150%;"  @click="deleteDom"  class="el-icon-circle-close"></i>
            </div>
            <div class="group-card">
                <permission-list :permissions="group.permissions"/>
            </div>
        </el-card>
    </el-col>
</template>
<script>
    import  {default as PermissionList} from '@/pages/system/permission/permission_list';
    export default {
        name:"group-card",
        props:['group'],
        data(){
            return{
                show:true
            }
        },
        components:{
            PermissionList,
        },
        methods:{
            deleteDom(){
                this.show = false;
            },
            goGroup(){
                this.$router.push("/group/" +this.group.id);
            }
        }
         

    }
</script>
<style lang="scss" scoped>
    .group-card{
        padding-bottom: 5px;
        padding-top: 5px;
    }
</style>

