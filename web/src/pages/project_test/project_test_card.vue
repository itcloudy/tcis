<template>
    <el-col :span="12"  :projectTest="projectTest" class="project-test-card" v-if="show">
        <el-card class="box-card">
            <div slot="header" class="clearfix" >
                <span @click="goProjectTest" style="color:rgb(102, 177, 255);">{{projectTest.name}}</span>
                <i class="el-icon-info" style="color:rgb(102, 177, 255);" @click="goProjectTest"></i>
                <i style="float: right;margin-left:10px;color:red;"  @click="deleteDom"  class="el-icon-circle-close"></i>
                <el-button style="float: right; padding: 3px 0; margin-left:10px" type="success" @click="changeProjectTestView(projectTest.id, 'list')" >测试列表</el-button>
            </div>
            <div class="project-test-echart">
                <el-row>
                    <el-col :span="24">
                        <project-test-card-echart :projectTest="projectTest" />
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
    import  {default as ProjectTestCardEchart} from './project_test_card_echart';
    export default {
        name:"project-test-card",
        props:['projectTest'],
        data(){
            return{
                show:true
            }
        },
        components:{
            ProjectTestCardEchart
        },
        methods:{
            changeProjectTestView(projectId, view){
                this.$emit("changeProjectTestView",projectId,view);
            },
            deleteDom(){
                this.show = false;
            },
            goProjectTest(){
                this.$router.push('/project_test/'+ this.projectTest.id);
            }
        }
         

    }
</script>
<style lang="scss" scoped>
    .project-test-card{
        padding-bottom: 5px;
        padding-top: 5px;
    }
</style>

