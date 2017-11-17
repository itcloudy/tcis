<template>
    <div id="project-bug" :loading="loading">
        <view-switch :views="view_list" :activeView="activeView" @switchView="switchView"/>
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[20,40,80,160,320]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        
        <el-row :gutter="20" class="main-content">
            <project-bug-list  v-if="activeView=='list'" :projectBugs="projectBugs"/>
            <project-bug-kanban v-if="activeView=='kanban'" @changeProjectBugView="changeProjectBugView"/>
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_PROJECT,SERVER_PROJECT_BUG} from '@/server_address';
    import  {default as Pagination} from '@/pages/common/Pagination';
    import  {default as ProjectBugList} from './project_bug_list';
    import  {default as ProjectBugKanban} from './project_bug_kanban';
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    import  {default as FormTop} from '@/pages/common/form_top';
    import localStore from '@/utils/local_store'; 
    export default {
        name:"project_bug_home",
        data(){
            let activeView = localStore.get("project_bug_home_view");
            if (activeView == "" || activeView == null ){
                activeView = "kanban";
            }
            return{
                formTopBtns:{
                    create:true,
                },
                view_list:["kanban","list"],
                activeView:activeView,
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                projectBugs:[]
            }
        },
        components:{
            ProjectBugList,
            ProjectBugKanban,
            ViewSwitch,
            Pagination,
            FormTop,
        },
        methods:{
            getAllProjectBug(){
                // 任务明细只在list下获得
                if (this.activeView != 'list'){
                    return;
                }
                this.loading = true;
                this.projectBugs = [];
                let params = {
                    page: this.page,
                    page_size: this.pageSize,
                };
                if (this.$route.query.project_id){
                    params.project_id = this.$route.query.project_id;
                }
                if (this.$route.query.check_child){
                    params.check_child = this.$route.query.check_child;
                }
                this.$ajax.get(SERVER_PROJECT_BUG,{
                        params:params
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectBugs = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.setLocalView(view);
                // 看板显示所有项目的任务情况，其他视图根据project_id进行过滤
                if(view=="list" ){
                    this.getAllProjectBug(this.pageSize,this.page);
                }else if (view=="kanban"){
                    this.$router.push("/project_bug/");
                } 
            },
            setLocalView(view){
                this.activeView = view;
                localStore.set("project_bug_home_view",view);
            },
            changeProjectBugView(projectId,view){
                this.activeView = view;
                this.switchView(view);
                this.$router.push("/project_bug/?project_id=" + projectId );
            },
            pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllProjectBug();
            }
        },
        created:function(){
            this.$nextTick(function(){
                if (this.$route.query.view){
                    let view = this.$route.query.view;
                    for(let i = 0; i < this.view_list.length; i++){
                        if(view === this.view_list[i]){
                            this.setLocalView(view);
                        }
                    }
                }
                this.getAllProjectBug();
            });
        },
        watch:{
            '$route':function(val,oldVal){
                if (val != oldVal){
                    this.getAllProjectBug();
                }
            }
        }
    }
</script>
