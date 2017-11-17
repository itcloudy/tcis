<template>
    <div>
        <el-table
            ref="multipleTable"
            :data="permissions"
            style="width: 100%">
            <el-table-column
            type="selection"
            width="55">
            </el-table-column>
            <el-table-column
            prop="name"
            label="权限名称">
            </el-table-column>
             <el-table-column
            prop="codename"
            label="权限编码">
            </el-table-column>
            <el-table-column
            v-if="userinfo.is_superuser"
            label="所属App">
                <template v-if="scope.row.content_type" scope="scope">
                {{scope.row.content_type.app_label}}
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
    import { mapState } from 'vuex';
    export default {
        name:"",
        props:['permissions'],
        data(){
            return{

            }
        },
        computed:{
           ...mapState({
               userinfo: state => state.userinfo
           })
        }
    }
</script>
