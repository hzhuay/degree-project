<template>
  <div class="about">
    <div class="left-block">
<!--      <input id="communityInput" placeholder="小区名称/address" v-model="address"/>-->

      <el-form  ref="form" :model="form" label-width="100px">
        <el-form-item label="小区地址">
        <el-input id="communityInput" v-model="address" placeholder="小区名称/address"></el-input>
        </el-form-item>

        <el-form-item label="面积">
          <el-input v-model="form.size"></el-input>
        </el-form-item>

        <el-form-item label="朝向">
          <el-checkbox-group v-model="form.direction">
            <el-checkbox label="南" name="direction"></el-checkbox>
            <el-checkbox label="北" name="direction"></el-checkbox>
            <el-checkbox label="西" name="direction"></el-checkbox>
            <el-checkbox label="东" name="direction"></el-checkbox>
            <el-checkbox label="西南" name="direction"></el-checkbox>
            <el-checkbox label="东南" name="direction"></el-checkbox>
            <el-checkbox label="西北" name="direction"></el-checkbox>
            <el-checkbox label="东北" name="direction"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>

        <el-form-item label="供暖方式" >
          <el-radio-group v-model="form.heating">
            <el-radio label="集中供暖"></el-radio>
            <el-radio label="自供暖"></el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item label="行政区">
          <el-select v-model="form.district" placeholder="请选择活动区域">
            <el-option label="东城区" value="0"></el-option>
            <el-option label="西城区" value="1"></el-option>
            <el-option label="朝阳区" value="2"></el-option>
            <el-option label="丰台区" value="3"></el-option>
            <el-option label="海淀区" value="4"></el-option>
            <el-option label="石景山区" value="5"></el-option>
            <el-option label="大兴区" value="6"></el-option>
            <el-option label="房山区" value="7"></el-option>
            <el-option label="昌平区" value="8"></el-option>
            <el-option label="顺义区" value="9"></el-option>
            <el-option label="通州区" value="10"></el-option>
            <el-option label="门头沟区" value="11"></el-option>
            <el-option label="密云区" value="12"></el-option>
            <el-option label="怀柔区" value="13"></el-option>
            <el-option label="延庆区" value="14"></el-option>
            <el-option label="亦庄开发区" value="15"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="环数">
          <el-select v-model="form.ring" placeholder="请选择环数">
            <el-option label="二环内" value="0"></el-option>
            <el-option label="二环 - 三环" value="1"></el-option>
            <el-option label="三环 - 四环" value="2"></el-option>
            <el-option label="四环 - 五环" value="3"></el-option>
            <el-option label="五环 - 六环" value="4"></el-option>
            <el-option label="六环外" value="5"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="房间分配 ">
          <el-row :gutter="0">
            <el-col :span="5">
              <el-input v-model="form.room" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="1">室</el-col>

            <el-col :span="5">
              <el-input v-model="form.hall" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="1">厅</el-col>

            <el-col :span="5">
              <el-input v-model="form.toilet" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="1">卫</el-col>

            <el-col :span="5">
              <el-input v-model="form.kitchen" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="1">厨</el-col>
          </el-row>
        </el-form-item>

        <el-form-item label="有无电梯">
          <el-switch v-model="form.elevator"></el-switch>
        </el-form-item>

        <el-form-item label="装修情况">
          <el-select v-model="form.decoration" placeholder="">
            <el-option label="精装/Exquisite Decoration" value="0"></el-option>
            <el-option label="简装/Simple Decoration" value="1"></el-option>
            <el-option label="毛坯/Roughcast House" value="2"></el-option>
            <el-option label="其他/Other" value="3"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="户型">
          <el-select v-model="form.structure" placeholder="">
            <el-option label="平层/Flat" value="0"></el-option>
            <el-option label="复式/maisonette" value="1"></el-option>
            <el-option label="跃层" value="2"></el-option>
            <el-option label="错层" value="3"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="总楼层数">
          <el-input v-model="form.totalFloor" placeholder="请输入内容"></el-input>
        </el-form-item>

        <el-form-item label="楼层">
          <el-select v-model="form.floor" placeholder="">
            <el-option label="地下室/Basement" value="0"></el-option>
            <el-option label="底层/Ground Floor" value="1"></el-option>
            <el-option label="低层/Low Floor" value="2"></el-option>
            <el-option label="中层/Middle Floor" value="3"></el-option>
            <el-option label="高层/High Floor" value="4"></el-option>
            <el-option label="顶层/Top Floor" value="5"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="predict">预测房价</el-button>
        </el-form-item>

      </el-form>
      <p>{{form.mall}}</p>
      <p>{{form.traffic}}</p>
      <p>{{form.school}}</p>
      <p>{{form.medicine}}</p>
    </div>
    <div id="container" tabindex="0"></div>
  </div>
</template>

<script>
import {request} from "@/network/request";

export default{
  name: 'Map',
  data() {
    return {
      position: [],
      map: {},
      circle: {},
      address: "",
      geocoder: {},
      marker: {},
      poiSearch: {},
      test: "",
      form: {
        mall: -1,
        medicine: -1,
        school: -1,
        traffic: -1,
        size: 0,
        direction: [],
        heating: 0,
        district: 0,
        ring: 0,
        room: 0,
        hall: 0,
        toilet: 0,
        kitchen: 0,
        elevator: true,
        decoration: 0,
        structure: 0,
        totalFloor: 0,
        floor: 0
      }
    }
  },
  mounted() {
    console.log("mounted");
    this.init();
  },
  created() {
    console.log("created");
  },
  methods: {
    // 实例化地图
    init(){
      let that = this;
      console.log("init");
      this.position = [116.397477, 39.908692];
      this.map = new AMap.Map('container',{
        center: this.position,
        lang: 'zh_en',
        resizeEnable: true,
        zoom: 14,
      })

      // 地图上的样式组件
      AMap.plugin(['AMap.ToolBar', 'AMap.Scale'], () => {
        this.map.addControl(new AMap.ToolBar())
        this.map.addControl(new AMap.Scale())
      })

      //输入提示
      AMap.plugin('AMap.Autocomplete', function(){
        let autoComplete= new AMap.Autocomplete({
          city: "010",
          input: "communityInput",
          citylimit: true
        });
        // 无需再手动执行search方法，autoComplete会根据传入input对应的DOM动态触发search
        AMap.event.addListener(autoComplete, 'select', function(e) {
          that.address = e.poi.name;
          that.getPosition();
          that.searchPOI();
        })
      })

      //地理编码
      this.geocoder = new AMap.Geocoder({
        city: "010", //城市设为北京，默认：“全国”
      });

      //标记点
      this.marker = new AMap.Marker({
        map: this.map,
        icon: "https://webapi.amap.com/theme/v1.3/markers/n/mark_b.png",
        position: this.position,
        label: {
          offset: new AMap.Pixel(10, -30),//修改label相对于maker的位置
          content: "不知道在哪里"
        }
        // offset: [2,2]
      });

      // 画圆
      this.circle = new AMap.Circle({
        center: this.position,
        radius: 2000, //半径
        borderWeight: 1,
        strokeColor: "#FF33FF",
        strokeWeight: 3,
        strokeOpacity: 0.2,
        fillOpacity: 0.3,
        strokeStyle: 'dashed',
        strokeDasharray: [10, 10],
        fillColor: '#1791fc',
        zIndex: 50,
      })
      this.map.add(this.circle);

      // POI查询插件
      AMap.plugin(["AMap.PlaceSearch"], ()=> {
        //构造地点查询类
        this.poiSearch = new AMap.PlaceSearch({
          type: '', // 兴趣点类别
          pageSize: 5, // 单页显示结果条数
          pageIndex: 1, // 页码
          city: "010", // 兴趣点城市
          citylimit: true,        //是否强制限制在设置的城市内搜索
          // map: map, // 展现结果的地图实例
          // autoFitView: true // 是否自动调整地图视野使绘制的 Marker点都处于视口的可见范围
        });
      });

      // 点击点标记，跳转高德地图
      this.marker.on('click', () => {
        this.marker.markOnAMAP({
          name: '首开广场',
          position: this.marker.getPosition()
        })
      })
    },
    searchPOI(){

      this.poiSearch.setType("综合医院|专科医院|诊所|急救中心|疾病预防机构|医药保健销售店");
      this. poiSearch.searchNearBy('', this.position, 2000, (status, result) => {
        this.form.medicine = result['poiList']['count'];

      });

      //查学校
      this.poiSearch.setType('中学|小学|幼儿园');
      this.poiSearch.searchNearBy('', this.position, 2000, (status, result) => {
        this.form.school = result['poiList']['count'];
      });

      //查商场
      this.poiSearch.setType('商场');
      this.poiSearch.searchNearBy('', this.position, 2000, (status, result) => {
        this.form.mall = result['poiList']['count'];
      });

      //查交通
      this.poiSearch.setType('地铁站|轻轨站|公交车站');
      this.poiSearch.searchNearBy('', this.position, 2000, (status, result) => {
        this.form.traffic = result['poiList']['count'];
      });

    },
    getPosition(){
      console.log("this " + this);
      this.geocoder.getLocation(this.address, (status, result) => {

        if (status === 'complete' && result.geocodes.length) {
          this.position = result.geocodes[0].location
          console.log(this);

          this.marker.setPosition(this.position);
          this.map.add(this.marker);
          // map.setFitView(marker);
          this.map.setCenter(this.position);
          this.circle.setCenter(this.position);
        } else {
          log.error('根据地址查询位置失败');
        }
      });
    },
    predict() {
      request({
        url: '/predict',
        data: this.form,
        method: "POST"
      }).then(res => {
        console.log(res);
      }).catch(err => {
        console.log(err);
      })
      // axios.post('http://127.0.0.1:5000/predict', this.form).then(res => {
      //   console.log(res);
      // })
    }

  },
}

</script>

<style scoped>
  #container{
    float: right;
    flex: 1;
  }
  .about{
    display: flex;
  }
  .left-block{
    flex: 1;
  }

</style>

<style>
.el-input-number--small{
  width: 80%;
}

</style>
