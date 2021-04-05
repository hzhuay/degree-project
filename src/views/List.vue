<template>
  <div class="main-area">
    <div class="left-block">
<!--      <div>{{this.list}}</div>-->
<!--      筛选区-->
      <div style=" background-color: #2c3e50" class="select-block">


        <el-button @click="dialogFormVisible = true">地区</el-button>
        <el-dialog title="收货地址" :visible.sync="dialogFormVisible" class="select-dialog">
          <div class="block">
            <span class="demonstration">默认 click 触发子菜单</span>
            <el-cascader
              v-model="value"
              :options="options"

              ></el-cascader>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
          </div>
        </el-dialog>

        <el-button @click="priceDialogVisible = true">price</el-button>
        <el-dialog title="Price Range" :visible.sync="priceDialogVisible" class="select-dialog-price">
          <div class="block">
            <span class="demonstration">默认 click 触发子菜单</span>
            <el-slider
              v-model="priceRange"
              range
              :show-tooltip="false"
              :min="0"
              :max="500"
              @input="priceRangeChange(value)"

              >
            </el-slider>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="priceDialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="priceDialogVisible = false">确 定</el-button>
          </div>
        </el-dialog>


<!--        <vc-calendar :columns="$screens({ default: 1, lg: 2 })"></vc-calendar>-->

      </div>
      <div v-for="(item, index) in list" :key="index" @mouseenter="showMarker(index)" @mouseleave="hideMarker(index)">
        <el-card shadow="hover" style="margin: 10px">
          <el-container style="height: 200px">
            <el-aside style="background-color: black; overflow: hidden">
              <img style="height: 100%; width: 100%" :src="item.url" alt="">
            </el-aside>
            <el-main class="main-text">
              <el-row :gutter="20" style="height: 100%">
                <el-col :span="16" style="height: 100%">
                  <div>
                    <div class="house-info house-title" style="">{{item.name}}</div>
                    <div class="house-info" style="">
                      <i class="el-icon-location-outline"></i>
                      {{item.community}}
                    </div>
                    <div class="house-info">
                      <i class="el-icon-house"></i>
                    </div>
                    <div class="house-info">
                    </div>
                    <div class="house-info">
                      <i class="el-icon-collection-tag"></i>
                      <el-tag size="small" class="house-tag">房本5年</el-tag>
                      <el-tag size="small" type="success" class="house-tag">房本5年</el-tag>
                      <el-tag size="small" type="warning" class="house-tag">房本5年</el-tag>
                      <el-tag size="small" type="danger" class="house-tag">房本5年</el-tag>


                    </div>
                  </div>
                </el-col>

                <el-col :span="8" style="height: 100%; border-left: rgba(0,0,0,0.1) solid 1px">
                  <div class="priceInfo">
                  <span class="totalPrice">
                    {{item.totalPrice}}
                  </span>
                    万
                  </div>
                </el-col>
              </el-row>
            </el-main>
          </el-container>
        </el-card>
      </div>

      <div style="text-align: center">
        <el-pagination background layout="prev, pager, next" :total="total" :page-size="pageSize" :current-page.sync="page" @prev-click="prevPage" @next-click="nextPage" @current-change="currentChange">
        </el-pagination>
      </div>

    </div>
<!--    高德地图-->
    <div id="container" tabindex="0"></div>

  </div>
</template>
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

.main-text{
  text-align: left;
  display: inline-block;
}
.priceInfo{
  text-align: right;

  height: 100%;
  margin-top: 20px;
  color: red;
}
.totalPrice{
  font-size: 26px;
  font-weight: bold;
  font-family: Tahoma;
  text-align: right !important;

}
.house-title{
  font-size: larger;
  overflow: hidden;
  /*white-space: nowrap;*/
  text-overflow: ellipsis;
  max-width: 100%;
  font-weight: bold;

  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  display: -moz-box;
  -moz-line-clamp: 2;
  -moz-box-orient: vertical;
  word-wrap: break-word;
  word-break: break-all;
  white-space: normal;
}
.el-divider--vertical{
  height: auto;
  margin: 0px 15px;
}

.house-info{
  margin-bottom: 10px;
}
.house-tag{
  margin-left: 10px;
  margin-bottom: 10px;
}
.block{
  padding: 0px 20px;
}
.el-dialog{
  width: 30%;
}

</style>

<style>
.amap-icon img{
  width: 25px;
  height: 34px;
}
.amap-marker-selected{

}
.select-dialog-price .el-dialog{
  background-color: #2c3e50;
  width: 30%;
}
</style>


<script>
import {request} from "@/network/request";
import district_data from "@/components/district_data";


export default {
  name: "List",
  components: {},
  data() {
    return {
      list: [],
      map: {},
      marks: [],
      infoWin: {},
      total: 30,
      pageSize: 10,
      page: 1,
      dialogFormVisible: false,
      priceDialogVisible: false,
      priceRange: [0,100],
      formLabelWidth: '120px',
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      options: district_data.options,
      value: '',
      selected: -1

    }
  },
  mounted() {

    this.map = new AMap.Map('container',{
      center: this.position,
      lang: 'zh_en',
      resizeEnable: true,
      zoom: 14,
    });

    this.getData({
      page: 1,
      offset: this.pageSize
    });
  },
  created() {

  },
  methods: {
    nextPage() {
      console.log("next page");
      this.page += 1
      this.getData({
        page: this.page,
        offset: this.pageSize
      })
    },
    prevPage() {
      console.log('prev page');
      this.page -= 1
      this.getData({
        page: this.page,
        offset: this.pageSize
      })
    },
    currentChange() {
      console.log("currentChange");
      this.getData({
        page: this.page,
        offset: this.pageSize
      })
    },
    getData(params){
      if(this.marks.length != 0){
          this.map.remove(this.marks);
      }

      request({
        url: '/getHouses',
        params: params,
        method: "GET"
      }).then(res => {
        this.list = res.data;
        this.total = res.total;

        let start = (this.page-1) * this.pageSize;
        let end = this.page * this.pageSize;
        console.log(this.list)
        //标记点
        for (let i=start; i<end; i++) {
          let tmp = this.list[i]['location'].split(',');
          let p = [Number(tmp[0]), Number(tmp[1])];

          this.marks[i] = new AMap.Marker({
            map: this.map,
            icon: "//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png",
            position: p,
            label: {},
            clickable: true
          });

          this.marks[i].price = String(this.list[i].totalPrice);

          this.marks[i].on('click', this.showInfo);

          // //构建自定义信息窗体，似乎只能有一个
          // this.infoWins[index] = new AMap.InfoWindow({
          //   position: p,
          //   anchor: 'top',
          //   content: '这是信息窗体！',
          // });
          // this.infoWins[index].open(this.map);
        }

        this.map.setFitView();


      }).catch(err => {
        console.log(err);
      });
    },
    showInfo(e) {
      let marker = e.target;

      this.infoWin = new AMap.InfoWindow({
        content: marker.price,  //使用默认信息窗体框样式，显示信息内容
        anchor: "top",
        closeWhenClickMap: true
      });
      this.infoWin.open(this.map, marker.getPosition());

    },
    showMarker(index) {
      // console.log(index);
      // console.log(this.selected);
      if(this.selected == index)return;

      if(this.selected != -1){
        this.marks[this.selected].setIcon("//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png");
        this.marks[this.selected].setzIndex(-1);
      }

      this.marks[index].setIcon("//webapi.amap.com/theme/v1.3/markers/b/mark_r.png");
      this.marks[index].setzIndex(999);
      this.selected = index;
    },
    hideMarker(index) {
      // console.log("hide");
    },
    priceRangeChange(range) {
      console.log(this.priceRange);
    },

  }
}
</script>


