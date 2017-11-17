<template>

    <div id="group-form">
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <div class="main-content"  v-loading="loading">
            <el-form :inline="true" ref="groupForm" :rules="groupFormRules"  :model="groupForm" label-width="80px">
                <el-form-item label="组名" prop="name">
                    <el-input v-model="groupForm.name"></el-input>
                </el-form-item>
            </el-form>
            <el-transfer
                filterable
                :titles="['可选项', '已选项']"
                :button-texts="['到左边', '到右边']"
                filter-placeholder="请输入条件"
                :props="{
                    key: 'id',
                    label: 'name'
                }"
                v-model="groupForm.permissions"
                :data="allPermissions">
            </el-transfer>
        </div>
    </div>
</template>
<script>
    import  {SERVER_GROUP,SERVER_PERMISSION,SERVER_PERMISSION_ALL} from '@/server_address';
    import  {default as FormTop} from '@/pages/common/form_top';
    export default {
        name:"group-form",
        data(){
            return{
                formTopBtns:{},
                loading:false,
                allPermissions:[],
                selectedPermissions:[],
                groupForm:{
                    name:"",
                    permissions:[],
                },
            }
        },
        components:{
            FormTop,
        },
        methods:{
            getAllPermissions(){
                this.loading = true;
                this.$ajax.get(SERVER_PERMISSION_ALL).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.allPermissions = data;
                    }
                });
            },
            getGroup(){
                let id  = this.$route.params.id;
                if (id!='new'){
                    this.formTopBtns.create = true;
                    this.formTopBtns.edit = true;
                    this.groupForm.id = id;
                    this.$ajax.get(SERVER_PERMISSION + this.groupForm.id).then(response=>{
                            this.loadging = false;
                            let status = response['status'];
                            let data = response['data'];
                            if (status ==200){
                                this.groupForm = data;
                            }
                    });
                }else{
                    this.formTopBtns.create = false;
                    this.formTopBtns.save = true;
                }

            },
        },
        created:function(){
            this.$nextTick(function(){
                 
                this.getAllPermissions();
                this.getGroup();
            });
        }
    }
</script>

