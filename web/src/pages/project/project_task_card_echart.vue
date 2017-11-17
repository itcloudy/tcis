<template>
    <div :id="'task-distribution-'+project.id" :style="chartStyle()">
    </div>
</template>
<script>
    import  {SERVER_PROJECT_TASK_INFO} from '@/server_address';
    export default {
        name:"project-task-card-echart",
        props:["project","checkChild"],
        data(){
            return{
                distributionxArixData:[],
                distributionSeris:[],
                distributionLegend:[]
            }
        },
        methods:{
            getProjectTaskInfo(){
                let params = {
                    project_id:this.project_id,
                }
                this.$ajax.get(SERVER_PROJECT_TASK_INFO,{
                        params:{
                            project_id:this.project.id,
                            check_child:this.checkChild,
                        }
                }).then(response=>{
                    let status = response['status'];
                    if (status ==200){
                        this.distributionSeris = response.data.series;
                        this.distributionxArixData = response.data.x_axis;
                        this.distributionLegend = response.data.legend;
                        this.echartDistributionView();
                    }
                });
            },
            chartStyle($div){
                return {
                    width: "800px",
                    height: "500px"
                }
            },
            echartDistributionView(){
                let echartDistributionChart = this.$echarts.init(document.getElementById("task-distribution-"+this.project.id));
                let option ={
                    tooltip : {
                        trigger: 'axis',
                        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                        }
                    },
                    toolbox: {
                        show : true,
                        x:'left',
                        y:'center',
                        feature : {
                            saveAsImage : {name:"project_task_bar",show: true}
                        }
                    },
                    legend: {
                        data:this.distributionLegend
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    xAxis : [
                        {
                            type : 'category',
                            data : this.distributionxArixData
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : this.distributionSeris
                };
                echartDistributionChart.setOption(option);
            }
        },
        created:function(){
            this.getProjectTaskInfo();
        },
        watch:{
             "checkChild": "getProjectTaskInfo"
        }
    }
</script>
