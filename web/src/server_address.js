// 服务器端地址

export const SERVER_USER = "/user/"; //用户
export const SERVER_USER_LOGIN = "/user/login/"; //用户登录
export const SERVER_USER_LOGOUT = "/user/logout/"; //用户登出
export const SERVER_USER_RESET_PASSWORD = "/user/reset_password/"; //重置密码
export const SERVER_USER_ACTIVE = '/user/user_active/'; // 无效用户
export const SERVER_GROUP = "/group/"; //用户组
export const SERVER_PERMISSION = "/permission/"; //用户权限
export const SERVER_PERMISSION_ALL = "/permission/get_all_permission/"; //所有用户权限
export const SERVER_PERMISSION_TRANSLATE = "/permission/translate_all_permission/"; //权限翻译

export const SERVER_PROJECT = "/project/project/"; //项目
export const SERVER_PROJECT_ALL = "/project/project/get_all_project/"; //所有项目
export const SERVER_PROJECT_TASK = "/project/project_task/"; //项目任务
export const SERVER_PROJECT_TASK_INFO = '/project/project_task/project_task_kanban/'; //项目任务信息
export const SERVER_PROJECT_TASK_GANTT = '/project/project_task/project_task_gantt/'; //项目任务甘特图
export const SERVER_PROJECT_MEMBER = "/project/project_member/"; //项目组成员
export const SERVER_PROJECT_BUG = "/project_bug/project_bug/"; //项目bug
export const SERVER_PROJECT_BUG_INFO = "/project_bug/project_bug/project_bug_kanban/"; //项目bug信息

export const SERVER_PROJECT_TEST = "/project_test/project_test/"; //项目test
export const SERVER_PROJECT_TEST_INFO = "/project_test/project_test/project_test_kanban/"; //项目test信息
export const SERVER_PROJECT_TEST_TYPE = "/project_test/project_test_type/"; //项目test类型