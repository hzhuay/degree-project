<template>
  <div class="main">
<!--    <el-card shadow="always">-->
<!--      <div class="info">-->
<!--        <h4>本地合租房</h4>-->
<!--        <p> <span>区域: </span> <el-link  v-for="item in items.a" :key="item.a">{{ item  }}  </el-link>   </p>-->
<!--        <p> <span>租金: </span> <el-link  v-for="item in items.b" :key="item.a">{{ item  }}  </el-link>   </p>-->
<!--        <p> <span>户型: </span> <el-link  v-for="item in items.c" :key="item.a">{{ item  }}  </el-link>   </p>-->
<!--        <p> <span>方式: </span> <el-link  v-for="item in items.d" :key="item.a">{{ item  }}  </el-link>   </p>-->
<!--        <p> <span>朝向: </span> <el-link  v-for="item in items.e" :key="item.a">{{ item  }}  </el-link>   </p>-->
<!--        <hr>-->
<!--      </div>-->
<!--    </el-card>-->

    <el-card  v-for="(item, index) in list" :key="index" shadow="always" style="margin: 10px">
      <el-container style="height: 200px">
        <el-aside style="background-color: black; overflow: hidden">
          <img style="height: 100%; width: 100%" :src="item.url" alt="">
        </el-aside>
        <el-main class="main-text">
          <div style="flex: 5;">
            <p style="font-size: small;">{{item['小区名']}}</p>
            <p>{{item['名称']}}</p>
          </div>
          <div style="flex: 2;">
            <p class="price">
              {{item['总价']}}
            </p>
          </div>
        </el-main>
      </el-container>
    </el-card>

  </div>
</template>

<style scoped>
  .main-text{
    text-align: left;
    display: flex;
  }

  .price{
    font-size: 26px;
    font-weight: bold;
    font-family: Tahoma;
    text-align: right !important;
    color: red;
  }
</style>

<script>
import {request} from "@/network/request";

export default {
  data() {
    return {
      list: [],
      items:{
        a: ['雁塔\u3000','碑林\u3000','莲湖\u3000','未央\u3000','新城\u3000','长安\u3000','灞桥\u3000','高新\u3000','曲江\u3000','新区\u3000','浐灞\u3000','经开\u3000','航天新城\u3000','西咸新区\u3000','咸阳\u3000','鄠邑\u3000','高陵\u3000','临潼\u3000','阎良\u3000','蓝田\u3000','周至\u3000','西安周边'],
        b:['500元以下\u3000','500-1000元\u3000','1000-2000元\u3000','2000-3000元\u3000','3000-5000元\u3000','5000-8000元\u3000','8000元以上'],
        c:['一居\u3000','二居\u3000','三居\u3000','四居\u3000','四居以上'],
        d:['整租\u3000','合租'],
        e:['南北\u3000','通透\u3000','东西\u3000','向\u3000','朝南\u3000','朝北\u3000','朝东\u3000','朝西'],
      },
    }
  },
  created() {
    request({
      url: '/predict',
      data: {},
      method: "POST"
    }).then(res => {
      this.list = res;
    }).catch(err => {
      console.log(err);
    })
  }
}
</script>

