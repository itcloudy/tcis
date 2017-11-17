<template>
    <div id="project-test-kanban">
        <project-test-card v-for="(projectTest,index) in projectTests" :projectTest="projectTest" :key="index" @changeProjectTestView='changeProjectTestView' />
    </div>
</template>
<script>
    import  {SERVER_PROJECT_TEST} from '@/server_address';
    import  {default as ProjectTestCard} from './project_test_card';
    export default {
        name:"project-test-kanban",
        props:["project_id","type_id"],
        data(){
            return{
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                projectTests:[]
            }
        },
         components:{
            ProjectTestCard,
        },
        methods:{
            getAllProjectTest(){
                this.loading = true;
                let params = {
                    page:this.page,
                    page_size:this.pageSize,
                    project_id:this.project_id,
                    type_idL:this.type_id
                };
                this.$ajax.get(SERVER_PROJECT_TEST,{
                        params:params
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectTests = data.results;
                    }
                });
            },
            changeProjectTestView(projectId,view){
                this.$emit("changeProjectTestView",projectId,view);
            }
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllProjectTest();
            });
        }
    }
</script>
