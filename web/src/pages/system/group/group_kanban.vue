<template>
    <div id="group-kanban">
        <group-card v-for="(group,index) in groups" :group="group" :key="index"  />
    </div>
</template>
<script>
    import  {SERVER_GROUP} from '@/server_address';
    import  {default as GroupCard} from './group_card';
    export default {
        name:"group-task-kanban",
        data(){
            return{
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                groups:[]
            }
        },
         components:{
            GroupCard,
        },
        methods:{
            getAllGroup(){
                this.loading = true;
                let params = {
                    page:this.page,
                    page_size:this.pageSize
                };
                this.$ajax.get(SERVER_GROUP,{
                        params:params
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.groups = data.results;
                    }
                });
            },
             
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllGroup();
            });
        }
    }
</script>
