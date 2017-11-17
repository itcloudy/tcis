<template>
    <div id="project-kanban">
         <el-row :gutter="20">
            <project-card v-for="project in projects" :project="project" :key="project.id" />
        </el-row>
    </div>
</template>
<script>
    import  {SERVER_PROJECT} from '@/server_address'; 
    import  {default as ProjectCard} from './project_card';
    export default {
        name:"project_kanban",
        props:["projects"],
        data(){
            return{
                 
            }
        },
        components:{
            ProjectCard,
        }
    }
</script>
