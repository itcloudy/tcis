<template>
    <div class="pagination">   
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="pageSizes"
            :page-size="pageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total">
        </el-pagination>
    </div>
</template>
<script>
    export default {
        methods: {
            pageInfoChange(pageSize,currentPage){
                this.$emit("pageInfoChange",pageSize,currentPage);
            },
            handleSizeChange(val) {
                // 每页显示数量改变，从第一页开始显示
                this.pageInfoChange(val,1);
            },
            handleCurrentChange(val) {
                this.pageInfoChange(this.pageSize,val);
            }
        },
        props:["pageSize","currentPage","total","pageSizes"],
        data() {
            return {
            };
        }
    }
</script>
<style lang="scss" scope>
    .pagination{
		margin: 5px;
        display: inline-block;
    }          
</style>
