<template>
  <div class="about">
    <h1>测试页面</h1>
    <button @click="requesttest">请求测试数据</button>
    <p>{{test_data}}</p>
<!--    <div>-->
<!--      <van-swipe :autoplay="3000" indicator-color="white">-->
<!--        <van-swipe-item  v-for="(item,index) in test_data ">-->
<!--          <a :href="item.url"><img :src="item.img" alt="" style="width:100%"></a>-->
<!--        </van-swipe-item>-->
<!--      </van-swipe>-->
<!--    </div>-->

<!--    <div class="tea_title">-->
<!--      <van-swipe :autoplay="3000" style="height: 50px;" vertical>-->
<!--        <van-swipe-item v-for="item in article_data">-->
<!--          <a :href="item.url">{{item.title}}"</a>-->
<!--        </van-swipe-item>-->
<!--      </van-swipe>-->
<!--    </div>-->

<!--&lt;!&ndash;    <div v-for="item in timegoods">&ndash;&gt;-->
<!--&lt;!&ndash;      <ul>&ndash;&gt;-->
<!--&lt;!&ndash;        <li>&ndash;&gt;-->
<!--&lt;!&ndash;          <img :src="item.img" alt="">&ndash;&gt;-->
<!--&lt;!&ndash;          <p>{{item.name}}</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p>{{item.price}}</p>&ndash;&gt;-->
<!--&lt;!&ndash;          <p>{{item.old_price}}</p>&ndash;&gt;-->
<!--&lt;!&ndash;        </li>&ndash;&gt;-->
<!--&lt;!&ndash;      </ul>&ndash;&gt;-->
<!--&lt;!&ndash;    </div>&ndash;&gt;-->


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
            // console.log(res.data,111);
            if (res.data.code === 200)
              console.log(res.data.code,333);
            this.timegoods = res.data;
            // console.log(this.timegoods,222);
          }).catch(err=>{
            console.log("发生错误",err)
          })
        }
      },
      created() {
        this.$http({
          url: `http://127.0.0.1:8000/api/v1/orders/`,
          method: "post"
        }).then(res=>{
          console.log(res.data,111);
          if (res.data.code === 200)
            console.log(res.data.code,333);
            this.test_data = res.data;
             console.log(this.test_data,222);
          }).catch(err=>{
            console.log("发生错误",err)
        });
      //
      //   this.$http({
          //         url: `http://127.0.0.1:8000/api/v1/articles/`,
          //         method: "get"
          //       }).then(res=>{
          //         // console.log(res.data,111);
          //         if (res.data.code === 200)
          //           console.log(res.data.code,333);
          //         this.article_data = res.data;
          //         // console.log(this.article_data,222);
          //       }).catch(err=>{
          //         console.log("发生错误",err)
          //       })
          }

  }

</script>

<!--<template>-->
<!--  <div class="usercenter">-->
<!--    <h1>用户中心</h1>-->
<!--    <div v-if="userinfo">-->
<!--      <div>-->
<!--        <h2>修改信息</h2>-->
<!--        &lt;!&ndash; 输入手机号，调起手机号键盘 &ndash;&gt;-->
<!--        <van-field v-model="userinfo.username" type="tel" label="用户名" />-->
<!--        <van-field v-model="userinfo.telephone" type="tel" label="手机号" />-->
<!--        <van-field v-model="userinfo.password" type="password" label="密码" />-->
<!--        <van-field v-model="userinfo.email" type="email" label="邮箱" />-->

<!--        <van-button @click="modify" round block type="info" native-type="submit">-->
<!--          修改信息-->
<!--        </van-button>-->
<!--      </div>-->
<!--    </div>-->


<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--  export default{-->
<!--    methods:{-->
<!--      modify(){-->
<!--        console.log("++");-->
<!--        this.$api.modifyUserInfo({-->
<!--          userinfo:this.userinfo-->
<!--        }).then(res=>{-->
<!--          console.log("更改成功",res);-->
<!--          this.$toast("更改成功")-->
<!--        }).catch(err=>{-->
<!--          console.log("更改出错",err);-->
<!--        })-->
<!--      }-->
<!--    },-->
<!--    data(){-->
<!--      return{-->
<!--        userinfo:null,-->
<!--        // tel: '',-->
<!--        // password: '',-->
<!--        // email: ''-->
<!--      }-->
<!--    },-->
<!--    created() {-->
<!--      this.$api.getUserinfo().then(res=>{-->
<!--        console.log("个人信息",res);-->
<!--        this.userinfo=res.data;-->
<!--        this.$jsCookie.set("userinfo",res.data)-->
<!--      }).catch(err=>{-->
<!--        console.log("出错了");-->
<!--      })-->
<!--    },-->
<!--    filters:{-->
<!--      dataFormat(date){-->
<!--        date = new Date(date);-->
<!--        console.log(date, typeof(date));-->
<!--        return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`-->
<!--      }-->
<!--    }-->
<!--  }-->


<!--</script>-->

<!--<style>-->
<!--</style>-->
