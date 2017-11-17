<template>
    <el-col :span="12"  :project="project" class="project-task-card" v-if="show">
        <el-card class="box-card">
            <div slot="header" class="clearfix" >
                <span @click="goProject" style="color:rgb(102, 177, 255);font-size:150%;">{{project.name}}</span>
                <i class="el-icon-info" style="color:rgb(102, 177, 255);font-size:150%;" @click="goProject"></i>
                <i style="float: right;margin-left:10px;color:red;font-size:150%;"  @click="deleteDom"  class="el-icon-circle-close"></i>
                <el-button style="float: right; padding: 3px 0; margin-left:10px" type="success" @click="changeProjectTaskView(project.id, 'list')" >任务列表</el-button>
                <el-button style="float: right; padding: 3px 0; margin-left:10px" type="warning" @click="changeProjectTaskView(project.id, 'gantt')" >甘特图</el-button>
            </div>
            <div class="project-task-echart">
                <el-row>
                    <el-col :span="24">
                        <project-task-card-echart :project="project" />
                    </el-col>
                    <el-col :span="12"></el-col>
                    <el-col :span="12"></el-col>
                    <el-col :span="12"></el-col>
                </el-row>
            </div>
        </el-card>
    </el-col>
</template>
<script>
    import  {default as ProjectTaskCardEchart} from './project_task_card_echart';
    export default {
        name:"project-task-card",
        props:['project'],
        data(){
            return{
                show:true
            }
        },
        components:{
            ProjectTaskCardEchart
        },
        methods:{
            changeProjectTaskView(projectId, view){
                this.$emit("changeProjectTaskView",projectId,view);
            },
            deleteDom(){
                this.show = false;
            },
            goProject(){
                this.$router.push('/project/'+ this.project.id);
            }
        }
         

    }
</script>
<style lang="scss" scoped>
    .project-task-card{
        padding-bottom: 5px;
        padding-top: 5px;
    }
</style>

