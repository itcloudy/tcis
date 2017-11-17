<template>
    <div class="group-detail">
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <div class="main-content">
            <group-from v-if="activeView =='form'" :group="newGroupForm" />
            <group-info v-if="activeView =='info'" :group="groupForm">
        </div>
    </div>
</template>
<script>
    import  {SERVER_GROUP} from '@/server_address'; 
    import localStore from '@/utils/local_store'; 
    import  {default as FormTop} from '@/pages/common/form_top';
    import  {default as GroupFrom} from './group_form';
    import  {default as GroupInfo} from './group_info';
    export default {
        name:"group_detail",
        data(){
            let activeView = localStore.get("group_detail_view");
            if (activeView == "" || activeView == null ){
                activeView = "info";
            }
            return{
                formTopBtns:{
                    create:true,
                },
                activeView:activeView,
                loadding:false,
                groupForm:{},
                newGroupForm:{
                    name:"",
                    permissions:[],
                },
            }
        },
        components:{
            GroupFrom,
            GroupInfo,
            FormTop,
        },
        methods:{
            getGroupInfo(){
                this.loadding = true;
                let id  = this.$route.params.id;
                if (id!='new'){
                    this.groupForm.id = id;
                    this.$ajax.get(SERVER_GROUP+this.groupForm.id).then(response=>{
                        this.loadging = false;
                        let status = response['status'];
                        let data = response['data'];
                        if (status ==200){
                            this.groupForm = data;
                        }
                    });
                }else{
                    this.groupForm = this.newGroupFrom;
                }
            },
        },
        created:function(){
            this.getGroupInfo();
        },
        watch: {
            // 如果路由有变化，会再次执行该方法
            '$route': 'getGroupInfo'
        },
    }
</script>

