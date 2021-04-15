<template>
  <div class="home">
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <button @click="search(0)">start</button>
    <button @click="write">write</button>
<!--    {{comms}}-->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {request} from "@/network/request";

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data() {
    return {
      comms: {},
      poiSearch: {}
    }
  },
  mounted() {
    // POI查询插件
    AMap.plugin(["AMap.PlaceSearch"], ()=> {
      //构造地点查询类
      this.poiSearch = new AMap.PlaceSearch({
        type: '', // 兴趣点类别
        pageSize: 1, // 单页显示结果条数
        pageIndex: 1, // 页码
        city: "010", // 兴趣点城市
        citylimit: true,        //是否强制限制在设置的城市内搜索
        lang: 'en'
        // map: map, // 展现结果的地图实例
        // autoFitView: true // 是否自动调整地图视野使绘制的 Marker点都处于视口的可见范围
      });
    });
    request({
      url: '/all',
      method: "GET"
    }).then(res => {
      this.comms = res;
      console.log(res);
    }).catch(err => {
      console.log(err);
    });
  },
  methods: {
    search(index) {
      if(index >= this.comms.length){
        this.write();
        return;
      }
      this.poiSearch.search(this.comms[index], (status, result) => {
        // console.log(result.poiList.pois[0]);
        let params = {}
        try{
          params = {
            index: this.comms[index],
            name: result.poiList.pois[0].name,
            address: result.poiList.pois[0].address
          }
        }catch {
          params = {
            index: this.comms[index],
            name: "error",
            address: "error"
          }
        }
        request({
          url: '/write',
          params: params,
          method: "GET"
        }).then(res => {
          // this.comms = res;
          this.search(index + 1);
          console.log(res);
        }).catch(err => {
          console.log(err);
        });

      });
    },
    write() {
      request({
        url: '/write_dict',
        method: "GET"
      })
    }
  }
}
</script>
