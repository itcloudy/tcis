<template>
    <div class="project-detail">
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <project-from v-if="activeView =='form'" :project="newProjectForm" />
        <project-info v-if="activeView =='info'" 
        @changeChildInfo="changeChildInfo"
        :checkChild="checkChild" 
        :project="projectForm" 
        :projectTasks="projectTasks"
        :childProjects="childProjects"
        :projectMembers="projectMembers"
        :projectBugs="projectBugs">
    </div>
</template>
<script>
    import  {SERVER_PROJECT,SERVER_PROJECT_TASK,SERVER_PROJECT_BUG,SERVER_PROJECT_MEMBER} from '@/server_address'; 
    import localStore from '@/utils/local_store'; 
    import  {default as FormTop} from '../common/form_top';
    import  {default as ProjectFrom} from './project_form';
    import  {default as ProjectInfo} from './project_info';
    export default {
        name:"project_detail",
        data(){
            let activeView = localStore.get("project_detail_view");
            if (activeView == "" || activeView == null ){
                activeView = "info";
            }
            let checkChild = localStore.get("project_detail_check_child");
            if (checkChild == "" || activeView == null ){
                checkChild = false;
            }
            return{
                formTopBtns:{
                    create:true,
                },
                checkChild:checkChild,
                activeView:activeView,
                loadding:false,
                projectForm:{},
                newProjectForm:{},
                projectTasks:[],
                projectBugs:[],
                childProjects:[],
                projectMembers:[]
            }
        },
        components:{
            ProjectFrom,
            ProjectInfo,
            FormTop,
        },
        methods:{
            getProjectInfo(){
                this.loadding = true;
                let id  = this.$route.params.id;
                if (id!='new'){
                    this.projectForm.id = id;
                    this.$ajax.get(SERVER_PROJECT+this.projectForm.id).then(response=>{
                        this.loadging = false;
                        let status = response['status'];
                        let data = response['data'];
                        if (status ==200){
                            this.projectForm = data;
                        }
                    });
                    this.getProjectTasks();
                    this.getProjectBugs();
                    this.getChildProjects();
                    this.getProjectMembers();
                }else{
                    this.projectForm = this.newProjectFrom;
                }
            },
            getProjectBugs(){
                let getParams = {
                　　params: { 'project_id': this.projectForm.id ,'check_child':this.checkChild}
                };
                this.$ajax.get(SERVER_PROJECT_BUG, getParams).then(response=>{
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectBugs = data.results;
                    }
                });
            },
            getProjectTasks(){
                let getParams = {
                　　params: { 'project_id': this.projectForm.id ,'check_child':this.checkChild}
                };
                this.$ajax.get(SERVER_PROJECT_TASK, getParams).then(response=>{
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectTasks = data.results;
                    }
                });
            },
            getChildProjects(){
                if(this.checkChild==true){
                    this.$ajax.get(SERVER_PROJECT,{
                        params:{
                            check_child:this.checkChild,
                            project_id:this.projectForm.id
                            }
                    }).then(response=>{
                        let status = response['status'];
                        let data = response['data'];
                        if (status ==200){
                            this.childProjects = data.results;
                        }
                    });
                }else{
                    this.childProjects = [];
                }
            },
            getProjectMembers(){
                this.$ajax.get(SERVER_PROJECT_MEMBER,{
                    params:{
                        check_child:true,
                        project_id:this.projectForm.id
                        }
                }).then(response=>{
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectMembers = data.results;
                    }
                });
            },
            changeChildInfo(state){
                this.checkChild = state;
                localStore.set("project_detail_check_child",state);
                this.getProjectTasks();
                this.getProjectBugs();
                this.getChildProjects();
                this.getProjectMembers()
              
            }
        },
        created:function(){
            this.getProjectInfo();
        },
        watch: {
            // 如果路由有变化，会再次执行该方法
            '$route': 'getProjectInfo'
        },
    }
</script>

