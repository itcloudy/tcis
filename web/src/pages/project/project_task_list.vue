<template>
    <div>
       
        <el-table
            v-loading.body="loading"
            ref="multipleTable"
            :data="projectTasks"
            @row-dblclick = "goProjectTaskDetail"
            style="width: 100%">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="任务描述">
                        <span>{{ props.row.description }}</span>
                    </el-form-item>
                    </el-form>
                </template>
            </el-table-column>
            <el-table-column
            type="selection"
            width="55">
            </el-table-column>
            <el-table-column
            label="所属项目">
                <template v-if="scope.row.project" scope="scope">
                {{scope.row.project.name}}
                </template>
            </el-table-column>
            <el-table-column
            prop="name"
            label="任务名称">
            </el-table-column>
            <el-table-column
            label="上级任务">
                <template v-if="scope.row.parent" scope="scope">
                {{scope.row.parent.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="处理人">
                <template v-if="scope.row.handler" scope="scope">
                {{scope.row.handler.name}}
                </template>
            </el-table-column>
            <el-table-column
            prop="active"
            label="是否有效">
            </el-table-column>
            <el-table-column
            prop="level"
            label="级别">
            </el-table-column>
             <el-table-column
            label="开始时间">
                <template v-if="scope.row.start_time" scope="scope">
                {{scope.row.start_time | stringTimeFormat}}
                </template>
            </el-table-column>
            <el-table-column
            prop="need_time"
            label="估计时长(h)">
            </el-table-column>
            <el-table-column
            label="计划完成时间">
                <template v-if="scope.row.end_time" scope="scope">
                {{scope.row.end_time | stringTimeFormat}}
                </template>
            </el-table-column>
            <el-table-column
            label="实际完成时间">
                <template v-if="scope.row.real_end_time" scope="scope">
                {{scope.row.real_end_time | stringTimeFormat}}
                </template>
            </el-table-column>
            <el-table-column
            prop="state"
            label="状态">
            </el-table-column>

            
        </el-table>
    </div>
</template>
<script>
    export default {
        name:"",
        props:['projectTasks'],
        data(){
            return{

            }
        },
        methods:{
            goProjectTaskDetail(row, event){
                this.$router.push('/project_task/'  +row.id);
            },
        },
    }
</script>
