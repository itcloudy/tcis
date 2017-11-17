<template>
    <div id="project-bug-kanban">
        <project-bug-card v-for="(project,index) in projects" :project="project" :key="index" @changeProjectBugView='changeProjectBugView' />
    </div>
</template>
<script>
    import  {SERVER_PROJECT,SERVER_PROJECT_BUG} from '@/server_address';
    import  {default as ProjectBugCard} from './project_bug_card';
    export default {
        name:"project-bug-kanban",
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
            ProjectBugCard,
        },
        methods:{
            getAllProject(){
                this.loading = true;
                let params = {
                    page:this.page,
                    page_size:this.pageSize
                };
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
            },
            changeProjectBugView(projectId,view){
                this.$emit("changeProjectBugView",projectId,view);
            }
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllProject();
            });
        }
    }
</script>
