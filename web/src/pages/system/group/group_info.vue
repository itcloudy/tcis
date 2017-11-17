<template>
    <div id="group-info">
        <el-row :gutter="20">
            <el-form :inline="true" ref="group_info" :model="group" class="form-read-only">
                <el-form-item label="用户组">
                        <span>{{group.name}}</span>
                </el-form-item>
            </el-form>  
        </el-row> 
    
        <el-tabs class='tcis-tabs' v-model="activeName" type="border-card" @tab-click="handleClick">
            <el-tab-pane label="权限明细" name="permission">
                <permission-list :permissions="group.permissions"/>
            </el-tab-pane>
            
        </el-tabs>
    </div>
</template>
<script>
    import  {default as PermissionList} from '@/pages/system/permission/permission_list';
    export default {
        name:"group_info",
        props:['group','checkChild','groupTasks','groupBugs','childGroups',"groupMembers"],
        data(){
            return{
                activeName:"permission",
            }
        },
        components:{
            PermissionList,
        }
    }
</script>
<style lang="scss" scoped>
    
</style>
