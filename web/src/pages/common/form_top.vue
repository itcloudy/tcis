<template>
    <div class="form-top">
        <el-button v-if="formTopBtns.create" plain type="primary" icon="el-icon-document" size="small" @click="formTopAction('create')" >创建</el-button>
        <el-button v-if="formTopBtns.edit" plain type="warning" icon="el-icon-edit" size="small" @click="formTopAction('edit')">编辑</el-button>
        <el-button v-if="formTopBtns.save" plain type="success" icon="el-icon-message" size="small" @click="formTopAction('save')" >保存</el-button>
        <el-button v-if="formTopBtns.cancel" plain type="danger" icon="el-icon-close" size="small" @click="formTopAction('cancel')">取消</el-button>
    </div>
</template>
<script>
    export default {
        name:"form-rop",
        props:['formTopBtns'],
        data() {
            return {
                
            };
        },
        methods:{
            formTopAction(action){
                this.$emit('formTopAction',action);
            }
        }
    }
</script>
<style lang="scss" scope>
    .form-top{
        display: inline-block;
        margin: 5px;
    }
    
</style>
