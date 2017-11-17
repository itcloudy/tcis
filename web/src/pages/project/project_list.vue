<template>
    <div>
       
        <el-table
            v-loading.body="loading"
            ref="multipleTable"
            :data="projects"
            @row-dblclick = "goProjectDetail"
            style="width: 100%">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="项目描述">
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
            prop="name"
            label="项目名称">
            </el-table-column>
            <el-table-column
            label="上级项目">
                <template v-if="scope.row.parent" scope="scope">
                {{scope.row.parent.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="项目经理">
                <template v-if="scope.row.manager" scope="scope">
                {{scope.row.manager.username_zh}}
                </template>
            </el-table-column>
             <el-table-column
            prop="start_date"
            label="开始时间">
            </el-table-column>
             <el-table-column
            prop="end_date"
            label="结束时间">
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
    export default {
        name:"",
        props:['projects'],
        data(){
            return{

            }
        },
        methods:{
            goProjectDetail(row, event){
                this.$router.push('/project/'  +row.id);
            },
        }
    }
</script>
