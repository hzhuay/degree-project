<template>
  <div class="main-area">
    <div class="left-block">
      <list-item></list-item>
    </div>
    <div id="container" tabindex="0"></div>
  </div>
</template>

<script>
import ListItem from "@/components/ListItem";
export default {
  name: "List",
  components: {ListItem},
  data() {
    return {
      position: [],
      map: {}
    }
  },
  mounted() {
    console.log("init");
    this.position = [116.397477, 39.908692];
    this.map = new AMap.Map('container',{
      center: this.position,
      lang: 'zh_en',
      resizeEnable: true,
      zoom: 14,
    })
  },
  methods: {

  }
}
</script>

<style scoped>
  #container{
    position: fixed !important;
    right: 0px;
    bottom: 0px;
    width: 34%;
    top: 70px;
    margin-top: 10px;
  }

  .left-block{
    width: 66%;

  }

  .main-area{

  }
</style>
