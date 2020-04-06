<template>
    <div class="detail">
        <div class="header">
            <van-nav-bar
                    title="商品详情"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="arrow-left" slot="left" color="#000000" size="20"></van-icon>
                <van-icon name="cart-o" slot="right" color="#000000" size="20"></van-icon>
            </van-nav-bar>
            <img src="../assets/name.png">
        </div>
        <div class="img">
            <img :src=detailgood.img alt="">
            <!--            <van-swipe :autoplay="3000" indicator-color="white">-->
            <!--                <van-swipe-item v-for="(item,index) in detail_imglist">-->
            <!--                    <img :src="item" alt="" style="width: 100%;">-->
            <!--                </van-swipe-item>-->
            <!--            </van-swipe>-->

        </div>

        <div class="con">
            <div class="good_name">
                <p>{{detailgood.name}}</p>
            </div>
            <div class="good_price">
                <p>现价 ￥{{detailgood.price}}</p>
                <p>原价 ￥{{detailgood.old_price}}</p>
            </div>

            <div class="choose"  @click="show=true">
                <p>已选择默认商品规格</p>
                <p>另选可点击此处选择商品</p>
            </div>

            <div class="goodshow">
                <div class="show_title">
                    <p>商品详情展示</p>
                    <img :src=detailgood.img alt="">
                </div>
            </div>
            <div>

            </div>
            <br>
            <br>
            <br>
        </div>

        <van-popup v-model="show" position="bottom" :style="{ height: '40%' }">
            <div>
                选择购买个数：<van-stepper v-model="buyNum" ></van-stepper>
            </div>
            <van-button type="warning" @click="addCart">加入购物车</van-button>
        </van-popup>

        <van-goods-action>
            <van-goods-action-icon icon="chat-o" text="首页" @click="goToHome" ></van-goods-action-icon>
            <van-goods-action-icon icon="cart-o" text="购物车" :info="$store.getters.getGoodList.length"  @click="$router.push('/cart')" ></van-goods-action-icon>
            <van-goods-action-icon icon="shop-o" text="客服" info="2" @click="$router.push('/kefu')"></van-goods-action-icon>
            <van-goods-action-button type="warning" text="加入购物车" @click="show=true" ></van-goods-action-button>
        </van-goods-action>
    </div>
</template>

<script>
    // import {detail_data1} from '../datas.js'
    export default{
        data(){
            return{
                show:false,
                buyNum:1,
                detailgood:""
            }
        },
        methods:{
            onClickLeft() {
                this.$router.go(-1);
            },
            onClickRight() {
                this.$router.push("/cart");
            },
            goToHome(){
                this.$router.push("/");
            },

            addCart(){
                this.show=false;
                this.$toast("加入成功");
                this.$store.commit("addGood",{num:this.buyNum})
            }
        },


        created() {
            this.$api.getTimegoodsDetail({
                id:this.$route.params.id
            }).then(res=>{
                // console.log("请求数据",res);
                this.detailgood = res.data;
            }).catch(err=>{
                console.log("请求出错",err);
            });
        }
    }


</script>

<style scoped="scoped" lang="less">
    .detail{
        overflow: auto;
    }
    .header{
        background-color: #f2f2f2;
        color: #000000;

        img{
            z-index: 5 ;
            width: 50px;
            position: absolute;
            top: 10px;
            left: 50px;
        }
    }
    .good_name{
        background-color: yellow;
        font-family: 黑体;
        font-size: 25px;
        color: black;
    }
    .good_price{
        background-color: #ffb400;
        color: #f56868;
        font-size: 25px;

    }
    .choose{
        background-color: #f56868;

    }
    .show_title{
        background-color: #ff6700;
        font-size: 30px ;
    }
    .imgshow{
        width: 100%;
        img{
            width: 100%;
        }
    }



</style>
