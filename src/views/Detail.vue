<template>
  <div>
    <el-carousel :interval="4000" type="card" height="300px">
      <el-carousel-item v-for="item in 6" :key="item">
        <el-image style="width: 100%; height: 100%" fit="cover" :src="srcList[0]" :preview-src-list="srcList">
        </el-image>
      </el-carousel-item>
    </el-carousel>

    <div style="width: 70%; margin: 10px auto 0px auto">
      <el-row :gutter="20">
        <el-col :span="16">
          <label class="detail-title">Basic Info</label>
          <el-divider></el-divider>
          <el-col :span="4" class="detail-name">基本信息</el-col>
          <el-col :span="20">
            <ul style="list-style: none; margin: 0px;">
              <li v-for="index in 10" class="detail-list-item">
                <span class="detail-label">房屋户型</span>2室2厅1厨1卫
              </li>
            </ul>
          </el-col>
        </el-col>
        <el-col :span="8">
          111
        </el-col>
      </el-row>

      <label class="detail-title">Neighborhood</label>
      <div id="container" tabindex="0"></div>
    </div>



  </div>
</template>

<script>
export default {
  name: "Detail",
  data() {
    return {
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        srcList: [
        'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
        'https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg'
      ]
    }
  },
  mounted() {

    this.map = new AMap.Map('container',{
      center: [116.397477, 39.908692],
      lang: 'zh_en',
      resizeEnable: true,
      scrollWheel: false,
      zoom: 14,
    });

    this.getData(this.params);

    console.log(this.location);
  },
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}

.detail-title{
  margin-bottom: 25px;
  font-weight: bold;
  font-size: 23px;
  line-height: 23px;
}
.detail-name{
  color: #999999;
  line-height: 23px;
}
.detail-list-item{
  width: 50%;
  display: inline-block;
  line-height: 24px;
  font-size: 14px;
  color: #394043;
  white-space: nowrap;
}
.detail-label{
  line-height: 24px;
  font-size: 14px;
  white-space: nowrap;
  color: #999999;
  margin-right: 30px;
}

#container{
  height: 500px;
  margin-top: 24px;
  margin-bottom: 100px;
}
</style>
