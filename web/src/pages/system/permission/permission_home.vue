<template>
    <div id="permission-home" :loading="loading">
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[15,40,80,200]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        <el-button style="display: inline-block;"  size="small" @click="translatePermissionName" >翻译</el-button>
        <el-row :gutter="20" class="main-content">
            <permission-list :permissions="permissions"/>
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_PERMISSION,SERVER_PERMISSION_TRANSLATE} from '@/server_address';
    import localStore from '@/utils/local_store'; 
    import  {default as PermissionList} from './permission_list';
    import  {default as Pagination} from '@/pages/common/Pagination';
    import { mapState } from 'vuex';
    export default {
        name:"permission_home",
        data(){
            return{
                pageSize:15,//每页数量
                total:0,//总数量
                page:1,//当前页
                permissions:[]
            }
        },
        components:{
            PermissionList,
            Pagination
        },
        methods:{
            getAllPermission(){
                this.loading = true;
                this.$ajax.get(SERVER_PERMISSION,{
                        params:{
                            page:this.page,
                            page_size:this.pageSize
                        }
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.permissions = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.activeView = view;
                localStore.set("permission_home_view",view);
            },
            pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllPermission();
            },
            translatePermissionName(){
                this.loading = true;
                this.$ajax.get(SERVER_PERMISSION_TRANSLATE).then(response=>{
                    this.loading = false;
                    if (status ==200){
                        this.$notify({
                            title: '成功',
                            message: '翻译完成，请刷新页面',
                            type: 'success'
                        });
                    }
                });
            }
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllPermission();
            });
        }
    }
</script>
