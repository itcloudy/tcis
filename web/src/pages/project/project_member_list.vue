<template>
    <div>
        <el-table
            v-loading.body="loading"
            ref="multipleTable"
            :data="projectMembers"
            style="width: 100%">
            <el-table-column
            type="selection"
            width="55">
            </el-table-column>
            
            <el-table-column
            label="项目名称">
                <template v-if="scope.row.project" scope="scope">
                {{scope.row.project.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="项目成员">
                <template v-if="scope.row.member" scope="scope">
                {{scope.row.member.username_zh}}
                </template>
            </el-table-column>
            <el-table-column
            label="职位">
                <template v-if="scope.row.position" scope="scope">
                {{scope.row.position.name}}
                </template>
            </el-table-column>
            <el-table-column
            label="是否有效">
                <template scope="scope"> 
                    <span v-if="scope.row.is_active">是</span>
                    <span v-else>否</span>
                </template>
            </el-table-column>
            <el-table-column label="操作" v-if=" userinfo.is_superuser || scope.row.project.manager && (userinfo.id == scope.row.project.manager.id)" align="center">
                <template scope="scope" >
                    <el-button
                    type="danger"
                    size="mini"
                    class="table-btn"
                    @click="disableProjectMember(scope.$index, scope.row)">无效</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
    export default {
        name:"",
        props:['projectMembers'],
        data(){
            return{

            }
        },
        methods:{
            disableProjectMember(index,row){
            }
        }
    }
</script>
