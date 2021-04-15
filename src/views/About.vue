<template>
  <div class="about-area">
    <div class="left-block">
<!--      <input id="communityInput" placeholder="小区名称/address" v-model="address"/>-->
      <div style="margin: 10px 0px">
        <el-form  ref="form" :model="form" label-width="100px">
          <el-row style="padding-right: 20px">
<!--            <el-col :span="12">-->
<!--              <el-form-item label="小区地址">-->
<!--                <el-input id="communityInput" v-model="address" placeholder="小区名称/address" @change="getPosition"></el-input>-->
<!--              </el-form-item>-->
<!--            </el-col>-->

            <el-col :span="12">
              <el-form-item label="Address">
                <el-autocomplete autocomplete="on" v-model="address" :fetch-suggestions="querySearchAsync" placeholder="Pleace Enter Community Address" :trigger-on-focus="false"
                  @select="handleSelect" value-key="name" style="width: 80%"></el-autocomplete>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Area">
                <el-input v-model="form.area" maxlength="10" style="width: 80%"></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Total Floor">
                <el-input v-model="form.totalFloor" placeholder="=" style="width: 80%"></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Elevator Rate">
                  <el-input v-model="form.elevatorRate" placeholder="" style="width: 80%"></el-input>
              </el-form-item>
            </el-col>

            <el-col :span="24">
              <el-form-item label="Directions">
                <el-checkbox-group v-model="form.directions">
                  <el-checkbox label="S" name="direction"></el-checkbox>
                  <el-checkbox label="N" name="direction"></el-checkbox>
                  <el-checkbox label="W" name="direction"></el-checkbox>
                  <el-checkbox label="E" name="direction"></el-checkbox>
                  <el-checkbox label="SW" name="direction"></el-checkbox>
                  <el-checkbox label="SE" name="direction"></el-checkbox>
                  <el-checkbox label="NW" name="direction"></el-checkbox>
                  <el-checkbox label="NE" name="direction"></el-checkbox>
                </el-checkbox-group>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Heating" >
                <el-radio-group v-model="form.heating">
                  <el-radio label="0">self-heating</el-radio>
                  <el-radio label="1">central-heating</el-radio>
                </el-radio-group>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Have elevator">
                <el-switch v-model="form.elevator" :active-value="1" :inactive-value="1"></el-switch>
              </el-form-item>
            </el-col>

<!--            <el-col :span="12">-->
<!--              <el-form-item label="行政区">-->
<!--                <el-select v-model="form.district" placeholder="请选择活动区域">-->
<!--                  <el-option label="东城区" value="0"></el-option>-->
<!--                  <el-option label="西城区" value="1"></el-option>-->
<!--                  <el-option label="朝阳区" value="2"></el-option>-->
<!--                  <el-option label="丰台区" value="3"></el-option>-->
<!--                  <el-option label="海淀区" value="4"></el-option>-->
<!--                  <el-option label="石景山区" value="5"></el-option>-->
<!--                  <el-option label="大兴区" value="6"></el-option>-->
<!--                  <el-option label="昌平区" value="7"></el-option>-->
<!--                  <el-option label="顺义区" value="8"></el-option>-->
<!--                  <el-option label="通州区" value="9"></el-option>-->
<!--                  <el-option label="房山区" value="10"></el-option>-->
<!--                  <el-option label="门头沟区" value="11"></el-option>-->
<!--                  <el-option label="延庆区" value="12"></el-option>-->
<!--                  <el-option label="怀柔区" value="13"></el-option>-->
<!--                  <el-option label="密云区" value="14"></el-option>-->
<!--                  <el-option label="亦庄开发区" value="15"></el-option>-->
<!--                  <el-option label="平谷区" value="16"></el-option>-->
<!--                </el-select>-->
<!--              </el-form-item>-->
<!--            </el-col>-->

            <el-col :span="12">
              <el-form-item label="Ring">
                <el-select v-model="form.ring" placeholder="请选择环数">
                  <el-option label="二环内/Within 2nd Ring" value="0"></el-option>
                  <el-option label="二环 - 三环/2nd - 3rd Ring" value="1"></el-option>
                  <el-option label="三环 - 四环/3rd - 4th Ring" value="2"></el-option>
                  <el-option label="四环 - 五环/4th - 5th Ring" value="3"></el-option>
                  <el-option label="五环 - 六环/5th - 6th Ring" value="4"></el-option>
                  <el-option label="六环外/Outside 6th Ring" value="5"></el-option>
                </el-select>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Decoration">
                <el-select v-model="form.decoration" placeholder="">
                  <el-option label="精装/Exquisite Decoration" value="0"></el-option>
                  <el-option label="简装/Simple Decoration" value="1"></el-option>
                  <el-option label="毛坯/Roughcast House" value="2"></el-option>
                  <el-option label="其他/Other" value="3"></el-option>
                </el-select>
              </el-form-item>
            </el-col>

            <el-col :span="12">
              <el-form-item label="Structure">
                <el-select v-model="form.structure" placeholder="">
                  <el-option label="平层/Flat" value="0"></el-option>
                  <el-option label="复式/Maisonette" value="1"></el-option>
                  <el-option label="跃层/Loft" value="2"></el-option>
                  <el-option label="错层/Staggered floor" value="3"></el-option>
                </el-select>
              </el-form-item>
            </el-col>




            <el-col :span="12">
              <el-form-item label="Floor">
                <el-select v-model="form.floor" placeholder="">
                  <el-option label="地下室/Basement" value="0"></el-option>
                  <el-option label="底层/Ground Floor" value="1"></el-option>
                  <el-option label="低层/Low Floor" value="2"></el-option>
                  <el-option label="中层/Middle Floor" value="3"></el-option>
                  <el-option label="高层/High Floor" value="4"></el-option>
                  <el-option label="顶层/Top Floor" value="5"></el-option>
                </el-select>
              </el-form-item>
            </el-col>

            <el-col :span="24">

              <el-form-item label="Allocation">
                <el-col :span="5">
                  <el-input v-model="form.room" placeholder="">
                    <template slot="append">Room</template>
                  </el-input>
                </el-col>
                <el-col :span="1" style="color:white;">-</el-col>
                <el-col :span="5">
                  <el-input v-model="form.parlor" placeholder="">
                    <template slot="append">Parlor</template>
                  </el-input>
                </el-col>
                <el-col :span="1" style="color:white;">-</el-col>
                <el-col :span="5">
                  <el-input v-model="form.bathroom" placeholder="">
                    <template slot="append">Toilet</template>
                  </el-input>
                </el-col>
                <el-col :span="1" style="color:white;">-</el-col>
                <el-col :span="5">
                  <el-input v-model="form.kitchen" placeholder="">
                    <template slot="append">Kitchen</template>
                  </el-input>
                </el-col>
                <el-col :span="1" style="color:white;">-</el-col>
              </el-form-item>

            </el-col>


            <el-col :span="24" style="display: flow">
              <label style="color: #606266; font-size: 14px; margin-left: 20px">Total House Price:</label>
              <el-input v-model="prediction" maxlength="10" style="width: 30%; margin-left: 15px"></el-input>
              <el-button type="primary" @click="predict" style="float: right; margin-right: 25px">Predict</el-button>
            </el-col>
          </el-row>




        </el-form>

      </div>

    </div>
    <div id="container" tabindex="0"></div>
  </div>
</template>

<script>
import {request, post} from "@/network/request";

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
        area: 0,
        directions: [],
        heating: '0',
        district: 0,
        ring: 0,
        room: 0,
        parlor: 0,
        bathroom: 0, // toilet
        kitchen: 0,
        elevator: true,
        elevatorRate: 0,
        decoration: 0,
        structure: 0,
        totalFloor: 0,
        floor: 0,

      },
      prediction: undefined
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
        // label: {
        //   offset: new AMap.Pixel(10, -30),//修改label相对于maker的位置
        //   content: "不知道在哪里"
        // }
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
          pageSize: 10, // 单页显示结果条数
          pageIndex: 1, // 页码
          city: "010", // 兴趣点城市
          citylimit: true,        //是否强制限制在设置的城市内搜索
          lang: 'en'
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
      console.log("在查了 "+ this.address);

      this.geocoder.getLocation(this.address, (status, result) => {

        if (status === 'complete' && result.geocodes.length) {
          this.position = result.geocodes[0].location;
          this.marker.setPosition(this.position);
          this.map.add(this.marker);
          // map.setFitView(marker);
          this.map.setCenter(this.position);
          this.circle.setCenter(this.position);
        } else {
          console.log("查不到");
          log.error('根据地址查询位置失败');
        }
      });
    },
    predict() {
      console.log(this.form);
      post({
        url: '/predict',
        data: this.form,
      }).then(res => {
        console.log(res);
        this.prediction = res;
      }).catch(err => {
        console.log(err);
      })
    },
    handleSelect(item) {
      console.log(item);
      // this.getPosition();
      this.position = [item.location.lng, item.location.lat];
      this.marker.setPosition(this.position);
      this.map.add(this.marker);
      // map.setFitView(marker);
      this.map.setCenter(this.position);
      this.circle.setCenter(this.position);
      this.searchPOI();
    },
    querySearchAsync(queryString, callback) {
      // callback([{'value':'a','address':'1'},{'value':'b','address':'2'}]);

      this.poiSearch.search(queryString, (status, result) => {
        console.log(result);
        try{
          callback(result.poiList.pois);
        }catch {
          callback([]);
        }

      });
    }

  },
}

</script>

<style scoped>
  #container{
    position: fixed !important;
    right: 0px;
    bottom: 0px;
    width: 40%;
    top: 50px;
  }

  .left-block{
    width: 60%;
    /*margin-left: 20px;*/
    /*background-color: #42b983;*/
    /*margin-right: 20px;*/
  }

  .about-area{

  }
  .right-block{
    flex: 2;
    height: 200px;
    background-color: gray;
  }

</style>

<style>
.el-input-number--small{
  width: 80%;
}

</style>
