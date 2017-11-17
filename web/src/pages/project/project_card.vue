<template>
    <el-col :span="12"  :project="project" class="project-card" v-if="show">
        <el-card class="box-card">
            <div slot="header" class="clearfix" >
                <span @click="getProjectDetail" style="color:rgb(102, 177, 255);font-size:150%;">{{project.name}}</span>
                <i class="el-icon-info" style="color:rgb(102, 177, 255); font-size:150%;" @click="getProjectDetail"></i>
                <i style="float: right;margin-left:10px;color:red; font-size:150%;"  @click="deleteDom"  class="el-icon-circle-close"></i>
            </div>
            <div class="project-info">
                <div>
                    <el-row>
                        <el-col :span="24">
                            <h3>项目进度</h3>
                            <el-progress :text-inside="true" :stroke-width="18" :percentage="project.percentage" :status="status"></el-progress>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="12">
                            <h3>基本信息</h3>
                            <table style="width:100%;">
                                <tr>
                                    <td>上级项目</td>
                                    <td><template v-if="project.parent"> {{project.parent.name}}</template></td>
                                </tr>
                                <tr>
                                    <td>项目经理</td>
                                    <td><template v-if="project.manager">{{project.manager.username_zh}}</template></td>
                                </tr>
                                <tr>
                                    <td>开始时间</td>
                                    <td>{{project.start_date}}</td>
                                </tr>
                                <tr>
                                    <td>结束时间</td>
                                    <td>{{project.end_date}}</td>
                                </tr>
                            </table>
                        </el-col>
                        <el-col :span="12">
                            <h3>项目描述</h3>
                            <p class="project-description">{{project.description}}</p>
                        </el-col>
                    </el-row>
                </div>
            </div>
        </el-card>
    </el-col>
</template>
<script>
    export default {
        props:['project'],
        data(){
            return{
                show:true,
            };
        },
        methods:{
            getProjectDetail(){
                this.$router.push('/project/'+this.project.id);
            },
            deleteDom(){
                this.show = false;
            }
        },
        computed:{
            "status":function(){
                if (this.project.percentage<50){
                    return "success";
                }else if(this.project.percentage<90){
                    return "";
                }else{
                    return "exception";
                }
            }
        }
    }
</script>
<style lang="scss" scoped>
    .project-description{
        border: 1px solid #e6ebf5;
        border-radius: 5px;
        min-height: 100px;
        padding: 5px;
    }
    .project-card{
        padding-bottom: 5px;
        padding-top: 5px;
    }
</style>
