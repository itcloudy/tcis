<template>
    <div>
        <el-table
            ref="multipleTable"
            :data="groups"
            @row-dblclick = "goGroupDetail"
            style="width: 100%">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <h3 >权限信息:</h3>
                    <template v-for="(permission,index) in props.row.permissions">
                        <span :key="index" style="margin:5px;border:1px solid #333;padding:2px;">{{ permission.name }}</span>
                    </template>
                </template>
            </el-table-column>
            <el-table-column
            type="selection"
            width="55">
            </el-table-column>
            <el-table-column
            prop="name"
            label="组名">
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
    export default {
        name:"",
        props:['groups'],
        data(){
            return{

            }
        },
        methods:{
            goGroupDetail(row, event){
                this.$router.push('/group/'  +row.id);
            },
        }
    }
</script>
