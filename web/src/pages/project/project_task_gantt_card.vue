<template>
    <el-col :span="24"  :project="project" class="project-task-gantt-card" v-if="show">
        <el-card class="box-card">
            <div slot="header" class="clearfix" >
                <span style="display:inline-block;margin-right:10px;">{{project.name}}</span><el-switch active-text="显示子项目数据" v-model="checkChild" @change="changeChildInfo" inactive-text="不显示子项目数据" >
</el-switch>
                <i style="float: right;margin-left:10px;color:red;font-size:150%;"  @click="deleteDom"  class="el-icon-circle-close"></i>
                <el-button style="float: right; padding: 3px 0; margin-left:10px" type="success" @click="changeProjectTaskView(project.id, 'list')" >任务列表</el-button>
            </div>
            <div :id="'task-gantt-'+project.id" :style="{'width':ganttWidth,'height':ganttHeight}">
            </div>
        </el-card>
    </el-col>
</template>
<script>
    import  {SERVER_PROJECT_TASK_GANTT} from '@/server_address';
    export default {
        name:"project-task-gantt-card",
        props:["project"],
        data(){
            return{
                checkChild:false,
                show:true,
                taskNames:[],
                taskSeries:[],
                ganttWidth:"1600px",
                ganttHeight: "500px",
            }
        },
        methods:{
            changeProjectTaskView(projectId, view){
                this.$emit("changeProjectTaskView",projectId,view);
            },
            deleteDom(){
                this.show = false;
            },
            getProjectTaskGantt(){
                let params = {
                    project_id:this.project_id,
                }
                this.$ajax.get(SERVER_PROJECT_TASK_GANTT,{
                        params:{
                            project_id:this.project.id,
                            check_child:this.checkChild,
                        }
                }).then(response=>{
                    let status = response['status'];
                    if (status ==200){
                        this.taskNames = response.data.task_names;
                        let start_time_list = this.timeChange(response.data.start_time_list);
                        this.ganttHeight = start_time_list.length*40 + 1000 + "px";
                        this.taskSeries.push({
                            name:'开始时间',
                            type:'bar',
                            stack: '计划',
                            itemStyle : { normal: {color:'rgba(0,0,0,0)'}},
                            data:start_time_list
                        });
                        this.taskSeries.push({
                            name:'计划完成时间',
                            type:'bar',
                            stack: '计划',
                            data:this.timeChange(response.data.end_time_list) 
                        });
                        this.taskSeries.push({
                            name:'开始时间',
                            type:'bar',
                            stack: '实际',
                            itemStyle : { normal: {color:'rgba(0,0,0,0)'}},
                            data:start_time_list
                        });
                        this.taskSeries.push({
                            name:'实际完成时间',
                            type:'bar',
                            stack: '实际',
                            data:this.timeChange(response.data.real_end_time_list )
                        });
                        this.echartDistributionView();
                    }
                });
            },
            timeChange(timeList){
                let len = timeList.length;
                let results = [];
                for(let i=0;i<len;i++){
                    let timeStr = timeList[i];
                    if (timeStr){
                        results.push(new Date(timeStr));
                    }else{
                        results.push(null);
                    }
                }
                return results;
            },
            echartDistributionView(){
                let echartDistributionChart = this.$echarts.init(document.getElementById("task-gantt-"+this.project.id));
                let option = {
                    legend: {
                        data: ['计划完成时间','实际完成时间']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        show : true,
                        x:'left',
                        y:'center',
                        feature : {
                            saveAsImage : {show: true, name:"project_task_gantt",}
                        }
                    },
                    xAxis:[
                        {
                            type : 'time',
                            name: "任务时间",
                        },
                        {
                            type : 'time',
                            name: "任务时间",
                        }
                    ],
                    yAxis: {
                        name: "任务名称",
                        data: this.taskNames
                    },
                    tooltip:{    trigger:'axis',
                        formatter:function(params) {
                            let res= "任务名：" + params[0].name+"</br>"
                            let date0=params[0].data;
                            let date1=params[1].data;
                            let date2=params[3].data;
                            if(date0){
                                date0=date0.getFullYear()+"-"+(date0.getMonth()+1)+"-"+date0.getDate() + " " + date0.getHours() +":"+date0.getMinutes();
                            }else{
                                date0 = "未计划";
                            }
                            if(date1){
                                date1=date1.getFullYear()+"-"+(date1.getMonth()+1)+"-"+date1.getDate() + " " + date1.getHours() +":"+date1.getMinutes();
                            }else{
                                date1 = "未计划";
                            }
                            if (date2){
                                date2=date2.getFullYear()+"-"+(date2.getMonth()+1)+"-"+date2.getDate() + " " + date2.getHours() +":"+date2.getMinutes();
                            }else{
                                date2 = "未计划";
                            }
                            res+=params[0].seriesName+":"+date0+"</br>"
                            res+=params[1].seriesName+":"+date1+"</br>"
                            res+=params[3].seriesName+":"+date2+"</br>"
                            return res;
                        }
                    },
                    series : this.taskSeries
                };
                echartDistributionChart.setOption(option);
            },
            changeChildInfo(state){
                this.checkChild = state;
                this.getProjectTaskGantt();
            },
            
        },
        created:function(){
            this.getProjectTaskGantt();
        },
    }
</script>
<style lang="scss" scoped>
    .project-task-gantt-card{
        padding-bottom: 5px;
        padding-top: 5px;
    }
</style>
