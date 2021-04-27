<template>
  <div>
    <my-header></my-header>
    <div id="container" tabindex="0"></div>
  </div>
</template>

<script>
import myHeader from "@/components/myHeader"
import HelloWorld from "@/components/HelloWorld";
export default {
  components: {
    myHeader,
    HelloWorld,
  },
  data() {
    return {
      map: null,
      dataset: null,
      position: [116.191031, 39.988585]
    }
  },
  mounted() {
    this.dataset =[
      {"lng":116.191031,"lat":39.988585,"count":10},
      {"lng":116.389275,"lat":39.925818,"count":11},
      {"lng":116.287444,"lat":39.810742,"count":12},
      {"lng":116.481707,"lat":39.940089,"count":13},
      {"lng":116.410588,"lat":39.880172,"count":14},
      {"lng":116.394816,"lat":39.91181,"count":15},
      {"lng":116.416002,"lat":39.952917,"count":16}
    ];
    this.map = new AMap.Map('container',{
      center: this.position,
      lang: 'zh_en',
      resizeEnable: true,
      zoom: 14
    });

    let heatmap;
    this.map.plugin(["AMap.Heatmap"], function () {
      //初始化heatmap对象
      heatmap = new AMap.Heatmap(this.map, {
        radius: 25, //给定半径
        opacity: [0, 0.8]
        /*,
        gradient:{
            0.5: 'blue',
            0.65: 'rgb(117,211,248)',
            0.7: 'rgb(0, 255, 0)',
            0.9: '#ffea00',
            1.0: 'red'
        }
         */
      });
      //设置数据集：该数据为北京部分“公园”数据
      heatmap.setDataSet({
        data: this.dataset,
        max: 100
      });
    });

    //判断浏览区是否支持canvas
    function isSupportCanvas() {
      var elem = document.createElement('canvas');
      return !!(elem.getContext && elem.getContext('2d'));
    }
    if (!isSupportCanvas()) {
      alert('热力图仅对支持canvas的浏览器适用,您所使用的浏览器不能使用热力图功能,请换个浏览器试试~')
    }
  }
};
</script>

<style scoped>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

#container{
  height: 500px;
  width: 1000px;
}
</style>
