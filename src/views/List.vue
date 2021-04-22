<template>
  <div class="main-area">
    <div class="left-block">
<!--      <div>{{this.list}}</div>-->
<!--      筛选区-->
      <div style="border-bottom: #f6f6f6 1px solid; padding: 5px 0px; display: flow">


        <el-button @click="locationDialogVisible = true" size="mini" :type="location[0] == null ? '' : 'primary'" class="select-button">{{ location[0] == null ? "Location" : location[1] }}</el-button>
        <el-dialog title="Select district and block" :visible.sync="locationDialogVisible" class="select-dialog" :before-close="locationChange">
          <div class="block" style="text-align: center;">
            <el-cascader v-model="location" :options="options" placeholder="">
              <template slot-scope="{ node, data }">
                <span>{{ data.label }}</span>
                <span v-if="!node.isLeaf"> ({{ data.children.length }}) </span>
              </template>
            </el-cascader>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="location=''">Reset</el-button>
            <el-button type="primary" @click="locationChange" >Confirm</el-button>
          </div>
        </el-dialog>

        <el-button @click="priceDialogVisible=true" :type="priceRange[0]==0&&priceRange[1]==maxPriceRange ? '' : 'primary'"
                   class="select-button" size="mini">{{ priceRangeBtn }}</el-button>
        <el-dialog title="Price Range" :visible.sync="priceDialogVisible" class="select-dialog" :before-close="priceRangeChange">
          <div class="block">
            <div>
              <el-row :gutter="20">
                <el-col :span="11">
                  <el-input v-model="minPrice">
                    <img slot="prefix" src="../assets/img/rmb.png" style="height: 20px; position: absolute; margin: auto; top: 0px; bottom: 0px">
                  </el-input>
                </el-col>
                <el-col :span="2" >
                  <span style="text-align: center; height: 40px; line-height: 40px; font-size: 26px;">-</span>
                </el-col>
                <el-col :span="11">
                  <el-input v-model="maxPrice">
                    <img slot="prefix" src="../assets/img/rmb.png" style="height: 20px; position: absolute; margin: auto; top: 0px; bottom: 0px">
                  </el-input>
                </el-col>
              </el-row>

            </div>
            <!--            价格区间-->
            <el-slider v-model="priceRange" range :show-tooltip="false" :min="0" :max="maxPriceRange" :step="1"></el-slider>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="priceRange=[0,maxPriceRange]">Reset</el-button>
            <el-button type="primary" @click="priceRangeChange">Confirm</el-button>
          </div>
        </el-dialog>

        <el-button @click="areaDialogVisible = true" :type="areaRange[0]==0&&areaRange[1]==200 ? '' : 'primary'"
                   class="select-button" size="mini">{{ areaRangeBtn }}</el-button>
        <el-dialog title="Price Range" :visible.sync="areaDialogVisible" class="select-dialog" :before-close="areaRangeChange">
          <div class="block">
            <div>
              <el-row :gutter="20">
                <el-col :span="11">
                  <el-input v-model="areaRange[0]" readonly>
                    <img slot="suffix" src="../assets/img/m2.png" style="height: 20px; position: absolute; margin: auto; top: 0px; bottom: 0px; right: 0px">
                  </el-input>
                </el-col>
                <el-col :span="2" >
                  <span style="text-align: center; height: 40px; line-height: 40px; font-size: 26px;">-</span>
                </el-col>
                <el-col :span="11">
                  <el-input v-model="areaRange[1] == 200 ? areaRange[1]+'+' : areaRange[1]" readonly>
                    <img slot="suffix" src="../assets/img/m2.png" style="height: 20px; position: absolute; margin: auto; top: 0px; bottom: 0px; right:0px">
                  </el-input>
                </el-col>
              </el-row>

            </div>
            <!--            面积区间-->
            <el-slider v-model="areaRange" range :show-tooltip="false" :min="0" :max="200" :step="1"></el-slider>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="areaRange=[0,200]">Reset</el-button>
            <el-button type="primary" @click="areaRangeChange">Confirm</el-button>
          </div>
        </el-dialog>
        <el-button-group style="flow: right">
          <i icon="el-icon-sort"></i>
          <el-button @click="sortByPrice" :type="sortBy==1 ? 'primary' : ''" class="select-button" size="mini">
            Price
            <i :class="priceClass" class="el-icon--right"></i>
          </el-button>
          <el-button @click="sortByIndex" :type="sortBy==2 ? 'primary' : ''" class="select-button" size="mini">
            recommendation
            <i :class="indexClass" class="el-icon--right"></i>
          </el-button>
        </el-button-group>



      </div>
      <div v-for="(item, index) in list" :key="index" @mouseenter="showMarker(index)" @mouseleave="hideMarker(index)" style="cursor: pointer" @click="aaa(index)">
        <el-card shadow="hover" style="margin: 10px" >
          <el-container style="height: 200px;" >
            <el-aside style="background-color: black; overflow: hidden">
              <el-image style="height: 200px; width: 300px" fit="fit" :src="require('@/assets/img/house'+ index +'.jpg')" alt=""></el-image>
            </el-aside>
            <el-main class="main-text">
              <el-row :gutter="20" style="height: 100%">
                <el-col :span="16" style="height: 100%">
                  <div>
                    <div class="house-info house-title two-line" style=" cursor:pointer">
                      {{item.title}}
                    </div>
                    <div class="house-info one-line" style="">
                      <i class="el-icon-map-location"></i>
                      {{item.name}}
                    </div>
                    <div class="house-info" style="font-size: x-small">
                      <i class="el-icon-house" style="font-size: medium"></i>
                      {{item.des}}
                    </div>
                    <div class="house-info two-line">
                      <i class="el-icon-collection-tag"></i>
                      <el-tag size="small" class="house-tag">Good</el-tag>
                      <el-tag size="small" type="success" class="house-tag">Nice</el-tag>
                      <el-tag size="small" type="warning" class="house-tag">Perfect</el-tag>
                      <el-tag size="small" type="danger" class="house-tag">Wonderful</el-tag>
                    </div>
                  </div>
                </el-col>

                <el-col :span="8" style="; border-left: rgba(0,0,0,0.1) solid 1px; height: 100%">
                  <div class="priceInfo">
                    <span class="totalPrice">{{item.total_price.toFixed(2)}}</span>
                    million
                  </div>
                  <div style="text-align: right; font-size: small">
                    {{ '¥ ' + item.avg_price + '/㎡'}}
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

<!--      <el-backtop target=".left-block"></el-backtop>-->

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
  top: 40px;
}

.left-block{
  width: 66%;
}

.main-text{
  text-align: left;
  display: inline-block;
  overflow: hidden;
}
.priceInfo{
  text-align: right;
  height: auto;
  margin-top: 20px;
  color: red;
  display: inline-block;
  width: 100%;
}
.totalPrice{
  font-size: 26px;
  font-weight: bold;
  font-family: Tahoma;
  text-align: right !important;
}
.house-title{
  font-size: larger;
  max-width: 100%;
  font-weight: bold;
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

.select-button{
  margin-left: 10px;
}

</style>

<style>
.amap-icon img{
  width: 25px;
  height: 34px;
}
.amap-marker-selected{

}
.select-dialog .el-dialog{
  /*background-color: #2c3e50;*/
  width: 30%;
  /*position: absolute;*/
  /*top: 40px;*/
  /*left: 30px;*/
}
.el-card__body{
  padding: 0px;
}
.info-title{
  margin: 10px 10px 0px 10px;
  color: #484848;
  font-size: 12px;
}
.info-name{
  margin: 10px 10px 0px 10px;
  color: #767676;
  font-size: 10px;
  line-height: 1.33333em;
  font-weight: 800;
}
.two-line{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  /*-moz-line-clamp: 2;*/
  /*-moz-box-orient: vertical;*/
  word-wrap: break-word;
  word-break: normal;
  white-space: normal;
}
.one-line{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  /*-moz-line-clamp: 2;*/
  /*-moz-box-orient: vertical;*/
  word-wrap: break-word;
  word-break: normal;
  white-space: normal;
}
</style>

<script>
import {request} from "@/network/request";
import district_data from "@/utils/district_data";
import {format} from "@/utils/funs";


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
      cnt: 10,
      page: 1,
      locationDialogVisible: false,
      priceDialogVisible: false,
      areaDialogVisible: false,
      maxPriceRange: 20,
      priceRange: [0,20],
      areaRange: [0, 200],
      formLabelWidth: '120px',
      options: district_data.options,
      value: '',
      selected: -1,
      location: [null, null],
      sortBy: 2, // 第一个数字表示正在根据哪个属性排序，第二个表示升序还是降序
      sortRule: 0

    }
  },
  computed: {
    maxPrice() {
      return this.priceRange[1] == this.maxPriceRange ? this.priceRange[1] + ' million+' : this.priceRange[1] + ' million';
    },
    minPrice() {
      return this.priceRange[0] + ' million';
    },
    params() {
      return {
        page: this.page,
        offset: this.pageSize,
        minPrice: this.priceRange[0],
        maxPrice: this.priceRange[1],
        district: this.location[0],
        block: this.location[1],
        minArea: this.areaRange[0],
        maxArea: this.areaRange[1],
        sortBy: this.sortBy,
        sortRule: this.sortRule,
      }
    },
    locationSelected() {
      return this.location[0] != null;
    },
    priceRangeBtn() {
      if(this.priceRange[0] == 0 && this.priceRange[1] == this.maxPriceRange){
        return "Price";
      }else if(this.priceRange[0] == 0 && this.priceRange[1] != this.maxPriceRange){
        return format("< {0} million", this.priceRange[1]);
      }else if(this.priceRange[0] != 0 && this.priceRange[1] == this.maxPriceRange){
        return format("> {0} million", this.priceRange[0]);
      }else if(this.priceRange[0] != 0 && this.priceRange[1] != this.maxPriceRange){
        return format("¥ {0} m - ¥ {1} m", this.priceRange[0], this.priceRange[1]);
      }
    },
    areaRangeBtn() {
      if(this.areaRange[0] == 0 && this.areaRange[1] == 200){
        return "Area";
      }else if(this.areaRange[0] == 0 && this.areaRange[1] != 200){
        return format("< {0} ㎡", this.areaRange[1]);
      }else if(this.areaRange[0] != 0 && this.areaRange[1] == 200){
        return format("> {0} ㎡", this.areaRange[0]);
      }else if(this.areaRange[0] != 0 && this.areaRange[1] != 200){
        return format("{0} ㎡ - {1} ㎡", this.areaRange[0], this.areaRange[1]);
      }
    },
    priceClass() {
      return {
        'el-icon-sort-up': this.sortBy==1 && this.sortRule==0,
        'el-icon-sort-down': this.sortBy==1 && this.sortRule==1,
        'el-icon-sort': this.sortBy!=1
      }

      // return this.sortBy==1 ? ['el-icon-sort-up','el-icon-sort-down'][this.sortStatus[1]] : 'el-icon-sort';
      // return 'el-icon-sort-up'
    },
    indexClass() {
      // return this.sortBy==2 ? ['el-icon-sort-up','el-icon-sort-down'][this.sortStatus[1]] : 'el-icon-sort';
      return {
        'el-icon-sort-up': this.sortBy==2 && this.sortRule==0,
        'el-icon-sort-down': this.sortBy==2 && this.sortRule==1,
        'el-icon-sort': this.sortBy!=2
      }
    }
  },
  mounted() {

    this.map = new AMap.Map('container',{
      center: this.position,
      lang: 'zh_en',
      resizeEnable: true,
      zoom: 14,
    });

    this.getData(this.params);

    console.log(this.location);
  },
  created() {

  },
  methods: {
    nextPage() {
      console.log("next page");
      this.page += 1
      // this.getData(this.params);
    },
    prevPage() {
      console.log('prev page');
      this.page -= 1
      // this.getData(this.params)
    },
    currentChange() {
      console.log("currentChange");
      console.log(this.page);
      this.getData(this.params);
    },
    getData(params){
      this.map.remove(this.marks);
      this.marks = []
      this.selected = -1

      console.log("requst");
      request({
        url: '/getHouses',
        params: params,
        method: "GET"
      }).then(res => {
        this.total = res.total;
        // let start = (this.page-1) * this.pageSize;
        // let end = this.page * this.pageSize;
        // for (let i=start; i<end; i++) {
        //   this.list[i-start] = res.data[i];
        // }
        this.list = res['data'];
        // console.log(res)
        console.log(this.list);
        // console.log(res['cnt']);
        //标记点
        for (let i=0; i<res['cnt']; i++) {

          let tmp = this.list[i]['location'].split(',');
          let p = [Number(tmp[0]), Number(tmp[1])];

          this.marks[i] = new AMap.Marker({
            map: this.map,
            icon: "//a.amap.com/jsapi_demos/static/demo-center/icons/poi-marker-default.png",
            position: p,
            label: {},
            clickable: true
          });
          // this.marks[i].price = String(this.list[i].totalPrice);

          this.marks[i].item = this.list[i];
          this.marks[i].index = i;
          this.marks[i].on('click', this.showInfo);
        }
        // console.log(this.marks);
        this.map.setFitView();
      }).catch(err => {
        console.log(err);
      });
    },
    showInfo(e) {
      let item = e.target.item;
      console.log(e.target);
      this.showMarker(e.target.index);

      let con = format(`
            <div style="height: 300px; width: 280px; background-color: white; border-radius: 5px">
              <div><img id="house-photo" src="http://tpc.googlesyndication.com/simgad/5843493769827749134" style="height: 180px; width: 280px; border-radius: 5px;" /></div>
              <div style="height: 120px">
                <div class="info-name two-line">{0}</div>
                <div class="info-title two-line">{1}</div>
                <div style="display: flow; margin: 10px 10px 0px 10px;">
                  <span style=" color: red; font-weight: bold">{2} million</span>
                  <a style="font-size: small; float: right" href="/detail?name={3}">more</a>
                </div>


              </div>
            </div>
        `, item.name, item.title, item.total_price.toFixed(2),item.name)


      this.infoWin = new AMap.InfoWindow({
        isCustom: true,
        content: con,  //使用默认信息窗体框样式，显示信息内容
        anchor: "buttom",
        closeWhenClickMap: true
      });
      this.infoWin.open(this.map, e.target.getPosition());
      this.map.setFitView();

      let photo = document.getElementById("house-photo");
      console.log(photo);
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
    priceRangeChange() {
      this.priceDialogVisible = false
      this.page = 1;
      console.log(this.params);
      this.getData(this.params);
    },
    locationChange() {
      console.log("选择地址了");
      console.log(this.location);
      console.log(typeof this.location);
      this.locationDialogVisible = false;
      this.page = 1;
      this.getData(this.params);
    },
    areaRangeChange(){
      this.areaDialogVisible = false;
      this.page = 1;
      this.getData(this.params);
    },
    sortByPrice() {
      if(this.sortBy == 1){
        this.sortRule =  (this.sortRule + 1) % 2;
      }else{
        this.sortBy = 1;
        this.sortRule = 0;
      }
      this.getData(this.params);
    },
    sortByIndex() {
      if(this.sortBy == 2){
        this.sortRule =  (this.sortRule + 1) % 2;
      }else{
        this.sortBy = 2;
        this.sortRule = 0;
      }
      this.getData(this.params);
    },
    aaa(id) {
      console.log('跳转');
      this.$router.push({
        path: '/detail',
        query: {
          name: id
        }
      })
    }
  }
}
</script>


