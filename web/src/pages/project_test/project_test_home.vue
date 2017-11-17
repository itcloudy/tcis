<template>
    <div id="project-test" :loading="loading">
        <view-switch :views="view_list" :activeView="activeView" @switchView="switchView"/>
        <form-top  @formTopAction="formTopAction" :formTopBtns="formTopBtns"/>
        <pagination 
            @pageInfoChange="pageInfoChange"
            :pageSizes="[20,40,80,160,320]"
            :pageSize="pageSize" 
            :currentPage="page"
            :total="total"/>
        <tcis-select :placeholder="'请选择项目'" :selectList="projectList" @filterSelectChange="filterProjectChange"/>
        <tcis-select :placeholder="'请选择测试类型'" :selectList="projectTestTypeList" @filterSelectChange="filterProjectTestTypeChange"/>
        <el-row :gutter="20"  class="main-content">
            <project-test-list  v-if="activeView=='list'" :projectTests="projectTests"/>
            <project-test-kanban v-if="activeView=='kanban'" 
            :type_id="type_id"
            :project_id="project_id"
            @changeProjectTestView="changeProjectTestView"/>
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_PROJECT_ALL,SERVER_PROJECT_TEST,SERVER_PROJECT_TEST_TYPE} from '@/server_address';
    import  {default as Pagination} from '@/pages/common/Pagination';
    import  {default as ProjectTestList} from './project_test_list';
    import  {default as ProjectTestKanban} from './project_test_kanban';
    import  {default as ViewSwitch} from '@/pages/common/view_switch';
    import  {default as TcisSelect} from '@/pages/common/tcis_select';
    import  {default as FormTop} from '@/pages/common/form_top';
    import localStore from '@/utils/local_store'; 
    import urlCode from '@/utils/url_code'; 
    export default {
        name:"project_test_home",
        data(){
            let activeView = localStore.get("project_test_home_view");
            if (activeView == "" || activeView == null ){
                activeView = "kanban";
            }
            return{
                formTopBtns:{
                    create:true,
                },
                projectList:[],
                projectTestTypeList:[],
                view_list:["kanban","list"],
                activeView:activeView,
                loading:false,
                pageSize:20,//每页数量
                total:0,//总数量
                page:1,//当前页
                projectTests:[],
                type_id:null,
                project_id:null,
            }
        },
        components:{
            ProjectTestList,
            ProjectTestKanban,
            ViewSwitch,
            Pagination,
            TcisSelect,
            FormTop,
        },
        methods:{
            filterProjectChange(projectId){
                this.project_id= projectId;
                this.getAllProjectTest()
            },
            filterProjectTestTypeChange(typeId){
                this.type_id = typeId;
                this.getAllProjectTest()
            },
            getAllProjectTest(){
                // 任务明细只在list下获得
                if (this.activeView != 'list'){
                    return;
                }
                this.loading = true;
                this.projectTests = [];
                let params = {
                    page: this.page,
                    page_size: this.pageSize,
                };
                if (this.$route.query.type_id){
                    this.type_id = this.$route.query.type_id;
                }
                if (this.$route.query.project_id){
                    this.project_id = this.$route.query.project_id;
                }
                if (this.project_id){
                    params.project_id = this.project_id;
                }
                if (this.type_id){
                   params.type_id = this.type_id;
                }
                this.$ajax.get(SERVER_PROJECT_TEST,{
                        params:params
                }).then(response=>{
                    this.loading = false;
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        this.projectTests = data.results;
                        this.total = data.count;
                    }
                });
            },
            switchView(view){
                this.setLocalView(view);
                // 看板显示所有项目的任务情况，其他视图根据project_id进行过滤
                if(view=="list" ){
                    this.getAllProjectTest();
                }else if (view=="kanban"){
                    this.$router.push("/project_test/");
                } 
            },
            setLocalView(view){
                this.activeView = view;
                localStore.set("project_test_home_view",view);
            },
            changeProjectTestView(projectId,view){
                this.activeView = view;
                this.switchView(view);
                this.$router.push("/project_test/?project_id=" + projectId );
            },
            pageInfoChange(pageSize,page){
                this.page = page;
                this.pageSize = pageSize;
                this.getAllProjectTest();
            },
            getAllProject(){
                this.$ajax.get(SERVER_PROJECT_ALL).then(response=>{
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        let projects = data;
                        let projectList = [{label:"所有",value:null}];
                        for(let i=0;i<projects.length;i++){
                            projectList.push({
                                label:projects[i].name,
                                value:projects[i].id
                            })
                        }
                        this.projectList = projectList;
                    }
                });
            },
            getProjectTestType(){
                this.$ajax.get(SERVER_PROJECT_TEST_TYPE).then(response=>{
                    let status = response['status'];
                    let data = response['data'];
                    if (status ==200){
                        let types = data.results;
                        let projectTestTypeList =  [{label:"所有",value:null}];
                        for(let i=0;i<types.length;i++){
                            projectTestTypeList.push({
                                label:types[i].name,
                                value:types[i].id
                            })
                        }
                        this.projectTestTypeList = projectTestTypeList;
                    }
                });
            }
        },
        created:function(){
            this.$nextTick(function(){
                if (this.$route.query.view){
                    let view = this.$route.query.view;
                    for(let i = 0; i < this.view_list.length; i++){
                        if(view === this.view_list[i]){
                            this.setLocalView(view);
                        }
                    }
                }
                this.getAllProjectTest();
                // 获得所有的项目
                this.getAllProject();
                // 获得所有的测试类型
                this.getProjectTestType();
            });
        },
        watch:{
            '$route':function(val,oldVal){
                if (val != oldVal){
                    this.getAllProjectTest();
                }
            }
        }
    }
</script>
<style lang="scss" scoped>
   
</style>

