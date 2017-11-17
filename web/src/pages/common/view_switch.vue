<template>
    <el-button-group class="view-switch">
        <template v-for="(view,index) in views">
            <el-button  size="mini" :key="index" @click="switchView(view)" :type="viewDict[view]" >{{viewLabel[view]}}</el-button>
        </template>
    </el-button-group>
</template>
<script>
    export default {
        name:"view_switch",
        props:["views","activeView"],
        data(){
            let viewDict = {};
            for(let index in this.views){
                let view = this.views[index];
                if (view == this.activeView){
                    viewDict[view] = 'primary';
                }else{
                    viewDict[view] = '';
                }
            }
            return{
                viewDict:viewDict,
                viewLabel:{
                    "kanban":"看板",
                    "list":"列表",
                    "gantt":"甘特图"
                },
            }
        },
        methods:{
            switchView(newView){
                for(let index in this.views){
                    let view = this.views[index];
                    if (view == newView){
                        this.viewDict[view] = 'primary';
                    }else{
                        this.viewDict[view] = '';
                    }
                }
                this.$emit("switchView",newView);
            }
        },
        watch:{
            activeView:function(val,oldVal){
                for(let index in this.views){
                    let view = this.views[index];
                    if (view == val){
                        this.viewDict[view] = 'primary';
                    }else{
                        this.viewDict[view] = '';
                    }
                }
            }
        }
    }
</script>
<style lang="scss" scoped>
    .view-switch{
        position: absolute;
        top: 30px;
        z-index: 999;
        display: inline-block;
    }
</style>

