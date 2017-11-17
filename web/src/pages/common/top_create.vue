<template>
    <div v-if="Create" id="tree-top" class="top-create">
        <el-button  icon="el-icon-document" size="small" @click="changeCreateForm" v-if="Create">创建</el-button>
    </div>
</template>
<script>
    
    export default {

        data() {
            return {
                
            };
        },
        props:["Create"],
        methods:{
            changeCreateForm(){
                this.$emit("changeCreateForm");
            },
           
        }
    }
</script>
<style lang="scss" scope>
    .top-create{
         display: inline-block;
    }
    
</style>
