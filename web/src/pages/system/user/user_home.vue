<template>
    <div id="user-home">
        <view-switch :views="view_list" :activeView="activeView" @switchView="switchView"/>
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[20,40,80]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        <el-row :gutter="20">
            <user-list v-if="activeView=='list'" 
            :users="users" />
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_USER} from '@/server_address';
    import localStore from '@/utils/local_store'; 
    import  {default as UserList} from './user_list';
    import  {default as Pagination} from '@/pages/common/Pagination';
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    import  {default as FormTop} from '@/pages/common/form_top';
    import { mapState } from 'vuex';
    export default {
        name:"user_home",
        data(){
            let activeView = localStore.get("user_home_view");
            if (activeView == "" || activeView == null ){
                activeView = "list";
            }
            let formTopBtns = {
                create:true,
            };
            return{
                formTopBtns:formTopBtns,
                view_list:["kanban","list"],
                activeView:activeView,
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                users:[]
            }
        },
        components:{
            UserList,
            ViewSwitch,
            Pagination,
            FormTop,
        },
        methods:{
            getAllUser(){
                this.loading = true;
                this.$ajax.get(SERVER_USER,{
                        params:{
                            page:this.page,
                            page_size:this.pageSize
                        }
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.users = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.activeView = view;
                localStore.set("user_home_view",view);
            },
            pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllUser()
            },
            changeCreateForm(){
                this.$router.push('/user/new');
            },
        },
        created:function(){
            this.$nextTick(function(){
                this.getAllUser();
            });
        },
        computed:{
           ...mapState({
               userinfo: state => state.userinfo
           })
        },
    }
</script>
