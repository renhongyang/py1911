<template>
  <div class="about">
    <h1>测试页面</h1>
    <button @click="requesttest">请求测试数据</button>
<!--    <p>{{timegoods}}</p>-->
    <div>
      <van-swipe :autoplay="3000" indicator-color="white">
        <van-swipe-item  v-for="(item,index) in test_data ">
          <a :href="item.url"><img :src="item.img" alt="" style="width:100%"></a>
        </van-swipe-item>
      </van-swipe>
    </div>

    <div class="tea_title">
      <van-swipe :autoplay="3000" style="height: 50px;" vertical>
        <van-swipe-item v-for="item in article_data">
          <a :href="item.url">{{item.title}}"</a>
        </van-swipe-item>
      </van-swipe>
    </div>

<!--    <div v-for="item in timegoods">-->
<!--      <ul>-->
<!--        <li>-->
<!--          <img :src="item.img" alt="">-->
<!--          <p>{{item.name}}</p>-->
<!--          <p>{{item.price}}</p>-->
<!--          <p>{{item.old_price}}</p>-->
<!--        </li>-->
<!--      </ul>-->
<!--    </div>-->


  </div>
</template>

<script>
  export default {
    name: 'about',
    components: {},
      data() {
        return{
          test_data:[],
          article_data:[],
          timegoods:[]

      }
    },
      methods:{
        requesttest(){
          console.log("点击了测试按钮！");
          this.$http({
            url: `http://127.0.0.1:8000/api/v1/timegoods/`,
            method: "get"
          }).then(res=>{
            console.log(res.data,111);
            if (res.data.code === 200)
              console.log(res.data.code,333);
            this.timegoods = res.data;
            console.log(this.timegoods,222);
          }).catch(err=>{
            console.log("发生错误",err)
          })
        }
      },
      created() {
        this.$http({
          url: `http://127.0.0.1:8000/api/v1/ads/`,
          method: "get"
        }).then(res=>{
          // console.log(res.data,111);
          if (res.data.code === 200)
            console.log(res.data.code,333);
            this.test_data = res.data;
             // console.log(this.test_data,222);
          }).catch(err=>{
            console.log("发生错误",err)
        });
            this.$http({
              url: `http://127.0.0.1:8000/api/v1/articles/`,
              method: "get"
            }).then(res=>{
              // console.log(res.data,111);
              if (res.data.code === 200)
                console.log(res.data.code,333);
              this.article_data = res.data;
              // console.log(this.article_data,222);
            }).catch(err=>{
              console.log("发生错误",err)
            })
      }


  }

</script>
