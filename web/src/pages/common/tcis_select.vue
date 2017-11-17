<template>
    <div class="tcis-select">
        <el-select v-model="selectValue" :placeholder="placeholder" filterable @change="filterSelectChange">
            <el-option
            v-for="item in selectList"
            :key="item.value"
            :label="item.label"
            :value="item.value">
            </el-option>
        </el-select>
    </div>
</template>
<script>
    export default {
        name:"tcis_select",
        props:["selectList","placeholder"],
        data(){
            return{
                selectValue:null,
            }
        },
        methods:{
            filterSelectChange(){
                this.$emit("filterSelectChange",this.selectValue);
            }
        },
    }
</script>
<style lang="scss" scoped>
    .tcis-select{
        display: inline-block;
    }
</style>



