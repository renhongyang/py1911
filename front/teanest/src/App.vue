<template>
  <div id="app">

    <van-tabbar  v-show="$route.meta.tabbar" v-model="active" active-color="#ff6700">
      <van-tabbar-item icon="home-o" to="/">商城首页</van-tabbar-item>
      <van-tabbar-item icon="description" to="/category">商品分类</van-tabbar-item>
      <van-tabbar-item icon="cart-o" to="/cart">购物小车</van-tabbar-item>
      <van-tabbar-item icon="friends-o" to="/mine">我的账户</van-tabbar-item>
    </van-tabbar>
    <router-view v-if="isRouterAlive" ></router-view>
  </div>
</template>

<script>
  export default {
    name: 'App',
    provide (){
      return {
        reload:this.reload
      }
    },
      data(){
        return {
          active: 0,
          isRouterAlive:true,
        }
      },
    methods:{
      reload (){
        this.isRouterAlive = false;
        this.$nextTick(function(){
          this.isRouterAlive = true
        })
      }
    },
  }
</script>
<style scoped="scoped" lang="less">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;

    a{
      font-weight: bold;
      color: #2c3e50;
      text-decoration: none;
      &.router-link-exact-active{
        color: #42b983;
      }
    }
  }


</style>




