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
                      <van-swipe-item  v-for="(item,index) in imgdata ">
                          <img :src="item.image" alt="" style="width:100%">
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
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/ZZWAWr2QD26FO0eD43abqQ">春茶 | 板山皇家古茶园正在热卖中，此时不出...</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/BjEpnKeenm8ApM3sVaQpiw">深度 | 为什么大益熟茶皆出精品？尤其是8592...</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/QZ-YwU8-SJKBwDwy_pU4kw">解密 | 关于中茶厚德的那些机密事,99%的人都...</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/9HzM9J1ux9gfNeHrBdUDeA">春茶 | 万万没想到，勐库早春东半山竟然这么...</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/GSjkVI7qbeHh76bGGdr0Cw">推荐 | 7年的时间，大雪山从未让失望过，堪...</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/pAzuWkX-K69yiDMkasa6ow">评测 | 2016年中茶传世印级，红印铁饼，茶....</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/SGn5xDw1PikqtkUlx_jK7w">科普 | 普洱茶界最具代表性的熟茶之一，中....</a></van-swipe-item>
                      <van-swipe-item><a href="https://mp.weixin.qq.com/s/AtNvqeIfiheI4sH-4KVVWQ">推荐 | 困鹿山凭什么被称之为皇家贡茶园？...</a></van-swipe-item>
                  </van-swipe>
              </div>

<!--              <div class="image" v-for="(item,index) in index_data">-->
<!--                  <div v-for="(item1,index) in item">-->
<!--                      <a :href="item1.data"><img :src="item1.image" alt="" style="width:100%"></a>-->
<!--                  </div>-->
<!--              </div>-->
              <br>
              <div>

                  <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=2019%E5%B9%B4%E8%80%81%E5%90%8C%E5%BF%97%20%E5%90%8D%E5%B1%B1%E7%B3%BB%E5%88%97"><img src="http://www.chawo.com/data/upload/mobile/special/s0/s0_06102178107647533.jpg" alt="" style="width:100%"></a>

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
                      <li>
<!--                          <a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=107505">-->
                          <router-link to="/detail">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/2/2019/05/2_06117653595331760_240.jpg">
                          </router-link>
<!--                          </a>-->
                          <p class="goods-name">2017年凤牌滇红 云茶滇品（te级功夫红茶） 滇红茶 250克/袋</p>
                          <p><span class="goods-price">￥35.00</span><span class="none-price">￥50.00</span></p>
                      </li>

                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=108266">
                      <img src="//www.chawo.com/data/upload/shop/store/goods/2/2019/08/2_06196347466379582_240.jpg"></a>
                          <p class="goods-name">2019年润元昌 开门红 熟茶 357克/饼</p>
                          <p><span class="goods-price">￥59.00</span>
                              <span class="none-price">￥168.00</span></p>
                      </li>

                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=105308">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/6/2019/02/6_06046900839891446_240.jpg"></a>
                          <p class="goods-name">2019年白沙溪 茯缘 安化黑茶 原叶金花手筑茯砖 750克/片</p>
                          <p><span class="goods-price">￥178.00</span><span class="none-price">￥178.00</span></p>
                      </li>

                      <li>
                          <a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=109066">
                              <img src="//www.chawo.com/data/upload/shop/store/goods/2/2020/01/2_06314667884652568_240.jpg"></a>
                          <p class="goods-name">大益 下关 中茶 八角亭 老同志 年货节茶样大礼包 8克/份 共计30份</p>
                          <p><span class="goods-price">￥99.00</span><span class="none-price">￥199.00</span></p>
                      </li>

                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=107263">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/2/2019/04/2_06099538472045491_240.jpg"></a>
                          <p class="goods-name">2017年妙贡堂 管阳一号 白茶(寿眉) 300克/饼</p>
                          <p><span class="goods-price">￥99.00</span><span class="none-price">￥260.00</span></p>
                      </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=105398">
                      <img src="//www.chawo.com/data/upload/shop/store/goods/2/2018/05/2_05802981138272905_240.jpg"></a>
                      <p class="goods-name">千山叶 茉莉花茶 125克/罐 1罐</p>
                          <p><span class="goods-price">￥58.00</span><span class="none-price">￥70.00</span></p>
                      </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=109060">
                      <img src="//www.chawo.com/data/upload/shop/store/goods/2/2020/01/2_06313888502213105_240.jpg"></a>
                      <p class="goods-name">2016年下关 南诏金芽沱茶 生茶 200克/沱 10沱</p>
                      <p><span class="goods-price">￥288.00</span><span class="none-price">￥700.00</span></p>
                  </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=108405">
                      <img src="//www.chawo.com/data/upload/shop/store/goods/2/2019/09/2_06207628231955402_240.jpg"></a>
                      <p class="goods-name">2019年千山叶 红叶金螺·蜜香金螺 滇红工夫红茶 400克/袋</p>
                      <p><span class="goods-price">￥128.00</span><span class="none-price">￥208.00</span></p>
                  </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=109013">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/6/2019/12/6_06297190591733270_240.jpg"></a>
                          <p class="goods-name">中茶蝴蝶白茶 5809子鼠开天 庚子鼠年生肖纪念茶 白牡丹饼 357克/饼</p>
                          <p><span class="goods-price">￥296.00</span><span class="none-price">￥296.00</span></p>
                      </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=108916">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/2/2020/01/2_06313884372599713_240.jpg"></a>
                          <p class="goods-name">2010年大益 7452 熟茶 357克/饼 整提</p>
                          <p><span class="goods-price">￥748.00</span><span class="none-price">￥1299.00</span></p>
                      </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=106692">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/2/2018/12/2_05987941053388899_240.jpg"></a>
                          <p class="goods-name">2018年大益 小龙柱 1801批 熟茶 357克/饼</p>
                          <p><span class="goods-price">￥175.00</span><span class="none-price">￥228.00</span></p>
                       </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=105372">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/2/2020/01/2_06313886928084191_240.jpg"></a>
                          <p class="goods-name">2015年八角亭 普洱金毫 熟茶 200克/饼 整提</p>
                          <p><span class="goods-price">￥358.00</span><span class="none-price">￥1260.00</span></p>
                       </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=108328">
                          <img src="//www.chawo.com/data/upload/shop/store/goods/3/2019/09/3_06207019864016246_240.jpg"></a>
                          <p class="goods-name">容天180cc 原矿朱泥【奉春燕作品】 宜兴紫砂壶</p>
                          <p><span class="goods-price">￥488.00</span><span class="none-price">￥898.00</span></p>
                        </li>
                      <li><a href="http://www.chawo.com/wap/tmpl/product_detail.html?goods_id=105869">
                      <img src="//www.chawo.com/data/upload/shop/store/goods/2/2018/06/2_05826502617617098_240.jpg"></a>
                      <p class="goods-name">2015年佤山映象 7561 熟茶 250克/砖</p>
                      <p><span class="goods-price">￥38.00</span><span class="none-price">￥138.00</span></p>
                  </li>

                  </ul>
              </div>

              <div class="kind">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111652008392456.png" alt="" style="width: 100%">
                      </a>
                  </div>

                  <div class="nav-img">
                      <div class="home3-img" v-for="(item,index) in home3data">
                          <a :href="item.data"><img :src="item.image" alt="" style="width: 187px"></a>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/tag.html">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111655294608459.png" alt="" style="width: 100%">
                      </a>
                  </div>

                  <div class="goods-img" @click="GoDetail">
                      <div class="good-img" v-for="(item,index) in goodsdata1">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/activity.html?id=12">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06225768452117294.png" alt="" style="width: 100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata2">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%94%9F%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111671460151599.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata3">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%86%9F%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111670541537206.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata4">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%BA%A2%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111672783388814.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata5">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?gc_id=26">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06225770586044598.png" alt="" width="100%"    >
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata6">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E9%BB%91%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06225769247665907.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata7">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?gc_id=20&amp;child_gc_id=36">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111674685574430.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata8">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E7%BB%BF%E8%8C%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111677078131084.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata9">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_first_categroy.html">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111677710958907.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata10">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>

              <div class="good_list">
                  <div class="item-pic">
                      <a href="http://www.chawo.com/wap/tmpl/product_list.html?keyword=%E5%A3%B6">
                          <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06111679366819727.png" alt="" width="100%">
                      </a>
                  </div>

                  <div class="goods-img">
                      <div class="good-img" v-for="(item,index) in goodsdata">
                          <img :src="item.goods_image" alt="" style="width: 170px">
                          <p>{{item.goods_name}}</p>
                          <p>￥{{item.goods_promotion_price}}</p>
                      </div>
                  </div>
              </div>
              <div class="item-pic">
                  <a href="http://www.chawo.com/wap/tmpl/product_first_categroy.html">
                      <img src="//www.chawo.com/data/upload/mobile/special/s0/s0_06227404716647644.jpg" alt="" width="100%">
                  </a>
              </div>
              <div class="footer" >
                  <div class="nav-text">
                      <a href="http://localhost:8080/#/mine">登录</a>
                      <a href="http://localhost:8080/#/regist">注册</a>
                      <a href="http://www.chawo.com/wap/tmpl/member/login.html">反馈</a>
                      <a href="http://localhost:8080/#/" class="gotop">返回顶部</a>
                  </div>
              </div>

      </div>

      </div>
  </div>
</template>

<script>
import {datas} from '../datas.js'

export default {
  name: 'home',
  components: {
  },
    data(){
      return{
          time: 30 * 60 * 60 * 1000,
          index_data:null,
          value:"大益",
          img_list:null,
          imgdata:null,
          home3data:null,
          goodsdata1:null,
          goodsdata2:null,
          goodsdata3:null,
          goodsdata4:null,
          goodsdata5:null,
          goodsdata6:null,
          goodsdata7:null,
          goodsdata8:null,
          goodsdata9:null,
          goodsdata10:null,
          goodsdata:null
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
            this.$router.push("/detail")
        }
    },
    created() {
        // this.$http({
        //     url: `http://www.chawo.com/mobile/index.php`,
        //     method: "get"
        // }).then(res=>{
        //     console.log(res.data.datas);
        //     if (res.data.code === 200) {
        //         this.index_data = res.data.datas;
        //         // this.getdata=res.data.data;
        //         // console.log(res.data.data.adv_list.item);
        //         // res是response的简写
        //         console.log(res.data.datas);
        //         console.log(res.data);
        //         // console.log(res.data.data);
        //
        //     }
        // });
        // this.img_list=img_list;
        this.imgdata=datas.datas[0].adv_list.item;
        this.home3data=datas.datas[3].home3.item;
        this.goodsdata1=datas.datas[5].goods.item;
        this.goodsdata2=datas.datas[7].goods.item;
        this.goodsdata3=datas.datas[9].goods.item;
        this.goodsdata4=datas.datas[11].goods.item;
        this.goodsdata5=datas.datas[13].goods.item;
        this.goodsdata6=datas.datas[15].goods.item;
        this.goodsdata7=datas.datas[17].goods.item;
        this.goodsdata8=datas.datas[19].goods.item;
        this.goodsdata9=datas.datas[21].goods.item;
        this.goodsdata10=datas.datas[23].goods.item;
        this.goodsdata=datas.datas[25].goods.item;
        // console.log(this.img_list);
        // console.log(this.imgdata);
        // console.log(this.home3data);
        // console.log(this.goodsdata);


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
        display: block;
        width: 100%;
        .nav-img{
            display: flex;
            width: 100%;
            flex-wrap: wrap;
        }
    }
    .good_list{
        display: block;
        width: 100%;
        .goods-img{
            display: flex;
            width: 100%;
            flex-wrap: wrap;
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


        }
    }




</style>
