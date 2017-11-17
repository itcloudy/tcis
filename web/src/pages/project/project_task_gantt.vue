<template>
    <div id="project-task-gantt-card">
        <project-task-gantt-card v-for="(project,index) in projects" :project="project" :key="index" @changeProjectTaskView='changeProjectTaskView' />
    </div>
</template>
<script>
    import  {SERVER_PROJECT,SERVER_PROJECT_TASK_GANTT} from '@/server_address';
    import  {default as ProjectTaskGanttCard} from './project_task_gantt_card';
    export default {
        name:"project-task-kanban",
        data(){
            return{
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                projects:[]
            }
        },
         components:{
            ProjectTaskGanttCard,
        },
        methods:{
            getAllProject(){
                this.loading = true;
                if (this.$route.query.project_id){
                    this.$ajax.get(SERVER_PROJECT +this.$route.query.project_id ).then(response=>{
                        this.loading = false;
                        this.projects = [response.data];
                    });
                }else{
                    let params = {};
                    params.page = this.page;
                    params.page_size = this.pageSize;
                    this.$ajax.get(SERVER_PROJECT,{
                            params:params
                    }).then(response=>{
                        this.loading = false;
                        let status = response['status'];
                        let data = response['data'];
                        if (status ==200){
                            this.projects = data.results;
                        }
                    });
                }
            },
            changeProjectTaskView(projectId,view){
                this.$emit("changeProjectTaskView",projectId,view);
            }
        },
       created:function(){
            this.$nextTick(function(){
                this.getAllProject();
            });
        }
    }
</script>
