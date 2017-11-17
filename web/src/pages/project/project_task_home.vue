<template>
    <div id="project-task" :loading="loading">
        <view-switch :views="view_list" :activeView="activeView" @switchView="switchView"/>
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[20,40,80]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        <el-row :gutter="20" class="main-content">
            <project-task-list  v-if="activeView=='list'" :projectTasks="projectTasks"/>
            <project-task-kanban v-if="activeView=='kanban'" @changeProjectTaskView="changeProjectTaskView"/>
            <project-task-gantt v-if="activeView=='gantt'" @changeProjectTaskView="changeProjectTaskView"/>
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_PROJECT,SERVER_PROJECT_TASK} from '@/server_address';
    import  {default as ProjectTaskList} from './project_task_list';
    import  {default as ProjectTaskKanban} from './project_task_kanban';
    import  {default as ProjectTaskGantt} from './project_task_gantt';
    import  {default as Pagination} from '@/pages/common/Pagination';
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    import  {default as FormTop} from '@/pages/common/form_top';
    import localStore from '@/utils/local_store'; 
    export default {
        name:"project_task_home",
        data(){
            let activeView = localStore.get("project_task_home_view");
            if (activeView == "" || activeView == null ){
                activeView = "kanban";
            }
            return{
                formTopBtns:{
                    create:true,
                },
                view_list:["kanban","list","gantt"],
                activeView:activeView,
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                projectTasks:[]
            }
        },
        components:{
            ProjectTaskList,
            ProjectTaskKanban,
            ProjectTaskGantt,
            ViewSwitch,
            Pagination,
            FormTop,
        },
        methods:{
            getAllProjectTask(){
                // 任务明细只在list下获得
                if (this.activeView != 'list'){
                    return;
                }
                this.loading = true;
                this.projectTasks = [];
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
                
                this.$ajax.get(SERVER_PROJECT_TASK,{
                        params:params
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectTasks = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.setLocalView(view);
                // 看板显示所有项目的任务情况，其他视图根据project_id进行过滤
                if(view=="list" ){
                    this.getAllProjectTask(this.pageSize,this.page);
                }else if (view=="kanban"){
                    this.$router.push("/project_task/");
                }else if(view=="gantt"){
                    let url = "/project_task/";
                    if (this.$route.query.project_id){
                        url += "?project_id=" +this.$route.query.project_id;
                    }
                    this.$router.push(url);
                }
            },
            setLocalView(view){
                this.activeView = view;
                localStore.set("project_task_home_view",view);
            },
            changeProjectTaskView(projectId,view){
                this.activeView = view;
                this.switchView(view);
                this.$router.push("/project_task/?project_id=" + projectId );
            },
            pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllProjectTask();
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
                this.getAllProjectTask();
            });
        },
        watch:{
            '$route':function(val,oldVal){
                if (val != oldVal){
                    this.getAllProjectTask();
                }
            }
        }
    }
</script>
