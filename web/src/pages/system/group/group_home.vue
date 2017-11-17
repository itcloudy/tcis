<template>
    <div id="group-home">
        <view-switch :views="view_list" :activeView="activeView" @switchView="switchView"/>
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[20,40,80,160,320]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        
        <el-row :gutter="20" class="main-content">
            <group-list v-if="activeView=='list'" :groups="groups" />
            <group-kanban v-if="activeView=='kanban'" :groups="groups" />
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_GROUP} from '@/server_address';
    import localStore from '@/utils/local_store'; 
    import  {default as GroupKanban} from './group_kanban';
    import  {default as GroupList} from './group_list';
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    import  {default as FormTop} from '@/pages/common/form_top';
    import  {default as Pagination} from '@/pages/common/Pagination';
    export default {
        name:"group_home",
        data(){
            let activeView = localStore.get("group_home_view");
            if (activeView == "" || activeView == null ){
                activeView = "list";
            }
            return{
                formTopBtns:{
                    create:this.$store.state.userinfo.is_superuser
                },
                view_list:["kanban","list"],
                activeView:activeView,
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                groups:[]
            }
        },
        components:{
            GroupList,
            ViewSwitch,
            FormTop,
            Pagination,
            GroupKanban,
        },
        methods:{
            getAllGroup(){
                this.loading = true;
                this.$ajax.get(SERVER_GROUP,{
                        params:{
                            page:this.page,
                            page_size:this.pageSize
                        }
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.groups = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.activeView = view;
                localStore.set("group_home_view",view);
            },
           pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllGroup();
            },
            formTopAction(action){
                if(action=='edit'){
                    this.$router.push('/group/' + this.userForm.id);
                }else if(action =='create'){
                    this.$router.push('/group/new');
                } 
            }
            
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllGroup();
            });
        },
    }
</script>
