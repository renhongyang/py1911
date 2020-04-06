<template>
    <div class="cart">
        <div class="header">
            <van-nav-bar
                    title="购物车"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="arrow-left" slot="left" color="#000000" size="20"></van-icon>
                <van-icon name="user-o" slot="right" color="#000000" size="20"></van-icon>
            </van-nav-bar>
            <img src="../assets/name.png">
        </div>

        <div>
            <van-card
                    v-for="(item,index) in $store.getters.getGoodList"
                      :num="item.num"
                      title="[头春滇红]2019年 凤庆滇红 大金芽(滇红金芽) 红茶 250克"
                      price="35元"
                      desc="开春红茶第一波，口感浓郁柔和，入口柔顺，香气四溢。"
                      thumb="//www.chawo.com/data/upload/shop/store/goods/2/2019/05/2_06117653595331760_360.jpg"
            >
                <van-stepper @change="change(index,item.num)" v-model="item.num" slot="bottom" ></van-stepper>

            </van-card>
        </div>

<!--        <div v-for="(item,index) in $store.getters.getGoodList">-->
<!--            <van-button color="#7232dd" plain @click="removeit(item)">删除商品</van-button>-->
<!--        </div>-->

        <div v-for="(item,index) in $store.getters.getGoodList">
            <van-submit-bar
                    :price="3500*item.num"
                    button-text="提交订单"
                    @submit="onSubmit"
            >
                <van-checkbox v-model="checked">全选</van-checkbox>
                                <span slot="tip">
                                你的收货地址不支持同城送, <span @click="goMine">修改地址</span>
                                </span>
            </van-submit-bar>

        </div>

<!--        <div v-for="(tea,index) in red_tea">-->
<!--            <van-card-->
<!--                    :price="tea.prise"-->
<!--                    :desc="tea.desc"-->
<!--                    :title="tea.name"-->
<!--                    :thumb="tea.tea_img">-->
<!--            </van-card>-->
<!--            <br>-->
<!--        </div>-->

<!--            <van-submit-bar-->
<!--                    :price="3500*this.Num"-->
<!--                    button-text="提交订单"-->
<!--                    @submit="onSubmit"-->
<!--            >-->
<!--                <van-checkbox v-model="checked">全选</van-checkbox>-->
<!--&lt;!&ndash;                <span slot="tip">&ndash;&gt;-->
<!--&lt;!&ndash;                你的收货地址不支持同城送, <span>修改地址</span>&ndash;&gt;-->
<!--&lt;!&ndash;                </span>&ndash;&gt;-->
<!--            </van-submit-bar>-->


        <div class="footer" v-if="!islogin">
            <van-cell title="登录后享受更多优惠" value="去登录" @click="goLogin" ></van-cell>
        </div>


    </div>
</template>
<script>
    import {red_tea} from '../datas.js'
    export	default{
        data(){
            return{
                islogin:localStorage.getItem("login"),
                checked:false,

            }
        },
        methods:{
            change(index,num){
                console.log(num,index);
                this.$store.commit("ChangeGoodNum",[index,num]);

            },
            // removeit(item){
            //     this.$store.commit("removeGood",item);
            // },
            onClickLeft() {

                this.$router.go(-1);
            },
            onClickRight() {

                this.$router.push("/mine")
            },
            onSubmit(){
                this.$toast("订单提交成功！")
            },
            goLogin(){
                this.flag=false;
                this.$router.push("/login");
                // localStorage.setItem("login");
            },
            goMine(){
                this.$router.push("/mine")
            }
        },
        created() {

        }
    }

</script>



<style scoped="scoped" lang="less">
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
    .cart{
        width: 100%;
        .footer{
        display: block;
        margin-bottom: -30px;
        background-color: #adadad;
    }
    }


</style>