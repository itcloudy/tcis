<template>
    <div>
     
        <el-table
            v-loading.body="loading"
            ref="multipleTable"
            :data="projectTests"
            @row-dblclick = "goProjectTestDetail"
            style="width: 100%">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="Test描述">
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
            label="Test名称">
            </el-table-column>
            <el-table-column
            label="测试员">
                <template v-if="scope.row.tester" scope="scope">
                {{scope.row.tester.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="处理员">
                <template v-if="scope.row.handler" scope="scope">
                {{scope.row.handler.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="验证员">
                <template v-if="scope.row.checker" scope="scope">
                {{scope.row.checker.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="处理人">
                <template v-if="scope.row.handler" scope="scope">
                {{scope.row.handler.name}}
                </template>
            </el-table-column>
            <el-table-column
            prop="level"
            label="级别">
            </el-table-column>
             <el-table-column
            prop="open_times"
            label="打开次数">
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
        props:['projectTests'],
        data(){
            return{

            }
        },
        methods:{
            goProjectTestDetail(row, event){
                this.$router.push('/project_test/'  +row.id);
            },
        },
    }
</script>
