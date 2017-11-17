<template>
    <div id="project-info">
        <el-row :gutter="20">
            <el-col :span="24">
                <p style="display:inline-block;margin-right:10px;">项目进度</p><el-switch active-text="显示子项目数据" v-model="checkChild" @change="changeChildInfo" inactive-text="不显示子项目数据" >
</el-switch>
                <el-progress :text-inside="true" :stroke-width="18" :percentage="project.percentage" :status="status"></el-progress>
            </el-col>
        </el-row >
        <el-row :gutter="20">
            <el-form :inline="true" ref="project_info" :model="project" class="form-read-only">
                <el-col :span="12">
                <el-form-item label="项目名称">
                        <span>{{project.name}}</span>
                </el-form-item>
                <el-form-item label="项目经理">
                        <span v-if="project.manager">{{project.manager.name}}</span>
                        <span v-else>未指派</span>
                </el-form-item>
                <el-form-item label="上级项目">
                        <span v-if="project.parent">{{project.parent.name}}</span>
                        <span v-else>无</span>
                </el-form-item>
                <el-form-item label="开始时间">
                        <span v-if="project.start_date">{{project.start_date}}</span>
                        <span v-else>暂未定</span>
                </el-form-item>
                <el-form-item label="结束时间">
                        <span v-if="project.end_date">{{project.end_date}}</span>
                        <span v-else>暂未定</span>
                </el-form-item>
                </el-col>
                <el-col :span="12">
                    <el-form-item label="项目描述">
                            <span >{{project.description}}</span>
                    </el-form-item>
                </el-col>
            </el-form>  
        </el-row> 
        <el-row>
            <el-col :span="12" style="padding-right:5px;">
                <el-card class="box-card" >
                    <div slot="header" class="clearfix">
                        <span>任务分布图</span>
                        <i style="float: right;margin-left:10px;color:red;font-size:150%;"  @click="showToggle('task')"  :class="taskClass"></i>
                    </div>
                   <div v-show='taskDisplay'>
                        <project-task-card-echart :project="project" :checkChild="checkChild"/>
                   </div>
                </el-card>
            </el-col>
            <el-col :span="12" style="padding-left:5px;">
                <el-card class="box-card"  >
                    <div slot="header" class="clearfix">
                        <span>Bug分布图</span>
                        <i style="float: right;margin-left:10px;color:red;font-size:150%;"  @click="showToggle('bug')"  :class="bugClass"></i>
                    </div>
                    <div  v-show='bugDisplay'>
                        <project-bug-card-echart :project="project" :checkChild="checkChild"/>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        <el-tabs class='tcis-tabs' v-model="activeName" type="border-card" @tab-click="handleClick">
            <el-tab-pane label="项目任务" name="project_task">
                <el-button type="success" v-if="projectTasks.length > 0" size="mini" @click="checkTaskDetail" round>查看任务明细</el-button>
                <project-task-list :projectTasks="projectTasks"/>
            </el-tab-pane>
            <el-tab-pane label="项目Bug" name="project_bug">
                <el-button type="success" v-if="projectBugs.length > 0" size="mini" @click="checkBugDetail" round>查看Bug明细</el-button>
                <project-bug-list  :projectBugs="projectBugs"  />
            </el-tab-pane>
            <el-tab-pane  label="项目组成员" name="project_members">
                <el-button type="primary" size="mini" @click="addProjectMember" round>添加成员</el-button>
                <project-member-list  :projectMembers="projectMembers"  />
            </el-tab-pane>
            <el-tab-pane v-if="childProjects.length > 0" label="子项目" name="child_project">
                <project-list  :projects="childProjects"  />
            </el-tab-pane>
            
        </el-tabs>
    </div>
</template>
<script>
    import  {default as ProjectBugList} from '../project_bug/project_bug_list';
    import  {default as ProjectTaskList} from './project_task_list';
    import  {default as ProjectList} from './project_list';
    import  {default as ProjectMemberList} from './project_member_list';
    import  {default as ProjectTaskCardEchart} from './project_task_card_echart';
    import  {default as ProjectBugCardEchart} from '@/pages/project_bug/project_bug_card_echart';
    export default {
        name:"project_info",
        props:['project','checkChild','projectTasks','projectBugs','childProjects',"projectMembers"],
        data(){
            return{
                bugDisplay:true,
                bugClass:"el-icon-remove",
                taskDisplay:true,
                taskClass:"el-icon-remove",
                activeName:"project_task",
                childProjects:[],
            }
        },
         components:{
            ProjectBugList,
            ProjectTaskList,
            ProjectList,
            ProjectMemberList,
            ProjectTaskCardEchart,
            ProjectBugCardEchart
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
        },
        methods:{
            changeChildInfo(state){
                this.$emit("changeChildInfo",state);
            },
            showToggle(type){
                if(type=='task'){
                    this.taskDisplay = ! this.taskDisplay;
                    if (this.taskDisplay){
                        this.taskClass = "el-icon-remove";
                    }else{
                        this.taskClass = "el-icon-circle-plus";
                    }
                }else if(type=='bug'){
                    this.bugDisplay = ! this.bugDisplay;
                        if (this.bugDisplay){
                            this.bugClass = "el-icon-remove";
                        }else{
                            this.bugClass = "el-icon-circle-plus";
                    }
                }
                
            },
            checkBugDetail(){
                this.$router.push('/project_bug/?project_id='  + this.project.id + "&check_child="+ this.checkChild + "&view=list");
            },
            checkTaskDetail(){
                 this.$router.push('/project_task/?project_id='  + this.project.id + "&check_child="+ this.checkChild+ "&view=list");
            },
            addProjectMember(){

            }
        },
         
    }
</script>
<style lang="scss" scoped>
    
</style>
