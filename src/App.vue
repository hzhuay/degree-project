<template>
  <div id="app">
    <div id="nav" class="fix-head">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/learn">Learn</router-link> |
      <router-link to="/list">List</router-link>
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
        isfix: false
      }
    },
    methods: {
      jump() {
        this.$router.push('/user/' + this.userId);
        this.$router.replace()
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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
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
  height: 80px;
  width: 100%;
}
</style>
