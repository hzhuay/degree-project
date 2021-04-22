<template>
  <div id="app">
    <div id="nav" class="fix-head">
<!--      <router-link to="/">Home</router-link> |-->
<!--      <router-link to="/about">About</router-link> |-->
<!--      <router-link to="/learn">Learn</router-link> |-->
<!--      <router-link to="/list">List</router-link>-->


      <el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect" router
               style="display: flow">
        <el-menu-item index="/">Home</el-menu-item>
        <el-menu-item index="about">Predict</el-menu-item>
        <el-menu-item index="list">List</el-menu-item>
        <el-menu-item style="float: right;">
          <el-input
            placeholder="请输入内容"
            prefix-icon="el-icon-search"
            v-model="input3" size="small" style=" vertical-align: middle">
          </el-input>
        </el-menu-item>

      </el-menu>
    </div>
    <div class="head-place"></div>

<!--      <router-link :to="'/user/'+userId">用户</router-link>-->
<!--      <router-link :to="{path: '/profile', query: {name: 'Jack', age: 18}}"></router-link>-->
<!--      <button @click="jump">跳转</button>-->

    <router-view></router-view>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: 'Jack',
        userId: 1,
        isfix: false,
        activeIndex: '1',
        input3: ''
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
}


#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #409EFF;
}

.fix-head{
  background-color: #f6f6f6;
  position: fixed;
  top: 0px;
  width: 100%;
  height: 10px;
  z-index: 999;
}

.head-place{
  height: 40px;
  width: 100%;
}

.el-menu{
  height: 40px; width: 100%; position: fixed; top: 0px; left: 0px; right: 0px; background-color: #f6f6f6; z-index: 999
}

.el-menu-item{
  height: 40px !important;
  line-height: 40px !important;
}
</style>
