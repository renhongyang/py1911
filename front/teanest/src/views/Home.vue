<template>
  <div class="home">
      <div class="cons">
          <div class="search" >
              <div>
                  <img src="http://www.chawo.com/wap/images/chawo-logo.png"
                       style="height: 20px;position: absolute;margin-top: 12px;
                       padding-left: 10px;width: 50px !important;">
              </div>
              <div class="van-search" @click="Gosearch">
                  <van-search  placeholder="请输入搜索商品名"  v-model="value"></van-search>
              </div>

              <div >
<!--                  <van-icon name="http://www.chawo.com/wap/images/more_w.png" size="30"></van-icon>-->
                <img src="http://www.chawo.com/wap/images/more_w.png" alt=""
                     style="width: 30px" @click="Gomine">
              </div>
          </div>

          <div class="section">
              <div>
                  <van-swipe :autoplay="3000" indicator-color="white">
                      <van-swipe-item  v-for="(item,index) in ads ">
                          <img :src="item.img" alt="" style="width:100%">
                      </van-swipe-item>
                  </van-swipe>
              </div>

              <div class="bar">
                  <van-grid :column-num="5"  >
                      <van-grid-item
                              icon="orders-o"
                              text="产品分类"
                              to="/category"
                      >
                      </van-grid-item>

                      <van-grid-item
                              icon="upgrade"
                              text="近期新品"
                              url="http://www.chawo.com/wap/tmpl/product_list.html?key=4&order=2"
                      >
                      </van-grid-item>

                      <van-grid-item

                              icon="clock-o"
                              text="限时折扣"
                              url="http://www.chawo.com/wap/tmpl/product_list.html?xianshi=1"
                      >
                      </van-grid-item>

                      <van-grid-item

                              icon="fire-o"
                              text="茶窝秒杀"
                              url="http://www.chawo.com/wap/tmpl/product_list.html?xianshi=1"
                      >
                      </van-grid-item>

                      <van-grid-item

                          icon="good-job-o"
                          text="茶窝优选"
                          url="http://www.chawo.com/wap/tmpl/product_list.html?xianshi=1"
                  >
                  </van-grid-item>

                      <van-grid-item

                          icon="discount"
                          text="优惠套餐"
                          url="http://www.chawo.com/wap/tmpl/product_list.html?xianshi=1"
                  >
                  </van-grid-item>

                      <van-grid-item

                              icon="gift-card-o"
                              text="中老期茶"
                              url="http://www.chawo.com/wap/activity.html?id=12"
                      >
                      </van-grid-item>

                      <van-grid-item

                              icon="new-o"
                              text="春茶上市"
                              url="http://www.chawo.com/wap/tmpl/product_list.html?keyword=2019%20%E6%98%A5%E8%8C%B6"
                      >
                      </van-grid-item>

                      <van-grid-item

                              icon="goods-collect-o"
                              text="积分兑换"
                              url="http://www.chawo.com/wap/tmpl/points/point_list.html"
                      >
                      </van-grid-item>

                      <van-grid-item

                              icon="smile-o"
                              text="签到有礼"
                              to="/mine"
                      >
                      </van-grid-item>

                  </van-grid>

              </div>
              <br>

              <div class="tea_title">
                  <img src="http://www.chawo.com/wap/images/toutiao.jpg" alt="">
                  <van-swipe :autoplay="3000" style="height: 50px;" vertical>
                      <van-swipe-item v-for="item in article">
                          <a :href="item.url">{{item.title}}"</a>
                      </van-swipe-item>
                  </van-swipe>
              </div>


              <!--              <div class="image" v-for="(item,index) in index_data">-->
<!--                  <div v-for="(item1,index) in item">-->
<!--                      <a :href="item1.data"><img :src="item1.image" alt="" style="width:100%"></a>-->
<!--                  </div>-->
<!--              </div>-->
              <br>
              <div>

                  <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=2019%E5%B9%B4%E8%80%81%E5%90%8C%E5%BF%97%20%E5%90%8D%E5%B1%B1%E7%B3%BB%E5%88%97">
                      <img src="http://www.chawo.com/data/upload/mobile/special/s0/s0_06102178107647533.jpg" alt="" style="width:100%"></a>

              </div>
              <br>

              <div style="color: red">
                  限时抢购
              </div>
              <br>
              <div class="timebuy">

<!--                  <van-count-down-->
<!--                          :time="time"-->
<!--                          format="DD 天 HH 时 mm 分 ss 秒">-->
<!--                  </van-count-down>-->
                  <ul>
                      <li v-for="item in timegood">
                          <router-link :to="'/detail/'+item.id+'/'">
                              <img :src="item.img">
                          </router-link>
                          <p class="goods-name">{{item.name}}</p>
                          <p><span class="goods-price">￥{{item.price}}</span><span class="none-price">￥{{item.old_price}}</span></p>
                      </li>
                  </ul>
              </div>


              <div class="kind" >
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111652008392456.png" alt="" style="width: 100%">
                      </a>
                  </div>

                  <div v-for="(item,index) in indexgood" v-if="item.category === 1" >
                      <div class="nav-img" >
                          <a href="#"><img :src="item.img"  alt="" style="width: 187px"></a>
                      </div>
                  </div>
              </div>



              <div class="good_list" >
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/tag.html">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111655294608459.png" alt="" style="width: 100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 2">
                          <router-link :to="'/detail/'+item.id+'/'">
                              <img :src="item.img" style="width: 170px">
                          </router-link>
<!--                          <img :src="item.img" alt="" >-->
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>

              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/activity.html?id=12">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06225768452117294.png" alt="" style="width: 100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 3">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%94%9F%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111671460151599.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 4">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%86%9F%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111670541537206.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 5">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%BA%A2%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111672783388814.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 6">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?gc_id=26">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06225770586044598.png" alt="" width="100%"    >
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 7">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E9%BB%91%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06225769247665907.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 8">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?gc_id=20&amp;child_gc_id=36">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111674685574430.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 9">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%BB%BF%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111677078131084.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 10">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_first_categroy.html">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111677710958907.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 11">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E5%A3%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111679366819727.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail"  >
                      <div class="good-img" v-for="(item,index) in indexgood" v-if="item.category === 12">
                          <img :src="item.img" alt="" style="width: 170px">
                          <p>{{item.name}}</p>
                          <p>￥{{item.price}}</p>
                      </div>
                  </div>
              </div>
              <div class="item-pic">
                  <a href="http://www.chawo.com/wap/tmpl/product_first_categroy.html">
                      <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06227404716647644.jpg" alt="" width="100%">
                  </a>
              </div>

<!--              <div class="footer" >-->
<!--                  <div class="nav-text">-->
<!--                      <a href="http://localhost:8080/#/mine">登录</a>-->
<!--                      <a href="http://localhost:8080/#/regist">注册</a>-->
<!--                      <a href="http://www.chawo.com/wap/tmpl/member/login.html">反馈</a>-->
<!--                      <a href="http://localhost:8080/#/" class="gotop">返回顶部</a>-->
<!--                  </div>-->
<!--              </div>-->

      </div>

      </div>
  </div>
</template>

<script>
// import {datas} from '../datas.js'

export default {
  name: 'home',
  components: {
  },
    data(){
      return{
          ads:[],
          article:[],
          timegood:[],
          indexgood:[],
          time: 30 * 60 * 60 * 1000,
          value:"",
      }
    },
    methods:{
        Gomine(){
            this.$router.push("/login")
        },
        Gosearch(){
            this.$router.push("/search")
        },
        GoDetail(){
            this.$router.push("/detail/10/")
        }
    },
    created() {
        // 获取ads
        this.$http({
            url: `http://127.0.0.1:8000/api/v1/ads/`,
            method: "get"
        }).then(res=>{
            // console.log(res.data,111);
            if (res.data.code === 200)
                console.log(res.data.code,333);
            this.ads = res.data;
            // console.log(this.ads,222);
        }).catch(err=>{
            console.log("发生错误",err)
        });
        // 获取文章
        this.$http({
            url: `http://127.0.0.1:8000/api/v1/articles/`,
            method: "get"
        }).then(res=>{
            // console.log(res.data,111);
            if (res.data.code === 200)
                console.log(res.data.code,333);
            this.article = res.data;
            // console.log(this.article_data,222);
        }).catch(err=>{
            console.log("发生错误",err)
        });
        // 获取限时商品
        this.$http({
            url: `http://127.0.0.1:8000/api/v1/timegoods/`,
            method: "get"
        }).then(res=>{
            // console.log(res.data,111);
            if (res.data.code === 200)
                console.log(res.data.code,333);
            this.timegood = res.data;
            // console.log(this.timegood,222);
        }).catch(err=>{
            console.log("发生错误",err)
        });
        // 获取首页展示商品
        this.$http({
            url: `http://127.0.0.1:8000/api/v1/indexgoods/`,
            method: "get"
        }).then(res=>{
            // console.log(res.data,111);
            if (res.data.code === 200)
                console.log(res.data.code,333);
            this.indexgood = res.data;
            // console.log(this.indexgood,222);
        }).catch(err=>{
            console.log("发生错误",err)
        });


        
    }

}




</script>

<style scoped="scoped" lang="less">
    .search{
        text-align: center;
        width: 100%;
        /*background-color: rgba(255,255,255,0.9);*/
        background-color: #f2f2f2;
        display: flex;
        justify-content: space-around;
        /*position: fixed;*/
        z-index: 10;
        .van-search{
            line-height: 30px;
            height: 30px;
        }
    }
    .section{
        margin-bottom: 30px ;
    }

    .tea_title{
        display: block;
        background-color:#eeeeee;
        img{
            width: 50px;
        }
        a{
            color: #000000;
        }
    }
    .timebuy{
        height: 200px;
        display: flex;
        overflow-x: auto;
        ul{
            display: flex;
            img{
                width: 100px;
                margin-left: 5px;
            }
        }
        .goods-name {
            display: block;
            font-size: 0.4rem;
            line-height: 0.8rem;
            color: #000;
            height: 1.5rem;
            overflow: hidden;
        }
        p {
            text-align: center;
            .goods-price {
                font-size: 0.7rem;
                color: #DB4453;
                line-height: 1rem;
                display: block;
            }
            .none-price {
                font-size: 0.5rem;
                text-decoration: line-through;
                color: #848484;
                line-height: 0.8rem;
                display: block;
            }
        }
    }

    .kind{
        display: flex;
        width: 100%;
        /*overflow-x: auto;*/
        /*border: solid 2px #DB4453;*/
        flex-wrap: wrap;
        justify-content: space-around;
        .nav-img{
            display: block;
            width: 100%;


        }
    }


    .good_list{
        display: flex;
        flex-wrap: wrap;
        width: 100%;
    }
    .goods-img{
        display: flex;
        flex-wrap: wrap;
        width: 100%;
    }
    .good-img{
        width: 50%;
        border-top: solid 1px #f56868;
        p:nth-of-type(1) {
            font-size: 0.85rem;
            line-height: 1rem;
            color: #000;
        }
        p:nth-of-type(2){
            color: #DB4453;
        }
    }








</style>
