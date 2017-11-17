<template>
    <el-aside width="200px" height="1000px">
        <el-menu  :default-active="activeMenu" @select="selectMenu">
            <el-submenu index="system">
                <template slot="title"><i class="el-icon-menu"></i>系统设置</template>
                <el-menu-item index="user">用户管理</el-menu-item>
                <el-menu-item index="group">用户组管理</el-menu-item>
                 <el-menu-item index="permission">权限查看</el-menu-item>
            </el-submenu>
            <el-submenu index="project">
                <template slot="title"><i class="el-icon-menu"></i>项目管理</template>
                <el-menu-item index="project">项目管理</el-menu-item>
                <el-menu-item index="project_task">任务管理</el-menu-item>
            </el-submenu>
            <el-submenu index="bug">
                <template slot="title"><i class="el-icon-menu"></i>Bug管理</template>
                <el-menu-item index="bug">Bug管理</el-menu-item>
            </el-submenu>
            <el-submenu index="test">
                <template slot="title"><i class="el-icon-menu"></i>测试管理</template>
                <el-menu-item index="test" >看板</el-menu-item>
            </el-submenu>
            <el-submenu index="ci">
                <template slot="title"><i class="el-icon-menu"></i>持续集成</template>
                <el-menu-item index="ci" >看板</el-menu-item>
            </el-submenu>
            <el-submenu index="test">
                <template slot="title"><i class="el-icon-menu"></i>服务器管理</template>
                <el-menu-item index="server" >看板</el-menu-item>
            </el-submenu>
                
        </el-menu>
    </el-aside>
</template>
<script>
    import localStore from '@/utils/local_store'; 
    export default {
        name:"aside",
        data(){
            let activeMenu = localStore.get("active_menu");
            return{
                activeMenu:activeMenu,
                menuRouters:{
                    "project":"/project/",
                    "project_task":"/project_task/",
                    "project_task_gantt":"/project_task_gantt/",
                    "ci":"/project_ci/",
                    "bug":"/project_bug/",
                    "test":"/project_test/",
                    "server":'/tcis_server/',
                    "user":"/user/",
                    "group":"/group/",
                    "permission":"/permission/"
                }
            }
        },
        methods:{
            selectMenu(index){
                localStore.set("active_menu",index);
                let router = this.menuRouters[index];
                this.$router.push(router);
            }
        },
        created:function(){
            if(this.activeMenu){
                this.$router.push(this.menuRouters[this.activeMenu]);
            }
        }
    }
</script>
