<template>
    <div :id="'test-distribution-'+projectTest.id" :style="chartStyle()">
    </div>
</template>
<script>
    import  {SERVER_PROJECT_TEST_INFO} from '@/server_address';
    export default {
        name:"project-test-card-echart",
        props:["projectTest"],
        data(){
            return{
                distributionxArixData:[],
                distributionSeris:[],
                distributionLegend:[]
            }
        },
        methods:{
            getProjectTestInfo(){
                let params = {
                    project_test_id:this.project_test_id,
                }
                this.$ajax.get(SERVER_PROJECT_TEST_INFO,{
                        params:{
                            project_test_id:this.projectTest.id,
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
                let echartDistributionChart = this.$echarts.init(document.getElementById("test-distribution-"+this.projectTest.id));
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
                            saveAsImage : {show: true,name:"project_test_bar"}
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
            this.getProjectTestInfo();
        },
        watch:{
             "checkChild": "getProjectTestInfo"
        }
    }
</script>
