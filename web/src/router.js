import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const Login = resolve => require(['@/pages/base/login'], resolve);
const Home = resolve => require(['@/pages/base/home'], resolve);
const Page404 = resolve => require(['@/pages/common/page_404'], resolve);

const MiddleRouterView = resolve => require(['@/pages/common/middle_router_view'], resolve);
// 权限组
const GroupHome = resolve => require(['@/pages/system/group/group_home'], resolve);
const GroupInfo = resolve => require(['@/pages/system/group/group_detail_home'], resolve);

// 权限明细
const PermissionForm = resolve => require(['@/pages/system/permission/permission_home'], resolve);
// 用户
const UserHome = resolve => require(['@/pages/system/user/user_home'], resolve);
const UserInfo = resolve => require(['@/pages/system/user/user_detail_home'], resolve);
// 项目管理
const ProjectHome = resolve => require(['@/pages/project/project_home'], resolve);
const ProjectInfo = resolve => require(['@/pages/project/project_detail_home'], resolve);
// 项目任务管理
const ProjectTaskHome = resolve => require(['@/pages/project/project_task_home'], resolve);
const ProjectTaskInfo = resolve => require(['@/pages/project/project_task_detail_home'], resolve);

// 项目bug
const ProjectBugHome = resolve => require(['@/pages/project_bug/project_bug_home'], resolve);
const ProjectBugInfo = resolve => require(['@/pages/project_bug/project_bug_detail_home'], resolve);

// 项目集成
const ProjectCIHome = resolve => require(['@/pages/project_ci/project_ci_home'], resolve);
const ProjectCIInfo = resolve => require(['@/pages/project_ci/form'], resolve);

// 项目测试
const ProjectTestHome = resolve => require(['@/pages/project_test/project_test_home'], resolve);
const ProjectTestInfo = resolve => require(['@/pages/project_test/project_test_detail_home'], resolve);

let routes = [{
        path: "/",
        name: "home",
        component: Home,
        children: [
            // 用户组
            { path: "/group/:id", component: GroupInfo, },
            { path: "/group/", component: GroupHome, },

            // 用户
            { path: "/user/:id", component: UserInfo, },
            { path: "/user/", component: UserHome, },

            // 权限
            { path: "/permission/", component: PermissionForm, },
            // 项目管理
            { path: "/project/:id", component: ProjectInfo, },
            { path: "/project/", component: ProjectHome, },
            { path: "/project_task/:id", component: ProjectTaskInfo, },
            { path: "/project_task/", component: ProjectTaskHome, },
            // 项目集成
            { path: "/project_ci/:id", component: ProjectCIInfo, },
            // Bug管理
            { path: "/project_bug/:id", component: ProjectBugInfo, },
            { path: "/project_bug/", component: ProjectBugHome, },
            // 测试管理
            { path: "/project_test/:id", component: ProjectTestInfo, },
            { path: "/project_test/", component: ProjectTestHome, },

        ]
    },
    { path: "/login", name: 'login', component: Login },
    // error
    { path: "/*", name: 'error', component: Page404 },

];

export default new VueRouter({
    // mode: 'history',
    base: __dirname,
    routes: routes
});