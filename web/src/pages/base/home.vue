<template>
    <el-container>
        <Aside/>
        <el-container class="is-vertical">
            <Header/>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>
<script>
    import  {default as Aside} from './aside';
    import  {default as Header} from './header';
    import  {default as Footer} from './footer';
    export default {
        name:"home",
        components:{
            Aside,
            Header,
            Footer
        },
        data(){
            return{}
        }
    }
</script>
