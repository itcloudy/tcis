<template>
    <div id="project-home" :loading="loading">
        <view-switch :views="view_list" :activeView="activeView" @switchView="switchView"/>
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[20,40,80]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        <el-row :gutter="20" class="main-content">
            <project-kanban v-if="activeView=='kanban'" :projects="projects"/>
            <project-list v-if="activeView=='list'" :projects="projects"/>
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_PROJECT} from '@/server_address';
    import localStore from '@/utils/local_store'; 
    import  {default as ProjectKanban} from './project_kanban';
    import  {default as ProjectList} from './project_list';
    import  {default as Pagination} from '@/pages/common/Pagination';
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    export default {
        name:"project_home",
        data(){
            let activeView = localStore.get("project_home_view");
            if (activeView == "" || activeView == null ){
                activeView = "kanban";
            }
            return{
                view_list:["kanban","list"],
                activeView:activeView,
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                projects:[]
            }
        },
        components:{
            ProjectKanban,
            ProjectList,
            ViewSwitch,
            Pagination
        },
        methods:{
            getAllProject(){
                this.loading = true;
                this.$ajax.get(SERVER_PROJECT,{
                        params:{
                            page:this.page,
                            page_size:this.pageSize
                        }
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projects = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.activeView = view;
                localStore.set("project_home_view",view);
            },
            pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllProject();
            }
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllProject();
            });
        }
    }
</script>
